"""업무 시나리오를 노드 기반 워크플로우 설계안으로 변환하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class BusinessScenario:
    """자동화하려는 업무 시나리오입니다."""

    title: str
    trigger: str
    goal: str
    required_inputs: list[str]


@dataclass
class WorkflowNodeSpec:
    """워크플로우 설계 문서에 들어갈 노드 명세입니다."""

    name: str
    node_type: str
    input_keys: list[str]
    output_key: str
    description: str


def design_nodes(scenario: BusinessScenario) -> list[WorkflowNodeSpec]:
    """업무 시나리오를 AIPP식 노드 명세로 변환합니다."""

    return [
        WorkflowNodeSpec(
            name="receive_ticket",
            node_type="Trigger",
            input_keys=[],
            output_key="ticket",
            description=scenario.trigger,
        ),
        WorkflowNodeSpec(
            name="classify_ticket",
            node_type="LLM",
            input_keys=["ticket.title", "ticket.message"],
            output_key="ticket_category",
            description="문의 유형과 긴급도를 분류합니다.",
        ),
        WorkflowNodeSpec(
            name="search_guide",
            node_type="Tool",
            input_keys=["ticket_category"],
            output_key="guide_documents",
            description="분류 결과에 맞는 도움말 문서를 조회합니다.",
        ),
        WorkflowNodeSpec(
            name="generate_answer",
            node_type="LLM",
            input_keys=["ticket", "guide_documents"],
            output_key="draft_answer",
            description="고객에게 보낼 답변 초안을 생성합니다.",
        ),
        WorkflowNodeSpec(
            name="review_answer",
            node_type="Condition",
            input_keys=["draft_answer"],
            output_key="review_result",
            description="답변이 정책과 품질 기준을 만족하는지 확인합니다.",
        ),
        WorkflowNodeSpec(
            name="send_or_escalate",
            node_type="Action",
            input_keys=["review_result", "draft_answer"],
            output_key="delivery_result",
            description="승인된 답변은 전달하고, 문제가 있으면 담당자에게 넘깁니다.",
        ),
    ]


def print_design(scenario: BusinessScenario, nodes: list[WorkflowNodeSpec]) -> None:
    """워크플로우 설계 결과를 출력합니다."""

    print(f"[Scenario] {scenario.title}")
    print(f"목표: {scenario.goal}")
    print(f"필요 입력: {', '.join(scenario.required_inputs)}")

    print("\n[Node Design]")
    for node in nodes:
        print(f"\n- {node.name} ({node.node_type})")
        print(f"  입력: {', '.join(node.input_keys) if node.input_keys else '없음'}")
        print(f"  출력: {node.output_key}")
        print(f"  설명: {node.description}")


if __name__ == "__main__":
    support_scenario = BusinessScenario(
        title="기술 지원 문의 자동 응답",
        trigger="새 고객 문의가 접수되면 워크플로우를 시작합니다.",
        goal="문의 유형을 분류하고 답변 초안을 생성해 담당자 검토 시간을 줄입니다.",
        required_inputs=["ticket_id", "title", "message", "customer_tier"],
    )

    print_design(support_scenario, design_nodes(support_scenario))
