"""Synthetic software checks for the baseline adapter.

The source manifests below copy the field layout written by
scripts/infer_generic_yolov10.py. Boxes and scores are invented test values, not
model output, and nothing here is inference or accuracy evidence.
"""

import copy
import json

import pytest

from sdp_xray.baseline import load_run_dir, read_record, shared_baseline, write_record
from sdp_xray.cli import main
from sdp_xray.model_catalog import DEFAULT_MODEL_ID, get_model

SPEC = get_model(DEFAULT_MODEL_ID)
WHEN = "2026-01-01T00:00:00+00:00"
PRIVATE = "C:\\Users\\someone\\private"


def source_run(name, status="ok"):
    manifest = {
        "status": status,
        "run_id": f"legacy-{name}",
        "command": ["python", f"{PRIVATE}\\infer.py"],
        "model_id": SPEC.id,
        "class_map_sha256": SPEC.class_map_sha256,
        "git_commit": "0000000",
        "git_status": "",
        "checkpoint": f"{PRIVATE}\\weights.pt",
        "checkpoint_sha256": SPEC.sha256,
        "input": f"{PRIVATE}\\{name}.jpg",
        "input_sha256": "c" * 64,
        "upstream_revision": "synthetic-revision",
        "requested_device": "cpu",
        "device": "cpu",
        "precision": "float32",
        "task": SPEC.task,
        "source_category_map": SPEC.source_category_map,
        "settings": {"imgsz": 640, "batch": 1, "conf": 0.25, "max_det": 300, "augment": False},
        "preprocessing": "synthetic preprocessing text",
        "postprocessing": "synthetic postprocessing text",
        "limitations": ["synthetic source run"],
        "model_names": {"0": "Explosive"},
    }
    if status != "ok":
        manifest.update(error_code="synthetic_failure", error=f"failed at {PRIVATE}")
        return manifest, None
    result = {
        "schema_version": "1.0", "scan_id": name, "status": "ok",
        "image": {"width": 200, "height": 100},
        "model": {"id": SPEC.id, "task": SPEC.task, "provenance": f"sha256:{SPEC.sha256}"},
        "run": {"id": f"legacy-{name}", "provenance": "manifest.json"},
        "threshold": 0.25, "error": None,
        "detections": [{
            "id": "threat-0", "kind": "suspicious_region",
            "box_xyxy": [10.5, 20.25, 60.0, 90.75],
            "category": {"namespace": SPEC.task, "label": "Explosive"},
            "confidence": 0.875, "device_id": None,
        }],
    }
    return manifest, result


def test_shared_record_keeps_identity_boxes_and_scores():
    source = source_run("scan-a")
    manifest, results = shared_baseline("shared-1", [source, source_run("scan-b")], WHEN)
    assert manifest["role"] == "baseline"
    assert manifest["model"]["checkpoint_sha256"] == SPEC.sha256
    assert manifest["model"]["source_category_map"] == {"0": "Explosive"}
    assert manifest["stages"]["roi"]["status"] == "absent"
    assert [item["source_run_id"] for item in manifest["inputs"]] == [
        "legacy-scan-a", "legacy-scan-b"]
    detection = results[0]["detections"][0]
    assert detection == source[1]["detections"][0]
    assert results[0]["run"] == {"id": "shared-1", "provenance": "run_manifest.json"}


def test_shared_record_has_no_local_paths():
    manifest, results = shared_baseline(
        "shared-1", [source_run("scan-a"), source_run("scan-b", status="error")], WHEN)
    assert "private" not in json.dumps([manifest, results])


def test_failed_run_stays_visible_as_error():
    manifest, results = shared_baseline(
        "shared-1", [source_run("scan-a"), source_run("scan-b", status="error")], WHEN)
    assert manifest["status"] == "error"
    assert results[1]["status"] == "error"
    assert results[1]["error"]["code"] == "synthetic_failure"
    assert results[1]["detections"] == []


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("checkpoint_sha256", "d" * 64),
        ("class_map_sha256", "d" * 64),
        ("task", "another.task"),
        ("source_category_map", {"1": "Explosive"}),
        ("model_names", {"0": "Something else"}),
        ("model_id", "not-in-catalog"),
    ],
)
def test_rejects_runs_outside_the_catalog_pairing(key, value):
    manifest, result = source_run("scan-a")
    manifest[key] = value
    with pytest.raises(ValueError):
        shared_baseline("shared-1", [(manifest, result)], WHEN)


def test_rejects_mixed_settings_and_unfinished_runs():
    other = source_run("scan-b")
    other[0]["settings"] = {**other[0]["settings"], "conf": 0.5}
    with pytest.raises(ValueError):
        shared_baseline("shared-1", [source_run("scan-a"), other], WHEN)
    started = source_run("scan-a")
    started[0]["status"] = "started"
    with pytest.raises(ValueError):
        shared_baseline("shared-1", [started], WHEN)
    with pytest.raises(ValueError):
        shared_baseline("shared-1", [], WHEN)


def test_rejects_predictions_from_another_scan():
    manifest, result = source_run("scan-a")
    wrong = copy.deepcopy(result)
    wrong["scan_id"] = "scan-z"
    with pytest.raises(ValueError):
        shared_baseline("shared-1", [(manifest, wrong)], WHEN)


def write_source(directory, name, status="ok"):
    manifest, result = source_run(name, status)
    directory.mkdir()
    (directory / "manifest.json").write_text(json.dumps(manifest))
    if result is not None:
        (directory / "predictions.json").write_text(json.dumps(result))
    return directory


def test_write_and_read_round_trip(tmp_path):
    runs = [load_run_dir(write_source(tmp_path / "a", "scan-a")),
            load_run_dir(write_source(tmp_path / "b", "scan-b", status="error"))]
    manifest, results = shared_baseline("shared-1", runs, WHEN)
    write_record(tmp_path / "shared-1", manifest, results)
    assert read_record(tmp_path / "shared-1") == (manifest, results)
    with pytest.raises(FileExistsError):
        write_record(tmp_path / "shared-1", manifest, results)


def test_cli_writes_record_and_reports_counts(tmp_path, capsys):
    first = write_source(tmp_path / "a", "scan-a")
    second = write_source(tmp_path / "b", "scan-b")
    output = tmp_path / "shared-cli"
    assert main(["baseline-record", str(output), str(first), str(second)]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report == {"ok": True, "run_id": "shared-cli", "model_id": SPEC.id,
                      "scans": 2, "failed_scans": 0, "detections": 2}
    manifest, results = read_record(output)
    assert manifest["run_id"] == "shared-cli" and len(results) == 2


def test_cli_fails_closed_on_bad_source(tmp_path, capsys):
    bad = write_source(tmp_path / "a", "scan-a")
    (bad / "manifest.json").write_text("{}")
    assert main(["baseline-record", str(tmp_path / "out"), str(bad)]) == 2
    assert json.loads(capsys.readouterr().out)["ok"] is False
    assert not (tmp_path / "out").exists()
