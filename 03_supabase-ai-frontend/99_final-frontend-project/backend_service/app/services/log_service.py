from app.services.supabase_service import get_service_client


def add_service_log(
    action: str,
    status: str,
    message: str,
    user: dict[str, str] | None = None,
) -> None:
    row = {
        "action": action,
        "status": status,
        "message": message,
        "user_id": user["id"] if user else None,
        "user_email": user["email"] if user else None,
    }

    get_service_client().table("frontend_service_logs").insert(row).execute()


def list_service_logs(user: dict[str, str]) -> list[dict]:
    result = (
        get_service_client()
        .table("frontend_service_logs")
        .select("id, action, status, message, created_at")
        .eq("user_id", user["id"])
        .order("created_at", desc=True)
        .limit(50)
        .execute()
    )

    return result.data or []
