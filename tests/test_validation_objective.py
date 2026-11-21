"""Synthetic checks of the T41 validation objective (T42). Not model or accuracy evidence.

Skipped unless pycocotools is installed (environments/evaluation.in).
"""

import copy

import pytest

from sdp_xray.model_catalog import get_model
from sdp_xray.validation_objective import evaluate_validation, objective

pytest.importorskip("pycocotools")

CHECKPOINT = "e" * 64
PARTITION = "f" * 64
ANNOTATIONS = "1" * 64
RESULT_FIELDS = {"status", "checkpoint_sha256", "completed_epoch", "task", "partition_sha256",
                 "annotation_sha256", "objective", "evaluated_image_ids", "value"}


def generic_task():
    spec = get_model("author-yolov10m-generic")
    return {"task": spec.task, "kind": spec.kind, "class_map_sha256": spec.class_map_sha256,
            "model_names": {str(k): v for k, v in spec.names.items()},
            "source_category_map": spec.source_category_map}


def request(**changes):
    value = {"checkpoint_sha256": CHECKPOINT, "completed_epoch": 3, "task": generic_task(),
             "partition_sha256": PARTITION, "validation_ids": [5, 6],
             "annotation_sha256": ANNOTATIONS, "objective": objective()}
    value.update(changes)
    return value


def validation_truth():
    """Two synthetic validation images; generic category ID 0 kept as in IEDXray."""
    return {
        "images": [{"id": 5, "file_name": "Train000005.jpg", "width": 100, "height": 80},
                   {"id": 6, "file_name": "Train000006.jpg", "width": 100, "height": 80}],
        "annotations": [{"id": 1, "image_id": 5, "category_id": 0, "bbox": [10, 10, 20, 20],
                         "area": 400, "iscrowd": 0}],
        "categories": [{"id": 0, "name": "Explosive"}],
    }


def perfect():
    return [{"image_id": 5, "category_id": 0, "bbox": [10, 10, 20, 20], "score": 0.9}]


def test_result_matches_t41_interface_and_scale():
    result = evaluate_validation(request(), validation_truth(), ANNOTATIONS, CHECKPOINT, perfect())
    assert set(result) == RESULT_FIELDS
    assert result["status"] == "ok"
    assert result["value"] == pytest.approx(1.0)
    assert result["evaluated_image_ids"] == [5, 6]
    for key in ("checkpoint_sha256", "completed_epoch", "task", "partition_sha256",
                "annotation_sha256", "objective"):
        assert result[key] == request()[key]


def test_no_detections_is_zero_ap_not_failure():
    result = evaluate_validation(request(), validation_truth(), ANNOTATIONS, CHECKPOINT, [])
    assert result["value"] == 0.0


@pytest.mark.parametrize(
    ("call", "message"),
    [
        (lambda: evaluate_validation(request(), validation_truth(), ANNOTATIONS, "9" * 64,
                                     perfect()), "different checkpoint"),
        (lambda: evaluate_validation(request(), validation_truth(), "2" * 64, CHECKPOINT,
                                     perfect()), "annotation file hash"),
        (lambda: evaluate_validation(request(validation_ids=[5]), validation_truth(),
                                     ANNOTATIONS, CHECKPOINT, perfect()), "exactly the requested"),
        (lambda: evaluate_validation(request(objective={**objective(), "scale": "percent"}),
                                     validation_truth(), ANNOTATIONS, CHECKPOINT, perfect()),
         "objective"),
        (lambda: evaluate_validation(request(task={**generic_task(), "kind": "device"}),
                                     validation_truth(), ANNOTATIONS, CHECKPOINT, perfect()),
         "catalog task"),
        (lambda: evaluate_validation({**request(), "extra": 1}, validation_truth(), ANNOTATIONS,
                                     CHECKPOINT, perfect()), "exactly"),
    ],
)
def test_identity_mismatches_are_refused(call, message):
    with pytest.raises(ValueError, match=message):
        call()


@pytest.mark.parametrize(
    "detection",
    [
        {"image_id": 99, "category_id": 0, "bbox": [1, 1, 5, 5], "score": 0.5},
        {"image_id": 5, "category_id": 1, "bbox": [1, 1, 5, 5], "score": 0.5},
        {"image_id": 5, "category_id": 0, "bbox": [1, 1, 0, 5], "score": 0.5},
        {"image_id": 5, "category_id": 0, "bbox": [1, 1, 5, float("nan")], "score": 0.5},
        {"image_id": 5, "category_id": 0, "bbox": [1, 1, 5, 5], "score": 1.5},
        {"image_id": 5, "category_id": 0, "bbox": [1, 1, 5, 5]},
    ],
)
def test_invalid_detections_are_refused(detection):
    with pytest.raises(ValueError):
        evaluate_validation(request(), validation_truth(), ANNOTATIONS, CHECKPOINT, [detection])


def test_validation_without_boxes_fails_instead_of_scoring_zero():
    truth = validation_truth()
    truth["annotations"] = []
    with pytest.raises(ValueError, match="undefined"):
        evaluate_validation(request(), truth, ANNOTATIONS, CHECKPOINT, [])


def test_inputs_are_not_modified():
    truth, detections = validation_truth(), perfect()
    before = copy.deepcopy((truth, detections))
    evaluate_validation(request(), truth, ANNOTATIONS, CHECKPOINT, detections)
    assert (truth, detections) == before
