"""Lab 06 solution: 메모 CRUD API.

이 예제는 Supabase로 넘어가기 전 CRUD의 기본 흐름을 연습하기 위한 코드입니다.
데이터는 Python dict에 저장되므로 서버를 재시작하면 초기값으로 돌아갑니다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Memo CRUD Solution")


class MemoCreate(BaseModel):
    """POST /memos 요청에서 받을 데이터입니다."""

    title: str = Field(min_length=1, examples=["FastAPI CRUD"])
    content: str = Field(min_length=1, examples=["메모 생성과 조회를 연습합니다."])
    tags: list[str] = Field(default_factory=list, examples=[["fastapi", "crud"]])


class MemoUpdate(BaseModel):
    """PUT /memos/{memo_id} 요청에서 받을 수정 데이터입니다."""

    title: str = Field(min_length=1, examples=["수정된 제목"])
    content: str = Field(min_length=1, examples=["수정된 내용입니다."])
    tags: list[str] = Field(default_factory=list, examples=[["updated"]])


# 메모리 저장소입니다.
# 초보자 실습에서는 DB 연결보다 API 흐름을 먼저 익히기 위해 dict를 사용합니다.
memos = {
    1: {
        "id": 1,
        "title": "First memo",
        "content": "FastAPI CRUD를 연습합니다.",
        "tags": ["fastapi"],
    }
}
next_memo_id = 2


@app.get("/health")
def health_check():
    """서버 실행 상태 확인용 API입니다."""

    return {"status": "ok"}


@app.get("/memos")
def list_memos():
    """전체 메모 목록을 반환합니다."""

    return {
        "count": len(memos),
        "data": list(memos.values()),
    }


@app.get("/memos/{memo_id}")
def get_memo(memo_id: int):
    """memo_id에 해당하는 메모 한 개를 반환합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    return {"data": memos[memo_id]}


@app.post("/memos", status_code=201)
def create_memo(memo: MemoCreate):
    """새 메모를 생성합니다."""

    global next_memo_id

    new_memo = {
        "id": next_memo_id,
        "title": memo.title,
        "content": memo.content,
        "tags": memo.tags,
    }
    memos[next_memo_id] = new_memo
    next_memo_id += 1

    return {"message": "memo created", "data": new_memo}


@app.put("/memos/{memo_id}")
def update_memo(memo_id: int, memo: MemoUpdate):
    """기존 메모를 수정합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    updated_memo = {
        "id": memo_id,
        "title": memo.title,
        "content": memo.content,
        "tags": memo.tags,
    }
    memos[memo_id] = updated_memo

    return {"message": "memo updated", "data": updated_memo}


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    """기존 메모를 삭제합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    deleted_memo = memos.pop(memo_id)

    return {"message": "memo deleted", "data": deleted_memo}
