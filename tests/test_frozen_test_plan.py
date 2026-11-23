"""Synthetic fail-closed checks; no images, models or GPU execution."""

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / "scripts/evaluate_t41_frozen.py"
spec = importlib.util.spec_from_file_location("frozen_test_pair", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def plan(tmp_path):
    data = tmp_path / "annotations.json"
    data.write_text(json.dumps({"images": [], "annotations": [], "categories": []}))
    second = tmp_path / "second.pt"
    second.write_bytes(b"synthetic checkpoint bytes, not a model")
    binding = {"path": str(data), "sha256": module.sha256(data)}
    return {"schema": "t41-frozen-test-pair-1", "settings": {"conf": 0.001, "max_det": 300},
            "operating_point": {"threshold": 0.25, "iou": 0.5},
            "ground_truth": binding, "initialization": binding, "training_receipts": [],
            "models": [{**binding, "role": "control"},
                       {"path": str(second), "sha256": module.sha256(second),
                        "role": "search_selected"}],
            "code_files": [{"path": data.name, "sha256": binding["sha256"]}]}


@pytest.mark.parametrize("change", ["confidence", "threshold", "checkpoint", "source", "outside_source"])
def test_changed_frozen_inputs_are_rejected_before_model_import(tmp_path, change):
    frozen = plan(tmp_path)
    if change == "confidence":
        frozen["settings"]["conf"] = 0.25
    elif change == "threshold":
        frozen["operating_point"]["threshold"] = 0.5
    elif change == "checkpoint":
        Path(frozen["models"][1]["path"]).write_bytes(b"changed")
    elif change == "source":
        frozen["code_files"][0]["sha256"] = "0" * 64
    else:
        frozen["code_files"][0]["path"] = "../outside.py"
    with pytest.raises(ValueError):
        module.checked_plan(frozen, tmp_path)


def test_preselected_pair_cannot_be_replaced_by_one_model(tmp_path):
    frozen = plan(tmp_path)
    frozen["models"][1].update(frozen["models"][0], role="search_selected")
    with pytest.raises(ValueError, match="different selected checkpoints"):
        module.checked_plan(frozen, tmp_path)


def test_missing_allocation_blocks_before_reading_plan(tmp_path, monkeypatch):
    monkeypatch.delenv("SLURM_JOB_ID", raising=False)
    with pytest.raises(ValueError, match="Slurm allocation"):
        module.run(tmp_path / "absent.json", tmp_path / "output")
