from datetime import datetime, timezone
from uuid import uuid4
import asyncio


logs: list[dict] = []
subscribers: list[asyncio.Queue] = []


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


def add_memory_log(payload: dict) -> dict:
    item = {
        "id": str(uuid4()),
        "created_at": now_text(),
        **payload,
    }
    logs.insert(0, item)
    return item


def recent_memory_logs(limit: int = 50) -> list[dict]:
    return logs[:limit]


async def publish_memory_event(item: dict) -> None:
    for queue in list(subscribers):
        await queue.put(item)


def subscribe_memory() -> asyncio.Queue:
    queue: asyncio.Queue = asyncio.Queue()
    subscribers.append(queue)
    return queue


def unsubscribe_memory(queue: asyncio.Queue) -> None:
    if queue in subscribers:
        subscribers.remove(queue)
