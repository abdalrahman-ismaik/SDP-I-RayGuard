"""Synthetic checks for the training-only box clamp. Not real-data or model evidence."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest

from sdp_xray.box_repair import find_overshoots, overshoot, repair_training_copy

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
    assert derived["annotations"][1]["area"] == 998
    assert record["source_sha256"] == SHA and record["tolerance_px"] == 0.001
    assert [c["annotation_id"] for c in record["changes"]] == [11, 12]
    for change in record["changes"]:
        assert {"bbox", "derived_bbox", "overshoot_px", "file_name", "image_id"} <= set(change)


def test_large_overshoot_is_blocked():
    doc = train_doc()
    doc["annotations"][2]["bbox"] = [5, -4, 10, 10]
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


def test_script_check_then_repair(tmp_path, capsys):
    source = tmp_path / "binary_explosive_det_train.json"
    source.write_text(json.dumps(train_doc()), encoding="utf-8")
    original = source.read_bytes()
    assert _script().main(["check", "--annotations", str(source)]) == 0
    assert json.loads(capsys.readouterr().out)["boxes_outside_image"] == 2
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
