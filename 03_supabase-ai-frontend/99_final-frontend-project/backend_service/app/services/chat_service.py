from app.schemas.chat_schema import ChatRequest
from app.services.cache_service import get_cached_answer, make_cache_key, set_cached_answer
from app.services.gemini_service import generate_ai_answer
from app.services.log_service import add_service_log
from app.services.supabase_service import get_service_client


def create_chat_response(user: dict[str, str], payload: ChatRequest) -> dict:
    cache_key = make_cache_key(user["id"], payload.message)
    cached_answer = get_cached_answer(cache_key)

    if cached_answer:
        ai_result = {
            "answer": cached_answer,
            "provider": "upstash-cache",
            "model": "cached",
            "actual_api_called": False,
        }
    else:
        ai_result = generate_ai_answer(payload.message)
        set_cached_answer(cache_key, ai_result["answer"])

    row = {
        "user_id": user["id"],
        "user_email": user["email"],
        "user_message": payload.message,
        "assistant_message": ai_result["answer"],
        "provider": ai_result["provider"],
        "model": ai_result["model"],
    }
    get_service_client().table("frontend_chat_logs").insert(row).execute()
    add_service_log("chat", "success", "AI 응답 생성과 대화 기록 저장 완료", user)

    return ai_result


def list_conversations(user: dict[str, str]) -> list[dict]:
    result = (
        get_service_client()
        .table("frontend_chat_logs")
        .select("id, user_message, assistant_message, provider, model, created_at")
        .eq("user_id", user["id"])
        .order("created_at", desc=True)
        .limit(50)
        .execute()
    )

    return result.data or []
