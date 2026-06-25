import asyncio
import json

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field


app = FastAPI(title="SSE Streaming Chat Example")


class ChatStreamRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)


def build_demo_chunks(message: str) -> list[str]:
    return [
        "질문을 확인했습니다. ",
        f"'{message}' 내용을 기준으로 ",
        "관련 정보를 정리하고 있습니다. ",
        "최종 답변은 스트리밍이 끝난 뒤 Supabase messages 테이블에 저장하는 흐름으로 설계합니다.",
    ]


async def stream_chat_events(message: str):
    final_answer = ""

    for chunk in build_demo_chunks(message):
        final_answer += chunk
        event = {"type": "chunk", "content": chunk}
        yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        await asyncio.sleep(0.4)

    done_event = {"type": "done", "content": final_answer}
    yield f"data: {json.dumps(done_event, ensure_ascii=False)}\n\n"


@app.get("/health")
def health_check():
    return {"api": "ok", "streaming": "ok"}


@app.post("/api/chat/stream")
def stream_chat(payload: ChatStreamRequest):
    return StreamingResponse(
        stream_chat_events(payload.message),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )
