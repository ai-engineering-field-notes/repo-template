"""Shape of every demo's tests: one shows the failure in before/, one shows the fix in after/."""

from pathlib import Path

import pytest

DEMO = Path(__file__).parents[1]


def test_before_a_negative_discount_raises_the_price(load):
    before = load(DEMO / "before" / "discount.py")
    assert before.apply_discount(1000, -10) == 1100


def test_after_a_negative_discount_is_rejected(load):
    after = load(DEMO / "after" / "discount.py")
    with pytest.raises(ValueError):
        after.apply_discount(1000, -10)
    assert after.apply_discount(1000, 10) == 900
