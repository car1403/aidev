"""Notes API에서 사용하는 Pydantic 모델입니다."""

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    """POST /notes 요청 Body입니다."""

    title: str = Field(min_length=1, examples=["FastAPI 구조 정리"])
    content: str = Field(min_length=1, examples=["router, schema, service를 나누어 봅니다."])


class NoteUpdate(BaseModel):
    """PUT /notes/{note_id} 요청 Body입니다."""

    title: str = Field(min_length=1, examples=["수정된 제목"])
    content: str = Field(min_length=1, examples=["수정된 내용"])


class NotePublic(BaseModel):
    """클라이언트에 반환하는 노트 응답 모델입니다."""

    id: str
    title: str
    content: str
    created_at: str | None = None
