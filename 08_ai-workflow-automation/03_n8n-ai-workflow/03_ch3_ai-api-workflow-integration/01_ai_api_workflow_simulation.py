"""n8n이 AI API를 호출하는 흐름을 로컬 함수로 시뮬레이션합니다.

실제 운영에서는 `call_ai_backend` 함수가 HTTP Request 노드가 됩니다.
여기서는 외부 서버 없이 데이터 흐름을 이해하기 위해 함수 호출로 표현합니다.
"""

from dataclasses import dataclass


@dataclass
class Ticket:
    """AI API에 전달할 문의 데이터입니다."""

    ticket_id: str
    title: str
    message: str


@dataclass
class AiAnalysisResult:
    """AI API가 반환한다고 가정하는 분석 결과입니다."""

    category: str
    urgency: str
    draft_answer: str


def call_ai_backend(ticket: Ticket) -> AiAnalysisResult:
    """HTTP Request 노드가 호출할 AI 백엔드 응답을 흉내 냅니다."""

    if "장애" in ticket.message or "접속" in ticket.message:
        category = "technical_issue"
        urgency = "high"
    else:
        category = "general_question"
        urgency = "normal"

    draft_answer = (
        f"{ticket.ticket_id} 문의를 확인했습니다. "
        f"분류는 {category}, 긴급도는 {urgency}입니다. "
        "담당자가 확인할 수 있도록 내용을 정리했습니다."
    )

    return AiAnalysisResult(category=category, urgency=urgency, draft_answer=draft_answer)


def decide_next_action(result: AiAnalysisResult) -> str:
    """AI 분석 결과를 보고 n8n의 다음 Action 경로를 결정합니다."""

    if result.urgency == "high":
        return "send_ops_alert"
    return "send_normal_reply"


def run_workflow() -> dict[str, str]:
    """n8n과 AI API 연동 흐름을 하나의 결과 딕셔너리로 반환합니다."""

    ticket = Ticket(
        ticket_id="N8N-AI-4001",
        title="서비스 접속 장애",
        message="서비스 접속이 되지 않습니다. 장애 여부를 확인해 주세요.",
    )

    ai_result = call_ai_backend(ticket)
    next_action = decide_next_action(ai_result)

    return {
        "ticket_id": ticket.ticket_id,
        "category": ai_result.category,
        "urgency": ai_result.urgency,
        "draft_answer": ai_result.draft_answer,
        "next_action": next_action,
    }


if __name__ == "__main__":
    result = run_workflow()

    print("[n8n -> AI API Workflow Result]")
    for key, value in result.items():
        print(f"- {key}: {value}")
