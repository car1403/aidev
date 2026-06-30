"""채팅 요청/응답 모델입니다."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, examples=["Redis 캐시는 언제 쓰나요?"])


class ChatResponse(BaseModel):
    user_message: str
    assistant_message: str
    cached: bool
    provider: str
    model: str
    actual_api_called: bool
    log_id: str | None = None


class ChatLogPublic(BaseModel):
    id: str
    user_id: str
    user_message: str
    assistant_message: str | None = None
    provider: str
    model: str | None = None
    actual_api_called: bool
    cached: bool
    status: str
    error_message: str | None = None
    created_at: str | None = None
