"""pytest 기초 예제입니다."""

import pytest

from calculator import add, divide


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(10, 2) == 5


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)
