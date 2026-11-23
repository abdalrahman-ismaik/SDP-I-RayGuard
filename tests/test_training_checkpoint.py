"""File-scope checks with a fake Torch loader; no pickle/model/GPU operations."""

import hashlib
import sys
from types import SimpleNamespace

import pytest

from sdp_xray.training_checkpoint import checkpoint_loading
from sdp_xray.training_workflow import offline_runtime


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_only_verified_checkpoint_loads_and_loader_is_restored(tmp_path, monkeypatch):
    known, unknown = tmp_path / "known.pt", tmp_path / "other.pt"
    known.write_bytes(b"synthetic checkpoint stand-in")
    unknown.write_bytes(known.read_bytes())
    calls = []
    def original(path, **kwargs):
        calls.append((path, kwargs))
        return "synthetic"
    fake = SimpleNamespace(load=original)
    monkeypatch.setitem(sys.modules, "torch", fake)
    with checkpoint_loading({known.resolve(): sha(known)}):
        assert fake.load(known, map_location="cpu") == "synthetic"
        with pytest.raises(ValueError, match="scope"):
            fake.load(unknown)
        known.write_bytes(b"changed")
        with pytest.raises(ValueError, match="scope"):
            fake.load(known)
    assert fake.load is original
    assert len(calls) == 1 and calls[0][1] == {"map_location": "cpu", "weights_only": False}


def test_changed_file_during_load_is_rejected(tmp_path, monkeypatch):
    path = tmp_path / "checkpoint.pt"
    path.write_bytes(b"before")
    def changing_loader(path, **kwargs):
        path.write_bytes(b"after")
    fake = SimpleNamespace(load=changing_loader)
    monkeypatch.setitem(sys.modules, "torch", fake)
    with checkpoint_loading({path.resolve(): sha(path)}):
        with pytest.raises(ValueError, match="during loading"):
            fake.load(path)
    assert fake.load is changing_loader


def test_font_provisioning_is_hash_bound_and_does_not_modify_source(tmp_path):
    source = tmp_path / "font.ttf"
    source.write_bytes(b"synthetic font bytes; not a rendered asset")
    asset = {"name": "Arial.ttf", "path": str(source), "sha256": sha(source)}
    directory = tmp_path / "settings"
    with offline_runtime(directory, [asset]):
        assert (directory / "Arial.ttf").read_bytes() == source.read_bytes()
    assert sha(source) == asset["sha256"]
    source.write_bytes(b"changed")
    with pytest.raises(ValueError, match="font asset"):
        with offline_runtime(tmp_path / "other", [asset]):
            pytest.fail("changed asset must not enter runtime")
