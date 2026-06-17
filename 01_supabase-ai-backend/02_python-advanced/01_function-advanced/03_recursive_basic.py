"""재귀 함수 기초 예제입니다."""


def factorial(number: int) -> int:
    """팩토리얼 값을 계산합니다."""

    if number <= 1:
        return 1
    return number * factorial(number - 1)


print("5! =", factorial(5))
