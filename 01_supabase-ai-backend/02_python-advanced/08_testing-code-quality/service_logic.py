"""테스트 대상이 되는 간단한 서비스 로직입니다."""


def normalize_question(question: str) -> str:
    """질문 앞뒤 공백을 제거합니다."""

    return question.strip()


def validate_question(question: str) -> None:
    """질문이 비어 있으면 오류를 발생시킵니다."""

    if normalize_question(question) == "":
        raise ValueError("질문은 비워둘 수 없습니다.")


def build_chat_response(question: str) -> dict[str, str]:
    """질문을 받아 API 응답처럼 사용할 dict를 만듭니다."""

    # 먼저 질문이 유효한지 확인합니다.
    validate_question(question)

    # 실제 LLM 호출 대신, 테스트하기 쉬운 고정 응답을 만듭니다.
    normalized = normalize_question(question)

    return {
        "question": normalized,
        "answer": f"'{normalized}' 질문을 처리했습니다.",
    }
