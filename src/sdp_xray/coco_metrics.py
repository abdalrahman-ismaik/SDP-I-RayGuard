"""COCO bounding-box metrics from the official pycocotools evaluator (T42).

pycocotools is not in the root CPU lock. Install it from environments/evaluation.in, for
example ``uv run --locked --with-requirements environments/evaluation.in ...``.
Inputs are COCO ground truth and COCO detections in original-pixel [x, y, width, height].
"""

import contextlib
import copy
import io
from typing import Any

# Order of COCOeval.stats for iouType="bbox" with the default parameters.
STAT_NAMES = (
    "AP@[.50:.95]",
    "AP50",
    "AP75",
    "AP_small",
    "AP_medium",
    "AP_large",
    "AR@1",
    "AR@10",
    "AR@100",
    "AR_small",
    "AR_medium",
    "AR_large",
)


def evaluator_version() -> str:
    from importlib.metadata import version

    return version("pycocotools")


def coco_bbox_metrics(
    ground_truth: dict[str, Any], detections: list[dict[str, Any]], image_ids: list[int]
) -> dict[str, float | None]:
    """Run COCOeval (bbox, default parameters) on the given images.

    COCOeval reports -1 when a metric is undefined, for example with no ground-truth boxes
    in an area range; that becomes None. The ground truth is copied, never modified.
    """
    from pycocotools.coco import COCO
    from pycocotools.cocoeval import COCOeval

    quiet = io.StringIO()
    with contextlib.redirect_stdout(quiet):
        truth = COCO()
        truth.dataset = copy.deepcopy(ground_truth)
        truth.createIndex()
        if detections:
            predicted = truth.loadRes(copy.deepcopy(detections))
        else:
            # loadRes cannot take an empty list; an empty result set is still evaluated.
            predicted = COCO()
            predicted.dataset = {"images": copy.deepcopy(ground_truth["images"]),
                                 "categories": copy.deepcopy(ground_truth["categories"]),
                                 "annotations": []}
            predicted.createIndex()
        evaluation = COCOeval(truth, predicted, iouType="bbox")
        evaluation.params.imgIds = sorted(image_ids)
        evaluation.evaluate()
        evaluation.accumulate()
        evaluation.summarize()
    return {
        name: (None if value < 0 else float(value))
        for name, value in zip(STAT_NAMES, evaluation.stats, strict=True)
    }


__all__ = ["STAT_NAMES", "coco_bbox_metrics", "evaluator_version"]
