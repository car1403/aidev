"""AI 질문 응답 백엔드 미니 서비스 Supabase 구현.

이 파일은 실제 Supabase 테이블에 질문/답변과 서비스 로그를 저장합니다.
실행 전 `03_supabase-schema/mini-service-schema.sql`을 SQL Editor에서 실행해야 합니다.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException

from llm_mock import generate_mock_answer
from schemas import QaCreate
from supabase_client import get_supabase


app = FastAPI(title="AI QA Mini Service Supabase")


@app.get("/health")
def health() -> dict[str, str]:
    """서버 상태를 확인합니다."""

    return {"status": "ok", "storage": "supabase", "llm": "mock"}


def insert_service_log(event_type: str, message: str, metadata: dict) -> None:
    """Supabase에 서비스 로그를 저장합니다."""

    supabase = get_supabase()
    supabase.table("mini_service_logs").insert(
        {
            "event_type": event_type,
            "message": message,
            "metadata": metadata,
        }
    ).execute()


@app.post("/qa", status_code=201)
def create_qa(request: QaCreate) -> dict[str, dict]:
    """사용자 질문을 받고 답변을 생성한 뒤 Supabase에 저장합니다."""

    answer = generate_mock_answer(request.question, request.model)

    supabase = get_supabase()
    result = (
        supabase.table("mini_qa_items")
        .insert(
            {
                "user_id": request.user_id,
                "question": request.question,
                "answer": answer,
                "model": request.model,
            }
        )
        .execute()
    )

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to save QA item.")

    item = result.data[0]

    insert_service_log(
        event_type="qa.created",
        message="질문/답변이 Supabase에 저장되었습니다.",
        metadata={
            "qa_item_id": item["id"],
            "model": request.model,
            "storage": "supabase",
        },
    )

    return {"item": item}


@app.get("/qa")
def list_qa() -> dict[str, list[dict]]:
    """저장된 질문/답변 목록을 조회합니다."""

    supabase = get_supabase()
    result = (
        supabase.table("mini_qa_items")
        .select("*")
        .order("created_at", desc=True)
        .limit(20)
        .execute()
    )
    return {"items": result.data}


@app.get("/qa/{item_id}")
def get_qa(item_id: str) -> dict[str, dict]:
    """id로 질문/답변 1개를 조회합니다."""

    supabase = get_supabase()
    result = supabase.table("mini_qa_items").select("*").eq("id", item_id).limit(1).execute()

    if not result.data:
        raise HTTPException(status_code=404, detail="QA item not found.")

    return {"item": result.data[0]}


@app.get("/service-logs")
def list_service_logs() -> dict[str, list[dict]]:
    """서비스 로그 목록을 조회합니다."""

    supabase = get_supabase()
    result = (
        supabase.table("mini_service_logs")
        .select("*")
        .order("created_at", desc=True)
        .limit(20)
        .execute()
    )
    return {"items": result.data}
