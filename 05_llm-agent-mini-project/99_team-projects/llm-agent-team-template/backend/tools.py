"""일정 조정 에이전트에서 사용할 Tool 함수 예시입니다."""


def check_calendar_tool(participants: list[str]) -> dict:
    """참석자의 Mock 일정을 조회합니다."""
    return {
        "participants": participants,
        "busy_slots": {
            "kim": ["2026-06-16 10:00", "2026-06-16 14:00"],
            "lee": ["2026-06-16 11:00"],
        },
    }


def find_available_slot_tool(duration_minutes: int) -> dict:
    """Mock 데이터 기준으로 가능한 회의 시간을 반환합니다."""
    return {
        "duration_minutes": duration_minutes,
        "available_slots": ["2026-06-16 15:00", "2026-06-17 10:00"],
    }


def draft_schedule_message_tool(selected_slot: str) -> str:
    """선택된 시간으로 사용자에게 보여줄 일정 제안 메시지를 만듭니다."""
    return f"가능한 일정은 {selected_slot}입니다. 이 시간으로 회의를 진행해도 좋습니다."
