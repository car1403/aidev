"""Lab 06 starter.

TODO를 채우면서 메모 CRUD API를 완성해 보세요.
정답은 solution.py에서 확인할 수 있습니다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Memo CRUD Starter")


class MemoCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list)


class MemoUpdate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list)


memos = {
    1: {
        "id": 1,
        "title": "Starter memo",
        "content": "TODO를 채워 CRUD API를 완성합니다.",
        "tags": ["practice"],
    }
}
next_memo_id = 2


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/memos")
def list_memos():
    # TODO: 전체 메모 목록을 반환하세요.
    return {"data": []}


@app.get("/memos/{memo_id}")
def get_memo(memo_id: int):
    # TODO: memo_id가 없으면 404 오류를 반환하세요.
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")
    return {"data": memos[memo_id]}


@app.post("/memos", status_code=201)
def create_memo(memo: MemoCreate):
    # TODO: 새 id를 만들고 memos에 저장하세요.
    return {"message": "TODO"}


@app.put("/memos/{memo_id}")
def update_memo(memo_id: int, memo: MemoUpdate):
    # TODO: 기존 메모를 수정하세요.
    return {"message": "TODO"}


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    # TODO: 기존 메모를 삭제하세요.
    return {"message": "TODO"}

