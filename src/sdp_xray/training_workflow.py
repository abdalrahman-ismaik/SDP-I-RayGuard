"""Conditional execution checks, bounded stages and pilot accounting for T41.

No optional model packages are imported here. A reviewed execution request is
separate from both the research configuration and strict inference manifests.
"""

import importlib.metadata
import importlib.util
import json
import math
import os
import signal
import socket
import subprocess
import sys
import time
import traceback
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from sdp_xray.training import UPSTREAM_REVISION, _digest, _sha256, _text
from sdp_xray.training_partition import fingerprint, reviewed
from sdp_xray.training_qualification import supported_python
from sdp_xray.training_research import research_plan, validate_initialization
from sdp_xray.training_validation import check_prediction_settings
from sdp_xray.tuning import (
    confirmation_plan,
    make_study_definition,
    repeatability_plan,
    validate_objective_result,
    validate_parameters,
    validation_request,
)

STAGES = ("pilot", "search", "confirmation", "repeatability")
CHECKS = ("data_conversion", "validation_adapter", "offline_runtime", "allocated_resources",
          "weights_on_execution_host", "environment_preflight")
CODE_FILES = ("training.py", "training_research.py", "training_partition.py", "training_backend.py", "training_validation.py", "training_qualification.py", "training_checkpoint.py",
              "training_workflow.py", "tuning.py")
DRAFT_GATES = {"execution:software_draft_only", "integration:live_trainer_not_connected"}


def implementation_identity():
    root = Path(__file__).parent
    return fingerprint({name: _sha256(root / name) for name in CODE_FILES})


def execution_request_example(plan, stage="pilot"):
    if stage not in STAGES:
        raise ValueError("unknown workflow stage")
    return {"schema_version": "t41-execution-1", "stage": stage, "review": None,
            "configuration_sha256": fingerprint(plan["configuration"]),
            "evidence_sha256": fingerprint(plan["evidence"]),
            "implementation_sha256": implementation_identity(),
            "runtime_sha256": None,
            "max_seconds": None, "pilot_epochs": None,
            "checks": {key: None for key in CHECKS},
            "python_version": None, "packages": {}, "runtime_files": [],
            "evaluator": {"file": None, "factory": None, "sha256": None},
            "pilot_receipt_sha256": None}


def execution_scope(request):
    return fingerprint({key: value for key, value in request.items() if key != "review"})


def add_execution_arguments(parser):
    parser.add_argument("--execute", action="store_true", help="Requires separately reviewed execution inputs")
    parser.add_argument("--authorization", type=Path, help="Private reviewed execution request JSON")
    parser.add_argument("--runtime", type=Path, help="Private paths and hash-bound stage inputs JSON")
    parser.add_argument("--stage", choices=STAGES, default="pilot", help="Stage for an incomplete request template")
    parser.add_argument("--write-execution-template", type=Path, help="Write a NEW incomplete request; never approves it")


def dispatch_cli(plan, args):
    """Planning is the default; only explicit, fully checked execution dispatches."""
    research = plan["configuration"].get("schema_version") == "t41-research-1"
    if args.write_execution_template:
        if not research or args.execute:
            raise ValueError("template generation is a separate research planning action")
        _write(args.write_execution_template, execution_request_example(plan, args.stage))
    authorization = (json.loads(args.authorization.read_text(encoding="utf-8-sig"))
                     if args.authorization else None)
    if authorization is not None and not research:
        raise ValueError("legacy configurations cannot dispatch research execution")
    checked = execution_plan(plan, authorization) if research else plan
    if not args.execute or checked["blockers"]:
        print(json.dumps({"status": "blocked" if checked["blockers"] else "ready_for_authorized_execution",
                          "training_started": False, "execution_requested": args.execute,
                          "blockers": checked["blockers"]}))
        return 2 if checked["blockers"] else 0
    if not args.runtime:
        raise ValueError("explicit runtime inputs required")
    runtime = json.loads(args.runtime.read_text(encoding="utf-8-sig"))
    try:
        result = run_workflow(plan, authorization, runtime)
    except Exception:
        # An exception after dispatch can occur after training began. Do not claim
        # False; inspect private started/epoch/result records during recovery.
        print(json.dumps({"status": "execution_failed", "training_started": None,
                          "blockers": ["inspect_private_execution_records"]}))
        return 1
    successful = (all(r["status"] in ("complete", "reuse") for r in result["results"])
                  if "results" in result else result["attempted_configurations"] == 20
                  and all(r["status"] in ("complete", "failed", "pruned") for r in result["trials"]))
    print(json.dumps({"status": "stage_finished" if successful else "stage_incomplete",
                      "training_started": result["training_started"],
                      "execution_kind": result["execution_kind"]}))
    return 0 if successful else 1


def execution_plan(plan, request, *, check_output=True):
    """Check supplied assertions; no model import, scan access, or execution.

    A pilot qualifies training, so it needs reviewed environment preflight rather
    than a claim that that very pilot already completed. Subsequent stages also
    require the existing train/save/reload qualification and pilot receipt.
    """
    checked = research_plan(plan["configuration"], plan["evidence"], plan["missing_documents"])
    config = checked["configuration"]
    blocked = set(checked["blockers"]) - DRAFT_GATES
    if not check_output:
        blocked.discard("execution:output_collision")  # Writers independently reserve new directories.
    if not _text(config.get("output_directory")) or not Path(config["output_directory"]).is_absolute():
        blocked.add("execution:absolute_owned_output_required")
    try:
        check_prediction_settings(config.get("validation_prediction"))
    except ValueError:
        blocked.add("validation:reviewed_prediction_controls_required")
    if checked["evidence"].get("conversions", {}).get("validation", {}).get("annotations", 0) < 1:
        blocked.add("validation:ap_requires_validation_annotations")
    if not isinstance(request, dict):
        blocked.add("execution:reviewed_request_required")
        return {"status": "blocked", "blockers": sorted(blocked), "training_started": False}
    stage = request.get("stage")
    if stage not in STAGES:
        blocked.add("execution:stage")
    if stage == "pilot":
        blocked.discard("environment:allocated_train_save_reload_and_storage_unqualified")
        blocked.discard("approval:common_initialization_comparison")
    expected = execution_request_example(checked, stage if stage in STAGES else "pilot")
    if set(request) != set(expected) or request.get("schema_version") != expected["schema_version"]:
        blocked.add("execution:schema")
    for key in ("configuration_sha256", "evidence_sha256", "implementation_sha256"):
        if request.get(key) != expected[key]:
            blocked.add(f"execution:{key}")
    if not _digest(request.get("runtime_sha256")):
        blocked.add("execution:bound_runtime_inputs")
    review = request.get("review") or {}
    if not reviewed(review) or review.get("scope_sha256") != execution_scope(request):
        blocked.add("execution:reviewed_scope_required")
    seconds = request.get("max_seconds")
    if type(seconds) not in (int, float) or not math.isfinite(seconds) or seconds <= 0:
        blocked.add("execution:bounded_seconds_required")
    epochs = request.get("pilot_epochs")
    if ((stage == "pilot" and (type(epochs) is not int or not 1 <= epochs <= 30))
            or (stage != "pilot" and epochs is not None)):
        blocked.add("execution:explicit_pilot_epoch_budget")
    checks = request.get("checks") or {}
    for key in CHECKS:
        if not isinstance(checks, dict) or not reviewed(checks.get(key)):
            blocked.add(f"execution:{key}")
    checkpoint = (config.get("initialization") or {}).get("checkpoint_sha256")
    weights = checks.get("weights_on_execution_host", {}) if isinstance(checks, dict) else {}
    if not isinstance(weights, dict) or weights.get("verified_sha256") != checkpoint:
        blocked.add("execution:host_checkpoint_hash")
    environment = config.get("environment") or {}
    if environment.get("upstream_revision") != UPSTREAM_REVISION or not _digest(environment.get("lock_sha256")):
        blocked.add("execution:reviewed_environment_lock")
    packages = request.get("packages") or {}
    if not supported_python(request.get("python_version")):
        blocked.add("execution:python_requires_3_11_to_3_14")
    required = {"torch", "torchvision", "ultralytics", "numpy", "pycocotools"}
    if stage == "search":
        required.add("optuna")
    if (not _text(request.get("python_version")) or not isinstance(packages, dict)
            or not required <= packages.keys() or not all(_text(v) for v in packages.values())):
        blocked.add("execution:runtime_package_inventory")
    files = request.get("runtime_files")
    if (not isinstance(files, list) or not files or any(
        not isinstance(row, dict) or set(row) != {"path", "sha256"}
        or not _text(row["path"]) or not _digest(row["sha256"]) for row in files
    )):
        blocked.add("execution:qualified_runtime_files")
    evaluator = request.get("evaluator") or {}
    if (not isinstance(evaluator, dict) or set(evaluator) != {"file", "factory", "sha256"}
            or not _text(evaluator.get("file")) or not _digest(evaluator.get("sha256"))
            or not isinstance(evaluator.get("factory"), str) or not evaluator["factory"].isidentifier()):
        blocked.add("execution:production_validation_factory")
    if stage != "pilot" and not _digest(request.get("pilot_receipt_sha256")):
        blocked.add("execution:qualified_pilot_receipt")
    return {"schema_version": "t41-execution-plan-1", "stage": stage,
            "status": "blocked" if blocked else "ready_for_authorized_execution",
            "blockers": sorted(blocked), "training_started": False,
            "request_sha256": fingerprint(request), "review_is_supplied_assertion": True}


def verify_runtime(request):
    """Check the approved interpreter/files/allocation before any optional import."""
    if (not supported_python(sys.version.split()[0])
            or sys.version.split()[0] != request["python_version"]
            or not os.environ.get("SLURM_JOB_ID") or not os.environ.get("CUDA_VISIBLE_DEVICES")):
        raise ValueError("qualified interpreter and allocated GPU mask required")
    for name, version in request["packages"].items():
        if importlib.metadata.version(name) != version:
            raise ValueError("runtime package version differs from qualification")
    for row in [*request["runtime_files"], request["evaluator"]]:
        path = Path(row.get("path", row.get("file", "")))
        if not path.is_absolute() or path.is_symlink() or _sha256(path) != row["sha256"]:
            raise ValueError("qualified runtime/validation source file changed")
    return {"python_version": sys.version.split()[0], "packages": deepcopy(request["packages"]),
            "slurm_job_id": os.environ["SLURM_JOB_ID"],
            "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
            "checked_files": deepcopy([*request["runtime_files"], request["evaluator"]])}


def load_validation_adapter(request, context):
    """Load only the explicitly reviewed local factory; no evaluator is implemented here."""
    entry = request["evaluator"]
    path = Path(entry["file"])
    if _sha256(path) != entry["sha256"]:
        raise ValueError("validation adapter source changed")
    spec = importlib.util.spec_from_file_location("t41_reviewed_validation_adapter", path)
    if spec is None or spec.loader is None:
        raise ValueError("validation adapter cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if _sha256(path) != entry["sha256"]:
        raise ValueError("validation adapter source changed during import")
    delegate = getattr(module, entry["factory"])(deepcopy(context))
    if getattr(delegate, "synthetic", False) or not callable(getattr(delegate, "evaluate_checkpoint", None)):
        raise ValueError("a production validation adapter is required")
    return delegate


@contextmanager
def offline_runtime(directory, font_assets=()):
    """Scoped single-process guard against network, installers and Git subprocesses."""
    def network_denied(*args, **kwargs):
        # The pinned fork probes connectivity at import and catches OSError.
        # Report an unavailable network without allowing any connection attempt.
        raise OSError("network dispatch is disabled for this runtime")

    def denied(*args, **kwargs):
        raise RuntimeError("subprocess dispatch is disabled for this runtime")
    original_connect, original_connect_ex = socket.socket.connect, socket.socket.connect_ex

    def local_connect(sock, *args, **kwargs):
        if hasattr(socket, "AF_UNIX") and sock.family == socket.AF_UNIX:
            return original_connect(sock, *args, **kwargs)
        return network_denied()

    def local_connect_ex(sock, *args, **kwargs):
        if hasattr(socket, "AF_UNIX") and sock.family == socket.AF_UNIX:
            return original_connect_ex(sock, *args, **kwargs)
        return network_denied()
    directory = Path(directory)
    directory.mkdir(exist_ok=False)
    for asset in font_assets:
        source = Path(asset["path"])
        if (asset["name"] not in {"Arial.ttf", "Arial.Unicode.ttf"}
                or not source.is_absolute() or source.is_symlink()
                or _sha256(source) != asset["sha256"]):
            raise ValueError("runtime font asset is not a verified local file")
        content = source.read_bytes()
        with (directory / asset["name"]).open("xb") as target:
            target.write(content)
        if _sha256(directory / asset["name"]) != asset["sha256"]:
            raise ValueError("runtime font asset changed during copy")
    with patch.dict(os.environ, {"YOLO_CONFIG_DIR": str(directory.resolve()),
                                "YOLO_AUTOINSTALL": "false", "PIP_NO_INDEX": "1",
                                "HF_HUB_OFFLINE": "1"}), \
            patch.object(socket.socket, "connect", local_connect), \
            patch.object(socket.socket, "connect_ex", local_connect_ex), \
            patch.object(socket, "create_connection", network_denied), \
            patch.object(subprocess, "Popen", denied):
        yield


@contextmanager
def termination_requested():
    """Turn TERM/INT into a stop flag; completed-epoch callbacks retain state."""
    stopped = [False]
    def stop(signum, frame):
        stopped[0] = True
    previous = {sig: signal.signal(sig, stop) for sig in (signal.SIGTERM, signal.SIGINT)}
    try:
        yield lambda: stopped[0]
    finally:
        for sig, handler in previous.items():
            signal.signal(sig, handler)


def _write(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, allow_nan=False, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def stage_schedule(exported, stage, *, confirmed=None, pilot_epochs=None):
    if stage == "confirmation":
        return confirmation_plan(exported)
    if stage == "repeatability":
        return repeatability_plan(exported, confirmed)
    if stage != "pilot" or type(pilot_epochs) is not int or not 1 <= pilot_epochs <= 30:
        raise ValueError("explicit bounded pilot epochs or a supported post-search stage required")
    return [{"stage": "pilot", "source_trial": 0, "status": "planned", "seed": 17,
             "parameters": deepcopy(exported["definition"]["configuration"]["study"]["control"]),
             "epochs": pilot_epochs, "definition_sha256": exported["definition_sha256"],
             "output_key": "pilot/seed-17", "checkpoint_sha256": None, "value": None}]


def run_stage(exported, stage, output, trainer, evaluator, receipts, *, confirmed=None,
               pilot_epochs=None, stop_requested=lambda: False, max_seconds=None,
               clock=time.perf_counter, plan=None, authorization=None, output_keys=None):
    """Run one bounded stage with injected adapters; synthetic results stay labelled.

    A new directory is required. Failed/interrupted attempts remain in the result;
    a later retry is a new explicit stage invocation, never a successful zero AP.
    """
    synthetic = exported["execution_kind"] == "synthetic_software_check"
    if any((getattr(a, "synthetic", False) is True) != synthetic for a in (trainer, evaluator)):
        raise ValueError("synthetic and live stage adapters cannot be mixed")
    if not synthetic:
        from sdp_xray.training_research import require_live_ready

        require_live_ready(plan, authorization)
        if (authorization["stage"] != stage or experiment_identity(exported["definition"]["configuration"])
                != experiment_identity(plan["configuration"])):
            raise ValueError("stage/configuration authorization mismatch")
        max_seconds = authorization["max_seconds"]
    if max_seconds is not None and (type(max_seconds) not in (int, float)
                                    or not math.isfinite(max_seconds) or max_seconds <= 0):
        raise ValueError("positive finite stage time budget required")
    schedule = stage_schedule(exported, stage, confirmed=confirmed, pilot_epochs=pilot_epochs)
    if output_keys is not None:
        if (stage == "pilot" or not isinstance(output_keys, list) or not output_keys
                or len(set(output_keys)) != len(output_keys)
                or not set(output_keys) <= {row["output_key"] for row in schedule}):
            raise ValueError("allocation output keys must select declared stage runs")
        schedule = [row for row in schedule if row["output_key"] in output_keys]
    config = exported["definition"]["configuration"] if synthetic else plan["configuration"]
    if exported["definition_sha256"] != fingerprint(exported["definition"]):
        raise ValueError("study definition fingerprint mismatch")
    definition = exported["definition"]
    if definition != make_study_definition(definition["configuration"], definition["partition"],
                                           definition["annotation_sha256"],
                                           execution_kind=exported["execution_kind"]):
        raise ValueError("inconsistent study definition")
    if not schedule:
        raise ValueError("stage has no eligible configurations")
    for row in schedule:
        validate_parameters(row["parameters"])
        if row["status"] != "reuse":
            receipt = receipts[str(row["seed"])]
            validate_initialization(receipt, config["task"], expected_seed=row["seed"])
            if any(receipt[k] != config["initialization"][k] for k in
                   ("checkpoint_sha256", "source_reference", "procedure", "task_head", "task")):
                raise ValueError("stage initialization differs from the common starting checkpoint")
    root = Path(output)
    root.mkdir(parents=False, exist_ok=False)
    _write(root / "stage-plan.json", {"stage": stage, "schedule": schedule,
                                     "definition_sha256": exported["definition_sha256"],
                                     "execution_kind": exported["execution_kind"]})
    started, results = clock(), []
    def stopping():
        return stop_requested() or (max_seconds is not None and clock() - started >= max_seconds)
    for number, row in enumerate(schedule):
        if row["status"] == "reuse":
            results.append(deepcopy(row))
            continue
        if stopping():
            results.append({**deepcopy(row), "status": "not_started"})
            continue
        directory = root / f"run-{number:03d}"
        directory.mkdir(exist_ok=False)
        attempt = directory / "attempt"
        attempt.mkdir(exist_ok=False)
        request = {"number": row["source_trial"], "configuration": config,
                   "parameters": row["parameters"], "initialization": receipts[str(row["seed"])],
                   "stage": stage, "seed": row["seed"], "epochs": row["epochs"],
                   "output_directory": attempt, "completed_epochs": 0, "resume_checkpoint": None}
        result = {**deepcopy(row), "status": "running", "reports": [], "validation": None,
                  "checkpoint": None, "value": None, "training_started": False, "failure": None,
                  "execution_kind": exported["execution_kind"]}
        _write(directory / "started.json", result)
        run_start, previous = clock(), clock()
        def report(event):
            nonlocal previous
            if event.get("phase") == "final_evaluation":
                return
            epoch = event.get("completed_epoch")
            path = Path(event["checkpoint"])
            if (path.is_symlink() or not path.resolve().is_relative_to(attempt.resolve())
                    or event.get("phase") != "fit" or type(epoch) is not int
                    or not 1 <= epoch <= row["epochs"]):
                raise ValueError("invalid completed epoch/checkpoint")
            digest = _sha256(path)
            if epoch <= len(result["reports"]):
                if digest != result["reports"][epoch - 1]["checkpoint_sha256"]:
                    raise ValueError("duplicate epoch changed checkpoint")
                return
            if epoch != len(result["reports"]) + 1:
                raise ValueError("missing completed epoch")
            validation = validation_request(exported["definition"], digest, epoch)
            response = (evaluator.evaluate_checkpoint(deepcopy(validation), path)
                        if hasattr(evaluator, "evaluate_checkpoint") else evaluator.evaluate(deepcopy(validation)))
            value = validate_objective_result(validation, response)
            now = clock()
            result["reports"].append({"epoch": epoch, "value": value,
                                      "checkpoint_sha256": digest, "seconds": now - previous})
            result["training_started"] = not synthetic and getattr(trainer, "training_started", False)
            previous = now
            if result["value"] is None or value > result["value"]:
                result.update(value=value, checkpoint_sha256=digest, validation=response,
                              checkpoint=str(path.resolve()))
            _write(directory / f"epoch-{epoch:03d}.json", result)
            if stopping():
                raise KeyboardInterrupt
            return value
        try:
            if hasattr(trainer, "run_with_callback"):
                trainer.run_with_callback(request, report)
            else:
                for event in trainer.run(request):
                    report(event)
            if len(result["reports"]) != row["epochs"]:
                raise ValueError("incomplete stage run")
            if _sha256(Path(result["checkpoint"])) != result["checkpoint_sha256"]:
                raise ValueError("selected checkpoint changed")
            result["status"] = "complete"
        except KeyboardInterrupt:
            result["status"] = "interrupted"
        except Exception as error:
            result["status"], result["failure"] = "failed", type(error).__name__
            result["failure_message"] = str(error)
            traceback.print_exc()
        result["training_started"] = not synthetic and getattr(trainer, "training_started", False)
        result["wall_seconds"] = clock() - run_start
        if result["status"] != "complete":
            result.update(value=None, checkpoint_sha256=None, validation=None, checkpoint=None)
        _write(directory / "result.json", result)
        results.append(result)
    summary = {"stage": stage, "definition_sha256": exported["definition_sha256"],
               "experiment_sha256": experiment_identity(config),
               "execution_kind": exported["execution_kind"], "results": results,
               "training_started": any(r.get("training_started", False) for r in results),
               "wall_seconds": clock() - started,
               "trainer_invocations": sum(r["status"] not in ("reuse", "not_started") for r in results)}
    _write(root / "stage-result.json", summary)
    return summary


def experiment_identity(config):
    """Scientific controls; environment approval/output paths can change after a pilot."""
    keys = ("dataset", "experiment", "task", "sources", "partition_sha256", "study", "batch",
            "precision", "objective")
    return fingerprint({**{key: config[key] for key in keys},
                        "validation_prediction": config.get("validation_prediction"),
                        "initialization": {key: config["initialization"][key] for key in
                                           ("checkpoint_sha256", "procedure", "task_head", "seed")}})


def _read_bound_json(entry):
    if not isinstance(entry, dict) or set(entry) != {"path", "sha256"}:
        raise ValueError("input artifact requires its path and expected byte hash")
    path = Path(entry["path"])
    if not path.is_absolute() or not _digest(entry["sha256"]) or _sha256(path) != entry["sha256"]:
        raise ValueError("input artifact identity mismatch")
    result = json.loads(path.read_text(encoding="utf-8"))
    if _sha256(path) != entry["sha256"]:
        raise ValueError("input artifact changed while reading")
    return result


def verify_validation_inputs(context, definition):
    """Check only the fixed validation membership and source bytes, never test metrics."""
    from sdp_xray.data.audit import _image_path
    from sdp_xray.training import convert_coco
    from sdp_xray.training_research import TASKS

    annotation, images = Path(context["annotation_file"]), Path(context["image_root"])
    if not annotation.is_absolute() or not images.is_absolute():
        raise ValueError("validation input paths must be explicit and absolute")
    if _sha256(annotation) != definition["annotation_sha256"]:
        raise ValueError("validation annotation identity mismatch")
    convert_coco(annotation, TASKS[definition["configuration"]["task"]])
    document = json.loads(annotation.read_text(encoding="utf-8-sig"))
    if not document["annotations"] or any(
        type(row.get("area")) not in (int, float) or not math.isfinite(row["area"])
        or row["area"] <= 0 or type(row.get("iscrowd")) is not int or row["iscrowd"] != 0
        for row in document["annotations"]
    ):
        raise ValueError("Ali's validation AP requires existing valid area/iscrowd annotations")
    if sorted(row["id"] for row in document["images"]) != definition["validation_ids"]:
        raise ValueError("validation membership differs from the fixed partition")
    inventory = {row["id"]: row["sha256"] for row in definition["partition"]["train_inventory"]}
    for row in document["images"]:
        if _sha256(_image_path(images, row["file_name"])) != inventory[row["id"]]:
            raise ValueError("validation image bytes changed")
    if _sha256(annotation) != definition["annotation_sha256"]:
        raise ValueError("validation annotation changed")


def search_runtime_identity(request):
    return {key: request[key] for key in
            ("implementation_sha256", "runtime_files", "packages", "python_version", "evaluator")}


def deadline_protocol(entry, config, stage):
    """Validate the explicit user amendment; retain the original study definition."""
    if entry is None:
        return None
    receipt = _read_bound_json(entry)
    terms = {"task": "generic", "attempted_configurations": 6, "search_epochs": 30,
             "confirmation": "best_completed_and_control", "confirmation_epochs": 100,
             "seeds": [17], "deferred": ["specific", "repeatability"]}
    if (receipt.get("schema_version") != "t41-deadline-protocol-1" or receipt.get("terms") != terms
            or not reviewed(receipt.get("authorization")) or config["task"] != "generic"
            or stage not in {"search", "confirmation"}
            or receipt.get("experiment_sha256") != experiment_identity(config)):
        raise ValueError("deadline protocol requires matching explicit generic-only authorization")
    return receipt


def deadline_confirmation_plan(exported):
    """One completed validation-selected candidate plus the original control."""
    completed = [row for row in exported["trials"] if row["status"] == "complete"]
    if not completed:
        return []
    best = min(completed, key=lambda row: (-row["value"], row["number"]))["number"]
    return [row for row in confirmation_plan(exported) if row["source_trial"] in {0, best}]


def verify_search_runtime(original, current, amendment, root):
    """Permit one recorded repair after the first failed configuration only.

    The original request, failed result and sampler history remain immutable.
    No completed/pruned configuration from another implementation is pooled.
    Subsequent allocations must use this exact replacement identity.
    """
    before, after = search_runtime_identity(original), search_runtime_identity(current)
    if before == after:
        return
    if amendment is None:
        raise ValueError("search runtime changed without a bound first-failure amendment")
    receipt = _read_bound_json(amendment)
    if (receipt.get("schema_version") != "t41-first-failure-amendment-1"
            or receipt.get("original_identity") != before or receipt.get("replacement_identity") != after
            or not reviewed(receipt.get("authorization")) or not _text(receipt.get("reason"))
            or before["packages"] != after["packages"] or before["python_version"] != after["python_version"]
            or any(before["evaluator"][key] != after["evaluator"][key] for key in ("file", "factory"))):
        raise ValueError("first-failure amendment does not match the original and replacement runtime")
    old_files = {row["path"]: row["sha256"] for row in before["runtime_files"]}
    new_files = {row["path"]: row["sha256"] for row in after["runtime_files"]}
    changes = [{"path": path, "before": old_files[path], "after": new_files[path]}
               for path in sorted(old_files.keys() & new_files.keys()) if old_files[path] != new_files[path]]
    if old_files.keys() != new_files.keys() or receipt.get("changed_files") != changes:
        raise ValueError("amendment must enumerate every changed runtime file")
    boundary = receipt["failed_boundary"]
    if Path(boundary["path"]).resolve() != (root / "allocations/000/workflow-result.json").resolve():
        raise ValueError("amendment must bind the first allocation's preserved failure")
    prior = _read_bound_json(boundary)
    rows = prior.get("trials", [])
    if (prior.get("attempted_configurations") != 1 or len(rows) != 1
            or rows[0].get("number") != 0 or rows[0].get("status") != "failed"
            or rows[0].get("value") is not None):
        raise ValueError("amendment cannot pool completed/pruned configurations or reset the attempt count")
    qualification = _read_bound_json(receipt["qualification"])
    if (qualification.get("implementation_sha256") != after["implementation_sha256"]
            or qualification.get("status") != "passed"
            or any(qualification.get(key) is not True for key in
                   ("all_detections_retained", "untouched_predictions_equal", "ali_evaluator_unchanged"))):
        raise ValueError("replacement runtime requires actual bound prediction qualification")


def run_workflow(plan, authorization, runtime):
    """Production composition, never called by the synthetic checks with real adapters.

    All gates, runtime identities, inputs and output reservation precede imports.
    The caller must explicitly request execution; planning does not call this API.
    """
    from sdp_xray.training_backend import (
        CheckpointValidationAdapter,
        YoloTrainerAdapter,
        check_training_bundle,
        live_trainer_class,
    )
    from sdp_xray.tuning import make_study_definition, open_optuna_backend, run_approved_study

    chunk = runtime.get("search_chunk")
    if chunk is not None and (authorization["stage"] != "search" or not isinstance(chunk, dict)
            or set(chunk) != {"index", "attempt_limit"} or type(chunk["index"]) is not int
            or chunk["index"] < 0 or type(chunk["attempt_limit"]) is not int
            or not 1 <= chunk["attempt_limit"] <= 20):
        raise ValueError("explicit search allocation index and attempt limit required")
    resume = chunk is not None and chunk["index"] > 0
    checked = execution_plan(plan, authorization, check_output=not resume)
    if checked["blockers"]:
        raise ValueError("execution requirements are unresolved")
    if fingerprint(runtime) != authorization["runtime_sha256"]:
        raise ValueError("runtime paths/inputs differ from the reviewed execution request")
    config, stage = plan["configuration"], authorization["stage"]
    deadline = deadline_protocol(runtime.get("deadline_protocol"), config, stage)
    required_attempts = 6 if deadline else 20
    if deadline and (stage == "search" and (chunk is None or chunk["index"] + chunk["attempt_limit"] > 6)):
        raise ValueError("deadline search must stop after six attempted configurations")
    if config["requested_device"] != "0":
        raise ValueError("live workflow requires allocation-relative GPU 0")
    runtime_verification = verify_runtime(authorization)
    weights, bundle = Path(runtime["weights"]), Path(runtime["bundle"])
    if (not weights.is_absolute() or weights.is_symlink()
            or _sha256(weights) != config["initialization"]["checkpoint_sha256"]):
        raise ValueError("execution-host weights do not match initialization")
    check_training_bundle(bundle, config)
    definition = make_study_definition(config, plan["evidence"]["partition"],
                                       config["sources"]["validation"]["annotation_sha256"],
                                       execution_kind="model_training")
    verify_validation_inputs(runtime["validation_context"], definition)
    if stage != "pilot":
        pilot = _read_bound_json(runtime["pilot"])
        if (runtime["pilot"]["sha256"] != authorization["pilot_receipt_sha256"]
                or pilot.get("execution_kind") != "model_training"
                or pilot.get("training_started") is not True
                or pilot.get("experiment_sha256") != experiment_identity(config)):
            raise ValueError("a matching real completed pilot is required")
        estimate_study_hours(pilot)  # Also requires a completed pilot and valid timing.
    exported = {"definition": definition, "definition_sha256": fingerprint(definition),
                "execution_kind": "model_training", "trials": []}
    confirmed = None
    if stage in ("confirmation", "repeatability"):
        exported = _read_bound_json(runtime["study"])
        if (exported["execution_kind"] != "model_training"
                or experiment_identity(exported["definition"]["configuration"]) != experiment_identity(config)):
            raise ValueError("stage study differs from the approved scientific controls")
        trials = exported.get("trials", [])
        if (exported.get("attempted_configurations") != required_attempts or len(trials) != required_attempts
                or [r["number"] for r in trials] != list(range(required_attempts))
                or any(r["status"] not in ("complete", "failed", "pruned") for r in trials)):
            raise ValueError("all authorized search attempts must be accounted for before confirmation")
        if deadline:
            allowed = {row["output_key"] for row in deadline_confirmation_plan(exported)}
            selected = runtime.get("stage_output_keys")
            if not isinstance(selected, list) or not selected or not set(selected) <= allowed:
                raise ValueError("deadline confirmation requires the best completed candidate or control")
        for row in trials:
            validate_parameters(row["parameters"])
            if row["parameters_sha256"] != fingerprint(row["parameters"]):
                raise ValueError("search parameter fingerprint mismatch")
            if row["status"] == "complete":
                value = row["value"]
                if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
                    raise ValueError("completed search objective is invalid")
            elif row["value"] is not None:
                raise ValueError("failed/pruned search is not zero AP")
        if trials[0]["parameters"] != config["study"]["control"]:
            raise ValueError("queued control differs from the protocol")
        if exported["definition_sha256"] != fingerprint(exported["definition"]):
            raise ValueError("study fingerprint mismatch")
        if stage == "repeatability":
            confirmation = _read_bound_json(runtime["confirmations"])
            if (confirmation.get("stage") != "confirmation"
                    or confirmation.get("execution_kind") != "model_training"
                    or confirmation.get("definition_sha256") != exported["definition_sha256"]):
                raise ValueError("confirmation identity mismatch")
            confirmed = confirmation["results"]
    root = Path(config["output_directory"])
    if resume:
        stored = json.loads((root / "research-plan.json").read_text(encoding="utf-8"))
        original_request = json.loads((root / "execution-request.json").read_text(encoding="utf-8"))
        previous = root / "allocations" / f"{chunk['index'] - 1:03d}" / "workflow-result.json"
        if (root.is_symlink() or stored["configuration"] != plan["configuration"]
                or stored["evidence"] != plan["evidence"]
                or not previous.is_file() or previous.is_symlink()):
            raise ValueError("search allocation identity or previous completed boundary differs")
        verify_search_runtime(original_request, authorization, runtime.get("implementation_amendment"), root)
        prior = json.loads(previous.read_text(encoding="utf-8"))
        if any(row["status"] not in {"complete", "failed", "pruned"} for row in prior["trials"]):
            raise ValueError("interrupted checkpoint continuation remains unsupported")
    else:
        root.mkdir(parents=False, exist_ok=False)
        _write(root / "execution-request.json", authorization)
        _write(root / "research-plan.json", plan)
    records = root
    if chunk is not None:
        (root / "allocations").mkdir(exist_ok=True)
        records = root / "allocations" / f"{chunk['index']:03d}"
        records.mkdir(exist_ok=False)
        _write(records / "execution-request.json", authorization)
    _write(records / "runtime-verification.json", runtime_verification)
    mask = os.environ["CUDA_VISIBLE_DEVICES"]
    with termination_requested() as stopped, offline_runtime(records / "runtime-settings", runtime.get("font_assets", ())):
        delegate = load_validation_adapter(authorization, {**runtime["validation_context"],
                                                           "definition": definition,
                                                           "qualified_sources": authorization["runtime_files"]})
        evaluator = CheckpointValidationAdapter(delegate)
        trainer = YoloTrainerAdapter(live_trainer_class(plan, authorization), weights, bundle,
                                     plan=plan, authorization=authorization,
                                     checkpoint_retention=runtime.get("checkpoint_retention", "all"))
        if stage == "search":
            backend = open_optuna_backend(plan, root, f"t41-{config['task']}", authorization)
            result = run_approved_study(definition, root / "study", backend, trainer, evaluator,
                                        plan, authorization, stop_requested=stopped,
                                        budget_seconds=authorization["max_seconds"], resume=resume,
                                        attempt_limit=chunk["attempt_limit"] if chunk is not None else None)
        else:
            receipts = {"17": config["initialization"], **runtime.get("initialization_receipts", {})}
            result = run_stage(exported, stage, root / "stage", trainer, evaluator, receipts,
                               confirmed=confirmed, pilot_epochs=authorization["pilot_epochs"],
                               max_seconds=authorization["max_seconds"],
                               stop_requested=stopped, plan=plan, authorization=authorization,
                               output_keys=runtime.get("stage_output_keys"))
        if os.environ.get("CUDA_VISIBLE_DEVICES") != mask:
            raise ValueError("allocated device mask changed during workflow")
    if deadline:
        result["deadline_protocol"] = deepcopy(runtime["deadline_protocol"])
    _write(records / "workflow-result.json", result)
    return result


def estimate_study_hours(pilot):
    """Conservative epoch-based projection, not a quota or approval."""
    if pilot.get("stage") != "pilot" or len(pilot.get("results", [])) != 1:
        raise ValueError("one completed pilot required")
    result = pilot["results"][0]
    seconds = [row["seconds"] for row in result.get("reports", [])]
    if result["status"] != "complete" or not seconds or any(
        type(v) not in (int, float) or not math.isfinite(v) or v <= 0 for v in seconds
    ):
        raise ValueError("completed finite positive pilot timing required")
    epochs = {"search": 20 * 30, "confirmation": 4 * 100, "repeatability_new_runs": 4 * 100}
    return {"execution_kind": pilot["execution_kind"], "per_task_epoch_ceilings": epochs,
            "per_task_hours_at_slowest_pilot_epoch": {
                stage: count * max(seconds) / 3600 for stage, count in epochs.items()},
            "basis": "Includes observed startup/validation overhead; excludes failed retries and queue time.",
            "limitations": "Pilot timing may not transfer to other optimizers/tasks or longer runs.",
            "approved_compute": False}
