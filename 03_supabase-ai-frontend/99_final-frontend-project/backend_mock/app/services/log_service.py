from datetime import datetime, timezone
from uuid import uuid4

from app.services.memory_store import service_logs


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


def add_log(
    action: str,
    status: str,
    detail: str | None = None,
    user_email: str | None = None,
) -> dict:
    item = {
        "id": str(uuid4()),
        "user_email": user_email,
        "action": action,
        "status": status,
        "detail": detail,
        "created_at": now_text(),
    }
    service_logs.append(item)
    return item


def list_logs_for_user(user_email: str) -> list[dict]:
    return [
        item
        for item in reversed(service_logs)
        if item["user_email"] in (None, user_email)
    ]
