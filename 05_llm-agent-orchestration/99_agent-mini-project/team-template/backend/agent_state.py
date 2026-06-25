"""팀 프로젝트의 AgentState를 정의하는 파일입니다."""

from typing import TypedDict


class AgentState(TypedDict):
    """팀 주제에 맞게 필드를 수정하세요."""

    user_request: str
    route: str
    tool_result: str
    retrieved_context: list[str]
    final_answer: str
