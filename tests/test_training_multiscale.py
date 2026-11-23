"""The pinned fork's multi-scale RNG must keep its sampling on Python 3.12+."""

import random

import pytest

from sdp_xray.training_backend import _integer_randrange


def test_integral_float_bounds_preserve_seeded_samples():
    legacy, explicit = random.Random(17), random.Random(17)
    actual = [_integer_randrange(legacy.randrange, 640 * 0.5, 640 * 1.5 + 32)
              for _ in range(100)]
    expected = [explicit.randrange(320, 992) for _ in range(100)]
    assert actual == expected
    assert legacy.getstate() == explicit.getstate()


@pytest.mark.parametrize("bound", [320.5, float("nan"), float("inf")])
def test_fractional_or_nonfinite_bounds_are_not_rounded(bound):
    rng = random.Random(17)
    before = rng.getstate()
    with pytest.raises(ValueError, match="integral bounds"):
        _integer_randrange(rng.randrange, bound, 992)
    assert rng.getstate() == before
