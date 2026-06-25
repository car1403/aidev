r"""멀티턴 LLM 호출 흐름을 비용 없이 확인하는 통합 예제입니다.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
이전 user/assistant 메시지를 함께 보내 문맥을 유지하는 구조를 mock 응답으로 확인합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\04_multi-turn-call\main.py
"""

from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    """멀티턴 호출에 사용할 대화 이력을 메모리에서 관리합니다."""

    system_prompt: str
    messages: list[dict[str, str]] = field(default_factory=list)

    def add_user_message(self, content: str) -> None:
        """사용자 질문을 대화 이력에 추가합니다."""

        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        """AI 답변을 대화 이력에 추가합니다."""

        self.messages.append({"role": "assistant", "content": content})

    def build_recent_messages(self, max_messages: int = 6) -> list[dict[str, str]]:
        """LLM API에 보낼 최근 대화 이력을 만듭니다."""

        system = {"role": "system", "content": self.system_prompt}
        recent = self.messages[-max_messages:]
        return [system, *recent]


def mock_multi_turn_call(messages: list[dict[str, str]]) -> dict[str, str | int]:
    """실제 API 호출 대신 대화 이력을 참고하는 mock 응답을 반환합니다."""

    last_user_message = next(
        message["content"]
        for message in reversed(messages)
        if message["role"] == "user"
    )

    answer = (
        "이전 대화에서 FastAPI와 Pydantic을 이야기했기 때문에, "
        "이번 질문의 '그 내용'은 요청 검증과 API 응답 안정성으로 이어집니다. "
        "멀티턴 호출은 이런 문맥을 messages 목록에 다시 넣어 보내는 방식입니다."
    )

    return {
        "provider": "mock",
        "message_count": len(messages),
        "last_user_message": last_user_message,
        "answer": answer,
    }


def main() -> None:
    """멀티턴 대화 이력 구성과 mock 응답을 순서대로 출력합니다."""

    memory = ConversationMemory(
        system_prompt="당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다."
    )

    memory.add_user_message("FastAPI가 무엇인가요?")
    memory.add_assistant_message("Python으로 API 서버를 쉽게 만들 수 있는 프레임워크입니다.")
    memory.add_user_message("Pydantic은 어떤 역할인가요?")
    memory.add_assistant_message("요청 데이터의 타입과 조건을 검증하고 응답 모델을 정리하는 데 사용합니다.")
    memory.add_user_message("그 내용을 바탕으로 메모 API에서 왜 중요한지 설명해 주세요.")

    messages = memory.build_recent_messages(max_messages=6)
    response = mock_multi_turn_call(messages)

    print("1. LLM API에 보낼 멀티턴 messages")
    print("-" * 50)
    for index, message in enumerate(messages, start=1):
        print(f"{index}) {message['role']}: {message['content']}")

    print()
    print("2. mock 멀티턴 응답")
    print("-" * 50)
    print(response)

    print()
    print("핵심 정리")
    print("-" * 50)
    print("모델이 대화를 자동으로 기억하는 것이 아닙니다.")
    print("이전 user/assistant 메시지를 코드에서 다시 보내기 때문에 문맥을 이어갈 수 있습니다.")
    print("실제 서비스에서는 이 대화 이력을 Supabase에 저장하고 다시 불러오게 됩니다.")


if __name__ == "__main__":
    main()
