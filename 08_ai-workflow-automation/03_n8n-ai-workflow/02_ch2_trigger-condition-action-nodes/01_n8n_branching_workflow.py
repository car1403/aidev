"""n8n의 Trigger, IF, Action 흐름을 Python으로 시뮬레이션합니다."""

from dataclasses import dataclass


@dataclass
class WebhookPayload:
    """n8n Webhook Trigger로 들어온 요청 데이터를 표현합니다."""

    ticket_id: str
    title: str
    message: str
    customer_tier: str


def webhook_trigger() -> WebhookPayload:
    """Webhook Trigger 노드가 받은 데이터를 흉내 냅니다."""

    return WebhookPayload(
        ticket_id="N8N-3001",
        title="AI 서비스 응답 지연",
        message="프리미엄 고객인데 AI 응답이 너무 느립니다. 긴급 확인이 필요합니다.",
        customer_tier="premium",
    )


def set_ticket_fields(payload: WebhookPayload) -> dict[str, str]:
    """Set 노드처럼 다음 단계에 필요한 필드만 정리합니다."""

    return {
        "ticket_id": payload.ticket_id,
        "title": payload.title,
        "message": payload.message,
        "customer_tier": payload.customer_tier,
    }


def if_urgent(ticket: dict[str, str]) -> bool:
    """IF 노드처럼 긴급 여부를 판단합니다."""

    urgent_keywords = ["긴급", "장애", "응답 지연", "접속 불가"]
    has_urgent_keyword = any(keyword in ticket["message"] for keyword in urgent_keywords)
    is_premium = ticket["customer_tier"] == "premium"
    return has_urgent_keyword or is_premium


def action_notify_ops(ticket: dict[str, str]) -> str:
    """긴급 경로의 Action 노드입니다."""

    return f"[Ops Alert] {ticket['ticket_id']} - {ticket['title']}"


def action_create_normal_response(ticket: dict[str, str]) -> str:
    """일반 경로의 Action 노드입니다."""

    return f"[Normal Response] {ticket['ticket_id']} 문의가 접수되었습니다."


def run_n8n_like_workflow() -> list[str]:
    """n8n 노드 실행 흐름을 순서대로 시뮬레이션합니다."""

    logs: list[str] = []

    payload = webhook_trigger()
    logs.append("Webhook Trigger 실행")

    ticket = set_ticket_fields(payload)
    logs.append("Set Node 실행: 필드 정리 완료")

    if if_urgent(ticket):
        logs.append("IF Node 결과: urgent")
        logs.append(action_notify_ops(ticket))
    else:
        logs.append("IF Node 결과: normal")
        logs.append(action_create_normal_response(ticket))

    logs.append("Respond to Webhook: 완료")
    return logs


if __name__ == "__main__":
    for log in run_n8n_like_workflow():
        print(log)
