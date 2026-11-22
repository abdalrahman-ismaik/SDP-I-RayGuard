"""Training-only clamp of COCO boxes that overshoot the image by a tiny amount (T41/T42).

Implements the proposal in docs/single-scan-data-policy.md#invalid-boxes. It never edits a
source file: it returns a derived copy plus a record of every change. It refuses to act on
test annotations, on any overshoot of TOLERANCE_PX or more, or when the number of affected
boxes differs from the expected count.

Coordinates: COCO original-pixel [x, y, width, height]. Image bounds are [0, width] x [0, height].
"""

import hashlib
import json
import math
from copy import deepcopy
from pathlib import PurePath
from typing import Any

TOLERANCE_PX = 0.001
REASON = ("box extends outside the image by less than 0.001 px, consistent with numerical "
          "rounding; clamped to the image edge in a training-only derived copy")


def _images(document: dict[str, Any]) -> dict[int, dict[str, Any]]:
    if not isinstance(document, dict) or not all(
        isinstance(document.get(key), list) for key in ("images", "annotations", "categories")
    ):
        raise ValueError("annotations must be a COCO object with images/annotations/categories")
    images = {}
    for image in document["images"]:
        if type(image.get("id")) is not int or image["id"] in images:
            raise ValueError("image IDs must be unique integers")
        images[image["id"]] = image
    return images


def overshoot(bbox: list[float], width: int, height: int) -> float:
    """Largest distance, in pixels, by which a box extends outside the image (0 if inside)."""
    x, y, w, h = bbox
    return max(0.0, -x, -y, x + w - width, y + h - height)


def find_overshoots(document: dict[str, Any]) -> list[dict[str, Any]]:
    """Every annotation that extends outside its image, with the overshoot amount."""
    images = _images(document)
    found = []
    for annotation in document["annotations"]:
        image = images.get(annotation.get("image_id"))
        if image is None:
            raise ValueError("annotation refers to an unknown image ID")
        bbox = annotation.get("bbox")
        if (not isinstance(bbox, list) or len(bbox) != 4
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in bbox)
                or bbox[2] <= 0 or bbox[3] <= 0):
            raise ValueError(f"annotation {annotation.get('id')}: bbox must be finite and positive")
        amount = overshoot(bbox, image["width"], image["height"])
        if amount > 0:
            found.append({"annotation_id": annotation.get("id"), "image_id": image["id"],
                          "file_name": image["file_name"], "bbox": list(bbox),
                          "overshoot_px": amount})
    return found


def _clamp(bbox: list[float], width: int, height: int) -> list[float]:
    x, y, w, h = bbox
    left, top = max(0.0, x), max(0.0, y)
    new_w, new_h = min(width, x + w) - left, min(height, y + h) - top
    # Floating-point addition can land one step past the edge; step back until inside.
    while left + new_w > width:
        new_w = math.nextafter(new_w, 0.0)
    while top + new_h > height:
        new_h = math.nextafter(new_h, 0.0)
    return [left, top, new_w, new_h]


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def repair_training_copy(
    document: dict[str, Any],
    source_file_name: str,
    source_sha256: str,
    expected_count: int,
    tolerance: float = TOLERANCE_PX,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return (derived training annotations, change record). The input is not modified."""
    if "test" in PurePath(source_file_name).name.lower():
        raise ValueError("test annotations are never repaired")
    images = _images(document)
    if any(PurePath(str(i.get("file_name", ""))).name.lower().startswith("test")
           for i in images.values()):
        raise ValueError("annotations contain test images; only training annotations may be repaired")
    found = find_overshoots(document)
    too_large = [item for item in found if item["overshoot_px"] >= tolerance]
    if too_large:
        raise ValueError(f"{len(too_large)} boxes overshoot by {tolerance} px or more; "
                         f"blocked by policy: {[i['annotation_id'] for i in too_large]}")
    if len(found) != expected_count:
        raise ValueError(f"found {len(found)} boxes outside the image, expected {expected_count}; "
                         "stop and review instead of repairing")

    derived = deepcopy(document)
    by_id = {a.get("id"): a for a in derived["annotations"]}
    if len(by_id) != len(derived["annotations"]):
        raise ValueError("annotation IDs must be unique")
    changes = []
    for item in found:
        annotation = by_id[item["annotation_id"]]
        image = images[item["image_id"]]
        annotation["bbox"] = _clamp(annotation["bbox"], image["width"], image["height"])
        changes.append({**item, "derived_bbox": annotation["bbox"]})

    if find_overshoots(derived):
        raise ValueError("a box is still outside the image after clamping")
    changed = {item["annotation_id"] for item in found}
    for original, new in zip(document["annotations"], derived["annotations"], strict=True):
        if original.get("id") not in changed and original != new:
            raise ValueError("an unaffected annotation changed")

    record = {
        "schema_version": "1.0",
        "purpose": "training-only derived annotations; source file unchanged",
        "source_file_name": PurePath(source_file_name).name,
        "source_sha256": source_sha256,
        "derived_content_sha256": _sha256_json(derived),
        "tolerance_px": tolerance,
        "reason": REASON,
        "area_field": "unchanged from source",
        "changes": changes,
    }
    return derived, record


__all__ = ["REASON", "TOLERANCE_PX", "find_overshoots", "overshoot", "repair_training_copy"]
