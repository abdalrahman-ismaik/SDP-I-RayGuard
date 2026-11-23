"""Sequential T41 study bookkeeping, with separate synthetic and authorized entries.

The optional Optuna factory checks execution evidence before importing Optuna.
Nothing here evaluates COCO or imports model packages.
"""

import json
import math
import os
import time
import traceback
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path

from sdp_xray.training import _digest, _sha256, _text
from sdp_xray.training_partition import fingerprint, validate_partition
from sdp_xray.training_research import (
    protocol_settings,
    require_live_ready,
    task_identity,
    validate_initialization,
)


def make_study_definition(config, partition, annotation_sha256, *, execution_kind="synthetic_software_check"):
    """Freeze a study's config, initialization, split, objective and execution label."""
    if execution_kind not in ("synthetic_software_check", "model_training"):
        raise ValueError("unknown execution kind")
    validate_partition(partition)
    validate_initialization(config["initialization"], config["task"])
    objective = config["objective"]
    if (config["experiment"] != "controlled_improvement"
            or config["study"] != protocol_settings() or not _digest(annotation_sha256)
            or annotation_sha256 != config["sources"]["validation"]["annotation_sha256"]
            or config["sources"]["validation"] in (config["sources"]["train"], config["sources"]["test"])
            or config["partition_sha256"] != partition["membership_sha256"]
            or objective.get("name") != "coco_bbox_AP_50_95"
            or objective.get("scale") != "fraction" or objective.get("direction") != "maximize"
            or not _text(objective.get("evaluator_id"))
            or not isinstance(objective.get("settings"), dict) or not objective["settings"]
            or type(config["batch"]) is not int or config["batch"] <= 0):
        raise ValueError("study settings/validation/objective identity are incomplete")
    return {
        "schema_version": "t41-study-definition-1", "execution_kind": execution_kind,
        "configuration": deepcopy(config), "task": task_identity(config["task"]),
        "partition": deepcopy(partition),
        "partition_sha256": partition["membership_sha256"],
        "validation_ids": partition["validation_ids"], "annotation_sha256": annotation_sha256,
        "objective": deepcopy(objective), "training_started": False,
    }


def validate_parameters(parameters):
    space = protocol_settings()["search_space"]
    if (not isinstance(parameters, dict)
            or set(parameters) != {"optimizer", "lr0", "weight_decay", "lrf", "mosaic"}
            or parameters["optimizer"] not in ("SGD", "AdamW")):
        raise ValueError("trial parameters do not match the declared conditional search space")
    for key in ("lr0", "weight_decay", "lrf", "mosaic"):
        value = parameters[key]
        bounds = space[parameters["optimizer"] + "_lr0"] if key == "lr0" else space[key]
        if type(value) not in (int, float) or not math.isfinite(value) or not bounds[0] <= value <= bounds[1]:
            raise ValueError("trial parameter outside frozen search space")


def validation_request(definition, checkpoint_sha256, completed_epoch):
    return {"checkpoint_sha256": checkpoint_sha256, "completed_epoch": completed_epoch,
            **{key: deepcopy(definition[key]) for key in
               ("task", "partition_sha256", "validation_ids", "annotation_sha256", "objective")}}


def validate_objective_result(request, result) -> float:
    """Proposed Ali interface: exact identities and complete IDs, not merely a count."""
    if not isinstance(result, dict) or set(result) != {
        "status", "checkpoint_sha256", "completed_epoch", "task", "partition_sha256",
        "annotation_sha256", "objective", "evaluated_image_ids", "value",
    } or result["status"] != "ok" or type(result["completed_epoch"]) is not int:
        raise ValueError("validation failed or has incomplete result fields")
    for key in ("checkpoint_sha256", "completed_epoch", "task", "partition_sha256",
                "annotation_sha256", "objective"):
        if result[key] != request[key]:
            raise ValueError("validation checkpoint/split/task/objective identity mismatch")
    ids = result["evaluated_image_ids"]
    if (not isinstance(ids, list) or not ids or any(type(i) is not int for i in ids)
            or len(set(ids)) != len(ids) or sorted(ids) != sorted(request["validation_ids"])):
        raise ValueError("validation must cover exactly every declared validation image")
    value = result["value"]
    if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("finite COCO AP in [0,1] required; failures are not zero AP")
    return float(value)


def _write_new(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


class StudyLedger:
    """Exclusive run directory and append-only, linked JSON snapshots.

    Each snapshot contains BOTH orchestration and sampler state. Torn snapshots,
    stale locks and mismatched definitions fail closed; no automatic repair.
    Filesystem locking still requires separate qualification on HPC storage.
    """

    def __init__(self, output, definition, *, resume=False):
        self.root = Path(output)
        self.definition = deepcopy(definition)
        self.identity = fingerprint(definition)
        self.generation, self.previous_hash = -1, None
        if self.root.is_symlink():
            raise ValueError("study output must not be a symlink")
        if resume:
            if (self.root / "study.json").is_symlink():
                raise ValueError("study definition must not be a symlink")
            stored = json.loads((self.root / "study.json").read_text(encoding="utf-8"))
            if stored != definition:
                raise ValueError("resume fingerprint differs; create a new study")
        else:
            self.root.mkdir(parents=False, exist_ok=False)
            _write_new(self.root / "study.json", definition)

    @contextmanager
    def locked(self):
        path = self.root / "writer.lock"
        with path.open("x", encoding="ascii") as stream:
            stream.write("single T41 writer; stale locks require human recovery\n")
        try:
            yield
        finally:
            path.unlink()

    def load(self):
        state, previous = None, None
        paths = sorted(self.root.glob("state-*.json"))
        for generation, path in enumerate(paths):
            if path.is_symlink() or path.name != f"state-{generation:06d}.json":
                raise ValueError("study snapshot sequence is incomplete")
            envelope = json.loads(path.read_text(encoding="utf-8"))
            payload = envelope["payload"]
            if (envelope.get("sha256") != fingerprint(payload)
                    or payload.get("previous_sha256") != previous
                    or payload.get("definition_sha256") != self.identity
                    or payload.get("generation") != generation):
                raise ValueError("study snapshot/sampler identity or integrity mismatch")
            previous, state = envelope["sha256"], payload
        if state is None:
            raise ValueError("no completed study snapshot; do not silently restart")
        self.generation, self.previous_hash = state["generation"], previous
        return state, previous

    def save(self, state, backend):
        state = deepcopy(state)
        state["sampler_state"] = deepcopy(backend.snapshot())
        state["definition_sha256"] = self.identity
        state.update(generation=self.generation + 1, previous_sha256=self.previous_hash)
        envelope = {"payload": state, "sha256": fingerprint(state)}
        _write_new(self.root / f"state-{state['generation']:06d}.json", envelope)
        self.generation, self.previous_hash = state["generation"], envelope["sha256"]


def _checkpoint(root, path):
    path = Path(path)
    resolved = path.resolve(strict=True)
    if path.is_symlink() or not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError("checkpoint must be a regular file inside its owned attempt directory")
    return {"path": str(resolved), "sha256": _sha256(resolved)}


def _resume_checkpoint(root, record):
    if record is None:
        return None
    path = root / record["path"]
    checked = _checkpoint(root, path)
    if checked["sha256"] != record["sha256"]:
        raise ValueError("saved checkpoint changed; resume is blocked")
    return checked["path"]


class TrialPruned(Exception):
    """Internal control flow, never converted to zero AP."""


def _prepare_attempt(ledger, definition, trial):
    attempt = len(trial["attempts"])
    relative = Path(f"trial-{trial['number']:03d}") / f"attempt-{attempt:03d}"
    directory = ledger.root / relative
    directory.parent.mkdir(exist_ok=True)
    directory.mkdir(exist_ok=False)
    resume_from = _resume_checkpoint(ledger.root, trial["last_checkpoint"])
    trial["attempts"].append({"directory": relative.as_posix(), "status": "running"})
    trial["status"] = "running"
    request = {"number": trial["number"], "parameters": deepcopy(trial["parameters"]),
               "configuration": deepcopy(definition["configuration"]),
               "output_directory": directory, "resume_checkpoint": resume_from,
               "completed_epochs": len(trial["reports"]), "epochs": 30,
               "initialization": deepcopy(definition["configuration"]["initialization"])}
    return request


def run_synthetic_study(definition, output, backend, trainer, evaluator, *, resume=False,
                        retry_interrupted=False, stop_requested=lambda: False,
                        budget_seconds=None, clock=time.monotonic, attempt_limit=None):
    return _run_study(definition, output, backend, trainer, evaluator, resume=resume,
                      retry_interrupted=retry_interrupted, stop_requested=stop_requested,
                      budget_seconds=budget_seconds, clock=clock, attempt_limit=attempt_limit)


def run_approved_study(definition, output, backend, trainer, evaluator, plan, authorization, **options):
    require_live_ready(plan, authorization)
    if authorization["stage"] != "search" or definition["configuration"] != plan["configuration"]:
        raise ValueError("search authorization/configuration mismatch")
    if options.get("budget_seconds", authorization["max_seconds"]) != authorization["max_seconds"]:
        raise ValueError("study time budget differs from authorization")
    options["budget_seconds"] = authorization["max_seconds"]
    return _run_study(definition, output, backend, trainer, evaluator,
                      live=True, **options)


def _run_study(definition, output, backend, trainer, evaluator, *, resume=False,
                retry_interrupted=False, stop_requested=lambda: False,
                budget_seconds=None, clock=time.monotonic, live=False, attempt_limit=None):
    """Shared state transitions, with the public live entry checking authorization.

    backend: ask/report/should_prune/tell/snapshot/restore; trainer: run(request)
    yields completed-epoch events, or run_with_callback(request, on_epoch) reports
    them synchronously. Evaluator: evaluate(request) or the private-path binding
    evaluate_checkpoint(request, checkpoint). Portable request/result fields stay unchanged.
    Synthetic adapters must explicitly declare synthetic=True. No model imports here.
    """
    execution_kind = "model_training" if live else "synthetic_software_check"
    if definition.get("execution_kind") != execution_kind or any(
        (getattr(adapter, "synthetic", False) is True) != (not live)
        for adapter in (backend, trainer, evaluator)
    ):
        raise ValueError("synthetic adapters cannot be mixed with live training")
    if definition != make_study_definition(definition["configuration"], definition["partition"],
                                           definition["annotation_sha256"], execution_kind=execution_kind):
        raise ValueError("inconsistent study definition")
    if budget_seconds is not None and (type(budget_seconds) not in (int, float)
                                      or not math.isfinite(budget_seconds) or budget_seconds < 0):
        raise ValueError("finite nonnegative time budget required")
    settings = definition["configuration"]["study"]
    if settings != protocol_settings():
        raise ValueError("study protocol changed")
    if attempt_limit is not None and (type(attempt_limit) is not int or not 1 <= attempt_limit <= 20):
        raise ValueError("allocation attempt limit must be an integer in [1,20]")
    started, attempted_here = clock(), 0
    def stopping():
        return stop_requested() or (budget_seconds is not None and clock() - started >= budget_seconds)
    ledger = StudyLedger(output, definition, resume=resume)
    with ledger.locked():
        if resume:
            state, _ = ledger.load()
            backend.restore(deepcopy(state["sampler_state"]))
            if len(state["trials"]) > 20:
                raise ValueError("study exceeds its configuration budget")
            for trial in state["trials"]:
                for record in (trial["last_checkpoint"], trial["best_checkpoint"]):
                    _resume_checkpoint(ledger.root, record)
            if any(t["status"] in ("running", "interrupted") for t in state["trials"]):
                if live:
                    raise ValueError("live checkpoint continuation is unqualified; preserve the interrupted attempt")
                if not retry_interrupted:
                    raise ValueError("explicit retry_interrupted required; no new configuration")
        else:
            state = {"schema_version": "t41-study-state-1", "trials": [],
                     "execution_kind": execution_kind, "training_started": False}
            ledger.save(state, backend)
        while not stopping():
            if attempt_limit is not None and attempted_here >= attempt_limit:
                break  # Stop only between attempts; never claim checkpoint continuation.
            unfinished = [t for t in state["trials"] if t["status"] in ("running", "interrupted")]
            if len(unfinished) > 1:
                raise ValueError("sequential study has multiple unfinished trials")
            if unfinished:
                trial = unfinished[0]
                if trial["attempts"]:
                    trial["attempts"][-1]["status"] = "interrupted"
            else:
                if len(state["trials"]) == 20:
                    break
                number = len(state["trials"])
                control = deepcopy(settings["control"]) if number == 0 else None
                parameters = backend.ask(number, control)
                validate_parameters(parameters)
                if control is not None and parameters != control:
                    raise ValueError("first attempted configuration must be the queued control")
                trial = {"number": number, "role": "untuned_control" if number == 0 else "search",
                         "parameters": parameters, "parameters_sha256": fingerprint(parameters),
                         "status": "running", "attempts": [], "reports": [],
                         "value": None, "best_checkpoint": None, "last_checkpoint": None,
                         "failure": None}
                state["trials"].append(trial)
                ledger.save(state, backend)  # Keep ask's sampler state before invoking the trainer.
            request = _prepare_attempt(ledger, definition, trial)
            attempted_here += 1
            ledger.save(state, backend)
            try:
                def completed_epoch(event):
                    state["training_started"] |= live and getattr(trainer, "training_started", False)
                    if event.get("phase") == "final_evaluation":
                        return  # Upstream calls on_fit_epoch_end again here.
                    epoch = event.get("completed_epoch")
                    if event.get("phase") != "fit" or type(epoch) is not int or not 1 <= epoch <= 30:
                        raise ValueError("completed fit epoch must be an integer in [1,30]")
                    checkpoint = _checkpoint(request["output_directory"], event["checkpoint"])
                    checkpoint["path"] = Path(checkpoint["path"]).relative_to(ledger.root.resolve()).as_posix()
                    if epoch <= len(trial["reports"]):
                        previous = trial["reports"][epoch - 1]
                        if checkpoint["sha256"] != previous["checkpoint"]["sha256"]:
                            raise ValueError("duplicate epoch has a different checkpoint")
                        return
                    if epoch != len(trial["reports"]) + 1:
                        raise ValueError("missing completed epoch; pruning steps must match")
                    validation = validation_request(definition, checkpoint["sha256"], epoch)
                    if hasattr(evaluator, "evaluate_checkpoint"):
                        result = evaluator.evaluate_checkpoint(
                            deepcopy(validation), ledger.root / checkpoint["path"])
                    else:
                        result = evaluator.evaluate(deepcopy(validation))
                    value = validate_objective_result(validation, result)
                    trial["reports"].append({"epoch": epoch, "value": value, "checkpoint": checkpoint})
                    trial["last_checkpoint"] = checkpoint
                    if trial["best_checkpoint"] is None or value > max(
                        (r["value"] for r in trial["reports"][:-1]), default=-1
                    ):
                        trial["best_checkpoint"] = checkpoint
                    backend.report(trial["number"], value, epoch)
                    ledger.save(state, backend)
                    if stopping():
                        raise KeyboardInterrupt
                    completed = sum(t["status"] == "complete" for t in state["trials"])
                    if epoch >= 10 and completed >= 5 and backend.should_prune(trial["number"]):
                        raise TrialPruned
                    return value
                if hasattr(trainer, "run_with_callback"):
                    trainer.run_with_callback(request, completed_epoch)
                else:
                    for event in trainer.run(request):
                        completed_epoch(event)
                if not trial["reports"]:
                    raise ValueError("trainer returned no completed validation epochs")
                # Early stop is valid only when the trainer explicitly records that decision.
                if len(trial["reports"]) != 30:
                    raise ValueError("incomplete trial; explicit interruption/resume required")
                _resume_checkpoint(ledger.root, trial["best_checkpoint"])
                trial["value"] = max(r["value"] for r in trial["reports"])
                trial["status"] = "complete"
            except KeyboardInterrupt:
                trial["status"] = "interrupted"
            except TrialPruned:
                trial["status"] = "pruned"
            except Exception as exc:
                trial["status"], trial["failure"] = "failed", type(exc).__name__
                trial["failure_message"] = str(exc)
                traceback.print_exc()
            trial["attempts"][-1]["status"] = trial["status"]
            state["training_started"] |= live and getattr(trainer, "training_started", False)
            if trial["status"] != "complete":
                trial["value"] = None
            if trial["status"] != "interrupted":
                backend.tell(trial["number"], trial["status"], trial["value"])
            ledger.save(state, backend)
            if trial["status"] == "interrupted":
                break
        return export_study(ledger.root)


def export_study(directory, output=None):
    directory = Path(directory)
    definition = json.loads((directory / "study.json").read_text(encoding="utf-8"))
    ledger = StudyLedger(directory, definition, resume=True)
    state, digest = ledger.load()
    exported = {"definition": definition, "definition_sha256": ledger.identity,
                "snapshot_sha256": digest, "execution_kind": state["execution_kind"],
                "training_started": state["training_started"],
                "attempted_configurations": len(state["trials"]),
                "trainer_invocations": sum(len(t["attempts"]) for t in state["trials"]),
                "trials": state["trials"]}
    if output is not None:
        _write_new(Path(output), exported)
    return deepcopy(exported)


def confirmation_plan(exported):
    """Separate planned compute, not additional search trials or completed runs."""
    completed = sorted((t for t in exported["trials"] if t["status"] == "complete"),
                       key=lambda t: (-t["value"], t["number"]))
    if not completed:
        return []
    by_number = {t["number"]: t for t in exported["trials"]}
    numbers = list(dict.fromkeys([0, *(t["number"] for t in completed[:3])]))
    return [{"stage": "confirmation", "status": "planned", "source_trial": n,
             "parameters": deepcopy(by_number[n]["parameters"]), "epochs": 100, "seed": 17,
             "definition_sha256": exported["definition_sha256"],
             "output_key": f"confirmation/trial-{n:03d}/seed-17",
             "checkpoint_sha256": None, "value": None} for n in numbers]


def repeatability_plan(exported, confirmed):
    """Accept validation-selected 100-epoch confirmations; preserve/reuse seed 17."""
    expected = {r["source_trial"]: r for r in confirmation_plan(exported)}
    if (not confirmed or len(confirmed) != len(expected)
            or set(r["source_trial"] for r in confirmed) != set(expected)):
        raise ValueError("record all scheduled confirmations, including explicit failures")
    valid = []
    for result in confirmed:
        target = expected[result["source_trial"]]
        for key in ("parameters", "epochs", "seed", "definition_sha256", "output_key", "stage"):
            if result.get(key) != target[key]:
                raise ValueError("confirmation differs from the frozen plan")
        if result.get("status") == "complete":
            value = result.get("value")
            if (type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1
                    or not _digest(result.get("checkpoint_sha256"))):
                raise ValueError("completed confirmation needs validation AP and actual checkpoint")
            validation = result.get("validation") or {}
            epoch = validation.get("completed_epoch")
            if type(epoch) is not int or not 1 <= epoch <= 100:
                raise ValueError("confirmation needs its completed validation epoch")
            request = validation_request(exported["definition"], result["checkpoint_sha256"], epoch)
            if validate_objective_result(request, validation) != value:
                raise ValueError("confirmation value differs from the frozen validation objective")
            valid.append(result)
        elif result.get("status") not in ("failed", "interrupted") or result.get("value") is not None:
            raise ValueError("failed/interrupted confirmations are not zero AP")
    controls = [r for r in valid if r["source_trial"] == 0]
    if not controls or not valid:
        return []
    selected = min(valid, key=lambda r: (-r["value"], r["source_trial"]))
    chosen = {r["source_trial"]: r for r in [controls[0], selected]}
    return [{"stage": "repeatability", "source_trial": n, "parameters": result["parameters"],
             "epochs": 100, "seed": seed, "status": "reuse" if seed == 17 else "planned",
             "definition_sha256": exported["definition_sha256"],
             "output_key": result["output_key"] if seed == 17 else f"repeat/trial-{n:03d}/seed-{seed}",
             "checkpoint_sha256": result["checkpoint_sha256"] if seed == 17 else None,
             "value": result["value"] if seed == 17 else None}
            for n, result in chosen.items() for seed in (17, 29, 43)]


def open_optuna_backend(plan, directory, name, authorization=None):
    """Future integration boundary. Gates run BEFORE optional imports or storage access."""
    require_live_ready(plan, authorization)
    import optuna  # Optional, not installed or imported by this draft's checks.
    from optuna.storages import JournalStorage
    from optuna.storages.journal import JournalFileBackend

    if optuna.__version__ != "4.5.0":
        raise ValueError("Optuna version differs from the qualified proposal")
    sampler = optuna.samplers.TPESampler(seed=17, n_startup_trials=5)
    pruner = optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=10)
    study = optuna.create_study(
        study_name=name, direction="maximize", sampler=sampler, pruner=pruner,
        storage=JournalStorage(JournalFileBackend(str(Path(directory) / "optuna.journal"))),
        load_if_exists=True,
    )
    return _OptunaBackend(optuna, study, fingerprint(plan["configuration"]))


class _OptunaBackend:
    """Unexecuted Optuna 4.5 adapter; JSON RNG state avoids unpickling sampler files.

    Two private RandomState fields are version-specific and remain qualification
    gates. Journal trial signatures must match a snapshot before restoring RNG.
    """
    synthetic = False

    def __init__(self, optuna, study, identity):
        self.optuna, self.study, self.identity, self.active = optuna, study, identity, {}
        old = study.user_attrs.get("t41_fingerprint")
        if old not in (None, identity) or (old is None and study.trials):
            raise ValueError("existing journal belongs to another study")
        study.set_user_attr("t41_fingerprint", identity)

    def ask(self, number, control):
        if number != len(self.study.trials):
            raise ValueError("journal advanced without matching ledger; recovery required")
        if control is not None:
            queued = deepcopy(control)
            queued["SGD_lr0"] = queued.pop("lr0")
            self.study.enqueue_trial(queued)
        trial = self.study.ask()
        self.active[number] = trial
        optimizer = trial.suggest_categorical("optimizer", ["SGD", "AdamW"])
        space = protocol_settings()["search_space"]
        return {"optimizer": optimizer,
                "lr0": trial.suggest_float(optimizer + "_lr0", *space[optimizer + "_lr0"], log=True),
                **{key: trial.suggest_float(key, *space[key], log=key != "mosaic")
                   for key in ("weight_decay", "lrf", "mosaic")}}

    def report(self, number, value, epoch):
        self.active[number].report(value, epoch)

    def should_prune(self, number):
        return self.active[number].should_prune()

    def tell(self, number, status, value):
        state = {"complete": self.optuna.trial.TrialState.COMPLETE,
                 "failed": self.optuna.trial.TrialState.FAIL,
                 "pruned": self.optuna.trial.TrialState.PRUNED}[status]
        self.study.tell(number, value if status == "complete" else None, state=state)
        self.active.pop(number, None)

    def _signature(self):
        return fingerprint([{"number": t.number, "state": t.state.name, "params": t.params,
                             "values": t.values, "reports": t.intermediate_values}
                            for t in self.study.trials])

    def snapshot(self):
        sampler = self.study.sampler
        def encode(rng):
            algorithm, keys, position, gaussian, cached = rng.get_state()
            return [algorithm, keys.tolist(), position, gaussian, cached]
        return {"version": "4.5.0", "identity": self.identity, "journal_sha256": self._signature(),
                "tpe_rng": encode(sampler._rng.rng),
                "random_rng": encode(sampler._random_sampler._rng.rng)}

    def restore(self, state):
        if (state["version"] != "4.5.0" or state["identity"] != self.identity
                or state["journal_sha256"] != self._signature()):
            raise ValueError("journal/sampler snapshot mismatch; no automatic replay")
        import numpy as np

        sampler = self.study.sampler
        for rng, values in ((sampler._rng.rng, state["tpe_rng"]),
                            (sampler._random_sampler._rng.rng, state["random_rng"])):
            rng.set_state((values[0], np.array(values[1], dtype=np.uint32), *values[2:]))
        self.active = {t.number: self.optuna.trial.Trial(self.study, t._trial_id)
                       for t in self.study.trials if t.state == self.optuna.trial.TrialState.RUNNING}
