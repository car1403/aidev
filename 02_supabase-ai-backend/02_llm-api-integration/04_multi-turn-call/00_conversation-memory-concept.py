r"""간단한 대화 메모리 관리 예제입니다.

실제 서비스에서는 대화 이력을 Supabase에 저장합니다.
이 예제는 멀티턴 messages 목록을 어떻게 관리하는지 메모리 리스트로만 보여줍니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\02_llm-api-integration\04_multi-turn-call\00_conversation-memory-concept.py
"""


# conversation은 현재 대화방의 전체 이력을 의미합니다.
# 실제 서비스에서는 이 데이터를 Supabase conversations/messages 테이블에 저장합니다.
conversation: list[dict[str, str]] = [
    {"role": "system", "content": "당신은 친절한 FastAPI 학습 도우미입니다."}
]


def add_user_message(content: str) -> None:
    """사용자 질문을 대화 이력에 추가합니다."""

    conversation.append({"role": "user", "content": content})


def add_assistant_message(content: str) -> None:
    """AI 답변을 대화 이력에 추가합니다."""

    conversation.append({"role": "assistant", "content": content})


def build_recent_messages(max_messages: int = 5) -> list[dict[str, str]]:
    """최근 메시지만 잘라서 API에 보낼 messages를 만듭니다."""

    # system 메시지는 대화 규칙이므로 항상 포함합니다.
    system = conversation[0]
    # 대화가 너무 길어지면 비용과 응답 속도에 영향을 줄 수 있으므로 최근 일부만 사용합니다.
    recent = conversation[1:][-max_messages:]
    return [system, *recent]


add_user_message("FastAPI에서 Pydantic을 왜 사용하나요?")
add_assistant_message("요청 데이터를 검증하고 응답 모델을 정리하는 데 사용합니다.")
add_user_message("그럼 메모 API에서는 어떤 부분에 도움이 되나요?")


print("전체 대화 메시지 개수:", len(conversation))
print("LLM API에 보낼 최근 messages")
print("-" * 50)

for message in build_recent_messages():
    print(f"{message['role']}: {message['content']}")

print()
print("실제 서비스에서는 이 목록을 Supabase에서 조회한 뒤 LLM API에 전달합니다.")
