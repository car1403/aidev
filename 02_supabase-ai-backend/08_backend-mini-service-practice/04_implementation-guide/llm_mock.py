"""비용 없는 mock-first 답변 생성 함수.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
먼저 mock 함수로 전체 백엔드 흐름을 완성한 뒤, 필요할 때 05 단원에서 배운 Gemini SDK 호출 함수로 교체합니다.
"""


def generate_mock_answer(question: str, model: str = "gemini-2.5-flash-lite") -> str:
    """질문을 받아 가짜 AI 답변 문자열을 생성합니다."""

    # 실제 Gemini SDK 연동 단계라면 이 위치에서 외부 API를 호출합니다.
    # 지금은 비용과 네트워크 의존성을 없애기 위해 문자열을 직접 만들어 반환합니다.
    return (
        f"[{model}] '{question}'에 대한 mock 답변입니다. "
        "이 위치는 나중에 Gemini SDK 호출 코드로 교체할 수 있습니다. "
        "OpenAI API 예제는 선택 비교용으로 연결할 수 있습니다."
    )
