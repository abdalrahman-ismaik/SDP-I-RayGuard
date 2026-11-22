"""Synthetic software checks. No real weights are read and no model is run."""

import hashlib
import json

import pytest

from sdp_xray import initialization
from sdp_xray.cli import main
from sdp_xray.initialization import (
    GENERAL_INITIALIZATION,
    file_identity,
    initialization_receipt,
    task_identity,
)
from sdp_xray.model_catalog import MODELS, get_model

# The key set T41's validate_initialization accepts (ahmed/t41-software-draft, 32091bc).
RECEIPT_KEYS = {"kind", "architecture", "checkpoint_sha256", "source_reference", "verification",
                "excludes_iedxray", "procedure", "task_head", "seed", "task"}


@pytest.fixture
def weights(tmp_path, monkeypatch):
    """A small stand-in file, with the recorded identity pointed at its bytes."""
    path = tmp_path / "stand-in.pt"
    path.write_bytes(b"synthetic stand-in, not model weights")
    recorded = dict(GENERAL_INITIALIZATION, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    size_bytes=path.stat().st_size)
    monkeypatch.setattr(initialization, "GENERAL_INITIALIZATION", recorded)
    return path


def test_recorded_identity_is_not_a_task_checkpoint():
    assert len(GENERAL_INITIALIZATION["sha256"]) == 64
    assert GENERAL_INITIALIZATION["sha256"] not in {spec.sha256 for spec in MODELS.values()}
    assert GENERAL_INITIALIZATION["source_reference"].startswith("https://github.com/THU-MIG/")


def test_file_identity_hashes_bytes(tmp_path):
    path = tmp_path / "file.bin"
    path.write_bytes(b"abc" * 700000)
    assert file_identity(path) == {"sha256": hashlib.sha256(b"abc" * 700000).hexdigest(),
                                   "size_bytes": 2100000}


@pytest.mark.parametrize("task", ["generic", "specific"])
def test_receipt_has_the_agreed_fields(weights, task):
    receipt = initialization_receipt(weights, task, "Reviewer Name")
    spec = get_model(initialization.TASK_MODELS[task])
    assert set(receipt) == RECEIPT_KEYS
    assert receipt["kind"] == "general_pretrained" and receipt["architecture"] == "YOLOv10-M"
    assert receipt["verification"]["verified_sha256"] == receipt["checkpoint_sha256"]
    assert receipt["seed"] == 17
    assert receipt["task"]["task"] == spec.task
    assert receipt["task"]["class_map_sha256"] == spec.class_map_sha256
    assert receipt["task"] == task_identity(task)
    for review in (receipt["verification"], receipt["excludes_iedxray"]):
        assert review["decision"] == "approved" and review["owner"] == "Reviewer Name"
        assert "docs/initialization-provenance.md" in review["reference"]
    json.dumps(receipt, allow_nan=False)


def test_changed_file_is_refused(weights):
    weights.write_bytes(weights.read_bytes() + b"!")
    with pytest.raises(ValueError, match="does not match"):
        initialization_receipt(weights, "generic", "Reviewer Name")


def test_task_checkpoint_is_refused(tmp_path, monkeypatch):
    path = tmp_path / "task.pt"
    path.write_bytes(b"stand-in for a supplied task checkpoint")
    spec = get_model("author-yolov10m-generic")
    stand_in = type(spec)(**{**spec.__dict__, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    monkeypatch.setitem(MODELS, spec.id, stand_in)
    with pytest.raises(ValueError, match="task checkpoint"):
        initialization_receipt(path, "generic", "Reviewer Name")


@pytest.mark.parametrize("task,owner,seed", [
    ("device", "Reviewer Name", 17), ("generic", " ", 17), ("generic", None, 17),
    ("generic", "Reviewer Name", -1), ("generic", "Reviewer Name", True),
])
def test_bad_arguments_are_refused(weights, task, owner, seed):
    with pytest.raises(ValueError):
        initialization_receipt(weights, task, owner, seed)


def test_cli_prints_receipt_and_can_write_it(weights, tmp_path, capsys):
    output = tmp_path / "receipt.json"
    arguments = ["init-receipt", str(weights), "--task", "specific", "--owner", "Reviewer Name"]
    assert main([*arguments, "--output", str(output)]) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed == json.loads(output.read_text(encoding="utf-8"))
    assert set(printed) == RECEIPT_KEYS
    assert main([*arguments, "--output", str(output)]) == 2  # never overwrites


def test_cli_failure_hides_the_path(weights, capsys):
    weights.write_bytes(b"different")
    assert main(["init-receipt", str(weights), "--task", "generic", "--owner", "Reviewer Name"]) == 2
    out = capsys.readouterr().out
    assert json.loads(out)["ok"] is False and str(weights.parent) not in out
