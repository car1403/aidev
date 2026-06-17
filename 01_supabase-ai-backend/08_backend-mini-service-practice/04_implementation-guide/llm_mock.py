"""비용 없는 mock LLM 답변 생성 함수.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
수업에서는 먼저 mock 함수로 전체 백엔드 흐름을 완성한 뒤,
나중에 실제 LLM API 호출 함수로 교체합니다.
"""


def generate_mock_answer(question: str, model: str = "mock-teacher") -> str:
    """질문을 받아 수업용 가짜 AI 답변을 생성합니다."""

    # 실제 LLM API라면 여기에서 외부 API를 호출합니다.
    # 지금은 비용과 네트워크 의존성을 없애기 위해 문자열을 직접 만들어 반환합니다.
    return (
        f"[{model}] 질문 '{question}'에 대한 수업용 mock 답변입니다. "
        "실제 서비스에서는 이 위치에 Gemini API 호출을 기본으로 연결합니다. "
        "OpenAI API는 선택/비교 실습으로 연결할 수 있습니다."
    )
