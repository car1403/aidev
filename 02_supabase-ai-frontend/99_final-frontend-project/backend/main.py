from __future__ import annotations

import os
import json
import time
from datetime import datetime, timezone
from urllib.parse import quote
from typing import Any
from uuid import uuid4

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


load_dotenv()

app = FastAPI(
    title="Final Frontend Project Backend",
    description="Streamlit 최종 프론트엔드 예제를 위한 간단한 FastAPI 백엔드입니다.",
    version="1.0.0",
)

# Streamlit Community Cloud처럼 다른 주소에서 실행되는 프론트엔드가
# 이 백엔드 API를 호출할 수 있도록 CORS를 열어 둡니다.
# 실제 서비스에서는 허용할 도메인을 정확히 제한하는 것이 좋습니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 수업용 예제에서는 별도 데이터베이스 없이 메모리에 대화와 로그를 저장합니다.
# 서버를 재시작하면 메모리 데이터는 사라집니다.
# 03 미니 프로젝트에서는 이 부분을 Supabase 테이블 저장으로 확장합니다.
CHAT_HISTORY: list[dict[str, Any]] = []
SERVICE_LOGS: list[dict[str, Any]] = []


class ChatRequest(BaseModel):
    user_name: str = Field(..., min_length=1, description="질문한 사용자 이름")
    message: str = Field(..., min_length=1, description="사용자가 입력한 질문")


class ChatResponse(BaseModel):
    conversation_id: str
    user_name: str
    user_message: str
    assistant_message: str
    created_at: str
    elapsed_ms: int


def utc_now() -> str:
    """프론트엔드에서 읽기 쉬운 ISO 날짜 문자열을 만듭니다."""
    return datetime.now(timezone.utc).isoformat()


def build_demo_answer(user_name: str, message: str) -> str:
    """실제 LLM API 대신 수업용 응답을 만들어 줍니다.

    02 과정의 목표는 프론트엔드와 백엔드 연결 흐름을 익히는 것입니다.
    실제 LLM 호출과 Supabase 저장은 01과 03 과정에서 더 깊게 다룹니다.
    """
    return (
        f"{user_name}님, 질문을 확인했습니다. "
        f"'{message}'에 대해서는 먼저 요구사항을 작게 나누고, "
        "입력값, API 응답, 화면 표시, 로그 기록 순서로 점검해 보세요."
    )


async def save_log_to_upstash(log: dict[str, Any]) -> None:
    """Upstash Redis REST API로 서비스 로그를 선택적으로 저장합니다.

    UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN이 비어 있으면
    로컬 실습 모드로 보고 아무 작업도 하지 않습니다.
    """
    redis_url = os.getenv("UPSTASH_REDIS_REST_URL", "").strip()
    redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip()

    if not redis_url or not redis_token:
        return

    # Upstash REST API는 명령어를 URL 경로로 전달할 수 있습니다.
    # 여기서는 최신 로그 20개만 빠르게 볼 수 있도록 list에 push합니다.
    encoded_log = quote(json.dumps(log, ensure_ascii=False))
    endpoint = f"{redis_url.rstrip('/')}/lpush/final_frontend_logs/{encoded_log}"
    headers = {"Authorization": f"Bearer {redis_token}"}

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.post(endpoint, headers=headers)
    except httpx.HTTPError:
        # 로그 저장 실패가 챗봇 응답 실패로 이어지지 않도록 수업용 예제에서는 조용히 넘어갑니다.
        # 실제 서비스에서는 실패 로그를 별도로 남기고 재시도 정책을 둡니다.
        return


def append_service_log(event: str, detail: dict[str, Any]) -> dict[str, Any]:
    """API 호출 기록을 메모리 로그 목록에 추가합니다."""
    log = {
        "log_id": str(uuid4()),
        "event": event,
        "detail": detail,
        "created_at": utc_now(),
    }
    SERVICE_LOGS.insert(0, log)
    return log


@app.get("/health")
def health() -> dict[str, Any]:
    """Render 배포 후에도 가장 먼저 확인할 기본 상태 점검 API입니다."""
    return {
        "ok": True,
        "service": "final-frontend-project-backend",
        "env": os.getenv("APP_ENV", "local"),
        "chat_count": len(CHAT_HISTORY),
        "log_count": len(SERVICE_LOGS),
    }


@app.post("/api/chat", response_model=ChatResponse)
async def create_chat(request: ChatRequest) -> ChatResponse:
    """사용자 질문을 받아 데모 AI 응답을 만들고 대화 이력과 로그를 저장합니다."""
    started_at = time.perf_counter()
    assistant_message = build_demo_answer(request.user_name, request.message)
    elapsed_ms = int((time.perf_counter() - started_at) * 1000)

    chat = {
        "conversation_id": str(uuid4()),
        "user_name": request.user_name,
        "user_message": request.message,
        "assistant_message": assistant_message,
        "created_at": utc_now(),
        "elapsed_ms": elapsed_ms,
    }
    CHAT_HISTORY.insert(0, chat)

    log = append_service_log(
        event="chat.created",
        detail={
            "conversation_id": chat["conversation_id"],
            "user_name": request.user_name,
            "elapsed_ms": elapsed_ms,
        },
    )
    await save_log_to_upstash(log)

    return ChatResponse(**chat)


@app.get("/api/chats")
def list_chats() -> dict[str, Any]:
    """Streamlit의 대화 이력 화면에서 호출하는 API입니다."""
    append_service_log(event="chat.listed", detail={"count": len(CHAT_HISTORY)})
    return {"items": CHAT_HISTORY}


@app.get("/api/logs")
def list_logs() -> dict[str, Any]:
    """Streamlit의 서비스 로그 화면에서 호출하는 API입니다."""
    return {"items": SERVICE_LOGS}
