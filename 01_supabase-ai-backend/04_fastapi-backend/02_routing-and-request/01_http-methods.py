"""HTTP Method(GET/POST/PUT/DELETE) 예제.

이 파일은 HTTP Method 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 실행은 같은 폴더의 main.py를 사용합니다.

실행:
    uvicorn main:app --reload

HTTP Method는 API 요청의 의도를 표현합니다.

GET    -> 데이터 조회
POST   -> 새 데이터 생성
PUT    -> 기존 데이터 전체 수정
DELETE -> 기존 데이터 삭제
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="HTTP Method Practice")


class MemoCreate(BaseModel):
    """POST 요청에서 받을 메모 데이터 형식입니다."""

    title: str = Field(min_length=1, examples=["오늘 배운 내용"])
    content: str = Field(min_length=1, examples=["GET과 POST의 차이를 배웠습니다."])


class MemoUpdate(BaseModel):
    """PUT 요청에서 받을 수정 데이터 형식입니다."""

    title: str = Field(min_length=1, examples=["수정된 제목"])
    content: str = Field(min_length=1, examples=["수정된 내용입니다."])


# 수업용 메모리 저장소입니다.
# 서버를 재시작하면 데이터가 사라집니다.
# 실제 서비스에서는 Supabase 같은 DB에 저장합니다.
memos = {
    1: {"id": 1, "title": "FastAPI 시작", "content": "Swagger UI를 확인했습니다."},
}
next_memo_id = 2


@app.get("/memos")
def list_memos():
    """전체 메모 목록을 조회합니다."""

    return {"data": list(memos.values())}


@app.post("/memos", status_code=201)
def create_memo(memo: MemoCreate):
    """새 메모를 생성합니다."""

    global next_memo_id

    new_memo = {
        "id": next_memo_id,
        "title": memo.title,
        "content": memo.content,
    }
    memos[next_memo_id] = new_memo
    next_memo_id += 1

    return {"message": "memo created", "data": new_memo}


@app.put("/memos/{memo_id}")
def update_memo(memo_id: int, memo: MemoUpdate):
    """기존 메모를 수정합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    memos[memo_id] = {
        "id": memo_id,
        "title": memo.title,
        "content": memo.content,
    }

    return {"message": "memo updated", "data": memos[memo_id]}


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    """기존 메모를 삭제합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    deleted = memos.pop(memo_id)
    return {"message": "memo deleted", "data": deleted}
