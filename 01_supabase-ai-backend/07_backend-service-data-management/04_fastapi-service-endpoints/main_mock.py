"""백엔드 서비스 데이터 관리 mock FastAPI 예제.

이 파일은 Supabase에 접속하지 않습니다.
메모리 리스트를 사용해 사용자 프로필, 대화 메시지, 서비스 로그 API 구조를 먼저 익힙니다.
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Backend Service Data Management Mock")


# 실제 서비스에서는 이 데이터들이 Supabase 테이블에 저장됩니다.
# mock 예제에서는 서버가 실행되는 동안만 메모리에 유지됩니다.
profiles: dict[str, dict] = {
    "student01": {
        "id": "student01",
        "display_name": "수강생 A",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
}
conversations: dict[str, dict] = {}
messages: list[dict] = []
service_logs: list[dict] = []


class ConversationCreate(BaseModel):
    """새 대화방을 만들 때 필요한 요청 모델입니다."""

    user_id: str = Field(min_length=1, examples=["student01"])
    title: str = Field(min_length=1, max_length=100, examples=["FastAPI 질문"])


class MessageCreate(BaseModel):
    """대화방에 메시지를 추가할 때 필요한 요청 모델입니다."""

    role: str = Field(pattern="^(user|assistant|system)$", examples=["user"])
    content: str = Field(min_length=1, examples=["FastAPI에서 Pydantic은 왜 사용하나요?"])


class ServiceLogCreate(BaseModel):
    """서비스 로그를 저장할 때 필요한 요청 모델입니다."""

    event_type: str = Field(min_length=1, examples=["message.created"])
    message: str = Field(min_length=1, examples=["메시지가 저장되었습니다."])
    metadata: dict = Field(default_factory=dict)


def now_iso() -> str:
    """UTC 현재 시간을 ISO 문자열로 반환합니다."""

    return datetime.now(timezone.utc).isoformat()


@app.get("/health")
def health() -> dict[str, str]:
    """서버 상태 확인용 endpoint입니다."""

    return {"status": "ok", "storage": "memory"}


@app.get("/profiles/{user_id}")
def get_profile(user_id: str) -> dict[str, dict]:
    """사용자 프로필을 조회합니다."""

    profile = profiles.get(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found.")
    return {"item": profile}


@app.post("/conversations", status_code=201)
def create_conversation(request: ConversationCreate) -> dict[str, dict]:
    """새 대화방을 생성합니다."""

    conversation_id = str(uuid4())
    item = {
        "id": conversation_id,
        "user_id": request.user_id,
        "title": request.title,
        "created_at": now_iso(),
    }
    conversations[conversation_id] = item
    return {"item": item}


@app.post("/conversations/{conversation_id}/messages", status_code=201)
def add_message(conversation_id: str, request: MessageCreate) -> dict[str, dict]:
    """대화방에 메시지를 추가합니다."""

    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found.")

    item = {
        "id": str(uuid4()),
        "conversation_id": conversation_id,
        "role": request.role,
        "content": request.content,
        "created_at": now_iso(),
    }
    messages.append(item)
    return {"item": item}


@app.get("/conversations/{conversation_id}/messages")
def list_messages(conversation_id: str) -> dict[str, list[dict]]:
    """특정 대화방의 메시지를 조회합니다."""

    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found.")

    items = [message for message in messages if message["conversation_id"] == conversation_id]
    return {"items": items}


@app.post("/service-logs", status_code=201)
def create_service_log(request: ServiceLogCreate) -> dict[str, dict]:
    """서비스 로그를 저장합니다."""

    item = {
        "id": str(uuid4()),
        "event_type": request.event_type,
        "message": request.message,
        "metadata": request.metadata,
        "created_at": now_iso(),
    }
    service_logs.append(item)
    return {"item": item}
