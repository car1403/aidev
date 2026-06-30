"""채팅 로그 API에서 사용하는 요청/응답 모델입니다."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, examples=["오늘 배운 내용을 요약해줘"])


class ChatResponse(BaseModel):
    user_message: str
    assistant_message: str
    provider: str
    model: str
    actual_api_called: bool
    log_id: str | None = None


class ChatLogPublic(BaseModel):
    id: str
    user_message: str
    assistant_message: str | None = None
    provider: str
    model: str | None = None
    actual_api_called: bool = False
    status: str
    error_message: str | None = None
    created_at: str | None = None
