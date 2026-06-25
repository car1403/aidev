"""Pydantic 요청 검증과 응답 모델을 한 번에 연습하는 FastAPI 예제입니다.

이 단원은 02_routing-and-request에서 만든 메모 API 흐름을 이어갑니다.
앞 단원에서는 URL, HTTP Method, Path Parameter, Query Parameter를 배웠고,
이번 단원에서는 "요청 데이터의 모양"과 "응답 데이터의 모양"을 명확히 정합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\04_fastapi-backend\03_pydantic-and-response
    uvicorn main:app --reload

브라우저:
    http://127.0.0.1:8000/docs
"""

from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="Memo API - Pydantic And Response Practice",
    description="메모 API를 사용해 요청 검증, 응답 모델, 표준 응답 구조를 연습합니다.",
    version="1.0.0",
)


class MemoCreate(BaseModel):
    """클라이언트가 새 메모를 만들 때 보내야 하는 요청 데이터입니다.

    BaseModel을 상속하면 FastAPI가 이 클래스의 타입 힌트와 Field 조건을 읽어서
    요청 JSON을 자동으로 검사합니다. 조건을 만족하지 못하면 엔드포인트 함수가
    실행되기 전에 FastAPI가 422 오류를 반환합니다.
    """

    title: str = Field(
        min_length=1,
        max_length=50,
        examples=["FastAPI 복습"],
        description="메모 제목입니다. 비어 있을 수 없고 50자 이하여야 합니다.",
    )
    content: str = Field(
        min_length=1,
        max_length=500,
        examples=["오늘 배운 Path Parameter와 Query Parameter를 정리합니다."],
        description="메모 본문입니다. 비어 있을 수 없고 500자 이하여야 합니다.",
    )
    tags: list[str] = Field(
        default_factory=list,
        max_length=5,
        examples=[["fastapi", "backend"]],
        description="메모를 분류하기 위한 태그 목록입니다. 최대 5개까지 허용합니다.",
    )


class MemoPublic(BaseModel):
    """API 응답으로 외부에 공개해도 되는 메모 데이터입니다.

    실제 서버 내부 데이터에는 관리용 값이나 민감한 값이 함께 들어갈 수 있습니다.
    response_model에 이 모델을 지정하면 여기에 정의된 필드만 응답으로 나갑니다.
    """

    id: int
    title: str
    content: str
    tags: list[str]


class ApiResponse(BaseModel):
    """프론트엔드가 공통으로 처리하기 쉬운 표준 응답 구조입니다."""

    success: bool
    message: str
    data: Any | None = None


# 아직 데이터베이스를 배우기 전이므로 메모 데이터를 메모리 변수에 저장합니다.
# 서버를 재시작하면 이 데이터는 초기값으로 돌아갑니다.
memos: dict[int, dict[str, Any]] = {
    1: {
        "id": 1,
        "title": "FastAPI 시작",
        "content": "GET, POST, PUT, DELETE의 차이를 정리합니다.",
        "tags": ["fastapi", "api"],
        # internal_note는 서버 내부 관리용 값입니다.
        # MemoPublic 응답 모델에 없기 때문에 GET /memos/1 응답에는 포함되지 않습니다.
        "internal_note": "수업 확인 메모: 02 단원과 연결해서 설명합니다.",
    }
}
next_memo_id = 2


@app.get("/health")
def health_check() -> dict[str, str]:
    """서버가 정상적으로 실행 중인지 확인하는 가장 단순한 엔드포인트입니다."""

    return {"status": "ok"}


@app.post("/memos", response_model=ApiResponse, status_code=status.HTTP_201_CREATED)
def create_memo(memo: MemoCreate) -> ApiResponse:
    """새 메모를 생성합니다.

    memo 매개변수의 타입이 MemoCreate이므로 FastAPI는 요청 Body를 자동 검증합니다.
    예를 들어 title이 비어 있거나 tags가 5개를 넘으면 이 함수는 실행되지 않고
    FastAPI가 422 Validation Error를 먼저 반환합니다.
    """

    global next_memo_id

    new_memo = {
        "id": next_memo_id,
        "title": memo.title,
        "content": memo.content,
        "tags": memo.tags,
        "internal_note": "새로 생성된 메모의 서버 내부 관리 값입니다.",
    }

    memos[next_memo_id] = new_memo
    next_memo_id += 1

    # ApiResponse.data는 Any 타입이므로 내부 값을 그대로 넣을 수도 있습니다.
    # 다만 응답에 내보낼 값만 담기 위해 MemoPublic으로 한 번 정리합니다.
    public_memo = MemoPublic(**new_memo).model_dump()

    return ApiResponse(
        success=True,
        message="memo created",
        data=public_memo,
    )


@app.get("/memos/{memo_id}", response_model=MemoPublic)
def get_memo(memo_id: int) -> dict[str, Any]:
    """메모 1개를 조회합니다.

    내부 데이터에는 internal_note가 있지만 response_model=MemoPublic을 사용했기 때문에
    실제 응답에는 id, title, content, tags만 포함됩니다.
    """

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    return memos[memo_id]


@app.get("/memos", response_model=ApiResponse)
def list_memos() -> ApiResponse:
    """메모 목록을 표준 응답 구조로 반환합니다.

    프론트엔드에서는 success로 성공 여부를 확인하고, message를 화면 메시지로 쓰고,
    data에 들어 있는 실제 목록을 화면에 표시할 수 있습니다.
    """

    public_memos = [MemoPublic(**memo).model_dump() for memo in memos.values()]

    return ApiResponse(
        success=True,
        message="memos loaded",
        data=public_memos,
    )


@app.get("/empty", response_model=ApiResponse)
def empty_response() -> ApiResponse:
    """데이터가 없어도 응답 구조를 일정하게 유지하는 예제입니다."""

    return ApiResponse(
        success=True,
        message="no data yet",
        data=None,
    )
