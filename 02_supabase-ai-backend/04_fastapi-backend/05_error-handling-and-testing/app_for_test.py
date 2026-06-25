"""테스트 클라이언트에서 사용할 작은 FastAPI 앱입니다."""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="App For Test")


class MessageRequest(BaseModel):
    text: str = Field(min_length=1, examples=["hello"])


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/messages")
def create_message(request: MessageRequest):
    return {
        "message": "created",
        "data": {
            "text": request.text,
            "length": len(request.text),
        },
    }
