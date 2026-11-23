"""Scoped legacy full-object loading of explicitly identified training artifacts."""

from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from sdp_xray.training import _sha256


@contextmanager
def checkpoint_loading(identities):
    """Allow only the supplied absolute paths and byte hashes during this scope.

    The caller owns this single-process mapping. Finalization may update an entry
    after its own optimizer-stripping write; no directory-wide load is allowed.
    Torch is optional and imported only when the authorized runtime enters here.
    """
    import torch

    original = torch.load

    def load(path, *args, **kwargs):
        candidate = Path(path)
        expected = identities.get(candidate.resolve())
        if (not candidate.is_absolute() or candidate.is_symlink() or expected is None
                or not candidate.is_file() or _sha256(candidate) != expected):
            raise ValueError("checkpoint load is outside the verified file scope")
        kwargs["weights_only"] = False
        result = original(path, *args, **kwargs)
        if _sha256(candidate) != expected:
            raise ValueError("checkpoint changed during loading")
        return result

    with patch.object(torch, "load", load):
        yield
