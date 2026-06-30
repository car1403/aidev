"""채팅 로그 API 경로를 정의합니다."""

from fastapi import APIRouter

from app.core.config import is_configured
from app.schemas.chat_schema import ChatRequest, ChatResponse, ChatLogPublic
from app.services import chat_service


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    return {"status": "ok", "supabase_configured": is_configured()}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    return chat_service.answer_and_log(request)


@router.get("/logs")
def list_logs() -> dict[str, int | list[ChatLogPublic]]:
    logs = chat_service.list_logs()
    return {"count": len(logs), "data": logs}
