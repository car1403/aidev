"""인증된 사용자의 채팅 API입니다."""

from fastapi import APIRouter

from app.schemas.auth_schema import UserPublic
from app.schemas.chat_schema import ChatRequest, ChatResponse, ChatLogPublic
from app.services import auth_service, chat_service


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    user: auth_service.CurrentUser,
) -> ChatResponse:
    return chat_service.answer_with_cache_and_log(user, request)


@router.get("/logs")
def logs(user: auth_service.CurrentUser) -> dict[str, int | list[ChatLogPublic]]:
    data = chat_service.list_logs(user.access_token)
    return {"count": len(data), "data": data}
