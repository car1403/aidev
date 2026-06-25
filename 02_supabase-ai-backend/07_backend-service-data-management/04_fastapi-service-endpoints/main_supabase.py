"""Supabase를 사용하는 백엔드 서비스 데이터 관리 FastAPI 예제.

이 파일은 실제 Supabase 테이블에 데이터를 저장하고 조회합니다.
먼저 main_mock.py로 API 구조를 확인한 뒤, .env와 Supabase 테이블이 준비되면 이 파일을 실행합니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from postgrest.exceptions import APIError
from pydantic import BaseModel, Field
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

app = FastAPI(title="Backend Service Data Management Supabase")


class ConversationCreate(BaseModel):
    """대화 생성 요청 모델입니다."""

    user_id: str | None = Field(default=None, examples=["00000000-0000-0000-0000-000000000001"])
    title: str = Field(min_length=1, max_length=100, examples=["FastAPI 질문"])


class MessageCreate(BaseModel):
    """메시지 저장 요청 모델입니다."""

    role: str = Field(pattern="^(user|assistant|system)$", examples=["user"])
    content: str = Field(min_length=1, examples=["대화 이력은 왜 저장하나요?"])


class ServiceLogCreate(BaseModel):
    """서비스 로그 저장 요청 모델입니다."""

    event_type: str = Field(min_length=1, examples=["message.created"])
    message: str = Field(min_length=1, examples=["메시지가 저장되었습니다."])
    metadata: dict = Field(default_factory=dict)


def get_supabase() -> Client:
    """환경변수에서 Supabase 접속 정보를 읽어 client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise HTTPException(
            status_code=500,
            detail="SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are required.",
        )

    return create_client(url, key)


def raise_supabase_error(error: APIError) -> None:
    """Supabase 오류를 FastAPI HTTP 오류로 변환합니다."""

    raise HTTPException(
        status_code=500,
        detail=(
            "Supabase request failed. "
            "Check .env values and run 06_supabase-db-and-auth/00_references/supabase-schema.sql."
        ),
    ) from error


@app.get("/health")
def health() -> dict[str, str]:
    """서버 상태를 확인하는 endpoint입니다."""

    return {"status": "ok", "storage": "supabase"}


@app.get("/profiles/{user_id}")
def get_profile(user_id: str) -> dict[str, dict]:
    """사용자 프로필을 조회합니다."""

    supabase = get_supabase()

    try:
        result = supabase.table("profiles").select("*").eq("id", user_id).limit(1).execute()
    except APIError as error:
        raise_supabase_error(error)

    if not result.data:
        raise HTTPException(status_code=404, detail="Profile not found.")

    return {"item": result.data[0]}


@app.post("/conversations", status_code=201)
def create_conversation(request: ConversationCreate) -> dict[str, dict]:
    """새 대화 묶음을 Supabase에 저장합니다."""

    supabase = get_supabase()

    try:
        result = supabase.table("conversations").insert(request.model_dump()).execute()
    except APIError as error:
        raise_supabase_error(error)

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create conversation.")

    return {"item": result.data[0]}


@app.post("/conversations/{conversation_id}/messages", status_code=201)
def add_message(conversation_id: str, request: MessageCreate) -> dict[str, dict]:
    """대화 묶음에 메시지를 저장합니다."""

    supabase = get_supabase()
    payload = {
        "conversation_id": conversation_id,
        "role": request.role,
        "content": request.content,
    }

    try:
        result = supabase.table("messages").insert(payload).execute()
    except APIError as error:
        raise_supabase_error(error)

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create message.")

    return {"item": result.data[0]}


@app.get("/conversations/{conversation_id}/messages")
def list_messages(conversation_id: str) -> dict[str, list[dict]]:
    """대화 묶음에 속한 메시지를 조회합니다."""

    supabase = get_supabase()

    try:
        result = (
            supabase.table("messages")
            .select("*")
            .eq("conversation_id", conversation_id)
            .order("created_at")
            .execute()
        )
    except APIError as error:
        raise_supabase_error(error)

    return {"items": result.data}


@app.post("/service-logs", status_code=201)
def create_service_log(request: ServiceLogCreate) -> dict[str, dict]:
    """서비스 로그를 Supabase에 저장합니다."""

    supabase = get_supabase()

    try:
        result = supabase.table("service_logs").insert(request.model_dump()).execute()
    except APIError as error:
        raise_supabase_error(error)

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create service log.")

    return {"item": result.data[0]}
