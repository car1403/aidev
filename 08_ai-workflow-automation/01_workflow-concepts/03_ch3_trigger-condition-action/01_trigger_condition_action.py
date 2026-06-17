"""Trigger, Condition, Action 흐름을 Python으로 구현하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class TicketEvent:
    """고객 문의가 들어왔을 때 워크플로우로 전달되는 이벤트입니다."""

    ticket_id: str
    title: str
    message: str
    customer_tier: str


def trigger_new_ticket() -> TicketEvent:
    """Trigger: 새 고객 문의가 접수된 상황을 만듭니다."""

    return TicketEvent(
        ticket_id="TICKET-1001",
        title="결제 후 서비스 접속 불가",
        message="프리미엄 결제를 했는데 서비스 접속이 안됩니다. 빠르게 확인 부탁드립니다.",
        customer_tier="premium",
    )


def condition_is_urgent(event: TicketEvent) -> bool:
    """Condition: 긴급 처리 대상인지 판단합니다."""

    urgent_keywords = ["접속 불가", "장애", "안됩니다", "긴급"]
    has_urgent_keyword = any(keyword in event.message for keyword in urgent_keywords)
    is_premium_customer = event.customer_tier == "premium"
    return has_urgent_keyword or is_premium_customer


def action_notify_ops(event: TicketEvent) -> str:
    """Action: 긴급 문의를 운영팀에 전달합니다."""

    return f"[운영팀 알림] {event.ticket_id} - {event.title}"


def action_create_normal_reply(event: TicketEvent) -> str:
    """Action: 일반 문의에 대한 기본 응답을 생성합니다."""

    return f"[일반 응답] {event.ticket_id} 문의가 접수되었습니다. 순서대로 확인하겠습니다."


def run_workflow() -> list[str]:
    """Trigger, Condition, Action 순서로 워크플로우를 실행합니다."""

    logs: list[str] = []

    event = trigger_new_ticket()
    logs.append(f"Trigger 실행: {event.ticket_id} 접수")

    if condition_is_urgent(event):
        logs.append("Condition 결과: 긴급 처리 대상")
        logs.append(action_notify_ops(event))
    else:
        logs.append("Condition 결과: 일반 처리 대상")
        logs.append(action_create_normal_reply(event))

    logs.append("Workflow 종료")
    return logs


if __name__ == "__main__":
    for log in run_workflow():
        print(log)
