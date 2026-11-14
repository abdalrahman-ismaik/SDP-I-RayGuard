"""Synthetic software checks for the shared run manifest; no inference evidence."""

import copy

import pytest

from sdp_xray.common.run_manifest import (
    dumps_run_manifest,
    loads_run_manifest,
    validate_prediction_set,
    validate_run_manifest,
)

HASH_A = "a" * 64
HASH_B = "b" * 64


def synthetic_manifest():
    return {
        "schema_version": "1.0",
        "run_id": "synthetic-run",
        "role": "baseline",
        "status": "ok",
        "timestamp_utc": "2026-01-01T00:00:00+00:00",
        "model": {
            "id": "synthetic-only",
            "task": "synthetic.task",
            "kind": "suspicious_region",
            "checkpoint_sha256": HASH_A,
            "parent_checkpoint_sha256": None,
            "class_map_sha256": HASH_B,
            "model_names": {"0": "example-region"},
            "source_category_map": {"7": "example-region"},
        },
        "code": {"git_commit": "0000000", "git_dirty": False, "upstream_revision": "synthetic"},
        "settings": {"imgsz": 640, "batch": 1, "conf": 0.25, "max_det": 300, "augment": False},
        "stages": {
            "preprocessing": {"status": "inherited", "detail": "synthetic"},
            "roi": {"status": "absent", "detail": "synthetic"},
            "features": {"status": "inherited", "detail": "synthetic"},
            "postprocessing": {"status": "inherited", "detail": "synthetic"},
        },
        "device": "cpu",
        "precision": "float32",
        "inputs": [{"scan_id": "synthetic-scan", "sha256": HASH_A, "source_run_id": "legacy-1"}],
        "limitations": ["synthetic software check only"],
    }


def synthetic_result(detections=1):
    return {
        "schema_version": "1.0",
        "scan_id": "synthetic-scan",
        "status": "ok",
        "image": {"width": 100, "height": 80},
        "model": {"id": "synthetic-only", "task": "synthetic.task",
                  "provenance": f"sha256:{HASH_A}"},
        "run": {"id": "synthetic-run", "provenance": "run_manifest.json"},
        "threshold": 0.25,
        "error": None,
        "detections": [
            {
                "id": f"threat-{index}",
                "kind": "suspicious_region",
                "box_xyxy": [2.5, 3, 9, 12.25],
                "category": {"namespace": "synthetic.task", "label": "example-region"},
                "confidence": 0.7,
                "device_id": None,
            }
            for index in range(detections)
        ],
    }


def test_prediction_set_accepts_matching_and_empty_results():
    validate_prediction_set(synthetic_manifest(), [synthetic_result()])
    validate_prediction_set(synthetic_manifest(), [synthetic_result(detections=0)])


def test_prediction_set_keeps_failed_scans():
    failed = synthetic_result(detections=0)
    failed.update(status="error", image=None,
                  error={"code": "synthetic", "message": "synthetic failure"})
    validate_prediction_set(synthetic_manifest(), [failed])


@pytest.mark.parametrize(
    "edit",
    [
        lambda r: r["model"].update(id="another-model"),
        lambda r: r["model"].update(provenance=f"sha256:{HASH_B}"),
        lambda r: r["run"].update(id="another-run"),
        lambda r: r.update(threshold=0.5),
        lambda r: r["detections"][0].update(kind="device"),
        lambda r: r["detections"][0]["category"].update(namespace="other.task"),
        lambda r: r["detections"][0]["category"].update(label="unknown-label"),
        lambda r: r.update(scan_id="unlisted-scan"),
    ],
)
def test_prediction_set_rejects_mismatches(edit):
    result = synthetic_result()
    edit(result)
    with pytest.raises(ValueError):
        validate_prediction_set(synthetic_manifest(), [result])


def test_prediction_set_requires_every_input_once():
    manifest = synthetic_manifest()
    with pytest.raises(ValueError):
        validate_prediction_set(manifest, [])
    with pytest.raises(ValueError):
        validate_prediction_set(manifest, [synthetic_result(), synthetic_result()])


def test_round_trip():
    manifest = synthetic_manifest()
    assert loads_run_manifest(dumps_run_manifest(manifest)) == manifest


def change(path, value):
    manifest = synthetic_manifest()
    target = manifest
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    return manifest


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("schema_version",), "2.0"),
        (("role",), "final"),
        (("status",), "started"),
        (("model", "kind"), "threat"),
        (("model", "checkpoint_sha256"), "ABC"),
        (("model", "checkpoint_sha256"), HASH_A.upper()),
        (("model", "model_names"), {}),
        (("model", "model_names"), {"zero": "example-region"}),
        (("model", "source_category_map"), {"7": "another-label"}),
        (("model", "parent_checkpoint_sha256"), HASH_B),
        (("code", "git_dirty"), "no"),
        (("settings", "batch"), 0),
        (("settings", "conf"), 1.5),
        (("settings", "augment"), 0),
        (("stages", "roi", "status"), "planned"),
        (("stages", "roi", "detail"), ""),
        (("inputs",), []),
        (("inputs", 0, "sha256"), "not-a-hash"),
        (("limitations",), [""]),
    ],
)
def test_rejects_invalid_values(path, value):
    with pytest.raises(ValueError):
        validate_run_manifest(change(path, value))


def test_rejects_missing_and_unknown_fields():
    missing = synthetic_manifest()
    del missing["stages"]
    with pytest.raises(ValueError):
        validate_run_manifest(missing)
    extra = synthetic_manifest()
    extra["checkpoint_path"] = "somewhere/local.pt"
    with pytest.raises(ValueError):
        validate_run_manifest(extra)


def test_rejects_duplicate_scan_ids():
    manifest = synthetic_manifest()
    manifest["inputs"].append(copy.deepcopy(manifest["inputs"][0]))
    with pytest.raises(ValueError):
        validate_run_manifest(manifest)


def test_candidate_requires_parent_checkpoint():
    candidate = change(("role",), "candidate")
    with pytest.raises(ValueError):
        validate_run_manifest(candidate)
    candidate["model"]["parent_checkpoint_sha256"] = HASH_B
    validate_run_manifest(candidate)
