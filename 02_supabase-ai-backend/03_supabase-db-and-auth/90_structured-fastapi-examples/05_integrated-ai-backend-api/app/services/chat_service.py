"""채팅 답변 생성, Gemini 선택 호출, Redis 캐시, Supabase 로그 저장을 연결합니다."""

from __future__ import annotations

from dataclasses import dataclass

import httpx
from fastapi import HTTPException

from app.core.config import get_settings
from app.schemas.auth_schema import UserPublic
from app.schemas.chat_schema import ChatLogPublic, ChatRequest, ChatResponse
from app.services import redis_service


TABLE_NAME = "ex90_user_chat_logs"


@dataclass(frozen=True)
class AnswerResult:
    answer: str
    provider: str
    model: str
    actual_api_called: bool


def table_url() -> str:
    return f"{get_settings().supabase_url}/rest/v1/{TABLE_NAME}"


def service_headers() -> dict[str, str]:
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(status_code=500, detail="Supabase 환경변수를 확인하세요.")
    return {
        "apikey": settings.supabase_service_role_key,
        "Authorization": f"Bearer {settings.supabase_service_role_key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def user_headers(access_token: str | None) -> dict[str, str]:
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_anon_key or not access_token:
        raise HTTPException(status_code=500, detail="Supabase anon key 또는 token을 확인하세요.")
    return {
        "apikey": settings.supabase_anon_key,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


def cache_key(user_id: str, message: str) -> str:
    return f"ex90:chat:{user_id}:{message}"


def create_mock_answer(message: str) -> AnswerResult:
    return AnswerResult(
        answer=f"'{message}'에 대한 통합 예제용 mock 답변입니다.",
        provider="mock",
        model="mock-integrated-example",
        actual_api_called=False,
    )


def call_gemini(message: str) -> AnswerResult:
    """USE_GEMINI=true일 때 Gemini SDK를 호출합니다."""

    settings = get_settings()
    if not settings.gemini_api_key:
        raise RuntimeError("USE_GEMINI=true이지만 GEMINI_API_KEY가 없습니다.")

    from google import genai

    client = genai.Client(api_key=settings.gemini_api_key)
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=message,
    )
    return AnswerResult(
        answer=response.text or "",
        provider="gemini",
        model=settings.gemini_model,
        actual_api_called=True,
    )


def create_answer(message: str) -> AnswerResult:
    settings = get_settings()
    if settings.use_gemini:
        return call_gemini(message)
    return create_mock_answer(message)


def insert_log(
    user: UserPublic,
    request: ChatRequest,
    answer: str | None,
    cached: bool,
    provider: str,
    model: str,
    actual_api_called: bool,
    status: str = "success",
    error_message: str | None = None,
) -> str | None:
    payload = {
        "user_id": user.id,
        "user_message": request.message,
        "assistant_message": answer,
        "provider": provider,
        "model": model,
        "actual_api_called": actual_api_called,
        "cached": cached,
        "status": status,
        "error_message": error_message,
    }
    try:
        response = httpx.post(table_url(), headers=service_headers(), json=payload, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"로그 저장 실패: {error}") from error
    data = response.json()
    return str(data[0]["id"]) if data else None


def answer_with_cache_and_log(user: UserPublic, request: ChatRequest) -> ChatResponse:
    key = cache_key(user.id, request.message)
    cached_answer = redis_service.get_answer(key)

    if cached_answer:
        log_id = insert_log(
            user=user,
            request=request,
            answer=cached_answer,
            cached=True,
            provider="redis-cache",
            model="cached-answer",
            actual_api_called=False,
        )
        return ChatResponse(
            user_message=request.message,
            assistant_message=cached_answer,
            cached=True,
            provider="redis-cache",
            model="cached-answer",
            actual_api_called=False,
            log_id=log_id,
        )

    try:
        answer_result = create_answer(request.message)
    except Exception as error:
        settings = get_settings()
        log_id = insert_log(
            user=user,
            request=request,
            answer=None,
            cached=False,
            provider="gemini" if settings.use_gemini else "mock",
            model=settings.gemini_model if settings.use_gemini else "mock-integrated-example",
            actual_api_called=settings.use_gemini,
            status="error",
            error_message=str(error),
        )
        raise HTTPException(
            status_code=502,
            detail={
                "message": "AI 답변 생성에 실패했습니다.",
                "log_id": log_id,
                "error": str(error),
            },
        ) from error

    redis_service.set_answer(key, answer_result.answer)
    log_id = insert_log(
        user=user,
        request=request,
        answer=answer_result.answer,
        cached=False,
        provider=answer_result.provider,
        model=answer_result.model,
        actual_api_called=answer_result.actual_api_called,
    )
    return ChatResponse(
        user_message=request.message,
        assistant_message=answer_result.answer,
        cached=False,
        provider=answer_result.provider,
        model=answer_result.model,
        actual_api_called=answer_result.actual_api_called,
        log_id=log_id,
    )


def to_log_public(row: dict) -> ChatLogPublic:
    return ChatLogPublic(
        id=str(row["id"]),
        user_id=str(row["user_id"]),
        user_message=row["user_message"],
        assistant_message=row.get("assistant_message"),
        provider=row["provider"],
        model=row.get("model"),
        actual_api_called=bool(row.get("actual_api_called", False)),
        cached=bool(row["cached"]),
        status=row["status"],
        error_message=row.get("error_message"),
        created_at=row.get("created_at"),
    )


def list_logs(access_token: str | None) -> list[ChatLogPublic]:
    try:
        response = httpx.get(
            table_url(),
            headers=user_headers(access_token),
            params={"select": "*", "order": "created_at.desc", "limit": "20"},
            timeout=10,
        )
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"로그 조회 실패: {error}") from error
    return [to_log_public(row) for row in response.json()]
