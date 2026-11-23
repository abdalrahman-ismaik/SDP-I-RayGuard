"""Identity of the general pretrained starting weights for the controlled study (T40).

The file is the official COCO-trained YOLOv10-M release. It is not an IEDXray task
checkpoint and is deliberately kept out of the model catalog. This module hashes a
local copy and writes the initialization receipt that T41's planner expects. It
never unpickles the file, imports a model package or downloads anything.
See docs/initialization-provenance.md for the evidence behind each constant.
"""

import hashlib
from pathlib import Path
from typing import Any

from sdp_xray.model_catalog import MODELS, get_model

DOCUMENT = "docs/initialization-provenance.md"
UPSTREAM_REVISION = "453c6e38a51e9d1d5a2aa5fb7f1014a711913397"
TASK_MODELS = {"generic": "author-yolov10m-generic", "specific": "author-yolov10m-specific"}

GENERAL_INITIALIZATION = {
    "architecture": "YOLOv10-M",
    "filename": "yolov10m.pt",
    "size_bytes": 66924323,
    "sha256": "ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d",
    "source_reference": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt",
    "release": "THU-MIG/yolov10 v1.1, asset uploaded 2024-05-26",
    "license": "AGPL-3.0",
}

# Both statements come from reading the pinned upstream code, not from a training run.
PROCEDURE = (
    "Give the hash-verified local file to the YOLOv10 detection trainer as its model at "
    f"upstream revision {UPSTREAM_REVISION}. The trainer builds the task model with the class "
    "count from the data file and copies every tensor whose name and shape match the file "
    "(BaseModel.load, intersect_dicts). No layer is frozen by this procedure."
)
TASK_HEAD = (
    "The last 1x1 class convolution of v10Detect cv3 and one2one_cv3 at each of the three "
    "scales depends on the class count, so those 12 tensors are not copied from the 80-class "
    "file. They are newly initialized under the training seed with upstream bias_init. "
    "The trainer's 'Transferred N/M items' log line is the executed evidence and must be kept."
)


def file_identity(path: Path) -> dict[str, Any]:
    """SHA-256 and size of the file's bytes. The file is read, never loaded."""
    digest, size = hashlib.sha256(), 0
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
            size += len(block)
    return {"sha256": digest.hexdigest(), "size_bytes": size}


def task_identity(task: str) -> dict[str, Any]:
    """Task and class maps of the matching catalog entry, for the receipt's task field."""
    if task not in TASK_MODELS:
        raise ValueError("task must be generic or specific")
    spec = get_model(TASK_MODELS[task])
    return {"task": spec.task, "kind": spec.kind, "class_map_sha256": spec.class_map_sha256,
            "model_names": {str(index): name for index, name in spec.names.items()},
            "source_category_map": spec.source_category_map}


def initialization_receipt(path: Path, task: str, owner: str, seed: int = 17) -> dict[str, Any]:
    """Hash a local copy of the starting weights and return the T41 receipt.

    `owner` is the person running the check; their name is what makes the two
    review entries a human statement. A file whose bytes differ from the recorded
    release is refused, and so is any IEDXray task checkpoint.
    """
    if not isinstance(owner, str) or not owner.strip():
        raise ValueError("owner must name the person verifying the file")
    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    identity_of_task = task_identity(task)
    actual = file_identity(path)
    if actual["sha256"] in {spec.sha256 for spec in MODELS.values()}:
        raise ValueError("this is an IEDXray task checkpoint, not general starting weights")
    if (actual["sha256"] != GENERAL_INITIALIZATION["sha256"]
            or actual["size_bytes"] != GENERAL_INITIALIZATION["size_bytes"]):
        raise ValueError("file does not match the recorded general starting weights")
    return {
        "kind": "general_pretrained",
        "architecture": GENERAL_INITIALIZATION["architecture"],
        "checkpoint_sha256": actual["sha256"],
        "source_reference": GENERAL_INITIALIZATION["source_reference"],
        "verification": {
            "decision": "approved", "owner": owner.strip(),
            "reference": f"file bytes re-hashed by sdp-xray init-receipt; expected value in {DOCUMENT}",
            "verified_sha256": actual["sha256"],
        },
        "excludes_iedxray": {
            "decision": "approved", "owner": owner.strip(),
            "reference": f"{DOCUMENT}#evidence-that-the-weights-exclude-iedxray",
        },
        "procedure": PROCEDURE,
        "task_head": TASK_HEAD,
        "seed": seed,
        "task": identity_of_task,
    }
