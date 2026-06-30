"""mock AI 답변을 만들고 Supabase에 로그를 저장합니다."""

from __future__ import annotations

from fastapi import HTTPException, status

from app.core.config import get_settings
from app.schemas.chat_schema import ChatLogPublic, ChatRequest, ChatResponse


TABLE_NAME = "ex90_simple_chat_logs"


def get_supabase_client():
    from supabase import create_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=".env의 SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY를 확인하세요.",
        )
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def create_mock_answer(message: str) -> str:
    return f"'{message}'에 대한 구조화 예제용 mock 답변입니다."


def to_log_public(row: dict) -> ChatLogPublic:
    return ChatLogPublic(
        id=str(row["id"]),
        user_message=row["user_message"],
        assistant_message=row.get("assistant_message"),
        provider=row["provider"],
        model=row.get("model"),
        actual_api_called=bool(row.get("actual_api_called", False)),
        status=row["status"],
        error_message=row.get("error_message"),
        created_at=row.get("created_at"),
    )


def answer_and_log(request: ChatRequest) -> ChatResponse:
    answer = create_mock_answer(request.message)
    payload = {
        "user_message": request.message,
        "assistant_message": answer,
        "provider": "mock",
        "model": "mock-structured-example",
        "actual_api_called": False,
        "status": "success",
    }
    result = get_supabase_client().table(TABLE_NAME).insert(payload).execute()
    log_id = str(result.data[0]["id"]) if result.data else None

    return ChatResponse(
        user_message=request.message,
        assistant_message=answer,
        provider="mock",
        model="mock-structured-example",
        actual_api_called=False,
        log_id=log_id,
    )


def list_logs() -> list[ChatLogPublic]:
    result = (
        get_supabase_client()
        .table(TABLE_NAME)
        .select("*")
        .order("created_at", desc=True)
        .limit(20)
        .execute()
    )
    return [to_log_public(row) for row in result.data]
