from fastapi import APIRouter, Depends

from app.core.security import parse_bearer_token
from app.schemas.chat_schema import ChatRequest, ChatResponse, ConversationItem
from app.services.auth_service import get_user_by_token
from app.services.chat_service import create_chat, list_conversations_for_user


router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest, token: str = Depends(parse_bearer_token)) -> dict:
    user = get_user_by_token(token)
    return create_chat(user, payload)


@router.get("/conversations", response_model=list[ConversationItem])
def conversations_endpoint(token: str = Depends(parse_bearer_token)) -> list[dict]:
    user = get_user_by_token(token)
    return list_conversations_for_user(user["email"])
