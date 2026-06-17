"""팀 프로젝트 LangGraph 구현 시작 파일입니다."""

from langgraph.graph import END, START, StateGraph

from agent_state import AgentState
from tools import (
    check_calendar_tool,
    draft_schedule_message_tool,
    find_available_slot_tool,
)


def analyze_intent(state: AgentState) -> dict:
    """사용자 요청에서 일정 조정 의도를 분석합니다."""
    return {
        "intent": "schedule_meeting",
        "required_tools": ["check_calendar", "find_available_slot"],
        "decision_reason": "사용자가 회의 가능 시간을 찾아 달라고 요청했습니다.",
    }


def call_tool(state: AgentState) -> dict:
    """필요한 Tool을 실행하고 결과를 State에 저장합니다."""
    calendar_result = check_calendar_tool(["kim", "lee"])
    slot_result = find_available_slot_tool(duration_minutes=30)
    return {
        "tools_called": ["check_calendar", "find_available_slot"],
        "tool_results": {
            "calendar": calendar_result,
            "available_slot": slot_result,
        },
    }


def validate_result(state: AgentState) -> dict:
    """Tool 결과에 가능한 시간이 있는지 검증합니다."""
    slots = state["tool_results"].get("available_slot", {}).get("available_slots", [])
    if not slots:
        return {
            "error_count": state["error_count"] + 1,
            "reflection_notes": ["가능한 시간이 없어 대체 전략이 필요합니다."],
        }
    return {"reflection_notes": ["가능한 시간이 확인되었습니다."]}


def generate_final_answer(state: AgentState) -> dict:
    """검증된 Tool 결과를 바탕으로 최종 일정 제안을 생성합니다."""
    slots = state["tool_results"].get("available_slot", {}).get("available_slots", [])
    if not slots:
        return {"final_answer": "가능한 시간을 찾지 못했습니다. 다른 날짜나 시간을 알려 주세요."}
    message = draft_schedule_message_tool(slots[0])
    return {"final_answer": message}


def build_graph():
    """팀 프로젝트 그래프를 생성합니다."""
    builder = StateGraph(AgentState)
    builder.add_node("analyze_intent", analyze_intent)
    builder.add_node("call_tool", call_tool)
    builder.add_node("validate_result", validate_result)
    builder.add_node("generate_final_answer", generate_final_answer)
    builder.add_edge(START, "analyze_intent")
    builder.add_edge("analyze_intent", "call_tool")
    builder.add_edge("call_tool", "validate_result")
    builder.add_edge("validate_result", "generate_final_answer")
    builder.add_edge("generate_final_answer", END)
    return builder.compile()


def run_agent(user_request: str) -> AgentState:
    """에이전트를 실행합니다."""
    graph = build_graph()
    initial_state: AgentState = {
        "user_request": user_request,
        "intent": "",
        "required_tools": [],
        "tools_called": [],
        "tool_results": {},
        "error_count": 0,
        "iteration": 1,
        "memory_summary": "",
        "decision_reason": "",
        "reflection_notes": [],
        "final_answer": "",
    }
    return graph.invoke(initial_state)


if __name__ == "__main__":
    result = run_agent("김님과 이님이 가능한 30분 회의 시간을 찾아줘")
    print(result["final_answer"])
