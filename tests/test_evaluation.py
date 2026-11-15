"""Synthetic software checks for T42 evaluation helpers. Not model or accuracy evidence."""

import copy
import json

import pytest

from sdp_xray.evaluation import (
    build_report,
    check_ground_truth,
    check_protocol,
    coco_detections,
    dumps_report,
    iou_xywh,
    matched_pair_differences,
    operating_point,
    validate_protocol,
    xyxy_to_xywh,
)

HASH_A = "a" * 64
HASH_B = "b" * 64
HASH_C = "c" * 64
TASK = "synthetic.task"
# Category ID 0 on purpose: it is valid in IEDXray's generic task and must not be renumbered.
CATEGORY_MAP = {"0": "example-region"}
SCANS = ("Test000001", "Test000002", "Test000003")


def ground_truth():
    return {
        "images": [
            {"id": 10, "file_name": "Test000001.jpg", "width": 100, "height": 80},
            {"id": 11, "file_name": "Test000002.jpg", "width": 100, "height": 80},
            {"id": 12, "file_name": "Test000003.jpg", "width": 100, "height": 80},
        ],
        "annotations": [
            {"id": 1, "image_id": 10, "category_id": 0, "bbox": [10, 10, 20, 20],
             "area": 400, "iscrowd": 0},
            {"id": 2, "image_id": 12, "category_id": 0, "bbox": [50, 40, 30, 20],
             "area": 600, "iscrowd": 0},
        ],
        "categories": [{"id": 0, "name": "example-region"}],
    }


def manifest(role="baseline", checkpoint=HASH_A, parent=None, conf=0.001):
    return {
        "schema_version": "1.0",
        "run_id": f"synthetic-{role}",
        "role": role,
        "status": "ok",
        "timestamp_utc": "2026-01-01T00:00:00+00:00",
        "model": {"id": f"synthetic-{role}", "task": TASK, "kind": "suspicious_region",
                  "checkpoint_sha256": checkpoint, "parent_checkpoint_sha256": parent,
                  "class_map_sha256": HASH_B, "model_names": {"0": "example-region"},
                  "source_category_map": dict(CATEGORY_MAP)},
        "code": {"git_commit": "0000000", "git_dirty": False, "upstream_revision": "synthetic"},
        "settings": {"imgsz": 640, "batch": 1, "conf": conf, "max_det": 300, "augment": False},
        "stages": {name: {"status": "inherited", "detail": "synthetic"}
                   for name in ("preprocessing", "roi", "features", "postprocessing")},
        "requested_device": "cpu",
        "device": "cpu",
        "precision": "float32",
        "inputs": [{"scan_id": scan, "sha256": HASH_C, "source_run_id": f"src-{scan}"}
                   for scan in SCANS],
        "limitations": ["synthetic software check only"],
    }


def result(scan_id, boxes, record=None, status="ok"):
    record = record or manifest()
    value = {
        "schema_version": "1.0", "scan_id": scan_id, "status": status,
        "image": {"width": 100, "height": 80} if status == "ok" else None,
        "model": {"id": record["model"]["id"], "task": TASK,
                  "provenance": f"sha256:{record['model']['checkpoint_sha256']}"},
        "run": {"id": record["run_id"], "provenance": "run_manifest.json"},
        "threshold": record["settings"]["conf"],
        "detections": [
            {"id": f"d{number}", "kind": "suspicious_region", "box_xyxy": box,
             "category": {"namespace": TASK, "label": "example-region"},
             "confidence": score, "device_id": None}
            for number, (box, score) in enumerate(boxes)
        ],
        "error": None if status == "ok" else {"code": "synthetic", "message": "synthetic"},
    }
    return value


def results(record=None):
    """One match on scan 1, one box on annotation-empty scan 2, one miss on scan 3."""
    return [
        result("Test000001", [([10, 10, 30, 30], 0.9)], record),
        result("Test000002", [([0, 0, 10, 10], 0.6)], record),
        result("Test000003", [], record),
    ]


def protocol(**changes):
    value = {
        "schema_version": "1.0", "protocol_id": "synthetic-protocol", "status": "draft",
        "task": TASK,
        "ground_truth": {"file_name": "synthetic.json", "sha256": None, "images": 3,
                         "annotations": 2},
        "evaluator": {"package": "pycocotools", "version": "0", "iou_type": "bbox"},
        "score_floor": 0.001,
        "operating_point": {"threshold": 0.25, "iou": 0.5, "basis": "synthetic"},
        "flagged_images": [{"file_name": "Test000002.jpg", "reason": "synthetic flag"}],
        "limitations": ["synthetic protocol"],
    }
    value.update(changes)
    return value


def test_xyxy_to_xywh_keeps_original_pixels():
    assert xyxy_to_xywh([2.5, 3, 9, 12.25]) == [2.5, 3, 6.5, 9.25]
    with pytest.raises(ValueError):
        xyxy_to_xywh([5, 5, 5, 9])


def test_iou_xywh():
    assert iou_xywh([0, 0, 10, 10], [0, 0, 10, 10]) == 1
    assert iou_xywh([0, 0, 10, 10], [20, 20, 5, 5]) == 0
    assert iou_xywh([0, 0, 10, 10], [5, 0, 10, 10]) == pytest.approx(50 / 150)


def test_ground_truth_index_and_summary():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    assert set(index["images_by_stem"]) == set(SCANS)
    assert index["summary"] == {"images": 3, "annotations": 2, "annotation_empty_images": 1,
                                "boxes_outside_image": 0, "crowd_annotations": 0}


def test_ground_truth_reports_out_of_bounds_without_clipping():
    truth = ground_truth()
    truth["annotations"][0]["bbox"] = [-4, 10, 20, 20]
    index = check_ground_truth(truth, CATEGORY_MAP)
    assert index["summary"]["boxes_outside_image"] == 1
    assert truth["annotations"][0]["bbox"] == [-4, 10, 20, 20]


@pytest.mark.parametrize(
    "edit",
    [
        lambda t: t["categories"].__setitem__(0, {"id": 1, "name": "example-region"}),
        lambda t: t["categories"].__setitem__(0, {"id": 0, "name": "other"}),
        lambda t: t["images"][1].__setitem__("file_name", "other/Test000001.jpg"),
        lambda t: t["images"][1].__setitem__("id", 10),
        lambda t: t["annotations"][0].__setitem__("image_id", 99),
        lambda t: t["annotations"][0].__setitem__("category_id", 5),
        lambda t: t["annotations"][0].pop("area"),
        lambda t: t["annotations"][0].__setitem__("bbox", [1, 1, 0, 5]),
    ],
)
def test_ground_truth_rejects_mismatch(edit):
    truth = ground_truth()
    edit(truth)
    with pytest.raises(ValueError):
        check_ground_truth(truth, CATEGORY_MAP)


def test_coco_detections_map_label_to_category_zero():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    prepared = coco_detections(manifest(), results(), index)
    assert prepared["detections"][0] == {"image_id": 10, "category_id": 0,
                                         "bbox": [10, 10, 20, 20], "score": 0.9}
    assert prepared["image_ids"] == [10, 11, 12]
    assert prepared["coverage"] == {"evaluated_images": 3, "failed_scans": [],
                                    "images_without_result": 0, "subset": False}


def test_empty_ok_scan_is_evaluated_and_has_no_detections():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    prepared = coco_detections(manifest(), results(), index)
    assert 12 in prepared["image_ids"]
    assert not [d for d in prepared["detections"] if d["image_id"] == 12]


def test_failed_scan_is_a_failure_not_an_empty_prediction():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    record = manifest()
    record["status"] = "error"
    items = results(record)
    items[2] = result("Test000003", [], record, status="error")
    with pytest.raises(ValueError, match="failed"):
        coco_detections(record, items, index)
    prepared = coco_detections(record, items, index, allow_subset=True)
    assert prepared["coverage"]["failed_scans"] == ["Test000003"]
    assert 12 not in prepared["image_ids"]
    assert prepared["coverage"]["subset"] is True


def test_missing_ground_truth_image_needs_explicit_subset():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    record = manifest()
    record["inputs"] = record["inputs"][:2]
    with pytest.raises(ValueError, match="no result"):
        coco_detections(record, results(record)[:2], index)
    prepared = coco_detections(record, results(record)[:2], index, allow_subset=True)
    assert prepared["coverage"]["images_without_result"] == 1


def test_scan_outside_ground_truth_or_wrong_size_is_rejected():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    record = manifest()
    record["inputs"][0]["scan_id"] = "Train000001"
    items = results(record)
    items[0]["scan_id"] = "Train000001"
    with pytest.raises(ValueError, match="not in the ground-truth"):
        coco_detections(record, items, index)
    items = results()
    items[0]["image"] = {"width": 200, "height": 80}
    items[0]["detections"] = []
    with pytest.raises(ValueError, match="image size"):
        coco_detections(manifest(), items, index)


def test_invalid_record_box_is_rejected_by_shared_contract():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    items = results()
    items[0]["detections"][0]["box_xyxy"] = [10, 10, 130, 30]
    with pytest.raises(ValueError, match="box"):
        coco_detections(manifest(), items, index)


def test_operating_point_counts_and_wording():
    truth = ground_truth()
    index = check_ground_truth(truth, CATEGORY_MAP)
    prepared = coco_detections(manifest(), results(), index)
    point = operating_point(truth, index, prepared["detections"], prepared["image_ids"], 0.25)
    assert (point["true_positives"], point["false_positives"], point["missed_boxes"]) == (1, 1, 1)
    assert point["false_positives_on_annotation_empty_images"] == 1
    assert point["precision"] == 0.5 and point["recall"] == 0.5
    assert point["missed_examples"] == [{"file_name": "Test000003.jpg", "bbox": [50, 40, 30, 20]}]
    assert "benign" not in json.dumps(point)


def test_operating_point_threshold_drops_low_scores_and_handles_no_predictions():
    truth = ground_truth()
    index = check_ground_truth(truth, CATEGORY_MAP)
    prepared = coco_detections(manifest(), results(), index)
    point = operating_point(truth, index, prepared["detections"], prepared["image_ids"], 0.95)
    assert point["true_positives"] == 0 and point["missed_boxes"] == 2
    assert point["precision"] is None and point["recall"] == 0


def test_operating_point_matches_each_truth_box_once():
    truth = ground_truth()
    index = check_ground_truth(truth, CATEGORY_MAP)
    detections = [{"image_id": 10, "category_id": 0, "bbox": [10, 10, 20, 20], "score": s}
                  for s in (0.9, 0.8)]
    point = operating_point(truth, index, detections, [10], 0.25)
    assert (point["true_positives"], point["false_positives"]) == (1, 1)
    assert point["false_positive_examples"][0]["score"] == 0.8


def test_protocol_and_record_must_fit():
    index = check_ground_truth(ground_truth(), CATEGORY_MAP)
    validate_protocol(protocol())
    check_protocol(protocol(), manifest(), index["summary"], HASH_A)
    with pytest.raises(ValueError, match="score floor"):
        check_protocol(protocol(), manifest(conf=0.25), index["summary"], HASH_A)
    with pytest.raises(ValueError, match="task"):
        check_protocol(protocol(task="other.task"), manifest(), index["summary"], HASH_A)
    pinned = protocol()
    pinned["ground_truth"]["sha256"] = HASH_B
    with pytest.raises(ValueError, match="hash"):
        check_protocol(pinned, manifest(), index["summary"], HASH_A)
    counts = protocol()
    counts["ground_truth"]["annotations"] = 3
    with pytest.raises(ValueError, match="counts"):
        check_protocol(counts, manifest(), index["summary"], HASH_A)
    with pytest.raises(ValueError):
        validate_protocol({**protocol(), "extra": 1})


def test_repository_protocol_file_is_valid():
    from pathlib import Path

    path = Path(__file__).parents[1] / "configs" / "evaluation" / "generic-explosive-test.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    validate_protocol(value)
    assert value["status"] == "draft"
    assert value["task"] == "iedxray.generic_explosive_detection"


def test_matched_pair_accepts_identical_conditions():
    baseline = manifest()
    candidate = manifest(role="candidate", checkpoint=HASH_B, parent=HASH_A)
    assert matched_pair_differences(baseline, candidate) == []


@pytest.mark.parametrize(
    ("edit", "message"),
    [
        (lambda c: c["model"].__setitem__("parent_checkpoint_sha256", HASH_C), "initialized"),
        (lambda c: c["model"].__setitem__("task", "other.task"), "model.task"),
        (lambda c: c["model"]["source_category_map"].update({"0": "x"}), "source_category_map"),
        (lambda c: c["settings"].__setitem__("imgsz", 320), "settings"),
        (lambda c: c["stages"]["preprocessing"].__setitem__("detail", "x"), "stages"),
        (lambda c: c["code"].__setitem__("upstream_revision", "x"), "upstream_revision"),
        (lambda c: c["inputs"][0].__setitem__("sha256", HASH_B), "input"),
        (lambda c: c.__setitem__("role", "baseline"), "role=candidate"),
    ],
)
def test_matched_pair_reports_each_difference(edit, message):
    candidate = manifest(role="candidate", checkpoint=HASH_B, parent=HASH_A)
    edit(candidate)
    problems = matched_pair_differences(manifest(), candidate)
    assert any(message in problem for problem in problems)


def _report():
    truth = ground_truth()
    index = check_ground_truth(truth, CATEGORY_MAP)
    record = manifest()
    prepared = coco_detections(record, results(), index)
    point = operating_point(truth, index, prepared["detections"], prepared["image_ids"], 0.25)
    return build_report(protocol(), index["summary"], HASH_A, record, HASH_B, "0", prepared,
                        {"AP@[.50:.95]": 0.5, "AP_small": None}, point, index)


def test_report_round_trip_carries_identity_and_limits():
    report = json.loads(dumps_report(_report()))
    assert report["evidence"] == "draft-protocol"
    assert report["record"]["checkpoint_sha256"] == HASH_A
    assert report["flagged_images_present"][0]["file_name"] == "Test000002.jpg"
    assert any("not a benign" in item for item in report["limitations"])
    assert "synthetic software check only" in report["limitations"]


@pytest.mark.parametrize("value", [float("nan"), float("inf"), "0.5", 1])
def test_report_rejects_non_finite_or_wrong_metric(value):
    report = copy.deepcopy(_report())
    report["metrics"]["AP50"] = value
    with pytest.raises(ValueError):
        dumps_report(report)


def test_report_rejects_unknown_fields():
    report = {**_report(), "verdict": "safe"}
    with pytest.raises(ValueError):
        dumps_report(report)
