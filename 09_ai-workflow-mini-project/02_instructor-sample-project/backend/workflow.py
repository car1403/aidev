"""기술 지원 AI 워크플로우의 핵심 로직입니다.

실제 프로젝트에서는 이 위치에 LLM API, Dify API, RAG 검색, n8n Webhook
연동이 들어갈 수 있습니다. 샘플은 외부 의존성 없이 구조를 이해하도록
규칙 기반으로 구현했습니다.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from backend.schemas import TicketAnalysis, TicketRequest


@dataclass
class WorkflowStore:
    """실행 이벤트와 간단한 운영 지표를 메모리에 저장합니다."""

    events: list[dict[str, str]] = field(default_factory=list)
    total_runs: int = 0
    urgent_runs: int = 0
    validation_failures: int = 0

    def add_event(self, ticket_id: str, stage: str, message: str) -> None:
        """운영자가 확인할 수 있도록 워크플로우 이벤트를 기록합니다."""

        self.events.append(
            {
                "time": datetime.now().isoformat(timespec="seconds"),
                "ticket_id": ticket_id,
                "stage": stage,
                "message": message,
            }
        )


KNOWLEDGE_BASE = {
    "technical_issue": [
        "AI 응답 지연 대응 가이드",
        "서비스 상태 페이지 확인 절차",
        "재시도 및 장애 알림 기준",
    ],
    "billing": [
        "결제 오류 확인 가이드",
        "환불 정책 안내",
    ],
    "general_question": [
        "서비스 사용 FAQ",
        "기술 지원 접수 가이드",
    ],
}


def classify_ticket(ticket: TicketRequest) -> tuple[str, str]:
    """문의 메시지를 유형과 긴급도로 분류합니다."""

    text = f"{ticket.title} {ticket.message}".lower()
    billing_keywords = ["결제", "환불", "billing", "refund", "payment"]
    technical_keywords = ["장애", "접속", "응답", "지연", "error", "timeout", "slow", "fail"]

    if any(keyword in text for keyword in billing_keywords):
        category = "billing"
    elif any(keyword in text for keyword in technical_keywords):
        category = "technical_issue"
    else:
        category = "general_question"

    urgent_keywords = ["긴급", "장애", "응답 지연", "접속 불가", "프리미엄"]
    is_urgent = ticket.customer_tier == "premium" or any(keyword in ticket.message for keyword in urgent_keywords)
    urgency = "high" if is_urgent else "normal"

    return category, urgency


def generate_answer(ticket: TicketRequest, category: str, documents: list[str]) -> str:
    """검색된 문서를 바탕으로 답변 초안을 생성합니다."""

    document_hint = ", ".join(documents[:2])
    return (
        f"{ticket.customer_name}님, 문의 내용을 확인했습니다. "
        f"분류 결과는 {category}입니다. "
        f"우선 {document_hint}를 기준으로 확인하겠습니다. "
        "필요하면 담당자가 추가로 안내드리겠습니다."
    )


def validate_answer(answer: str) -> str:
    """답변 초안의 최소 품질과 위험 표현을 검증합니다."""

    blocked_words = ["100% 해결", "무조건 보장", "비밀 키"]
    if len(answer) < 40:
        return "failed: answer too short"
    if any(word in answer for word in blocked_words):
        return "failed: blocked word"
    return "passed"


def estimate_cost(answer: str) -> float:
    """간단한 문자 수 기반 비용 추정값을 반환합니다."""

    return round(len(answer) / 1000 * 0.002, 4)


def run_workflow(ticket: TicketRequest, store: WorkflowStore) -> TicketAnalysis:
    """기술 지원 문의 분석 워크플로우를 실행합니다."""

    ticket_id = f"TS-{uuid4().hex[:8].upper()}"
    store.total_runs += 1
    store.add_event(ticket_id, "trigger", "ticket received")

    category, urgency = classify_ticket(ticket)
    store.add_event(ticket_id, "classify", f"category={category}, urgency={urgency}")

    documents = KNOWLEDGE_BASE[category]
    store.add_event(ticket_id, "retrieve", f"matched_documents={len(documents)}")

    answer = generate_answer(ticket, category, documents)
    store.add_event(ticket_id, "generate", "draft answer created")

    validation_status = validate_answer(answer)
    if validation_status != "passed":
        store.validation_failures += 1
    store.add_event(ticket_id, "validate", validation_status)

    if urgency == "high":
        store.urgent_runs += 1
        next_action = "send_ops_alert"
    elif validation_status != "passed":
        next_action = "escalate_to_human"
    else:
        next_action = "send_draft_reply"
    store.add_event(ticket_id, "action", next_action)

    return TicketAnalysis(
        ticket_id=ticket_id,
        category=category,
        urgency=urgency,
        matched_documents=documents,
        draft_answer=answer,
        validation_status=validation_status,
        next_action=next_action,
        estimated_cost_usd=estimate_cost(answer),
    )
