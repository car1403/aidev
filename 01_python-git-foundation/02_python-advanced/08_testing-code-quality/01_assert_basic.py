"""assert로 함수 결과를 직접 확인하는 기본 예제입니다."""


def normalize_question(question: str) -> str:
    """질문 앞뒤 공백을 제거합니다."""

    return question.strip()


# assert는 조건이 True인지 확인합니다.
# 조건이 True이면 아무 일 없이 다음 줄로 넘어갑니다.
assert normalize_question("  FastAPI란?  ") == "FastAPI란?"

# 빈 문자열에 strip을 적용하면 빈 문자열이 됩니다.
assert normalize_question("   ") == ""

print("assert 검사 통과")
