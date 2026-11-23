"""Synthetic integration of Faisal's hashing API and the read-only HPC inventory."""

import hashlib
import json
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from sdp_xray import initialization, training_qualification
from sdp_xray.training_qualification import inventory, main
from sdp_xray.training_research import validate_initialization


@pytest.fixture
def weights(tmp_path, monkeypatch):
    path = tmp_path / "synthetic.pt"
    path.write_bytes(b"synthetic stand-in, not model weights")
    expected = {**initialization.GENERAL_INITIALIZATION,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size_bytes": path.stat().st_size}
    monkeypatch.setattr(initialization, "GENERAL_INITIALIZATION", expected)
    monkeypatch.setattr(training_qualification, "GENERAL_INITIALIZATION", expected)
    return path


@pytest.mark.parametrize("task", ["generic", "specific"])
@pytest.mark.parametrize("seed", [17, 29, 43])
def test_faisal_receipt_integrates_with_both_task_and_seed_validators(weights, task, seed):
    receipt = initialization.initialization_receipt(weights, task, "Synthetic fixture owner", seed)
    before = deepcopy(receipt)
    validate_initialization(receipt, task, expected_seed=seed)
    assert receipt == before


def test_inventory_hashes_without_loading_model_or_manufacturing_approval(weights):
    with patch("importlib.metadata.version", return_value="synthetic-only"), \
            patch.dict("os.environ", {"SLURM_JOB_ID": "fixture", "CUDA_VISIBLE_DEVICES": "fixture"}):
        result = inventory(weights)
    assert result["weights"]["matches_recorded_initialization"] is True
    assert result["slurm_allocation_present"] is True and not result["qualified_for_training"]
    assert not result["model_imported"] and not result["training_started"]
    assert "approved" not in json.dumps(result) and str(weights.parent) not in json.dumps(result)
    assert all(name not in sys.modules for name in ("torch", "ultralytics", "optuna"))


def test_bad_weights_do_not_produce_success_receipt(weights, capsys):
    weights.write_bytes(b"changed")
    assert main(["--weights", str(weights)]) == 2
    report = json.loads(capsys.readouterr().out)
    assert report["status"] == "blocked_checkpoint_mismatch"
    assert not report["weights"]["matches_recorded_initialization"]


def test_output_collision_precedes_hashing(weights, tmp_path, capsys):
    output = tmp_path / "existing.json"
    output.write_text("preserve")
    with patch("sdp_xray.training_qualification.file_identity", side_effect=AssertionError("read")):
        assert main(["--weights", str(weights), "--output", str(output)]) == 2
    assert output.read_text() == "preserve" and str(output) not in capsys.readouterr().out


def test_inventory_only_cli_is_successful_but_not_qualification(tmp_path, capsys):
    output = tmp_path / "new.json"
    assert main(["--output", str(output)]) == 0
    report = json.loads(capsys.readouterr().out)
    assert json.loads(output.read_text()) == report
    assert report["weights"] is None and report["qualified_for_training"] is False


def test_invalid_weights_path_is_sanitized(capsys):
    assert main(["--weights", "relative.pt"]) == 2
    assert "relative.pt" not in capsys.readouterr().out


@pytest.mark.parametrize("version", ["3.10.22", "3.15.0"])
def test_unsupported_interpreter_inventory_blocks_without_model_import(version, capsys):
    with patch("platform.python_version", return_value=version):
        assert main([]) == 2
    report = json.loads(capsys.readouterr().out)
    assert report["status"] == "blocked_python_version"
    assert report["python_requirement"] == ">=3.11,<3.15"
    assert not report["python_supported"] and not report["model_imported"]
