users: dict[str, dict] = {}
sessions: dict[str, str] = {}
conversations: list[dict] = []
service_logs: list[dict] = []


def reset_store() -> None:
    users.clear()
    sessions.clear()
    conversations.clear()
    service_logs.clear()
