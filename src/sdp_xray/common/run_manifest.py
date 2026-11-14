"""Shared run manifest for baseline and candidate runs.

One manifest describes one run over one or more scans. It carries identities and
hashes only, never local paths. See docs/baseline-run-contract.md.
"""

import json
from typing import Any

from sdp_xray.common.contracts import (
    SCHEMA_VERSION,
    _object,
    _score,
    _text,
    _version,
    validate_scan_result,
)

ROLES = ("baseline", "candidate")
STAGES = ("preprocessing", "roi", "features", "postprocessing")
STAGE_STATUSES = ("implemented", "inherited", "absent")


def _sha256(value: Any, path: str) -> None:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise ValueError(f"{path} must be a lowercase SHA-256 hex digest")


def _positive_int(value: Any, path: str) -> None:
    if type(value) is not int or value <= 0:
        raise ValueError(f"{path} must be a positive integer")


def _label_map(value: Any, path: str) -> None:
    """A JSON object of integer-like string keys to nonempty label names."""
    if not isinstance(value, dict) or not value:
        raise ValueError(f"{path} must be a nonempty object")
    for key, label in value.items():
        if not isinstance(key, str) or not key.isdigit():
            raise ValueError(f"{path} keys must be integer strings")
        _text(label, f"{path}[{key}]")
    if len(set(value.values())) != len(value):
        raise ValueError(f"{path} labels must be unique")


def validate_run_manifest(value: Any) -> None:
    """Raise ValueError unless value is a complete shared run manifest."""
    _object(
        value,
        {
            "schema_version",
            "run_id",
            "role",
            "status",
            "timestamp_utc",
            "model",
            "code",
            "settings",
            "stages",
            "requested_device",
            "device",
            "precision",
            "inputs",
            "limitations",
        },
        "run_manifest",
    )
    _version(value)
    for key in ("run_id", "timestamp_utc", "requested_device", "precision"):
        _text(value[key], key)
    # device is where inference actually ran. It is null when no scan got that far,
    # which is only possible for a failed run.
    if value["device"] is None:
        if value["status"] == "ok":
            raise ValueError("an ok run must record the device that ran inference")
    else:
        _text(value["device"], "device")
    if value["role"] not in ROLES:
        raise ValueError(f"role must be one of {ROLES}")
    if value["status"] not in ("ok", "error"):
        raise ValueError("status must be ok or error")

    model = value["model"]
    _object(
        model,
        {
            "id",
            "task",
            "kind",
            "checkpoint_sha256",
            "parent_checkpoint_sha256",
            "class_map_sha256",
            "model_names",
            "source_category_map",
        },
        "model",
    )
    _text(model["id"], "model.id")
    _text(model["task"], "model.task")
    if model["kind"] not in ("device", "suspicious_region"):
        raise ValueError("model.kind must be device or suspicious_region")
    _sha256(model["checkpoint_sha256"], "model.checkpoint_sha256")
    _sha256(model["class_map_sha256"], "model.class_map_sha256")
    _label_map(model["model_names"], "model.model_names")
    _label_map(model["source_category_map"], "model.source_category_map")
    if sorted(model["model_names"].values()) != sorted(model["source_category_map"].values()):
        raise ValueError("model_names and source_category_map must name the same labels")
    # A baseline is the original checkpoint. A candidate must say what it started from.
    parent = model["parent_checkpoint_sha256"]
    if value["role"] == "baseline":
        if parent is not None:
            raise ValueError("a baseline has parent_checkpoint_sha256=null")
    else:
        _sha256(parent, "model.parent_checkpoint_sha256")

    code = value["code"]
    _object(code, {"git_commit", "git_dirty", "upstream_revision"}, "code")
    _text(code["git_commit"], "code.git_commit")
    _text(code["upstream_revision"], "code.upstream_revision")
    if type(code["git_dirty"]) is not bool:
        raise ValueError("code.git_dirty must be true or false")

    settings = value["settings"]
    _object(settings, {"imgsz", "batch", "conf", "max_det", "augment"}, "settings")
    for key in ("imgsz", "batch", "max_det"):
        _positive_int(settings[key], f"settings.{key}")
    _score(settings["conf"], "settings.conf")
    if type(settings["augment"]) is not bool:
        raise ValueError("settings.augment must be true or false")

    stages = value["stages"]
    _object(stages, set(STAGES), "stages")
    for name in STAGES:
        _object(stages[name], {"status", "detail"}, f"stages.{name}")
        if stages[name]["status"] not in STAGE_STATUSES:
            raise ValueError(f"stages.{name}.status must be one of {STAGE_STATUSES}")
        _text(stages[name]["detail"], f"stages.{name}.detail")

    inputs = value["inputs"]
    if not isinstance(inputs, list) or not inputs:
        raise ValueError("inputs must be a nonempty list")
    scan_ids = set()
    for item in inputs:
        _object(item, {"scan_id", "sha256", "source_run_id"}, "input")
        _text(item["scan_id"], "input.scan_id")
        _sha256(item["sha256"], "input.sha256")
        _text(item["source_run_id"], "input.source_run_id")
        if item["scan_id"] in scan_ids:
            raise ValueError("input scan IDs must be unique within a run")
        scan_ids.add(item["scan_id"])

    if not isinstance(value["limitations"], list):
        raise ValueError("limitations must be a list")
    for item in value["limitations"]:
        _text(item, "limitation")


def validate_prediction_set(manifest: Any, results: Any) -> None:
    """Check that scan results belong to this manifest: same run, model and scans.

    Failed scans stay in the set so a missing prediction is never read as "no detection".
    """
    validate_run_manifest(manifest)
    if not isinstance(results, list):
        raise ValueError("results must be a list of scan results")
    model = manifest["model"]
    labels = set(model["model_names"].values())
    expected = {
        "id": model["id"],
        "task": model["task"],
        "provenance": f"sha256:{model['checkpoint_sha256']}",
    }
    seen = []
    for result in results:
        validate_scan_result(result)
        scan_id = result["scan_id"]
        seen.append(scan_id)
        if result["model"] != expected:
            raise ValueError(f"{scan_id}: model identity differs from the run manifest")
        if result["run"]["id"] != manifest["run_id"]:
            raise ValueError(f"{scan_id}: run ID differs from the run manifest")
        if result["threshold"] != manifest["settings"]["conf"]:
            raise ValueError(f"{scan_id}: threshold differs from the run manifest")
        for detection in result["detections"]:
            if detection["kind"] != model["kind"]:
                raise ValueError(f"{scan_id}: detection kind differs from the model kind")
            if detection["category"]["namespace"] != model["task"]:
                raise ValueError(f"{scan_id}: category namespace is not the model task")
            if detection["category"]["label"] not in labels:
                raise ValueError(f"{scan_id}: label is not in the model class map")
    if sorted(seen) != sorted(item["scan_id"] for item in manifest["inputs"]):
        raise ValueError("results must cover each manifest input exactly once")


def dumps_run_manifest(value: dict[str, Any]) -> str:
    """Validate and serialize one run manifest as JSON."""
    validate_run_manifest(value)
    return json.dumps(value, allow_nan=False, sort_keys=True, indent=2)


def loads_run_manifest(value: str) -> dict[str, Any]:
    """Parse and validate one JSON run manifest."""
    manifest = json.loads(value)
    validate_run_manifest(manifest)
    return manifest


__all__ = [
    "ROLES",
    "SCHEMA_VERSION",
    "STAGES",
    "STAGE_STATUSES",
    "dumps_run_manifest",
    "loads_run_manifest",
    "validate_prediction_set",
    "validate_run_manifest",
]
