"""메모 관리 API로 라우팅과 요청 데이터를 연습하는 FastAPI 예제입니다.

이 파일은 실제 실행용입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\01_fastapi-backend\02_routing-and-request
    uvicorn main:app --reload

브라우저:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(
    title="Memo Routing Practice",
    description="메모 API 하나로 GET, POST, PUT, DELETE, Path, Query, Body를 연습합니다.",
    version="1.0.0",
)


class MemoCreate(BaseModel):
    """POST /memos 요청에서 받을 메모 생성 데이터입니다."""

    title: str = Field(min_length=1, examples=["오늘 배운 내용"])
    content: str = Field(min_length=1, examples=["GET과 POST의 차이를 배웠습니다."])


class MemoUpdate(BaseModel):
    """PUT /memos/{memo_id} 요청에서 받을 메모 수정 데이터입니다."""

    title: str = Field(min_length=1, examples=["수정된 제목"])
    content: str = Field(min_length=1, examples=["수정된 내용입니다."])


# 서버 메모리에만 저장되는 수업용 데이터입니다.
# 서버를 종료하거나 다시 시작하면 처음 상태로 돌아갑니다.
# 이후 Supabase 단원에서는 이 부분을 테이블 저장으로 바꾸게 됩니다.
memos: dict[int, dict[str, object]] = {
    1: {
        "id": 1,
        "title": "FastAPI 시작",
        "content": "Swagger UI에서 API를 확인했습니다.",
    },
    2: {
        "id": 2,
        "title": "요청 데이터",
        "content": "Path, Query, Body의 차이를 배웁니다.",
    },
}
next_memo_id = 3


@app.get("/health")
def health_check() -> dict[str, str]:
    """서버가 실행 중인지 확인합니다."""

    return {"status": "ok"}


@app.get("/memos")
def list_memos() -> dict[str, list[dict[str, object]]]:
    """GET Method로 전체 메모 목록을 조회합니다."""

    return {"data": list(memos.values())}


@app.get("/memos/search")
def search_memos(
    keyword: str = Query(default="", description="메모 제목과 내용에서 찾을 검색어"),
    limit: int = Query(default=10, ge=1, le=20, description="최대 반환 개수"),
) -> dict[str, object]:
    """Query Parameter로 메모를 검색합니다."""

    result = list(memos.values())

    if keyword:
        result = [
            memo
            for memo in result
            if keyword.lower() in str(memo["title"]).lower()
            or keyword.lower() in str(memo["content"]).lower()
        ]

    return {
        "keyword": keyword,
        "limit": limit,
        "count": len(result[:limit]),
        "data": result[:limit],
    }


@app.get("/memos/{memo_id}")
def get_memo(memo_id: int) -> dict[str, object]:
    """Path Parameter로 메모 id를 받아 메모 한 건을 조회합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    return {"data": memos[memo_id]}


@app.post("/memos", status_code=201)
def create_memo(memo: MemoCreate) -> dict[str, object]:
    """POST Method와 Request Body로 새 메모를 생성합니다."""

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
def update_memo(memo_id: int, memo: MemoUpdate) -> dict[str, object]:
    """Path Parameter와 Request Body로 기존 메모를 수정합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    memos[memo_id] = {
        "id": memo_id,
        "title": memo.title,
        "content": memo.content,
    }

    return {"message": "memo updated", "data": memos[memo_id]}


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int) -> dict[str, object]:
    """DELETE Method와 Path Parameter로 기존 메모를 삭제합니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    deleted = memos.pop(memo_id)
    return {"message": "memo deleted", "data": deleted}
