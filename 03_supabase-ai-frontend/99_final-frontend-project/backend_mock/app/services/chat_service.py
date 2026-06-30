from time import sleep
from uuid import uuid4

from app.core.config import ENABLE_FAKE_DELAY
from app.schemas.chat_schema import ChatRequest
from app.services.log_service import add_log, now_text
from app.services.memory_store import conversations


def build_mock_answer(user_email: str, message: str) -> str:
    recent = [
        item
        for item in conversations
        if item["user_email"] == user_email
    ][-3:]

    context_hint = ""
    if recent:
        context_hint = f" 이전 대화 {len(recent)}개를 참고해 이어서 답변합니다."

    return f"'{message}'에 대한 수업용 mock AI 답변입니다.{context_hint}"


def create_chat(user: dict, payload: ChatRequest) -> dict:
    if ENABLE_FAKE_DELAY:
        sleep(0.5)

    answer = build_mock_answer(user["email"], payload.message)
    item = {
        "id": str(uuid4()),
        "user_email": user["email"],
        "user_message": payload.message,
        "assistant_message": answer,
        "created_at": now_text(),
    }
    conversations.append(item)
    add_log("chat", "success", "mock AI 답변 생성", user["email"])

    return {
        "conversation_id": item["id"],
        "answer": answer,
        "actual_api_called": False,
        "provider": "mock",
        "model": "mock-chat-ux-v1",
    }


def list_conversations_for_user(user_email: str) -> list[dict]:
    return [
        item
        for item in reversed(conversations)
        if item["user_email"] == user_email
    ]
