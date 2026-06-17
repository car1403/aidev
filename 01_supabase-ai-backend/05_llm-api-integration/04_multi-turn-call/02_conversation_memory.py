"""간단한 대화 메모리 관리 예제.

실제 서비스에서는 대화 이력을 Supabase에 저장합니다.
이 예제는 멀티턴 messages 목록을 어떻게 관리하는지 메모리에서만 보여줍니다.
"""


# conversation은 현재 대화방의 전체 이력을 의미합니다.
# 실제 서비스에서는 이 데이터를 Supabase conversations/messages 테이블에 저장합니다.
conversation: list[dict[str, str]] = [
    {"role": "system", "content": "당신은 친절한 백엔드 강사입니다."}
]


def add_user_message(content: str) -> None:
    # 사용자가 질문을 입력하면 user 역할의 메시지로 추가합니다.
    conversation.append({"role": "user", "content": content})


def add_assistant_message(content: str) -> None:
    # AI가 답변을 생성하면 assistant 역할의 메시지로 추가합니다.
    conversation.append({"role": "assistant", "content": content})


def build_recent_messages(max_messages: int = 5) -> list[dict[str, str]]:
    """최근 메시지만 잘라서 API에 보낼 messages를 만듭니다."""

    # system 메시지는 대화 규칙이므로 항상 포함합니다.
    system = conversation[0]
    # 대화가 너무 길어지면 비용과 응답 속도에 영향을 줄 수 있으므로 최근 일부만 사용합니다.
    recent = conversation[1:][-max_messages:]
    return [system, *recent]


add_user_message("FastAPI가 무엇인가요?")
add_assistant_message("Python API 서버를 쉽게 만들 수 있는 프레임워크입니다.")
add_user_message("그럼 Pydantic은 어떤 역할인가요?")


for message in build_recent_messages():
    print(f"{message['role']}: {message['content']}")
