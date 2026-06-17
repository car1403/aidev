"""AIPP식 AI 워크플로우의 큰 그림을 출력하는 예제입니다.

실제 AIPP API를 호출하지 않고, 워크플로우 도구에서 자주 사용하는
노드 개념을 Python 데이터 구조로 표현합니다.
"""

from dataclasses import dataclass


@dataclass
class AippNode:
    """워크플로우 도구의 한 노드를 표현합니다."""

    node_id: str
    node_type: str
    purpose: str
    example_output: str


def build_aipp_like_workflow() -> list[AippNode]:
    """기술 지원 자동화 예시를 AIPP식 노드 흐름으로 구성합니다."""

    return [
        AippNode("start", "Trigger", "새 기술 지원 문의가 들어오면 시작", "ticket_received"),
        AippNode("input", "Input", "문의 제목, 본문, 고객 등급을 수집", "ticket_payload"),
        AippNode("classify", "LLM", "문의 유형과 긴급도 분류", "technical_issue/high"),
        AippNode("retrieve", "Tool", "관련 도움말 문서 검색", "matched_documents"),
        AippNode("generate", "LLM", "고객 답변 초안 생성", "draft_answer"),
        AippNode("validate", "Condition", "답변 품질과 정책 위반 여부 확인", "approved_or_rejected"),
        AippNode("notify", "Action", "담당자 또는 고객에게 결과 전달", "notification_sent"),
        AippNode("log", "Log", "실행 결과와 오류 기록", "workflow_event_log"),
    ]


def print_nodes(nodes: list[AippNode]) -> None:
    """노드 목록을 사람이 읽기 좋은 형태로 출력합니다."""

    print("[AIPP-like Workflow Nodes]")
    for index, node in enumerate(nodes, start=1):
        print(f"\n{index}. {node.node_id}")
        print(f"   유형: {node.node_type}")
        print(f"   목적: {node.purpose}")
        print(f"   예시 출력: {node.example_output}")


if __name__ == "__main__":
    print_nodes(build_aipp_like_workflow())
