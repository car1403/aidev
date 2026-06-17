"""비용 없는 멀티턴 대화 예제.

이전 대화를 messages 목록에 담아 다음 요청에 함께 보내는 구조를 확인합니다.
"""


# 멀티턴 대화에서는 이전 질문과 답변을 messages 목록에 계속 쌓습니다.
# 모델은 이 목록을 보고 "방금 무엇을 이야기했는지"를 이어서 이해합니다.
messages = [
    {"role": "system", "content": "당신은 백엔드 수업 조교입니다."},
    {"role": "user", "content": "FastAPI가 무엇인가요?"},
    {"role": "assistant", "content": "Python으로 API 서버를 만들 수 있는 프레임워크입니다."},
    {"role": "user", "content": "그럼 Swagger UI는 어떤 역할인가요?"},
]


def mock_multi_turn_response(history: list[dict[str, str]]) -> str:
    """대화 이력을 보고 마지막 질문에 답하는 척하는 함수입니다."""

    # reversed(history)는 최신 메시지부터 거꾸로 살펴봅니다.
    # 그중 role이 user인 마지막 질문을 찾아 답변 대상으로 삼습니다.
    last_user_message = next(
        message["content"]
        for message in reversed(history)
        if message["role"] == "user"
    )

    # 실제 LLM이라면 history 전체를 참고해서 답변을 만들지만,
    # 이 mock 함수는 구조 학습을 위해 고정된 답변을 반환합니다.
    return (
        f"마지막 질문: {last_user_message}\n"
        "Swagger UI는 FastAPI가 자동으로 만들어 주는 API 문서이자 테스트 화면입니다."
    )


print("전달할 메시지 개수:", len(messages))
print(mock_multi_turn_response(messages))
