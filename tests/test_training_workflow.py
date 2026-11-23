"""Execution receipts and orchestration with invented approvals and fake trainers only."""

import io
import json
import os
import runpy
import socket
import subprocess
import sys
from contextlib import redirect_stdout
from copy import deepcopy
from itertools import count
from pathlib import Path
from unittest.mock import patch

import pytest
from test_training_backend import (
    FakeBoundEvaluator,
    FakeUpstreamTrainer,
    bundle_case,
    prepared_case,
)
from test_training_research import ROOT, digest, init_receipt, research_case, review
from test_tuning import FakeEvaluator, FakeSampler, FakeTrainer, definition

from sdp_xray.training_backend import (
    CheckpointValidationAdapter,
    YoloTrainerAdapter,
    prepare_training_bundle,
)
from sdp_xray.training_partition import fingerprint
from sdp_xray.training_research import audit_findings, inspect_partition_sources, research_plan
from sdp_xray.training_workflow import (
    CHECKS,
    estimate_study_hours,
    execution_plan,
    execution_request_example,
    execution_scope,
    experiment_identity,
    load_validation_adapter,
    offline_runtime,
    run_stage,
    run_workflow,
    verify_runtime,
    verify_validation_inputs,
)
from sdp_xray.tuning import run_synthetic_study


def request_case(tmp_path, stage="pilot"):
    config, evidence = research_case()
    config["output_directory"] = str(tmp_path / "new-owned-run")
    config["validation_prediction"] = {"conf": 0.001, "max_det": 100}  # Synthetic choice only.
    plan = research_plan(config, evidence)
    request = execution_request_example(plan, stage)
    request.update(max_seconds=60, pilot_epochs=2 if stage == "pilot" else None,
                   runtime_sha256=digest("synthetic private runtime"),
                   python_version=sys.version.split()[0],
                   packages={key: "synthetic-version" for key in
                             ("torch", "torchvision", "ultralytics", "numpy", "pycocotools", "optuna")},
                   runtime_files=[{"path": str(tmp_path / "qualified-source.py"), "sha256": digest("source")}],
                   evaluator={"file": str(tmp_path / "adapter.py"), "factory": "create", "sha256": digest("adapter")},
                   pilot_receipt_sha256=None if stage == "pilot" else digest("synthetic pilot"))
    request["checks"] = {key: review() for key in CHECKS}
    request["checks"]["weights_on_execution_host"]["verified_sha256"] = config["initialization"]["checkpoint_sha256"]
    request["review"] = {**review(), "scope_sha256": execution_scope(request)}
    return plan, request


@pytest.mark.parametrize("stage", ["pilot", "search", "confirmation", "repeatability"])
def test_execution_requires_bound_separate_receipts_without_imports(tmp_path, stage):
    plan, request = request_case(tmp_path, stage)
    before = deepcopy(plan)
    with patch("sdp_xray.training_workflow.run_workflow", side_effect=AssertionError("dispatch")):
        assert execution_plan(plan, request)["blockers"] == []
    assert plan == before and execution_plan(plan, request)["training_started"] is False
    request["max_seconds"] = 61
    assert "execution:reviewed_scope_required" in execution_plan(plan, request)["blockers"]


@pytest.mark.parametrize("field", ["configuration_sha256", "evidence_sha256", "implementation_sha256",
                                  "runtime_sha256", "review", "evaluator", "runtime_files", "packages",
                                  "python_version", "max_seconds", "pilot_epochs"])
def test_missing_execution_evidence_blocks(tmp_path, field):
    plan, request = request_case(tmp_path)
    request[field] = None
    request["review"] = {**review(), "scope_sha256": execution_scope(request)} if field != "review" else None
    assert execution_plan(plan, request)["blockers"]


def test_pilot_needs_preflight_but_cannot_claim_completed_qualification(tmp_path):
    plan, request = request_case(tmp_path)
    plan["configuration"]["environment"]["qualification"] = None
    plan["configuration"]["approvals"]["common_initialization_comparison"] = None
    request["configuration_sha256"] = fingerprint(plan["configuration"])
    request["review"] = {**review(), "scope_sha256": execution_scope(request)}
    assert execution_plan(plan, request)["blockers"] == []
    request.update(stage="search", pilot_epochs=None)
    request["review"] = {**review(), "scope_sha256": execution_scope(request)}
    blocked = execution_plan(plan, request)["blockers"]
    assert "environment:allocated_train_save_reload_and_storage_unqualified" in blocked
    assert "execution:qualified_pilot_receipt" in blocked
    request["checks"]["environment_preflight"] = None
    assert "execution:environment_preflight" in execution_plan(plan, request)["blockers"]


def test_output_collision_cannot_dispatch_or_replace_work(tmp_path):
    plan, request = request_case(tmp_path)
    output = Path(plan["configuration"]["output_directory"])
    output.mkdir()
    (output / "existing").write_text("keep")
    with patch("sdp_xray.training_workflow.verify_runtime", side_effect=AssertionError("runtime")):
        with pytest.raises(ValueError, match="requirements"):
            run_workflow(plan, request, {})
    assert (output / "existing").read_text() == "keep"


def test_unsupported_hpc_python_blocks_even_when_request_matches_host(tmp_path):
    plan, request = request_case(tmp_path)
    request["python_version"] = "3.10.22"
    request["review"] = {**review(), "scope_sha256": execution_scope(request)}
    assert "execution:python_requires_3_11_to_3_14" in execution_plan(plan, request)["blockers"]
    with patch("sys.version", "3.10.22 (synthetic unsupported interpreter)"), \
            patch.dict(os.environ, {"SLURM_JOB_ID": "fixture", "CUDA_VISIBLE_DEVICES": "fixture"}), \
            patch("importlib.metadata.version", side_effect=AssertionError("must stop before packages")):
        with pytest.raises(ValueError, match="qualified interpreter"):
            verify_runtime(request)


@pytest.mark.parametrize("script", ["finetune_yolov10.py", "tune_yolov10.py"])
def test_cli_template_remains_incomplete_and_execute_never_dispatches(tmp_path, script):
    main = runpy.run_path(str(ROOT / "scripts" / script))["main"]
    template = tmp_path / "execution.json"
    with redirect_stdout(io.StringIO()), patch("sdp_xray.training_workflow.run_workflow",
                                               side_effect=AssertionError("dispatch")):
        assert main(["--write-execution-template", str(template)]) == 2
        assert main(["--execute", "--authorization", str(template)]) == 2
    receipt = json.loads(template.read_text())
    assert receipt["review"] is None and receipt["runtime_sha256"] is None
    with redirect_stdout(io.StringIO()) as output:
        assert main([]) == 2
    blocked = json.loads(output.getvalue())["blockers"]
    assert "execution:reviewed_request_required" in blocked
    assert "integration:live_trainer_not_connected" not in blocked
    assert not any(name in sys.modules for name in ("torch", "ultralytics", "optuna"))


def test_offline_guard_blocks_network_subprocesses_and_restores_state(tmp_path):
    original = subprocess.Popen
    with offline_runtime(tmp_path / "settings"):
        assert os.environ["YOLO_AUTOINSTALL"] == "false"
        with pytest.raises(OSError, match="disabled"):
            socket.create_connection(("unused.invalid", 1))
        with socket.socket() as connection:
            for connect in (connection.connect, connection.connect_ex):
                with pytest.raises(OSError, match="disabled"):
                    connect(("unused.invalid", 1))
        with pytest.raises(RuntimeError, match="disabled"):
            subprocess.Popen(["never-dispatched"])
    assert subprocess.Popen is original


def test_pinned_fork_connectivity_probe_can_report_offline(tmp_path):
    # Pinned ultralytics.utils.is_online catches these errors during module import.
    with offline_runtime(tmp_path / "settings"):
        try:
            socket.create_connection(("unused.invalid", 53), timeout=2)
        except (socket.timeout, socket.gaierror, OSError):
            online = False
        else:
            online = True
    assert online is False


def test_runtime_checks_precede_optional_import_and_reject_changed_files(tmp_path):
    _, request = request_case(tmp_path)
    source = tmp_path / "qualified-source.py"
    source.write_text("source")
    adapter = tmp_path / "adapter.py"
    adapter.write_text("adapter")
    with patch.dict(os.environ, {"SLURM_JOB_ID": "synthetic", "CUDA_VISIBLE_DEVICES": "GPU-synthetic"}), \
            patch("importlib.metadata.version", return_value="synthetic-version"):
        verify_runtime(request)
        source.write_text("changed")
        with pytest.raises(ValueError, match="changed"):
            verify_runtime(request)


def test_bound_validation_factory_loading_and_hash_rejection(tmp_path):
    path = tmp_path / "adapter.py"
    content = "class Adapter:\n    def evaluate_checkpoint(self, request, checkpoint):\n        raise NotImplementedError\ndef create(context):\n    return Adapter()\n"
    path.write_text(content, encoding="utf-8", newline="\n")
    request = {"evaluator": {"file": str(path), "factory": "create", "sha256": digest(content)}}
    assert callable(load_validation_adapter(request, {}).evaluate_checkpoint)
    path.write_text("raise AssertionError('must not execute')")
    with pytest.raises(ValueError, match="changed"):
        load_validation_adapter(request, {})


def test_pilot_callback_stage_snapshot_selection_and_timing(tmp_path):
    config, _, weights, bundle, definition = prepared_case(tmp_path)
    exported = {"definition": definition, "definition_sha256": fingerprint(definition),
                "execution_kind": "synthetic_software_check", "trials": []}
    result = run_stage(exported, "pilot", tmp_path / "pilot",
                       YoloTrainerAdapter(FakeUpstreamTrainer, weights, bundle),
                       CheckpointValidationAdapter(FakeBoundEvaluator()),
                       {"17": config["initialization"]}, pilot_epochs=3, clock=count(1).__next__)
    row = result["results"][0]
    assert row["status"] == "complete" and row["value"] == 0.8
    assert row["checkpoint"].endswith("epoch-002.pt")
    assert result["training_started"] is False and len(row["reports"]) == 3
    projection = estimate_study_hours(result)
    assert projection["per_task_epoch_ceilings"] == {"search": 600, "confirmation": 400, "repeatability_new_runs": 400}
    assert projection["execution_kind"] == "synthetic_software_check" and not projection["approved_compute"]


class StageTrainer:
    synthetic = True

    def __init__(self, interrupt=False):
        self.calls, self.interrupt = [], interrupt

    def run(self, request):
        self.calls.append(deepcopy(request))
        for epoch in range(1, request["epochs"] + 1):
            checkpoint = request["output_directory"] / f"epoch-{epoch}.txt"
            checkpoint.write_text(f"synthetic {request['number']} {request['seed']} {epoch}")
            event = {"phase": "fit", "completed_epoch": epoch, "checkpoint": checkpoint}
            yield event
            yield event  # Duplicate notifications must not create duplicate reports.
            if self.interrupt:
                raise KeyboardInterrupt


def test_confirmation_repeatability_keep_receipts_budgets_and_reuse(tmp_path):
    sampler = FakeSampler()
    exported = run_synthetic_study(definition(), tmp_path / "study", sampler, FakeTrainer(), FakeEvaluator(),
                                    stop_requested=lambda: len(sampler.tells) == 3)
    receipts = {str(seed): {**init_receipt(), "seed": seed} for seed in (17, 29, 43)}
    trainer = StageTrainer()
    confirmed = run_stage(exported, "confirmation", tmp_path / "confirm", trainer, FakeEvaluator(), receipts)
    assert len(confirmed["results"]) == 3 and all(r["status"] == "complete" for r in confirmed["results"])
    assert all(len(r["reports"]) == 100 for r in confirmed["results"])
    repeated = run_stage(exported, "repeatability", tmp_path / "repeat", trainer, FakeEvaluator(), receipts,
                         confirmed=confirmed["results"])
    assert repeated["results"][0]["status"] == "reuse"
    assert repeated["trainer_invocations"] == 2  # Equal synthetic AP selects the control.
    assert [r["seed"] for r in trainer.calls[-2:]] == [29, 43]
    assert len({r["initialization"]["checkpoint_sha256"] for r in trainer.calls}) == 1
    assert exported["attempted_configurations"] == 3  # Post-search work never asks Optuna.
    with pytest.raises(FileExistsError):
        run_stage(exported, "confirmation", tmp_path / "confirm", trainer, FakeEvaluator(), receipts)


@pytest.mark.parametrize("failure", ["interrupt", "nonfinite", "checkpoint", "coverage"])
def test_stage_failure_never_becomes_zero_ap(tmp_path, failure):
    item = definition()
    exported = {"definition": item, "definition_sha256": fingerprint(item),
                "execution_kind": "synthetic_software_check", "trials": []}
    def edit(result):
        if failure == "nonfinite":
            result["value"] = float("nan")
        elif failure == "checkpoint":
            result["checkpoint_sha256"] = "0" * 64
        elif failure == "coverage":
            result["evaluated_image_ids"] = []
    result = run_stage(exported, "pilot", tmp_path / "pilot", StageTrainer(failure == "interrupt"),
                       FakeEvaluator(edit), {"17": init_receipt()}, pilot_epochs=2)
    row = result["results"][0]
    assert row["status"] == ("interrupted" if failure == "interrupt" else "failed")
    assert row["value"] is None and row["checkpoint_sha256"] is None
    with pytest.raises(ValueError, match="completed"):
        estimate_study_hours(result)


def test_stage_stop_before_dispatch_and_changed_definition(tmp_path):
    item = definition()
    exported = {"definition": item, "definition_sha256": fingerprint(item),
                "execution_kind": "synthetic_software_check", "trials": []}
    trainer = StageTrainer()
    result = run_stage(exported, "pilot", tmp_path / "pilot", trainer, FakeEvaluator(),
                       {"17": init_receipt()}, pilot_epochs=2, stop_requested=lambda: True)
    assert not trainer.calls and result["results"][0]["status"] == "not_started"
    exported["definition_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="fingerprint"):
        run_stage(exported, "pilot", tmp_path / "bad", trainer, FakeEvaluator(), {"17": init_receipt()}, pilot_epochs=2)
    assert not (tmp_path / "bad").exists()


def test_experiment_identity_allows_new_phase_outputs_not_changed_science():
    config, _ = research_case()
    original = experiment_identity(config)
    config.update(output_directory="new stage", owner="new named human")
    config["environment"]["qualification"] = None
    assert experiment_identity(config) == original
    config["batch"] += 1
    assert experiment_identity(config) != original


def test_validation_context_is_bound_to_exact_partition_and_bytes(tmp_path):
    _, _, _, _, definition = prepared_case(tmp_path)
    context = {"annotation_file": str(tmp_path / "originals" / "validation.json"),
               "image_root": str(tmp_path / "originals")}
    path = Path(context["annotation_file"])
    document = json.loads(path.read_text())
    document["annotations"] = [{"id": 0, "image_id": definition["validation_ids"][0], "category_id": 0,
                                "bbox": [1, 1, 2, 2], "area": 4, "iscrowd": 0}]
    path.write_text(json.dumps(document), encoding="utf-8", newline="\n")
    definition["annotation_sha256"] = digest(json.dumps(document))
    verify_validation_inputs(context, definition)
    image_id = definition["validation_ids"][0]
    (tmp_path / "originals" / f"train-{image_id}.png").write_bytes(b"synthetic changed bytes")
    with pytest.raises(ValueError, match="bytes changed"):
        verify_validation_inputs(context, definition)


def test_workflow_composes_inputs_without_loading_or_running_a_model(tmp_path):
    config, _, sources, partition, weights = bundle_case(tmp_path)
    path = sources["validation"][0]
    truth = json.loads(path.read_text())
    truth["annotations"] = [{"id": 99, "image_id": partition["validation_ids"][0], "category_id": 0,
                             "bbox": [1, 1, 2, 2], "area": 4, "iscrowd": 0}]
    path.write_text(json.dumps(truth))
    evidence = inspect_partition_sources(sources, "generic", partition)
    config["sources"] = deepcopy(evidence["sources"])
    config["data_policy"]["audit_findings_sha256"] = fingerprint(audit_findings(evidence))
    bundle = prepare_training_bundle(config, sources, partition, tmp_path / "bundle")
    config.update(output_directory=str(tmp_path / "owned"), requested_device="0")
    config["validation_prediction"] = {"conf": 0.001, "max_det": 100}
    plan = research_plan(config, evidence)
    _, authorization = request_case(tmp_path)
    authorization["configuration_sha256"] = fingerprint(config)
    authorization["evidence_sha256"] = fingerprint(evidence)
    runtime = {"weights": str(weights), "bundle": str(bundle), "validation_context": {
        "annotation_file": str(tmp_path / "originals" / "validation.json"),
        "image_root": str(tmp_path / "originals")}}
    authorization["runtime_sha256"] = fingerprint(runtime)
    authorization["review"] = {**review(), "scope_sha256": execution_scope(authorization)}
    # The production composition is exercised only up to injected boundaries.
    # This fake stage performs no epochs and produces no model metric or weights.
    fixture = {"execution_kind": "synthetic_software_check", "training_started": False, "results": []}
    with patch.dict(os.environ, {"CUDA_VISIBLE_DEVICES": "GPU-synthetic"}), \
            patch("sdp_xray.training_workflow.verify_runtime", return_value={"synthetic": True}), \
            patch("sdp_xray.training_workflow.load_validation_adapter", return_value=object()), \
            patch("sdp_xray.training_backend.live_trainer_class", return_value=object), \
            patch("sdp_xray.training_backend.YoloTrainerAdapter", return_value=object()) as factory, \
            patch("sdp_xray.training_workflow.run_stage", return_value=fixture) as stage:
        result = run_workflow(plan, authorization, runtime)
    assert result == fixture
    assert factory.call_args.args[1:] == (weights, bundle)
    assert stage.call_args.args[1:3] == ("pilot", tmp_path / "owned" / "stage")
    assert stage.call_args.kwargs["authorization"] == authorization
    assert json.loads((tmp_path / "owned" / "workflow-result.json").read_text()) == fixture
    assert not any(name in sys.modules for name in ("torch", "ultralytics", "optuna"))


@pytest.mark.parametrize("script", ["finetune_yolov10.py", "tune_yolov10.py"])
def test_explicit_cli_dispatch_uses_reviewed_request_and_reports_failure_honestly(tmp_path, script):
    plan, request = request_case(tmp_path)
    runtime = {"synthetic": "not executed"}
    request["runtime_sha256"] = fingerprint(runtime)
    request["review"] = {**review(), "scope_sha256": execution_scope(request)}
    files = {}
    for key, content in (("config", plan["configuration"]), ("evidence", plan["evidence"]),
                         ("authorization", request), ("runtime", runtime)):
        files[key] = tmp_path / f"{key}.json"
        files[key].write_text(json.dumps(content))
    args = [item for key, path in files.items() for item in (f"--{key}", str(path))]
    main = runpy.run_path(str(ROOT / "scripts" / script))["main"]
    with patch("sdp_xray.training_workflow.run_workflow", side_effect=RuntimeError("private details")) as dispatch:
        with redirect_stdout(io.StringIO()) as output:
            assert main(args) == 0  # Ready planning still does not dispatch.
        assert json.loads(output.getvalue())["training_started"] is False
        dispatch.assert_not_called()
        with redirect_stdout(io.StringIO()) as output:
            assert main([*args, "--execute"]) == 1
        assert json.loads(output.getvalue())["training_started"] is None
        assert "private details" not in output.getvalue()
        dispatch.assert_called_once()
