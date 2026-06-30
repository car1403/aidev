from app.core.config import SUPABASE_SERVICE_ROLE_KEY, SUPABASE_URL
from app.services.memory_store import add_memory_log, recent_memory_logs


def _client():
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        return None

    try:
        from supabase import create_client
    except ImportError:
        return None

    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


def save_log(payload: dict) -> dict:
    client = _client()
    if client is None:
        return add_memory_log(payload)

    result = client.table("realtime_service_logs").insert(payload).execute()
    if result.data:
        return result.data[0]

    return add_memory_log(payload)


def list_logs(limit: int = 50) -> list[dict]:
    client = _client()
    if client is None:
        return recent_memory_logs(limit)

    result = (
        client.table("realtime_service_logs")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return result.data or []


def summarize_logs() -> list[dict]:
    counts: dict[str, int] = {}
    for item in list_logs(200):
        level = item.get("level", "unknown")
        counts[level] = counts.get(level, 0) + 1
    return [{"level": level, "count": count} for level, count in sorted(counts.items())]
