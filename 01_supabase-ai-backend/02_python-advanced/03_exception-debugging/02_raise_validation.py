"""raise를 사용한 입력 검증 예제입니다."""


def validate_score(score: int) -> None:
    """점수가 0부터 100 사이인지 확인합니다."""

    if score < 0 or score > 100:
        raise ValueError("score는 0부터 100 사이여야 합니다.")


for value in [90, 120]:
    try:
        validate_score(value)
        print(value, "정상")
    except ValueError as error:
        print(value, "오류:", error)
