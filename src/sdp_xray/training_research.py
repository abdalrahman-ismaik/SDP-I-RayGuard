"""T41 research configuration and provenance. No model imports or execution switch."""

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from sdp_xray.baseline import write_record
from sdp_xray.common.run_manifest import validate_prediction_set
from sdp_xray.model_catalog import MODELS, get_model
from sdp_xray.training import PAIRS, SPLITS, UPSTREAM_REVISION, _digest, _sha256, _text
from sdp_xray.training_partition import fingerprint, reviewed, validate_partition
from sdp_xray.validation_objective import objective

PROTOCOL_COMMIT = "6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a"
TASKS = {"generic": "author-yolov10m-generic", "specific": "author-yolov10m-specific"}
EXPERIMENTS = ("supplied_checkpoint_reproduction", "author_training_reproduction",
               "controlled_improvement")
APPROVALS = ("data_policy", "source_identity", "validation_design", "compute_scope",
             "faisal_provenance_interface", "ali_validation_interface",
             "common_initialization_comparison")


def protocol_settings() -> dict:
    """Documented project choices, never represented as recovered author settings."""
    return {
        "attempts": 20, "sampler": "TPE", "sampler_seed": 17, "startup_trials": 5,
        "workers": 1, "trial_epochs": 30, "imgsz": 640, "training_seed": 17,
        "pruner": "Median", "prune_after_epochs": 10, "prune_after_completed_trials": 5,
        "search_space": {"SGD_lr0": [0.0001, 0.01], "AdamW_lr0": [0.00001, 0.001],
                         "weight_decay": [0.00001, 0.001], "lrf": [0.01, 0.1],
                         "mosaic": [0.0, 0.5]},
        "fixed": {"fliplr": 0.5, "multi_scale": True, "hsv_h": 0.0, "hsv_s": 0.0,
                  "mixup": 0.0, "copy_paste": 0.0},
        "control": {"optimizer": "SGD", "lr0": 0.001, "weight_decay": 0.0005,
                    "lrf": 0.01, "mosaic": 0.0},
        "confirmation": {"top_completed": 3, "epochs": 100, "seed": 17},
        "repeatability": {"epochs": 100, "seeds": [17, 29, 43], "reuse_seed_17": True},
    }


def example_research_config() -> dict:
    return {
        "schema_version": "t41-research-1", "protocol_commit": PROTOCOL_COMMIT,
        "dataset": "public_iedxray", "experiment": "controlled_improvement",
        "task": "generic", "task_order": ["generic", "specific"],
        "initialization": None, "author_training_details": None,
        "sources": {split: None for split in SPLITS}, "source_provenance": None,
        "partition_sha256": None, "data_policy": None,
        "study": protocol_settings(), "batch": None, "precision": "float32",
        "objective": objective(), "validation_prediction": {"conf": 0.001, "max_det": 300},
        "approvals": {name: None for name in APPROVALS}, "generic_completion": None,
        "environment": {"upstream_revision": UPSTREAM_REVISION, "optuna_version": "4.5.0",
                        "lock_sha256": None, "qualification": None,
                        "journal_locking": None, "effective_defaults_sha256": None},
        "requested_device": None, "owner": None, "output_directory": None,
    }


def task_identity(task: str) -> dict:
    if task not in TASKS:
        raise ValueError("research task must be generic or specific")
    spec = get_model(TASKS[task])
    return {"task": spec.task, "kind": spec.kind, "class_map_sha256": spec.class_map_sha256,
            "model_names": {str(k): v for k, v in spec.names.items()},
            "source_category_map": spec.source_category_map}


def validate_initialization(receipt: dict, task: str, *, expected_seed: int = 17) -> None:
    """Check a receipt against the intended run seed, without hashing real weights.

    Search/confirmation callers retain seed 17. Repeatability callers must name
    29 or 43 explicitly and provide a matching receipt; never rewrite its seed.
    """
    if (type(expected_seed) is not int
            or expected_seed not in protocol_settings()["repeatability"]["seeds"]):
        raise ValueError("initialization seed must be one of the protocol's repeatability seeds")
    if not isinstance(receipt, dict):
        raise ValueError("initialization receipt is missing")
    expected = {"kind", "architecture", "checkpoint_sha256", "source_reference",
                "verification", "excludes_iedxray", "procedure", "task_head", "seed", "task"}
    if (set(receipt) != expected or receipt["kind"] != "general_pretrained"
            or receipt["architecture"] != "YOLOv10-M" or receipt["task"] != task_identity(task)
            or not _digest(receipt["checkpoint_sha256"])
            or receipt["checkpoint_sha256"] in {spec.sha256 for spec in MODELS.values()}
            or not all(_text(receipt[key]) for key in ("source_reference", "procedure", "task_head"))
            or type(receipt["seed"]) is not int or receipt["seed"] != expected_seed
            or not reviewed(receipt["excludes_iedxray"])
            or not reviewed(receipt["verification"])
            or receipt["verification"].get("verified_sha256") != receipt["checkpoint_sha256"]):
        raise ValueError("general initialization identity/exposure/procedure/head evidence unresolved")


def research_candidate_manifest(task, initialization, checkpoint, run, results, *, model_id,
                                expected_seed=17):
    """Candidate inference record with an explicitly supplied common starting identity.

    The new checkpoint is byte-hashed here. The parent's verification is a receipt
    from its owner, not a hash performed by this helper. Interface agreement remains
    an execution gate in research_plan; shared validators are unchanged.
    """
    validate_initialization(initialization, task, expected_seed=expected_seed)
    if not _text(model_id) or not isinstance(run, dict) or any(
        key in run for key in ("schema_version", "role", "status", "model")
    ) or not isinstance(results, list) or not results:
        raise ValueError("explicit model id, completed results and ordinary run metadata required")
    manifest = deepcopy(run)
    manifest.update(schema_version="1.0", role="candidate",
                    status="ok" if all(r.get("status") == "ok" for r in results) else "error",
                    model={"id": model_id, **task_identity(task),
                           "checkpoint_sha256": _sha256(Path(checkpoint)),
                           "parent_checkpoint_sha256": initialization["checkpoint_sha256"]})
    validate_prediction_set(manifest, results)
    if manifest["device"] is None and any(r["status"] == "ok" for r in results):
        raise ValueError("successful scans require the actual inference device")
    return manifest


def write_research_record(output, task, initialization, checkpoint, run, results, *, model_id,
                          expected_seed=17):
    manifest = research_candidate_manifest(task, initialization, checkpoint, run, results,
                                           model_id=model_id, expected_seed=expected_seed)
    write_record(Path(output), manifest, results)
    return manifest


def audit_findings(evidence: dict) -> dict:
    """Bind review to findings, omitting auditor path fields from the identity."""
    return {name: {key: report.get(key) for key in ("errors", "warnings", "summary")}
            for name, report in evidence["audits"].items()}


def _research_audit_blockers(config, evidence, partition):
    blocked, summaries = [], {}
    spec = get_model(TASKS[config["task"]])
    policy = config.get("data_policy") or {}
    policy_ok = (reviewed(policy.get("review"))
                 and policy.get("audit_findings_sha256") == fingerprint(audit_findings(evidence))
                 and policy.get("duplicate_action") == "preserve_and_group"
                 and policy.get("test_overlap_action") == "preserve_and_report"
                 and policy.get("boundary_action") == "block_invalid_geometry")
    if not policy_ok:
        blocked.append("data:reviewed_findings_dispositions_required")
    exploratory = partition["policy"]["grouping"] == "exploratory_exact_bytes"
    for left, right in PAIRS:
        name = f"{left}_{right}"
        report = evidence["audits"].get(name, {})
        errors = report.get("errors")
        if not isinstance(errors, list) or report.get("ok") is not (not errors):
            blocked.append(f"audit:{name}:errors_or_missing")
        elif any(not (policy_ok and right == "test" and isinstance(error, str)
                      and error.startswith(("Split filename overlap:",
                                            "Physical-group overlap across splits:",
                                            "Exact file content overlaps across splits:")))
                 for error in errors):
            # A reviewed retained test overlap is a caveat. Geometry/other errors still block.
            blocked.append(f"audit:{name}:errors_or_missing")
        summary = report.get("summary", {})
        warnings = report.get("warnings")
        if not isinstance(warnings, list):
            blocked.append(f"audit:{name}:missing_warnings")
        else:
            for warning in warnings:
                normalized = warning.removeprefix("Other split: ") if isinstance(warning, str) else ""
                allowed = policy_ok and (
                    normalized.startswith("Exact file duplicates within split:")
                    or (right == "test" and normalized.startswith(
                        ("Split filename overlap:", "Split physical-group overlap:",
                         "Exact file duplicates across splits:")))
                    or (exploratory and normalized.startswith("Physical-group metadata not checked:"))
                )
                if not allowed:
                    blocked.append(f"audit:{name}:unresolved_warning")
        for key, split in (("primary", left), ("other", right)):
            row = summary.get(key, {})
            count = row.get("images")
            if (type(count) is not int or count < 1 or row.get("image_file_checks") != "complete"
                    or type(row.get("image_files_checked")) is not int
                    or row["image_files_checked"] != count
                    or not isinstance(row.get("exact_file_duplicate_groups"), list)):
                blocked.append(f"audit:{split}:incomplete_image_checks")
            if row.get("category_map") != spec.source_category_map:
                blocked.append(f"audit:{split}:wrong_class_map")
            group_valid = (row.get("physical_group_checks") == "not_checked"
                           and row.get("physical_group_key") is None
                           and row.get("physical_group_count") == 0) if exploratory else (
                row.get("physical_group_checks") == "complete"
                and _text(row.get("physical_group_key"))
                and type(row.get("physical_group_count")) is int
                and 0 < row["physical_group_count"] <= count)
            if not group_valid:
                blocked.append(f"audit:{split}:group_evidence")
            if split in summaries and summaries[split] != row:
                blocked.append(f"audit:{split}:inconsistent_summary")
            summaries[split] = row
        overlap = summary.get("split_overlap", {})
        if (not isinstance(overlap, dict)
                or overlap.get("exact_file_checks") != "checked_available_files"
                or overlap.get("category_maps_match") is not True
                or any(not isinstance(overlap.get(k), list) for k in
                       ("filenames", "physical_group_values", "exact_file_duplicates"))):
            blocked.append(f"audit:{name}:incomplete_overlap_checks")
        elif right != "test" and any(overlap[k] for k in
                                      ("filenames", "physical_group_values", "exact_file_duplicates")):
            blocked.append("validation:fit_overlap")
    for split, ids_key in (("train", "fit_ids"), ("validation", "validation_ids"),
                           ("test", "test_inventory")):
        row = summaries.get(split, {})
        conversion = evidence.get("conversions", {}).get(split, {})
        if (row.get("images") != len(partition[ids_key])
                or conversion.get("images") != row.get("images")
                or conversion.get("annotations") != row.get("annotations")
                or type(conversion.get("annotations")) is not int
                or conversion["annotations"] < 0
                or conversion.get("class_map_sha256") != spec.class_map_sha256):
            blocked.append(f"conversion:{split}:missing_or_inconsistent")
    binding = evidence.get("partition_binding", {})
    if binding != {"partition_sha256": partition["membership_sha256"],
                   "sources_sha256": fingerprint(evidence["sources"]),
                   "task": config["task"], "image_membership_and_bytes_checked": True}:
        blocked.append("data:partition_source_binding_required")
    return blocked


def inspect_partition_sources(sources, task, partition):
    """Explicit read-only adapter, tested only on tiny synthetic images in this draft."""
    from sdp_xray.data.audit import _image_path
    from sdp_xray.training import inspect_training_sources

    validate_partition(partition)
    group_key = partition["policy"].get("group_key")
    evidence = inspect_training_sources(sources, TASKS[task], group_key)
    training = {r["id"]: r for r in partition["train_inventory"]}
    inventories = {"train": {i: training[i] for i in partition["fit_ids"]},
                   "validation": {i: training[i] for i in partition["validation_ids"]},
                   "test": {r["id"]: r for r in partition["test_inventory"]}}
    for split, (annotation, root) in sources.items():
        rows = json.loads(Path(annotation).read_text(encoding="utf-8-sig"))["images"]
        actual = {r["id"]: _sha256(_image_path(Path(root), r["file_name"])) for r in rows}
        if actual != {i: r["sha256"] for i, r in inventories[split].items()}:
            raise ValueError("derived split does not match planned image membership/bytes")
        if group_key and any(json.dumps(row.get(group_key)) !=
                             json.dumps(inventories[split][row["id"]]["group"]) for row in rows):
            raise ValueError("derived physical metadata differs from the reviewed inventory")
        if _sha256(Path(annotation)) != evidence["sources"][split]["annotation_sha256"]:
            raise ValueError("annotation changed during inspection")
    evidence.update(partition=deepcopy(partition), partition_binding={
        "partition_sha256": partition["membership_sha256"],
        "sources_sha256": fingerprint(evidence["sources"]), "task": task,
        "image_membership_and_bytes_checked": True,
    })
    return evidence


def research_plan(config: dict, evidence: dict | None = None, missing_documents=()) -> dict:
    config, evidence = deepcopy(config), deepcopy({} if evidence is None else evidence)
    if not isinstance(config, dict) or not isinstance(evidence, dict):
        raise ValueError("configuration and evidence must be objects")
    blocked = [f"document:{p}" for p in missing_documents]
    template = example_research_config()
    # Older saved synthetic drafts remain inspectable; live execution requires
    # the new explicit prediction controls without rewriting old fingerprints.
    if (set(config) not in (set(template), set(template) - {"validation_prediction"})
            or config.get("schema_version") != "t41-research-1"):
        blocked.append("config:schema")
    for key, value in (("dataset", "public_iedxray"), ("protocol_commit", PROTOCOL_COMMIT),
                       ("task_order", ["generic", "specific"]), ("precision", "float32")):
        if config.get(key) != value:
            blocked.append(f"config:{key}")
    task, model = config.get("task"), None
    try:
        model = task_identity(task)
    except (ValueError, TypeError):
        blocked.append("task:explicit_generic_or_specific_required")
    experiment = config.get("experiment")
    if experiment not in EXPERIMENTS:
        blocked.append("experiment:unknown")
    elif experiment == "supplied_checkpoint_reproduction":
        blocked.append("experiment:faisal_ali_evaluation_handoff_no_training")
    elif experiment == "author_training_reproduction":
        blocked.append("experiment:author_protocol_not_qualified")
    else:
        try:
            validate_initialization(config.get("initialization"), task)
        except (ValueError, TypeError, KeyError):
            blocked.append("initialization:verified_general_pretraining_receipt_required")
    if config.get("study") != protocol_settings():
        blocked.append("study:versioned_protocol_settings_required")
    if type(config.get("batch")) is not int or config["batch"] < 1:
        blocked.append("environment:pilot_selected_fixed_batch_required")
    objective = config.get("objective") or {}
    if (not isinstance(objective, dict) or set(objective) != set(template["objective"])
            or any(objective.get(k) != template["objective"][k]
                   for k in ("name", "direction", "scale"))
            or not _text(objective.get("evaluator_id"))
            or not isinstance(objective.get("settings"), dict) or not objective["settings"]):
        blocked.append("objective:frozen_ali_adapter_required")
    approvals = config.get("approvals") or {}
    for name in APPROVALS:
        if not isinstance(approvals, dict) or not reviewed(approvals.get(name)):
            blocked.append(f"approval:{name}")
    if task == "specific":
        completion = config.get("generic_completion") or {}
        if (not reviewed(completion)
                or completion.get("partition_sha256") != config.get("partition_sha256")):
            blocked.append("sequence:generic_confirmation_first")
    if not reviewed(config.get("source_provenance")):
        blocked.append("sources:published_origin_and_preservation_review_required")
    sources = config.get("sources") or {}
    if not isinstance(sources, dict) or sources != evidence.get("sources"):
        blocked.append("sources:identity_evidence")
    for split in SPLITS:
        row = sources.get(split) if isinstance(sources, dict) else None
        if (not isinstance(row, dict) or set(row) != {"annotation_sha256", "image_inventory_sha256"}
                or not all(_digest(v) for v in row.values())):
            blocked.append(f"sources:{split}:missing_hashes")
    if isinstance(sources, dict) and sources.get("validation") and sources["validation"] in (
        sources.get("train"), sources.get("test")
    ):
        blocked.append("validation:train_or_test_fallback")
    try:
        partition = evidence["partition"]
        validate_partition(partition)
        if config.get("partition_sha256") != partition["membership_sha256"]:
            blocked.append("partition:identity_mismatch")
        blocked.extend(_research_audit_blockers(config, evidence, partition))
    except (ValueError, TypeError, KeyError, AttributeError):
        blocked.append("data:complete_partition_audit_evidence_required")
    environment = config.get("environment") or {}
    if (not isinstance(environment, dict)
            or environment.get("upstream_revision") != UPSTREAM_REVISION
            or environment.get("optuna_version") != "4.5.0"
            or not _digest(environment.get("lock_sha256"))
            or not _digest(environment.get("effective_defaults_sha256"))
            or not reviewed(environment.get("qualification"))
            or not reviewed(environment.get("journal_locking"))):
        blocked.append("environment:allocated_train_save_reload_and_storage_unqualified")
    for key in ("owner", "requested_device", "output_directory"):
        if not _text(config.get(key)):
            blocked.append(f"execution:{key}_required")
    if _text(config.get("output_directory")):
        path = Path(config["output_directory"])
        if path.exists() or path.is_symlink():
            blocked.append("execution:output_collision")
    blocked.extend(["execution:software_draft_only", "integration:live_trainer_not_connected"])
    return {
        "schema_version": "t41-research-plan-1", "status": "blocked",
        "created_at_utc": datetime.now(timezone.utc).isoformat(), "configuration": config,
        "configuration_sha256": fingerprint(config), "model": model, "evidence": evidence,
        "missing_documents": list(missing_documents), "blockers": sorted(set(blocked)),
        "execution": {"training_started": False, "device": None},
        "checkpoint_verification": {"performed_by_this_planner": False, "sha256": None},
        "outputs": {"checkpoint_sha256": None, "metrics": None},
        "interface_status": "proposed; local code authorization is not owner agreement",
    }


def require_live_ready(plan, authorization=None):
    """Recompute gates; a caller cannot remove blockers from a supplied plan."""
    if authorization is not None:
        from sdp_xray.training_workflow import execution_plan

        checked = execution_plan(plan, authorization, check_output=False)
        if checked["blockers"]:
            raise ValueError("live execution blocked; execution evidence is incomplete")
        return
    checked = research_plan(plan["configuration"], plan["evidence"], plan["missing_documents"])
    if checked["blockers"]:
        raise ValueError("live execution blocked; no model/Optuna backend may be loaded")
