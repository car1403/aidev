from pydantic import BaseModel, Field


class LogCreate(BaseModel):
    level: str = Field(default="info", examples=["info"])
    source: str = Field(default="backend", examples=["chat-api"])
    message: str = Field(min_length=1, examples=["AI 응답 생성 완료"])
    request_path: str | None = Field(default="/chat")
    status_code: int | None = Field(default=200)
    latency_ms: int | None = Field(default=120)
    metadata: dict = Field(default_factory=dict)


class LogItem(LogCreate):
    id: str
    created_at: str


class LogSummary(BaseModel):
    level: str
    count: int
