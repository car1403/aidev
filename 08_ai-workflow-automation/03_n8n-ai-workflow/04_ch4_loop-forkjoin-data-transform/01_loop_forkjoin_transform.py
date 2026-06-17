"""Loop, Fork-Join, 데이터 변환 노드 흐름을 시뮬레이션합니다."""

from dataclasses import dataclass


@dataclass
class Ticket:
    """기술 지원 문의 데이터를 표현합니다."""

    ticket_id: str
    message: str
    customer_tier: str


def parse_payload(raw_items: list[dict[str, str]]) -> list[Ticket]:
    """Parse 노드처럼 원본 JSON을 Ticket 객체로 변환합니다."""

    return [
        Ticket(
            ticket_id=item["ticket_id"],
            message=item["message"].strip(),
            customer_tier=item.get("customer_tier", "standard"),
        )
        for item in raw_items
    ]


def classify_ticket(ticket: Ticket) -> str:
    """분류 경로입니다."""

    if "로그인" in ticket.message:
        return "account"
    if "느림" in ticket.message or "지연" in ticket.message:
        return "performance"
    return "general"


def summarize_ticket(ticket: Ticket) -> str:
    """요약 경로입니다."""

    return ticket.message[:30] + ("..." if len(ticket.message) > 30 else "")


def recommend_action(ticket: Ticket, category: str) -> str:
    """권장 조치 경로입니다."""

    if ticket.customer_tier == "premium" or category == "performance":
        return "notify_ops"
    return "create_reply"


def run_fork_join(ticket: Ticket) -> dict[str, str]:
    """Fork-Join 구조처럼 여러 작업 결과를 모아 하나로 합칩니다."""

    category = classify_ticket(ticket)
    summary = summarize_ticket(ticket)
    next_action = recommend_action(ticket, category)

    return {
        "ticket_id": ticket.ticket_id,
        "category": category,
        "summary": summary,
        "next_action": next_action,
    }


def aggregate_results(results: list[dict[str, str]]) -> dict[str, int]:
    """Aggregate 노드처럼 결과를 집계합니다."""

    return {
        "total": len(results),
        "notify_ops": sum(result["next_action"] == "notify_ops" for result in results),
        "create_reply": sum(result["next_action"] == "create_reply" for result in results),
    }


def main() -> None:
    """Loop와 Fork-Join 결과를 출력합니다."""

    raw_payload = [
        {"ticket_id": "T-1", "message": "ERP 로그인이 되지 않습니다.", "customer_tier": "standard"},
        {"ticket_id": "T-2", "message": "AI 응답이 너무 느립니다.", "customer_tier": "premium"},
    ]

    tickets = parse_payload(raw_payload)
    results = [run_fork_join(ticket) for ticket in tickets]
    summary = aggregate_results(results)

    print("[Item Results]")
    for result in results:
        print(result)

    print("\n[Aggregate]")
    print(summary)


if __name__ == "__main__":
    main()
