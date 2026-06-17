"""가변 매개변수와 키워드 매개변수 예제입니다."""


def add_all(*numbers: int):
    """전달받은 모든 숫자를 더합니다."""

    return sum(numbers)


def build_profile(**fields: str) -> dict[str, str]:
    """키워드 인자를 딕셔너리로 모읍니다."""

    return fields


print("합계:", add_all(1, 2, 3, 4, 5))
print("프로필:", build_profile(name="Jean", role="student", language="Python"))
