"""`ex90_notes` API 경로를 정의합니다."""

from fastapi import APIRouter, HTTPException, status

from app.core.config import is_configured
from app.schemas.note_schema import NoteCreate, NotePublic, NoteUpdate
from app.services import notes_service


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    """서버 상태와 환경변수 준비 여부를 확인합니다."""

    return {"status": "ok", "supabase_configured": is_configured()}


@router.get("/notes")
def list_notes() -> dict[str, int | list[NotePublic]]:
    """노트 목록을 조회합니다."""

    notes = notes_service.list_notes()
    return {"count": len(notes), "data": notes}


@router.post("/notes", response_model=NotePublic, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate) -> NotePublic:
    """새 노트를 저장합니다."""

    return notes_service.create_note(note)


@router.get("/notes/{note_id}", response_model=NotePublic)
def get_note(note_id: str) -> NotePublic:
    """id로 노트 1개를 조회합니다."""

    note = notes_service.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/notes/{note_id}", response_model=NotePublic)
def update_note(note_id: str, note: NoteUpdate) -> NotePublic:
    """노트 제목과 내용을 수정합니다."""

    updated = notes_service.update_note(note_id, note)
    if updated is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated


@router.delete("/notes/{note_id}")
def delete_note(note_id: str) -> dict[str, str]:
    """노트를 삭제합니다."""

    deleted = notes_service.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "deleted"}
