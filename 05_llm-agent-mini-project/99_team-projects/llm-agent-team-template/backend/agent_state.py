"""팀 프로젝트의 AgentState를 정의하는 파일입니다."""

from typing import Any, TypedDict


class AgentState(TypedDict):
    """LangGraph 전체에서 공유하는 상태입니다."""

    user_request: str
    intent: str
    required_tools: list[str]
    tools_called: list[str]
    tool_results: dict[str, Any]
    error_count: int
    iteration: int
    memory_summary: str
    decision_reason: str
    reflection_notes: list[str]
    final_answer: str
