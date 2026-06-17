"""n8n 워크플로우의 기본 노드 구성을 출력하는 예제입니다.

실제 n8n 서버를 호출하지 않고, n8n 화면에서 만들게 될 노드 흐름을
Python 데이터 구조로 먼저 이해하는 목적입니다.
"""

from dataclasses import dataclass


@dataclass
class N8nNode:
    """n8n 워크플로우의 한 노드를 표현합니다."""

    name: str
    node_type: str
    purpose: str
    example_data: str


def build_n8n_ai_workflow_nodes() -> list[N8nNode]:
    """고객 문의 자동화 예시를 n8n 노드 흐름으로 구성합니다."""

    return [
        N8nNode("Webhook Trigger", "Trigger", "외부 요청을 받아 워크플로우 시작", "ticket payload"),
        N8nNode("Set Ticket Fields", "Data", "필요한 필드만 정리", "title, message, customer_tier"),
        N8nNode("Check Urgency", "Condition", "긴급 처리 여부 판단", "urgent or normal"),
        N8nNode("Call AI Backend", "HTTP Request", "AI 분류/답변 생성 API 호출", "draft answer"),
        N8nNode("Notify Team", "Action", "운영팀 또는 담당자에게 알림", "notification result"),
        N8nNode("Respond", "Response", "Webhook 호출자에게 결과 반환", "workflow result"),
    ]


def print_node_map(nodes: list[N8nNode]) -> None:
    """n8n 노드 흐름을 읽기 쉽게 출력합니다."""

    print("[n8n AI Workflow Node Map]")
    for index, node in enumerate(nodes, start=1):
        print(f"\n{index}. {node.name}")
        print(f"   유형: {node.node_type}")
        print(f"   목적: {node.purpose}")
        print(f"   예시 데이터: {node.example_data}")


if __name__ == "__main__":
    print_node_map(build_n8n_ai_workflow_nodes())
