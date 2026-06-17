"""테스트 대상 함수입니다."""


def add(a: int, b: int) -> int:
    """두 숫자를 더합니다."""

    return a + b


def divide(a: int, b: int) -> float:
    """a를 b로 나눕니다."""

    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
