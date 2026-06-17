"""LLM, Tool, Memory의 역할을 단순한 Python 코드로 이해하는 예제입니다.

실제 LLM API를 호출하지 않고, 규칙 기반 함수로 LLM 역할을 흉내 냅니다.
처음에는 구조를 이해하는 것이 목적이므로 외부 서비스 없이 실행되게 구성했습니다.
"""

from dataclasses import dataclass, field


@dataclass
class Memory:
    """워크플로우가 이전 실행 맥락을 기억하는 공간입니다."""

    user_name: str
    preferred_channel: str
    history: list[str] = field(default_factory=list)

    def add_history(self, event: str) -> None:
        """새 실행 이력을 Memory에 추가합니다."""

        self.history.append(event)


def fake_llm_classify(message: str) -> str:
    """LLM의 '분류' 역할을 간단한 규칙으로 흉내 냅니다."""

    lowered = message.lower()
    if "error" in lowered or "장애" in message or "안돼" in message:
        return "technical_issue"
    if "환불" in message or "refund" in lowered:
        return "billing"
    return "general_question"


def search_knowledge_base(category: str) -> list[str]:
    """Tool 역할: 분류 결과에 맞는 도움말 문서를 조회합니다."""

    documents = {
        "technical_issue": [
            "서비스 상태 페이지 확인",
            "브라우저 캐시 삭제 후 재시도",
            "오류 화면 캡처 후 지원팀 전달",
        ],
        "billing": [
            "환불 정책 문서",
            "결제 내역 확인 방법",
            "영업일 기준 처리 시간",
        ],
        "general_question": [
            "자주 묻는 질문",
            "서비스 사용 가이드",
        ],
    }
    return documents.get(category, documents["general_question"])


def fake_llm_generate_reply(message: str, category: str, docs: list[str], memory: Memory) -> str:
    """LLM의 '답변 생성' 역할을 흉내 냅니다."""

    doc_summary = ", ".join(docs[:2])
    return (
        f"{memory.user_name}님, 문의 유형은 '{category}'로 분류되었습니다. "
        f"확인할 자료는 {doc_summary}입니다. "
        f"안내는 {memory.preferred_channel} 채널로 전달하겠습니다."
    )


def run_workflow(message: str, memory: Memory) -> str:
    """LLM, Tool, Memory를 연결해 하나의 워크플로우를 실행합니다."""

    memory.add_history(f"입력 수신: {message}")
    category = fake_llm_classify(message)
    memory.add_history(f"LLM 분류 결과: {category}")
    documents = search_knowledge_base(category)
    memory.add_history(f"Tool 문서 조회 결과: {len(documents)}건")
    reply = fake_llm_generate_reply(message, category, documents, memory)
    memory.add_history("답변 생성 완료")
    return reply


if __name__ == "__main__":
    user_memory = Memory(user_name="Jean", preferred_channel="이메일")
    user_message = "서비스 접속이 안돼요. 장애가 있는 것 같아요."

    result = run_workflow(user_message, user_memory)

    print("[Workflow Result]")
    print(result)

    print("\n[Memory History]")
    for item in user_memory.history:
        print(f"- {item}")
