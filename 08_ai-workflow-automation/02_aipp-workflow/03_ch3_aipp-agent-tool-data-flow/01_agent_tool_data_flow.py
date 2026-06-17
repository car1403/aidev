"""Agent, Tool, Data 흐름을 단순한 실행 파이프라인으로 표현하는 예제입니다."""

from dataclasses import dataclass, field


@dataclass
class WorkflowContext:
    """노드 사이에서 전달되는 실행 컨텍스트입니다."""

    ticket: dict[str, str]
    data: dict[str, object] = field(default_factory=dict)
    logs: list[str] = field(default_factory=list)

    def log(self, message: str) -> None:
        """운영 확인을 위해 실행 이력을 남깁니다."""

        self.logs.append(message)


def agent_analyze_ticket(context: WorkflowContext) -> WorkflowContext:
    """Agent 노드: 문의 내용을 분석해서 다음 Tool 실행에 필요한 값을 만듭니다."""

    message = context.ticket["message"]
    if "접속" in message or "장애" in message:
        category = "technical_issue"
    else:
        category = "general_question"

    context.data["category"] = category
    context.log(f"Agent 분석 완료: category={category}")
    return context


def tool_search_documents(context: WorkflowContext) -> WorkflowContext:
    """Tool 노드: 카테고리에 맞는 문서를 조회합니다."""

    category = str(context.data["category"])
    document_map = {
        "technical_issue": ["장애 확인 가이드", "서비스 상태 페이지", "재시도 안내문"],
        "general_question": ["사용자 가이드", "FAQ"],
    }
    context.data["documents"] = document_map.get(category, document_map["general_question"])
    context.log("Tool 문서 조회 완료")
    return context


def agent_generate_answer(context: WorkflowContext) -> WorkflowContext:
    """Agent 노드: Tool 결과를 바탕으로 답변 초안을 만듭니다."""

    documents = context.data["documents"]
    context.data["draft_answer"] = (
        f"문의 내용을 확인했습니다. 우선 {documents[0]}를 기준으로 확인해 주세요. "
        "필요하면 담당자가 추가로 안내드리겠습니다."
    )
    context.log("Agent 답변 초안 생성 완료")
    return context


def condition_validate_answer(context: WorkflowContext) -> WorkflowContext:
    """Condition 노드: 답변이 너무 짧거나 비어 있는지 검증합니다."""

    draft_answer = str(context.data.get("draft_answer", ""))
    context.data["is_valid"] = len(draft_answer) >= 30
    context.log(f"Condition 검증 완료: is_valid={context.data['is_valid']}")
    return context


def action_finish(context: WorkflowContext) -> WorkflowContext:
    """Action 노드: 최종 처리 방식을 결정합니다."""

    if context.data["is_valid"]:
        context.data["final_action"] = "send_to_customer"
    else:
        context.data["final_action"] = "escalate_to_human"

    context.log(f"Action 결정 완료: {context.data['final_action']}")
    return context


def run_pipeline(context: WorkflowContext) -> WorkflowContext:
    """AIPP식 노드 흐름을 Python 함수 파이프라인으로 실행합니다."""

    for node in [
        agent_analyze_ticket,
        tool_search_documents,
        agent_generate_answer,
        condition_validate_answer,
        action_finish,
    ]:
        context = node(context)
    return context


if __name__ == "__main__":
    initial_context = WorkflowContext(
        ticket={
            "ticket_id": "TS-2001",
            "title": "서비스 접속 장애",
            "message": "서비스 접속이 되지 않습니다. 장애 여부를 확인하고 싶습니다.",
        }
    )

    result_context = run_pipeline(initial_context)

    print("[Final Data]")
    for key, value in result_context.data.items():
        print(f"- {key}: {value}")

    print("\n[Logs]")
    for log in result_context.logs:
        print(f"- {log}")
