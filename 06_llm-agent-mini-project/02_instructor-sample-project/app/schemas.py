"""일정 조정 에이전트에서 사용하는 데이터 구조입니다."""

from typing import TypedDict


class AgentState(TypedDict):
    """LangGraph 전체에서 공유하는 상태입니다."""

    user_request: str
    participants: list[str]
    duration_minutes: int
    available_slots: list[str]
    selected_slot: str
    draft_message: str
    final_answer: str
