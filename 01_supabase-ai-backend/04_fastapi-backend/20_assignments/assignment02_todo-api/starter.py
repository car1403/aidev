"""Assignment 02 starter: Todo API.

요구사항:
1. Todo 목록 조회
2. Todo 생성
3. Todo 완료 처리
4. 없는 Todo id 요청 시 404 반환
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Todo API Assignment")


class TodoCreate(BaseModel):
    title: str = Field(min_length=1)


todos = {
    1: {"id": 1, "title": "FastAPI 복습", "done": False},
}
next_todo_id = 2


@app.get("/todos")
def list_todos():
    # TODO: todos 전체 목록을 반환하세요.
    return {"data": list(todos.values())}


@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    # TODO: 새 Todo를 생성하세요.
    return {"message": "TODO"}


@app.put("/todos/{todo_id}/done")
def mark_done(todo_id: int):
    # TODO: Todo를 완료 상태로 바꾸세요.
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "TODO"}
