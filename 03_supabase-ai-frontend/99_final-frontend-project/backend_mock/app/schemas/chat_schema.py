from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, description="사용자 질문")


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str
    actual_api_called: bool
    provider: str
    model: str


class ConversationItem(BaseModel):
    id: str
    user_email: str
    user_message: str
    assistant_message: str
    created_at: str
