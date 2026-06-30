"""Supabase `ex90_notes` 테이블을 호출하는 service 모듈입니다."""

from __future__ import annotations

from fastapi import HTTPException, status

from app.core.config import get_settings
from app.schemas.note_schema import NoteCreate, NotePublic, NoteUpdate


TABLE_NAME = "ex90_notes"


def get_supabase_client():
    """Supabase client를 만듭니다. 외부 패키지 import는 실제 호출 시점에 합니다."""

    from supabase import create_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=".env의 SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY를 확인하세요.",
        )

    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def to_note_public(row: dict) -> NotePublic:
    """Supabase row를 응답 모델로 변환합니다."""

    return NotePublic(
        id=str(row["id"]),
        title=row["title"],
        content=row["content"],
        created_at=row.get("created_at"),
    )


def list_notes() -> list[NotePublic]:
    """최근 노트를 조회합니다."""

    result = (
        get_supabase_client()
        .table(TABLE_NAME)
        .select("*")
        .order("created_at", desc=True)
        .limit(20)
        .execute()
    )
    return [to_note_public(row) for row in result.data]


def create_note(note: NoteCreate) -> NotePublic:
    """새 노트를 저장합니다."""

    result = (
        get_supabase_client()
        .table(TABLE_NAME)
        .insert({"title": note.title, "content": note.content})
        .execute()
    )
    return to_note_public(result.data[0])


def get_note(note_id: str) -> NotePublic | None:
    """id로 노트 1개를 조회합니다."""

    result = (
        get_supabase_client()
        .table(TABLE_NAME)
        .select("*")
        .eq("id", note_id)
        .limit(1)
        .execute()
    )
    if not result.data:
        return None
    return to_note_public(result.data[0])


def update_note(note_id: str, note: NoteUpdate) -> NotePublic | None:
    """id 조건으로 노트를 수정합니다."""

    result = (
        get_supabase_client()
        .table(TABLE_NAME)
        .update({"title": note.title, "content": note.content})
        .eq("id", note_id)
        .execute()
    )
    if not result.data:
        return None
    return to_note_public(result.data[0])


def delete_note(note_id: str) -> bool:
    """id 조건으로 노트를 삭제합니다."""

    result = get_supabase_client().table(TABLE_NAME).delete().eq("id", note_id).execute()
    return bool(result.data)
