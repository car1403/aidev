"""Lab 99 solution: Mini API Server.

이 파일은 FastAPI 단원의 작은 마무리 프로젝트입니다.
Supabase 연결 전 단계이므로 메모리 dict에 데이터를 저장합니다.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(title="FastAPI Mini Learning Notes")


class LearningNoteCreate(BaseModel):
    """학습 기록 생성 요청 모델입니다."""

    title: str = Field(min_length=1, examples=["FastAPI 라우팅"])
    content: str = Field(min_length=1, examples=["GET과 POST의 차이를 배웠습니다."])
    difficulty: int = Field(ge=1, le=5, examples=[2])


class LearningNoteResponse(BaseModel):
    """학습 기록 응답 모델입니다."""

    id: int
    title: str
    content: str
    difficulty: int


notes = {
    1: {
        "id": 1,
        "title": "FastAPI 시작",
        "content": "Swagger UI를 열어 API를 확인했습니다.",
        "difficulty": 1,
    }
}
next_note_id = 2


@app.get("/health")
def health_check():
    """서버 상태 확인 API입니다."""

    return {"status": "ok"}


@app.get("/notes")
def list_notes(max_difficulty: int | None = Query(default=None, ge=1, le=5)):
    """학습 기록 목록을 조회합니다."""

    result = list(notes.values())

    if max_difficulty is not None:
        result = [note for note in result if note["difficulty"] <= max_difficulty]

    return {
        "count": len(result),
        "data": result,
    }


@app.post("/notes", status_code=201, response_model=LearningNoteResponse)
def create_note(note: LearningNoteCreate):
    """새 학습 기록을 생성합니다."""

    global next_note_id

    new_note = {
        "id": next_note_id,
        "title": note.title,
        "content": note.content,
        "difficulty": note.difficulty,
    }
    notes[next_note_id] = new_note
    next_note_id += 1

    return new_note


@app.get("/notes/{note_id}", response_model=LearningNoteResponse)
def get_note(note_id: int):
    """id로 학습 기록 한 개를 조회합니다."""

    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")

    return notes[note_id]
