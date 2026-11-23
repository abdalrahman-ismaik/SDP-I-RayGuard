"""Synthetic checks for the training-only box clamp. Not real-data or model evidence."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from sdp_xray import box_repair
from sdp_xray.box_repair import (
    find_overshoots,
    overshoot,
    repair_training_copy,
    verify_training_source,
)

SHA = "a" * 64
SCRIPT = Path(__file__).parents[1] / "scripts" / "repair_train_boxes.py"


def train_doc():
    """Three boxes: one inside, one 0.0002 px past the right edge, one 0.0001 px above the top."""
    return {
        "images": [{"id": 1, "file_name": "Train000001.jpg", "width": 100, "height": 80},
                   {"id": 2, "file_name": "Train000002.jpg", "width": 100, "height": 80}],
        "annotations": [
            {"id": 10, "image_id": 1, "category_id": 0, "bbox": [10, 10, 20, 20],
             "area": 400, "iscrowd": 0},
            {"id": 11, "image_id": 1, "category_id": 0, "bbox": [50.1, 10, 49.9002, 20],
             "area": 998, "iscrowd": 0},
            {"id": 12, "image_id": 2, "category_id": 0, "bbox": [5, -0.0001, 10, 10],
             "area": 100, "iscrowd": 0},
        ],
        "categories": [{"id": 0, "name": "Explosive"}],
    }


def _script():
    spec = importlib.util.spec_from_file_location("repair_train_boxes", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bind_fixture(monkeypatch, document, source_sha256=SHA):
    """Test-only provenance substitution; never a real-data approval receipt."""
    canonical = json.dumps(document, sort_keys=True, separators=(",", ":"), allow_nan=False)
    monkeypatch.setattr(box_repair, "VERIFIED_TRAIN_SOURCES", {
        source_sha256: {"task": "synthetic", "published_name": "synthetic-train.json",
                        "content_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
                        "image_count": len(document["images"])}})


@pytest.fixture(autouse=True)
def synthetic_provenance(monkeypatch):
    bind_fixture(monkeypatch, train_doc())


def test_overshoot_measures_each_edge():
    assert overshoot([0, 0, 100, 80], 100, 80) == 0
    assert overshoot([-0.5, 0, 10, 10], 100, 80) == 0.5
    assert overshoot([95, 0, 10, 10], 100, 80) == 5
    assert overshoot([0, 75, 10, 7], 100, 80) == 2


def test_find_overshoots_lists_only_affected_boxes():
    found = find_overshoots(train_doc())
    assert [item["annotation_id"] for item in found] == [11, 12]
    assert all(0 < item["overshoot_px"] < 0.001 for item in found)


def test_repair_clamps_into_a_copy_and_records_every_change():
    source = train_doc()
    before = copy.deepcopy(source)
    derived, record = repair_training_copy(source, "binary_explosive_det_train.json", SHA, 2)
    assert source == before
    assert find_overshoots(derived) == []
    assert derived["annotations"][0] == source["annotations"][0]
    x, y, w, h = derived["annotations"][1]["bbox"]
    assert x == 50.1 and x + w <= 100 and abs(w - 49.9002) < 0.001
    assert derived["annotations"][2]["bbox"][1] == 0
    assert derived["annotations"][1]["area"] == w * h
    assert derived["annotations"][2]["area"] != source["annotations"][2]["area"]
    assert record["source_sha256"] == SHA and record["tolerance_px"] == 0.001
    assert record["source_split"]["split"] == "published_train"
    assert record["area_field"] == "derived bbox width * height for changed annotations only"
    assert [c["annotation_id"] for c in record["changes"]] == [11, 12]
    for change in record["changes"]:
        assert {"bbox", "derived_bbox", "overshoot_px", "file_name", "image_id"} <= set(change)
        original = next(a for a in source["annotations"] if a["id"] == change["annotation_id"])
        assert change["source_area"] == original["area"]
        assert change["derived_area"] == change["derived_bbox"][2] * change["derived_bbox"][3]
    assert derived["images"] == source["images"]
    assert derived["categories"] == source["categories"]
    for original, changed in zip(source["annotations"], derived["annotations"], strict=True):
        assert {k: v for k, v in original.items() if k not in {"bbox", "area"}} == {
            k: v for k, v in changed.items() if k not in {"bbox", "area"}}


def test_large_overshoot_is_blocked(monkeypatch):
    doc = train_doc()
    doc["annotations"][2]["bbox"] = [5, -4, 10, 10]
    bind_fixture(monkeypatch, doc)
    with pytest.raises(ValueError, match="blocked"):
        repair_training_copy(doc, "train.json", SHA, 2)


def test_unexpected_count_stops():
    with pytest.raises(ValueError, match="expected 5"):
        repair_training_copy(train_doc(), "train.json", SHA, 5)


@pytest.mark.parametrize(
    ("name", "edit"),
    [
        ("binary_explosive_det_test.json", lambda d: None),
        ("train.json", lambda d: d["images"][0].__setitem__("file_name", "Test000001.jpg")),
    ],
)
def test_test_annotations_are_never_repaired(name, edit):
    doc = train_doc()
    edit(doc)
    with pytest.raises(ValueError, match="test"):
        repair_training_copy(doc, name, SHA, 2)


def test_script_check_then_repair(tmp_path, capsys, monkeypatch):
    source = tmp_path / "binary_explosive_det_train.json"
    source.write_text(json.dumps(train_doc()), encoding="utf-8")
    original = source.read_bytes()
    bind_fixture(monkeypatch, train_doc(), hashlib.sha256(original).hexdigest())
    assert _script().main(["check", "--annotations", str(source), "--verify-training-source"]) == 0
    checked = json.loads(capsys.readouterr().out)
    assert checked["boxes_outside_image"] == 2
    assert checked["verified_source"]["split"] == "published_train"
    out = tmp_path / "derived"
    assert _script().main(["repair", "--annotations", str(source), "--expected", "2",
                           "--output-dir", str(out)]) == 0
    assert source.read_bytes() == original
    record = json.loads((out / "repair-record.json").read_text(encoding="utf-8"))
    derived = json.loads((out / record["derived_file_name"]).read_text(encoding="utf-8"))
    assert find_overshoots(derived) == []
    assert str(tmp_path) not in json.dumps(record)
    # Never overwrite, and refuse a wrong count without writing anything.
    assert _script().main(["repair", "--annotations", str(source), "--expected", "2",
                           "--output-dir", str(out)]) == 2
    assert _script().main(["repair", "--annotations", str(source), "--expected", "5",
                           "--output-dir", str(tmp_path / "other")]) == 2
    assert not (tmp_path / "other").exists()


def test_unknown_bytes_cannot_gain_training_identity_from_a_filename():
    with pytest.raises(ValueError, match="verified published training"):
        repair_training_copy(train_doc(), "train.json", "b" * 64, 2)


@pytest.mark.parametrize("change", [
    lambda d: d["images"][0].__setitem__("file_name", "renamed.jpg"),
    lambda d: d["annotations"][0].__setitem__("category_id", 7),
    lambda d: d["images"].pop(),
])
def test_claiming_a_known_hash_does_not_allow_changed_or_mixed_membership(change):
    document = train_doc()
    change(document)
    with pytest.raises(ValueError, match="verified published training"):
        verify_training_source(document, SHA)


def test_renamed_test_like_export_is_rejected_without_writes(tmp_path, capsys):
    document = train_doc()
    # IDs can overlap across published splits; names and IDs do not prove provenance.
    for row in document["images"]:
        row["file_name"] = str(row["id"]) + ".jpg"
    source = tmp_path / "train.json"
    source.write_text(json.dumps(document), encoding="utf-8")
    original = source.read_bytes()
    output = tmp_path / "derived"
    assert _script().main(["repair", "--annotations", str(source), "--expected", "2",
                           "--output-dir", str(output)]) == 2
    assert "verified published training" in capsys.readouterr().err
    assert source.read_bytes() == original and not output.exists()


@pytest.mark.parametrize("edit", [
    lambda a: a.__setitem__("segmentation", [[1, 1, 2, 1, 2, 2]]),
    lambda a: a.pop("area"),
])
def test_area_policy_refuses_segmentation_or_missing_area(monkeypatch, edit):
    document = train_doc()
    edit(document["annotations"][1])
    bind_fixture(monkeypatch, document)
    with pytest.raises(ValueError, match="box-only"):
        repair_training_copy(document, "train.json", SHA, 2)


def test_tolerance_cannot_be_relaxed_by_a_caller():
    with pytest.raises(ValueError, match="fixed"):
        repair_training_copy(train_doc(), "train.json", SHA, 2, tolerance=1)
