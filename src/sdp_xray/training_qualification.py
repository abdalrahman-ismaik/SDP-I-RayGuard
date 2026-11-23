"""Read-only environment/weight inventory. No model imports, kernels or training.

Run this with the intended HPC overlay interpreter. A successful inventory is
not a qualification receipt and never sets an approval or loads a checkpoint.
"""

import argparse
import importlib.metadata
import json
import os
import platform
from pathlib import Path

from sdp_xray.initialization import GENERAL_INITIALIZATION, file_identity

PACKAGES = ("torch", "torchvision", "ultralytics", "optuna", "pycocotools", "numpy", "Pillow")


def supported_python(version):
    """Match the project's >=3.11,<3.15 interpreter requirement without imports."""
    try:
        major, minor = (int(part) for part in version.split(".")[:2])
    except (AttributeError, TypeError, ValueError):
        return False
    return major == 3 and 11 <= minor < 15


def inventory(weights=None):
    packages = {}
    for name in PACKAGES:
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    report = {"schema_version": "t41-qualification-inventory-1", "status": "inventory_only",
              "python_version": platform.python_version(), "platform": platform.system(),
              "python_requirement": ">=3.11,<3.15",
              "python_supported": supported_python(platform.python_version()),
              "architecture": platform.machine(), "packages": packages,
              "slurm_allocation_present": bool(os.environ.get("SLURM_JOB_ID")),
              "visible_gpu_mask_present": bool(os.environ.get("CUDA_VISIBLE_DEVICES")),
              "weights": None, "qualified_for_training": False,
              "model_imported": False, "training_started": False,
              "unverified": ["GPU kernels", "upstream source and dependency lock",
                             "data policy and partition", "head transfer", "train/save/reload",
                             "fixed batch and memory", "storage locking", "checkpoint continuation"]}
    if not report["python_supported"]:
        report["status"] = "blocked_python_version"
    if weights is not None:
        path = Path(weights)
        if not path.is_absolute() or path.is_symlink() or not path.is_file():
            raise ValueError("explicit absolute regular weights file required")
        stat_before = path.stat()
        identity = file_identity(path)  # Faisal's byte hashing; never unpickle.
        stat_after = path.stat()
        if (stat_before.st_size, stat_before.st_mtime_ns) != (stat_after.st_size, stat_after.st_mtime_ns):
            raise ValueError("weights changed while hashing")
        matches = all(identity[key] == GENERAL_INITIALIZATION[key] for key in ("sha256", "size_bytes"))
        report["weights"] = {**identity, "matches_recorded_initialization": matches,
                             "verification_scope": "bytes read on this host; no provenance approval"}
        if not matches:
            report["status"] = "blocked_checkpoint_mismatch"
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weights", type=Path, help="Optional existing weights to hash; never load")
    parser.add_argument("--output", type=Path, help="New JSON file; parent must exist; no overwrite")
    args = parser.parse_args(argv)
    try:
        if args.output and (args.output.exists() or args.output.is_symlink()):
            raise ValueError("output already exists")
        result = inventory(args.weights)
        payload = json.dumps(result, indent=2, allow_nan=False) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(payload)
        print(payload, end="")
        return 2 if result["status"].startswith("blocked") else 0
    except (OSError, ValueError):
        print(json.dumps({"status": "blocked", "error": "invalid_input_or_output", "training_started": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
