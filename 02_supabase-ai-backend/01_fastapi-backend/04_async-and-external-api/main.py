"""비동기 처리와 외부 API 호출을 함께 연습하는 FastAPI 예제입니다.

이 단원은 앞에서 만든 메모 API 흐름을 유지하면서, 서버가 오래 걸리는 작업을
기다리는 방법과 외부 API 데이터를 가져와 우리 API 응답에 연결하는 방법을 배웁니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\01_fastapi-backend\04_async-and-external-api
    uvicorn main:app --reload

브라우저:
    http://127.0.0.1:8000/docs
"""

import asyncio
from collections.abc import AsyncGenerator
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field


app = FastAPI(
    title="Memo API - Async And External API Practice",
    description="메모 API를 기준으로 async/await, 외부 API 호출, 기본 스트리밍 구조를 연습합니다.",
    version="1.0.0",
)


class ApiResponse(BaseModel):
    """프론트엔드가 공통으로 처리하기 쉬운 표준 응답 구조입니다."""

    success: bool
    message: str
    data: Any | None = None


class ChatDraftRequest(BaseModel):
    """AI 답변 초안을 만들 때 사용할 요청 데이터입니다.

    실제 Gemini 또는 OpenAI API 호출은 다음 단원에서 다룹니다.
    이번 단원에서는 외부 API 호출 구조와 비동기 흐름을 먼저 이해하기 위해
    가짜 AI 응답 함수를 사용합니다.
    """

    question: str = Field(
        min_length=1,
        max_length=300,
        examples=["FastAPI에서 async def를 언제 사용하나요?"],
    )
    tone: str = Field(default="friendly", max_length=30, examples=["friendly"])


# 아직 데이터베이스를 배우기 전이므로 메모 데이터를 메모리 변수에 저장합니다.
memos: dict[int, dict[str, Any]] = {
    1: {
        "id": 1,
        "title": "비동기 처리 복습",
        "content": "외부 API 호출처럼 기다리는 시간이 있는 작업은 async/await로 다룹니다.",
        "tags": ["async", "external-api"],
    }
}


@app.get("/health")
def health_check() -> dict[str, str]:
    """서버가 정상적으로 실행 중인지 확인합니다."""

    return {"status": "ok"}


@app.get("/async/wait", response_model=ApiResponse)
async def wait_for_seconds(
    seconds: float = Query(default=1, ge=0, le=5, description="기다릴 시간입니다. 0~5초만 허용합니다."),
) -> ApiResponse:
    """일부러 잠깐 기다리는 비동기 엔드포인트입니다.

    time.sleep()은 서버의 이벤트 루프를 막을 수 있으므로 FastAPI의 async 함수 안에서는
    asyncio.sleep()처럼 await 가능한 함수를 사용합니다.
    """

    await asyncio.sleep(seconds)

    return ApiResponse(
        success=True,
        message="async wait finished",
        data={"waited_seconds": seconds},
    )


@app.get("/async/parallel", response_model=ApiResponse)
async def run_parallel_tasks() -> ApiResponse:
    """여러 비동기 작업을 동시에 기다리는 예제입니다."""

    async def fetch_mock_data(name: str, seconds: float) -> dict[str, Any]:
        """외부 서비스 호출처럼 기다리는 작업을 흉내 냅니다."""

        await asyncio.sleep(seconds)
        return {"name": name, "waited_seconds": seconds}

    # asyncio.gather는 여러 작업을 동시에 시작하고, 모두 끝날 때까지 기다립니다.
    # 순서대로 기다리면 1 + 2 + 1 = 약 4초가 걸리지만, 동시에 기다리면 약 2초에 끝납니다.
    results = await asyncio.gather(
        fetch_mock_data("memo", 1),
        fetch_mock_data("external_post", 2),
        fetch_mock_data("usage_log", 1),
    )

    return ApiResponse(
        success=True,
        message="parallel tasks finished",
        data=results,
    )


@app.get("/external/posts/{post_id}", response_model=ApiResponse)
async def get_external_post(post_id: int) -> ApiResponse:
    """로그인이 필요 없는 공개 테스트 API에서 게시글 데이터를 가져옵니다.

    외부 API는 우리가 만든 서버 밖에 있는 다른 서비스입니다. 네트워크 문제, 잘못된 ID,
    외부 서비스 오류가 생길 수 있으므로 try/except로 실패 상황을 우리 API 오류로 바꿉니다.
    """

    external_data = await fetch_jsonplaceholder_post(post_id)

    return ApiResponse(
        success=True,
        message="external post loaded",
        data={
            "raw": external_data,
            "parsed": {
                "id": external_data["id"],
                "title": external_data["title"],
                "body_preview": external_data["body"][:80],
            },
        },
    )


@app.get("/memos/{memo_id}/external-context", response_model=ApiResponse)
async def enrich_memo_with_external_context(memo_id: int, post_id: int = 1) -> ApiResponse:
    """메모 데이터와 외부 API 데이터를 하나의 응답으로 묶습니다.

    이후 LLM API 단원에서는 이런 구조를 사용해 사용자 질문, 저장된 대화 이력,
    외부 데이터, AI 응답을 함께 연결하게 됩니다.
    """

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    external_data = await fetch_jsonplaceholder_post(post_id)

    return ApiResponse(
        success=True,
        message="memo enriched with external context",
        data={
            "memo": memos[memo_id],
            "external_context": {
                "source": "jsonplaceholder",
                "post_id": external_data["id"],
                "title": external_data["title"],
                "body_preview": external_data["body"][:80],
            },
        },
    )


@app.post("/ai/draft-response", response_model=ApiResponse)
async def create_ai_draft_response(request: ChatDraftRequest) -> ApiResponse:
    """AI API 호출 전 전체 흐름을 미리 이해하기 위한 placeholder 엔드포인트입니다."""

    answer = await call_fake_ai_model(request.question, request.tone)

    return ApiResponse(
        success=True,
        message="draft response generated",
        data={
            "question": request.question,
            "answer": answer,
        },
    )


@app.get("/stream")
async def stream_words() -> StreamingResponse:
    """텍스트를 한 번에 보내지 않고 조금씩 나누어 보내는 기초 스트리밍 예제입니다.

    이 예제는 일반 텍스트 스트리밍입니다. Server-Sent Events(SSE)를 이용한 실제 AI 응답
    스트리밍 통합은 04_supabase-ai-mini-project에서 백엔드, 프론트엔드, Supabase 저장과
    함께 다룹니다.
    """

    return StreamingResponse(generate_words(), media_type="text/plain")


async def fetch_jsonplaceholder_post(post_id: int) -> dict[str, Any]:
    """JSONPlaceholder 공개 API에서 게시글 하나를 가져옵니다."""

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail="External API returned an error",
        ) from error
    except httpx.RequestError as error:
        raise HTTPException(
            status_code=503,
            detail="External API is not reachable",
        ) from error

    return response.json()


async def call_fake_ai_model(question: str, tone: str) -> str:
    """실제 AI 모델 호출 대신 비동기 가짜 응답을 반환합니다."""

    await asyncio.sleep(1)
    return f"[{tone}] '{question}'에 대한 샘플 답변입니다. 실제 LLM API 호출은 다음 단원에서 연결합니다."


async def generate_words() -> AsyncGenerator[str, None]:
    """단어를 하나씩 천천히 보내는 비동기 generator입니다."""

    words = ["FastAPI", "async", "external", "API", "streaming"]

    for word in words:
        await asyncio.sleep(0.4)
        yield word + " "
