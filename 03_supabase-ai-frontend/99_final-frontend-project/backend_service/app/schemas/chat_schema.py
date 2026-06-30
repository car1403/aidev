from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)


class ChatResponse(BaseModel):
    answer: str
    provider: str
    model: str
    actual_api_called: bool


class ConversationResponse(BaseModel):
    id: str
    user_message: str
    assistant_message: str
    provider: str
    model: str | None = None
    created_at: str | None = None
