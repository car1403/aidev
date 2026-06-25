"""AI 질문 응답 백엔드 미니 서비스 Supabase 구현.

이 파일은 실제 Supabase 테이블에 질문/답변과 서비스 로그를 저장합니다.
실행 전 `03_supabase-schema/mini-service-schema.sql`을 SQL Editor에서 실행해야 합니다.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from postgrest.exceptions import APIError

from llm_mock import generate_mock_answer
from schemas import QuestionCreateRequest, ServiceLogCreateRequest
from supabase_client import get_supabase


app = FastAPI(title="AI Question Mini Service Supabase")


@app.get("/health")
def health() -> dict[str, str | bool]:
    """서버 상태를 확인합니다."""

    return {
        "ok": True,
        "status": "healthy",
        "service": "backend-mini-service",
        "storage": "supabase",
        "llm": "mock-first",
    }


def insert_service_log(event_type: str, message: str, metadata: dict) -> dict | None:
    """Supabase에 서비스 로그를 저장합니다."""

    supabase = get_supabase()
    result = (
        supabase.table("mini_service_logs")
        .insert(
            {
                "event_type": event_type,
                "message": message,
                "metadata": metadata,
            }
        )
        .execute()
    )
    return result.data[0] if result.data else None


def raise_storage_error(error: Exception) -> None:
    """Supabase 처리 중 발생한 오류를 FastAPI HTTPException으로 바꿉니다."""

    raise HTTPException(
        status_code=502,
        detail={
            "code": "storage_error",
            "message": "Supabase 저장소 처리 중 오류가 발생했습니다.",
            "details": str(error),
        },
    )


@app.post("/questions", status_code=201)
def create_question(request: QuestionCreateRequest) -> dict[str, bool | dict]:
    """사용자 질문을 받고 답변을 생성한 뒤 Supabase에 저장합니다."""

    answer = generate_mock_answer(request.question, request.model)
    supabase = get_supabase()

    try:
        result = (
            supabase.table("mini_questions")
            .insert(
                {
                    "user_id": request.user_id,
                    "question": request.question,
                    "answer": answer,
                    "provider": request.provider,
                    "model": request.model,
                    "actual_api_called": False,
                    "llm_call_mode": "mock-first",
                }
            )
            .execute()
        )
    except APIError as error:
        raise_storage_error(error)

    if not result.data:
        raise HTTPException(
            status_code=502,
            detail={
                "code": "question_save_failed",
                "message": "질문 답변 기록 저장에 실패했습니다.",
            },
        )

    item = result.data[0]

    insert_service_log(
        event_type="question_created",
        message="질문 답변 생성 성공",
        metadata={
            "question_id": item["id"],
            "user_id": request.user_id,
            "provider": request.provider,
            "model": request.model,
            "actual_api_called": False,
            "llm_call_mode": "mock-first",
            "storage": "supabase",
        },
    )

    return {"ok": True, "item": item}


@app.get("/questions")
def list_questions(
    user_id: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
) -> dict[str, bool | list[dict]]:
    """저장된 질문/답변 목록을 조회합니다."""

    supabase = get_supabase()
    query = supabase.table("mini_questions").select("*").order("created_at", desc=True).limit(limit)

    if user_id:
        query = query.eq("user_id", user_id)

    try:
        result = query.execute()
    except APIError as error:
        raise_storage_error(error)

    return {"ok": True, "items": result.data}


@app.get("/questions/{question_id}")
def get_question(question_id: str) -> dict[str, bool | dict]:
    """id로 질문/답변 1개를 조회합니다."""

    supabase = get_supabase()

    try:
        result = (
            supabase.table("mini_questions")
            .select("*")
            .eq("id", question_id)
            .limit(1)
            .execute()
        )
    except APIError as error:
        raise_storage_error(error)

    if not result.data:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "question_not_found",
                "message": "질문 기록을 찾을 수 없습니다.",
            },
        )

    return {"ok": True, "item": result.data[0]}


@app.post("/service-logs", status_code=201)
def create_service_log(request: ServiceLogCreateRequest) -> dict[str, bool | dict | None]:
    """서비스 로그를 직접 저장합니다."""

    try:
        item = insert_service_log(
            event_type=request.event_type,
            message=request.message,
            metadata=request.metadata,
        )
    except APIError as error:
        raise_storage_error(error)

    return {"ok": True, "item": item}


@app.get("/service-logs")
def list_service_logs(
    event_type: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
) -> dict[str, bool | list[dict]]:
    """서비스 로그 목록을 조회합니다."""

    supabase = get_supabase()
    query = supabase.table("mini_service_logs").select("*").order("created_at", desc=True).limit(limit)

    if event_type:
        query = query.eq("event_type", event_type)

    try:
        result = query.execute()
    except APIError as error:
        raise_storage_error(error)

    return {"ok": True, "items": result.data}
