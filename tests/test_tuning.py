"""No Optuna study or model execution: deterministic fake sampler/trainer/evaluator."""

import io
import json
import math
import random
import runpy
import shutil
import subprocess
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import pytest
from test_training_research import ROOT, digest, research_case

from sdp_xray.training_research import research_plan
from sdp_xray.tuning import (
    StudyLedger,
    confirmation_plan,
    export_study,
    make_study_definition,
    open_optuna_backend,
    repeatability_plan,
    run_synthetic_study,
    validate_objective_result,
    validate_parameters,
    validation_request,
)


class FakeSampler:
    synthetic = True

    def __init__(self, prune=False):
        self.rng = random.Random(17)
        self.asks, self.reports, self.tells = [], [], []
        self.prune = prune

    def ask(self, number, control):
        assert number == len(self.asks)
        self.asks.append(number)
        if control is not None:
            return deepcopy(control)
        optimizer = self.rng.choice(["SGD", "AdamW"])
        low, high = (-4, -2) if optimizer == "SGD" else (-5, -3)
        return {"optimizer": optimizer, "lr0": 10 ** self.rng.uniform(low, high),
                "weight_decay": 10 ** self.rng.uniform(-5, -3),
                "lrf": 10 ** self.rng.uniform(-2, -1), "mosaic": self.rng.uniform(0, 0.5)}

    def report(self, number, value, epoch):
        assert [number, epoch] not in [r[:2] for r in self.reports]
        self.reports.append([number, epoch, value])

    def should_prune(self, number):
        assert sum(t[1] == "complete" for t in self.tells) >= 5
        assert max(r[1] for r in self.reports if r[0] == number) >= 10
        return self.prune

    def tell(self, number, status, value):
        self.tells.append([number, status, value])

    def snapshot(self):
        return {"rng": list(self.rng.getstate()), "asks": deepcopy(self.asks),
                "reports": deepcopy(self.reports), "tells": deepcopy(self.tells)}

    def restore(self, state):
        version, numbers, gaussian = state["rng"]
        self.rng.setstate((version, tuple(numbers), gaussian))
        self.asks, self.reports, self.tells = deepcopy((state["asks"], state["reports"], state["tells"]))


class FakeTrainer:
    synthetic = True

    def __init__(self, fail=(), interrupt=None, duplicate=False, escape=None):
        self.fail, self.interrupt, self.duplicate, self.escape = fail, interrupt, duplicate, escape
        self.calls = []

    def run(self, request):
        self.calls.append(deepcopy(request))
        number = request["number"]
        if number in self.fail:
            raise RuntimeError("synthetic failure; do not expose this text")
        for epoch in range(request["completed_epochs"] + 1, 31):
            path = request["output_directory"] / f"epoch-{epoch}.bin"
            path.write_text(json.dumps([number, epoch, request["parameters"]], sort_keys=True))
            event = {"phase": "fit", "completed_epoch": epoch, "checkpoint": self.escape or path}
            yield event
            if self.duplicate:
                yield deepcopy(event)
            if self.interrupt == (number, epoch):
                raise KeyboardInterrupt
        yield {"phase": "final_evaluation", "completed_epoch": 30}  # No duplicate metric report.


class FakeEvaluator:
    synthetic = True

    def __init__(self, edit=None):
        self.edit, self.calls = edit, []

    def evaluate(self, request):
        self.calls.append(deepcopy(request))
        result = {"status": "ok", **{k: deepcopy(v) for k, v in request.items() if k != "validation_ids"},
                  "evaluated_image_ids": deepcopy(request["validation_ids"]),
                  "value": 0.25 + (request["completed_epoch"] % 7) / 100}  # Invented fixture only.
        if self.edit:
            self.edit(result)
        return result


def definition():
    config, evidence = research_case()
    return make_study_definition(config, evidence["partition"], config["sources"]["validation"]["annotation_sha256"])


@pytest.fixture(scope="module")
def completed_study(tmp_path_factory):
    output = tmp_path_factory.mktemp("synthetic-study-parent") / "study"
    sampler, trainer, evaluator = FakeSampler(), FakeTrainer(fail=(1, 2), duplicate=True), FakeEvaluator()
    result = run_synthetic_study(definition(), output, sampler, trainer, evaluator)
    return output, sampler, trainer, evaluator, result


def test_twenty_attempts_include_control_failures_and_distinct_outputs(completed_study):
    output, sampler, trainer, evaluator, result = completed_study
    assert len(sampler.asks) == result["attempted_configurations"] == 20
    assert result["trainer_invocations"] == 20 and result["training_started"] is False
    assert result["execution_kind"] == "synthetic_software_check"
    assert result["trials"][0]["parameters"] == definition()["configuration"]["study"]["control"]
    assert result["trials"][1]["status"] == "failed" and result["trials"][1]["value"] is None
    assert len({str(r["output_directory"]) for r in trainer.calls}) == 20
    assert all(Path(r["output_directory"]).is_relative_to(output) for r in trainer.calls)
    assert len(evaluator.calls) == 18 * 30  # Duplicate callbacks/final evaluation never report again.
    assert len(sampler.reports) == 18 * 30


def test_selection_uses_declared_ap_checkpoint_not_last_epoch(completed_study):
    _, _, _, _, result = completed_study
    trial = result["trials"][0]
    assert trial["value"] == 0.31
    assert trial["best_checkpoint"]["path"].endswith("epoch-6.bin")
    assert trial["last_checkpoint"]["path"].endswith("epoch-30.bin")


def test_export_is_exclusive_and_contains_provenance(completed_study, tmp_path):
    output, _, _, _, original = completed_study
    exported = export_study(output, tmp_path / "export.json")
    assert exported == original
    assert exported["definition"]["configuration"]["initialization"]["checkpoint_sha256"]
    assert exported["definition"]["partition_sha256"]
    with pytest.raises(FileExistsError):
        export_study(output, tmp_path / "export.json")
    main = runpy.run_path(str(ROOT / "scripts/tune_yolov10.py"))["main"]
    with redirect_stdout(io.StringIO()) as stream:
        assert main(["--export-from", str(output), "--output", str(tmp_path / "cli-export.json")]) == 0
        assert json.loads(stream.getvalue())["execution_kind"] == "synthetic_software_check"


def test_confirmation_and_repeatability_have_separate_budgets(completed_study):
    exported = completed_study[-1]
    planned = confirmation_plan(exported)
    assert 1 <= len(planned) <= 4
    assert all(r["epochs"] == 100 and r["seed"] == 17 and r["value"] is None for r in planned)
    confirmed = [{**r, "status": "complete", "value": 0.2 + r["source_trial"] / 100,
                  "checkpoint_sha256": digest(str(r["source_trial"]))} for r in planned]
    for result in confirmed:
        request = validation_request(exported["definition"], result["checkpoint_sha256"], 100)
        result["validation"] = FakeEvaluator().evaluate(request)
        result["validation"]["value"] = result["value"]
    repeat = repeatability_plan(exported, confirmed)
    assert set(r["seed"] for r in repeat) == {17, 29, 43}
    assert all(r["status"] == "reuse" for r in repeat if r["seed"] == 17)
    assert all(r["value"] is None and r["checkpoint_sha256"] is None for r in repeat if r["seed"] != 17)
    assert exported["attempted_configurations"] == 20
    confirmed[0]["value"] = float("nan")
    with pytest.raises(ValueError):
        repeatability_plan(exported, confirmed)
    assert confirmation_plan({"trials": []}) == []


def test_pruning_waits_for_five_completed_trials_and_ten_epochs(tmp_path):
    sampler = FakeSampler(prune=True)
    result = run_synthetic_study(definition(), tmp_path / "pruned", sampler, FakeTrainer(), FakeEvaluator(),
                                 stop_requested=lambda: len(sampler.tells) >= 6)
    assert [t["status"] for t in result["trials"]] == ["complete"] * 5 + ["pruned"]
    assert len(result["trials"][-1]["reports"]) == 10
    assert result["trials"][-1]["value"] is None


@pytest.mark.parametrize("edit", [
    lambda r: r.update(value=float("nan")), lambda r: r.update(value=float("inf")),
    lambda r: r.update(value=None), lambda r: r.pop("value"), lambda r: r.update(value=True),
    lambda r: r.update(checkpoint_sha256="a" * 64), lambda r: r.update(partition_sha256="a" * 64),
    lambda r: r.update(evaluated_image_ids=[]), lambda r: r["evaluated_image_ids"].append(999),
    lambda r: r["evaluated_image_ids"].append(r["evaluated_image_ids"][0]),
    lambda r: r["objective"].update(evaluator_id="other"),
    lambda r: r["objective"]["settings"].update(max_detections=1),
    lambda r: r.update(status="error"), lambda r: r.update(completed_epoch=2),
    lambda r: r.update(completed_epoch=True),
])
def test_invalid_objective_is_rejected(edit):
    request = validation_request(definition(), digest("checkpoint"), 1)
    result = FakeEvaluator(edit).evaluate(request)
    with pytest.raises(ValueError):
        validate_objective_result(request, result)


def test_invalid_objective_fails_attempt_without_zero_ap(tmp_path):
    sampler = FakeSampler()
    result = run_synthetic_study(definition(), tmp_path / "invalid", sampler, FakeTrainer(),
                                 FakeEvaluator(lambda r: r.update(value=None)),
                                 stop_requested=lambda: len(sampler.tells) == 1)
    assert result["trials"][0]["status"] == "failed"
    assert result["trials"][0]["value"] is None


def test_interruption_resume_reuses_configuration_and_restores_sampler(tmp_path):
    first, sampler = tmp_path / "interrupted", FakeSampler()
    interrupted = run_synthetic_study(definition(), first, sampler, FakeTrainer(interrupt=(0, 4)), FakeEvaluator())
    assert interrupted["trials"][0]["status"] == "interrupted"
    assert interrupted["trials"][0]["value"] is None
    with pytest.raises(ValueError, match="retry_interrupted"):
        run_synthetic_study(definition(), first, FakeSampler(), FakeTrainer(), FakeEvaluator(), resume=True)
    restored, trainer = FakeSampler(), FakeTrainer()
    resumed = run_synthetic_study(definition(), first, restored, trainer, FakeEvaluator(),
                                  resume=True, retry_interrupted=True,
                                  stop_requested=lambda: len(restored.tells) == 2)
    assert resumed["attempted_configurations"] == 2 and resumed["trainer_invocations"] == 3
    assert len(restored.asks) == 2
    assert trainer.calls[0]["completed_epochs"] == 4
    assert trainer.calls[0]["resume_checkpoint"].endswith("epoch-4.bin")
    assert len(resumed["trials"][0]["reports"]) == 30
    continuous_sampler = FakeSampler()
    continuous = run_synthetic_study(definition(), tmp_path / "continuous", continuous_sampler, FakeTrainer(),
                                     FakeEvaluator(), stop_requested=lambda: len(continuous_sampler.tells) == 2)
    assert [t["parameters"] for t in resumed["trials"]] == [t["parameters"] for t in continuous["trials"]]
    assert restored.snapshot() == continuous_sampler.snapshot()


def test_resume_rejects_changed_definition_and_corrupt_sampler_snapshot(tmp_path):
    root = tmp_path / "study"
    run_synthetic_study(definition(), root, FakeSampler(), FakeTrainer(interrupt=(0, 1)), FakeEvaluator())
    changed = definition()
    changed["objective"]["settings"]["max_detections"] = 50
    changed["configuration"]["objective"] = deepcopy(changed["objective"])
    with pytest.raises(ValueError, match="fingerprint"):
        run_synthetic_study(changed, root, FakeSampler(), FakeTrainer(), FakeEvaluator(), resume=True)
    latest = sorted(root.glob("state-*.json"))[-1]
    contents = json.loads(latest.read_text())
    contents["payload"]["sampler_state"]["asks"] = []
    latest.write_text(json.dumps(contents))
    with pytest.raises(ValueError, match="integrity"):
        export_study(root)


def test_resume_rejects_changed_checkpoint_and_output_collision(tmp_path):
    root = tmp_path / "study"
    result = run_synthetic_study(definition(), root, FakeSampler(), FakeTrainer(interrupt=(0, 1)), FakeEvaluator())
    with pytest.raises(FileExistsError):
        run_synthetic_study(definition(), root, FakeSampler(), FakeTrainer(), FakeEvaluator())
    path = root / result["trials"][0]["last_checkpoint"]["path"]
    path.write_bytes(b"changed synthetic bytes")
    with pytest.raises(ValueError, match="checkpoint changed"):
        run_synthetic_study(definition(), root, FakeSampler(), FakeTrainer(), FakeEvaluator(),
                            resume=True, retry_interrupted=True)


def test_output_escape_and_writer_collision_are_rejected(tmp_path):
    outside = tmp_path / "keep.bin"
    outside.write_bytes(b"preserve")
    sampler = FakeSampler()
    result = run_synthetic_study(definition(), tmp_path / "study", sampler, FakeTrainer(escape=outside),
                                 FakeEvaluator(), stop_requested=lambda: len(sampler.tells) == 1)
    assert result["trials"][0]["status"] == "failed"
    assert outside.read_bytes() == b"preserve"
    ledger = StudyLedger(tmp_path / "locked", definition())
    with ledger.locked(), pytest.raises(FileExistsError):
        with ledger.locked():
            pass


def test_budget_stop_starts_no_trial_and_live_adapters_are_rejected(tmp_path):
    sampler = FakeSampler()
    result = run_synthetic_study(definition(), tmp_path / "budget", sampler, FakeTrainer(), FakeEvaluator(),
                                 budget_seconds=0)
    assert result["attempted_configurations"] == 0 and not sampler.asks
    trainer = FakeTrainer()
    trainer.synthetic = False
    with pytest.raises(ValueError, match="synthetic adapters"):
        run_synthetic_study(definition(), tmp_path / "live", sampler, trainer, FakeEvaluator())
    assert not (tmp_path / "live").exists()
    with pytest.raises(ValueError, match="time budget"):
        run_synthetic_study(definition(), tmp_path / "invalid-budget", sampler,
                            FakeTrainer(), FakeEvaluator(), budget_seconds=float("nan"))


def test_live_optuna_factory_checks_gates_before_import_or_storage(tmp_path):
    config, evidence = research_case()
    plan = research_plan(config, evidence)
    plan["blockers"] = []  # Caller cannot clear recomputed gates.
    with patch("builtins.__import__", side_effect=AssertionError("optional import attempted")):
        with pytest.raises(ValueError, match="live execution blocked"):
            open_optuna_backend(plan, tmp_path / "new", "synthetic")
    assert not (tmp_path / "new").exists()


def test_search_space_rejects_auto_optimizer_and_nonfinite_values():
    parameters = definition()["configuration"]["study"]["control"]
    for key, value in (("optimizer", "auto"), ("lr0", math.inf), ("mosaic", 0.6)):
        with pytest.raises(ValueError):
            validate_parameters({**parameters, key: value})


def test_slurm_resources_arguments_mask_and_signal_are_explicit():
    source = (ROOT / "environments/training/train.slurm").read_text()
    for line in ("--partition=gpu-student", "--qos=gpu-student", "--gres=gpu:1",
                 "--cpus-per-task=4", "--mem=32G", "--time=04:00:00", "--signal=B:TERM@120"):
        assert line in source
    assert "${CUDA_VISIBLE_DEVICES:?" in source and "export CUDA_VISIBLE_DEVICES=" not in source
    assert 'kill -TERM -- "-$child"' in source and 'trap forward_term TERM INT' in source
    assert '--authorization "$authorization" --runtime "$runtime" --execute' in source
    assert '--config "$config" --evidence "$evidence"' in source
    assert '[[ $# -eq 4 ]]' in source
    assert "pip install" not in source and "sbatch " not in source


def test_slurm_bash_syntax_when_native_bash_is_available():
    candidates = [Path("C:/Program Files/Git/bin/bash.exe"), Path("/bin/bash")]
    found = shutil.which("bash")
    if found and "system32" not in found.lower():
        candidates.append(Path(found))  # Avoid launching the Windows WSL shim.
    bash = next((path for path in candidates if path.is_file()), None)
    if bash is None:
        pytest.skip("native Bash parser unavailable; template was checked statically only")
    checked = subprocess.run([str(bash), "--noprofile", "--norc", "-n",
                              str(ROOT / "environments/training/train.slurm")],
                             capture_output=True, text=True, timeout=15, check=False)
    if checked.returncode == 3221225794 and "NtCreateDirectoryObject" in checked.stderr:
        pytest.skip("Bash cannot initialize in this sandbox (Windows named-object access denied)")
    assert checked.returncode == 0, "Bash syntax check failed"
