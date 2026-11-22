"""Synthetic checks for the training-only box clamp. Not real-data or model evidence."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from sdp_xray.box_repair import find_overshoots, overshoot, repair_training_copy

SHA = "a" * 64
TEST_SHA = "b" * 64
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


def make_test_doc():
    """Published test export stand-in; its file names define the split guard."""
    return {"images": [{"id": 1, "file_name": "Test000001.jpg", "width": 100, "height": 80}],
            "annotations": [], "categories": [{"id": 0, "name": "Explosive"}]}


def repair(doc, name="binary_explosive_det_train.json", expected=2, test=None, test_sha=TEST_SHA,
           source_sha=SHA):
    return repair_training_copy(doc, name, source_sha, expected,
                                test if test is not None else make_test_doc(), test_sha)


def _script():
    spec = importlib.util.spec_from_file_location("repair_train_boxes", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    derived, record = repair(source)
    assert source == before
    assert find_overshoots(derived) == []
    assert derived["annotations"][0] == source["annotations"][0]
    x, y, w, h = derived["annotations"][1]["bbox"]
    assert x == 50.1 and x + w <= 100 and abs(w - 49.9002) < 0.001
    assert derived["annotations"][2]["bbox"][1] == 0
    assert derived["annotations"][1]["area"] == 998
    assert record["source_sha256"] == SHA and record["tolerance_px"] == 0.001
    assert [c["annotation_id"] for c in record["changes"]] == [11, 12]
    assert record["split_check"] == {"test_sha256": TEST_SHA, "test_images": 1,
                                     "shared_file_names": 0}
    assert "unchanged" in record["area_field"]
    assert "overall AP@[.50:.95]" in record["area_field"]
    assert "size-specific validation metrics can be affected" in record["area_field"]
    for change in record["changes"]:
        assert {"bbox", "derived_bbox", "overshoot_px", "file_name", "image_id"} <= set(change)
        assert change["area"] == source["annotations"][change["annotation_id"] - 10]["area"]
        assert -0.001 * 100 < change["bbox_area_change_px2"] <= 0


def test_large_overshoot_is_blocked():
    doc = train_doc()
    doc["annotations"][2]["bbox"] = [5, -4, 10, 10]
    with pytest.raises(ValueError, match="blocked"):
        repair(doc, "train.json")


def test_unexpected_count_stops():
    with pytest.raises(ValueError, match="expected 5"):
        repair(train_doc(), "train.json", expected=5)


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
        repair(doc, name)


def test_images_in_published_test_split_are_refused_whatever_their_name():
    doc = train_doc()
    split = make_test_doc()
    split["images"][0]["file_name"] = "Train000002.jpg"  # same image, misleading name
    with pytest.raises(ValueError, match="published test split"):
        repair(doc, test=split)


def test_source_identical_to_published_test_file_is_refused():
    with pytest.raises(ValueError, match="published test annotation file"):
        repair(train_doc(), source_sha=TEST_SHA)


def test_script_check_then_repair(tmp_path, capsys):
    source = tmp_path / "binary_explosive_det_train.json"
    source.write_text(json.dumps(train_doc()), encoding="utf-8")
    split = tmp_path / "binary_explosive_det_test.json"
    split.write_text(json.dumps(make_test_doc()), encoding="utf-8")
    original = source.read_bytes()
    guard = ["--test-annotations", str(split)]
    assert _script().main(["check", "--annotations", str(source)]) == 0
    assert json.loads(capsys.readouterr().out)["boxes_outside_image"] == 2
    out = tmp_path / "derived"
    assert _script().main(["repair", "--annotations", str(source), "--expected", "2",
                           "--output-dir", str(out), *guard]) == 0
    assert source.read_bytes() == original
    record = json.loads((out / "repair-record.json").read_text(encoding="utf-8"))
    derived = json.loads((out / record["derived_file_name"]).read_text(encoding="utf-8"))
    written = (out / record["derived_file_name"]).read_bytes()
    assert record["derived_file_sha256"] == hashlib.sha256(written).hexdigest()
    assert find_overshoots(derived) == []
    assert record["split_check"]["test_file_name"] == split.name
    assert str(tmp_path) not in json.dumps(record)
    # Never overwrite, and refuse a wrong count without writing anything.
    assert _script().main(["repair", "--annotations", str(source), "--expected", "2",
                           "--output-dir", str(out), *guard]) == 2
    assert _script().main(["repair", "--annotations", str(source), "--expected", "5",
                           "--output-dir", str(tmp_path / "other"), *guard]) == 2
    assert not (tmp_path / "other").exists()


@pytest.mark.parametrize("edit", [
    lambda image: image.pop("width"),
    lambda image: image.update(height=0),
    lambda image: image.update(width="100"),
    lambda image: image.pop("file_name"),
])
def test_image_without_usable_size_or_name_is_refused(edit):
    doc = train_doc()
    edit(doc["images"][0])
    with pytest.raises(ValueError, match="positive width/height"):
        find_overshoots(doc)
    with pytest.raises(ValueError, match="positive width/height"):
        repair(doc)
