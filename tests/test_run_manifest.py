"""Synthetic software checks for the shared run manifest; no inference evidence."""

import copy

import pytest

from sdp_xray.common.run_manifest import (
    dumps_run_manifest,
    loads_run_manifest,
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
