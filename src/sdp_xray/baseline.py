"""Turn saved batch-one inference runs into one shared baseline record.

Reads the manifest.json and predictions.json that scripts/infer_generic_yolov10.py
already writes. It runs no model and copies no local paths. Every run is checked
against the inspected model catalog before it is accepted.
"""

import json
from pathlib import Path, PureWindowsPath
from typing import Any

from sdp_xray.common.contracts import SCHEMA_VERSION, dumps_scan_result, validate_scan_input
from sdp_xray.common.run_manifest import dumps_run_manifest, validate_prediction_set
from sdp_xray.model_catalog import get_model

MANIFEST_NAME = "run_manifest.json"
PREDICTIONS_NAME = "predictions.jsonl"

# Fields that must be identical in every source run of one shared record.
SAME_FOR_ALL = ("model_id", "checkpoint_sha256", "class_map_sha256", "task", "settings",
                "upstream_revision", "git_commit", "requested_device", "precision",
                "preprocessing", "postprocessing")


def plan_runs(
    scan_inputs: list[dict[str, Any]], model_id: str, checkpoint: str, output_root: str
) -> list[dict[str, Any]]:
    """List the runner arguments for each scan input. Nothing is executed here.

    The runner names a scan after its image file, so a scan ID that differs from
    the file name would be lost; refuse it instead.
    """
    spec = get_model(model_id)
    if not scan_inputs:
        raise ValueError("at least one scan input is required")
    seen, runs = set(), []
    for scan_input in scan_inputs:
        validate_scan_input(scan_input)
        scan_id = scan_input["scan_id"]
        if scan_id in seen:
            raise ValueError("scan IDs must be unique")
        seen.add(scan_id)
        if PureWindowsPath(scan_input["image_path"]).stem != scan_id:
            raise ValueError(f"{scan_id}: scan ID must equal the image file name without suffix")
        runs.append({
            "scan_id": scan_id,
            "arguments": ["scripts/infer_generic_yolov10.py", checkpoint, scan_input["image_path"],
                          f"{output_root}/{scan_id}", "--checkpoint-sha256", spec.sha256,
                          "--model", spec.id],
        })
    return runs


def summarize(manifest: dict[str, Any], results: list[dict[str, Any]]) -> dict[str, Any]:
    """Counts for a validated record. These describe the file, not model quality."""
    validate_prediction_set(manifest, results)
    labels: dict[str, int] = {}
    for result in results:
        for detection in result["detections"]:
            label = detection["category"]["label"]
            labels[label] = labels.get(label, 0) + 1
    ok = [result for result in results if result["status"] == "ok"]
    return {
        "ok": True,
        "run_id": manifest["run_id"],
        "role": manifest["role"],
        "status": manifest["status"],
        "model_id": manifest["model"]["id"],
        "task": manifest["model"]["task"],
        "checkpoint_sha256": manifest["model"]["checkpoint_sha256"],
        "threshold": manifest["settings"]["conf"],
        "scans": len(results),
        "failed_scans": len(results) - len(ok),
        "scans_without_detections": sum(not result["detections"] for result in ok),
        "detections": sum(labels.values()),
        "detections_by_label": dict(sorted(labels.items())),
        "note": "File summary only. Scans without detections are not benign results.",
    }


def load_run_dir(path: Path) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Read one runner output directory. A failed run has no predictions file."""
    manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
    predictions = path / "predictions.json"
    result = json.loads(predictions.read_text(encoding="utf-8")) if predictions.is_file() else None
    return manifest, result


def _checked_model(source: dict[str, Any]) -> dict[str, Any]:
    """Model identity from the catalog, after confirming the run used that pairing."""
    spec = get_model(source["model_id"])
    names = {str(index): name for index, name in spec.names.items()}
    if (
        source["checkpoint_sha256"] != spec.sha256
        or source["class_map_sha256"] != spec.class_map_sha256
        or source["task"] != spec.task
        or source["source_category_map"] != spec.source_category_map
        or source.get("model_names", names) != names
    ):
        raise ValueError("run does not match the inspected catalog pairing for its model")
    return {
        "id": spec.id,
        "task": spec.task,
        "kind": spec.kind,
        "checkpoint_sha256": spec.sha256,
        "parent_checkpoint_sha256": None,
        "class_map_sha256": spec.class_map_sha256,
        "model_names": names,
        "source_category_map": spec.source_category_map,
    }


def shared_baseline(
    run_id: str, runs: list[tuple[dict[str, Any], dict[str, Any] | None]], timestamp_utc: str
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Build the shared manifest and scan results from (manifest, result) pairs."""
    if not runs:
        raise ValueError("at least one source run is required")
    first = runs[0][0]
    for source, _ in runs:
        if source["status"] not in ("ok", "error"):
            raise ValueError("source run did not finish; rerun it before recording")
        for key in SAME_FOR_ALL:
            if source[key] != first[key]:
                raise ValueError(f"source runs differ in {key}; record them separately")
    # Every run is checked against the catalog, not only the first one: the class and
    # category maps are per-run fields and are not covered by SAME_FOR_ALL.
    model = _checked_model(first)
    for source, _ in runs[1:]:
        if _checked_model(source) != model:
            raise ValueError("source runs differ in model identity; record them separately")
    provenance = f"sha256:{model['checkpoint_sha256']}"
    # A run that failed before its device was resolved has device=None. The requested
    # device is kept separately and is never reported as the device that ran inference.
    resolved = {source["device"] for source, _ in runs if source["device"]}
    if len(resolved) > 1:
        raise ValueError("source runs differ in device; record them separately")
    device = resolved.pop() if resolved else None

    inputs, results = [], []
    for source, result in runs:
        # The runner names a scan after its image file; keep the name, drop the path.
        scan_id = PureWindowsPath(source["input"]).stem
        inputs.append({"scan_id": scan_id, "sha256": source["input_sha256"],
                       "source_run_id": source["run_id"]})
        if source["status"] == "ok":
            if result is None or result["scan_id"] != scan_id:
                raise ValueError(f"{source['run_id']}: predictions do not match the run input")
            result = {**result, "run": {"id": run_id, "provenance": MANIFEST_NAME}}
        else:
            # Keep the failure visible. The message stays generic because the
            # original error text can contain local paths.
            result = {
                "schema_version": SCHEMA_VERSION, "scan_id": scan_id, "status": "error",
                "image": None,
                "model": {"id": model["id"], "task": model["task"], "provenance": provenance},
                "run": {"id": run_id, "provenance": MANIFEST_NAME},
                "threshold": first["settings"]["conf"], "detections": [],
                "error": {"code": source.get("error_code") or "inference_failed",
                          "message": f"see source run {source['run_id']}"},
            }
        results.append(result)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "role": "baseline",
        "status": "ok" if all(source["status"] == "ok" for source, _ in runs) else "error",
        "timestamp_utc": timestamp_utc,
        "model": model,
        "code": {"git_commit": first["git_commit"],
                 "git_dirty": any(source["git_status"].strip() for source, _ in runs),
                 "upstream_revision": first["upstream_revision"]},
        "settings": first["settings"],
        "stages": {
            "preprocessing": {"status": "inherited", "detail": first["preprocessing"]},
            "roi": {"status": "absent",
                    "detail": "no separate ROI or segmentation step; the full image is the input"},
            "features": {"status": "inherited",
                         "detail": "detector backbone inside the checkpoint; no separate stage"},
            "postprocessing": {"status": "inherited", "detail": first["postprocessing"]},
        },
        "requested_device": first["requested_device"],
        "device": device,
        "precision": first["precision"],
        "inputs": inputs,
        "limitations": ["batch-one diagnostic runs; not an accuracy evaluation",
                        "an empty detection list is not a benign or safe result",
                        *first["limitations"]],
    }
    validate_prediction_set(manifest, results)
    return manifest, results


def write_record(output: Path, manifest: dict[str, Any], results: list[dict[str, Any]]) -> None:
    """Write run_manifest.json and predictions.jsonl into a new directory."""
    validate_prediction_set(manifest, results)
    output.mkdir(parents=True, exist_ok=False)
    (output / MANIFEST_NAME).write_text(dumps_run_manifest(manifest) + "\n", encoding="utf-8")
    lines = "".join(dumps_scan_result(result) + "\n" for result in results)
    (output / PREDICTIONS_NAME).write_text(lines, encoding="utf-8")


def read_record(directory: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Load and re-validate a shared record; the entry point for training/evaluation code."""
    manifest = json.loads((directory / MANIFEST_NAME).read_text(encoding="utf-8"))
    text = (directory / PREDICTIONS_NAME).read_text(encoding="utf-8")
    results = [json.loads(line) for line in text.splitlines() if line.strip()]
    validate_prediction_set(manifest, results)
    return manifest, results
