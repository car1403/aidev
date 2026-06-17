"""Lab 99 starter: Mini API Server.

지금까지 배운 내용을 모아 작은 학습 기록 API를 완성합니다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Mini API Starter")


class LearningNoteCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


notes = {}
next_note_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/notes")
def list_notes():
    # TODO: 전체 학습 기록 목록을 반환하세요.
    return {"data": []}


@app.post("/notes", status_code=201)
def create_note(note: LearningNoteCreate):
    # TODO: 새 학습 기록을 생성하세요.
    return {"message": "TODO"}


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    # TODO: note_id가 없으면 404 오류를 반환하세요.
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"data": notes[note_id]}
