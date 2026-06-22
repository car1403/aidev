from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from supabase import Client, create_client


# uvicorn을 03_fastapi-supabase-integration 폴더에서 실행하면
# 상위 폴더의 .env를 자동으로 찾지 못할 수 있습니다.
# 수업에서는 C:\aidev\01_supabase-ai-backend에서 실행하거나,
# README의 명령처럼 가상환경을 활성화한 뒤 실행합니다.
load_dotenv()

app = FastAPI(title="Supabase First Backend Practice")


class NoteCreate(BaseModel):
    """새 학습 메모를 만들 때 클라이언트가 보내는 요청 모델입니다."""

    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=1000)


class NoteUpdate(BaseModel):
    """기존 학습 메모를 수정할 때 사용하는 요청 모델입니다."""

    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1, max_length=1000)


def get_supabase() -> Client:
    """FastAPI endpoint에서 사용할 Supabase client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")
    if not url or not key:
        raise HTTPException(status_code=500, detail="Supabase environment values are missing.")
    return create_client(url, key)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "database": "supabase"}


@app.get("/notes")
def list_notes() -> dict[str, list[dict]]:
    """최근 학습 메모 목록을 조회합니다."""

    supabase = get_supabase()
    result = supabase.table("learning_notes").select("*").order("created_at", desc=True).limit(20).execute()
    return {"items": result.data}


@app.get("/notes/{note_id}")
def get_note(note_id: str) -> dict[str, dict]:
    """id로 학습 메모 1개를 조회합니다."""

    supabase = get_supabase()
    result = supabase.table("learning_notes").select("*").eq("id", note_id).limit(1).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Note not found.")
    return {"item": result.data[0]}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate) -> dict[str, dict]:
    """학습 메모를 새로 저장합니다."""

    supabase = get_supabase()
    result = supabase.table("learning_notes").insert(note.model_dump()).execute()
    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create note.")
    return {"item": result.data[0]}


@app.put("/notes/{note_id}")
def update_note(note_id: str, note: NoteUpdate) -> dict[str, dict]:
    """학습 메모를 수정합니다."""

    update_data = note.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update.")

    supabase = get_supabase()
    result = supabase.table("learning_notes").update(update_data).eq("id", note_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Note not found.")
    return {"item": result.data[0]}


@app.delete("/notes/{note_id}")
def delete_note(note_id: str) -> dict[str, str]:
    """학습 메모를 삭제합니다."""

    supabase = get_supabase()
    supabase.table("learning_notes").delete().eq("id", note_id).execute()
    return {"deleted_id": note_id}
