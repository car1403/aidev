"""StreamingResponse 기초 예제입니다.

이 파일은 스트리밍 응답 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

이 파일은 스트리밍 응답의 개념을 보여주는 아주 작은 예제입니다.
Server-Sent Events(SSE)를 이용한 실제 AI 응답 스트리밍 통합은
`03_supabase-ai-mini-project`에서 백엔드, 프론트엔드, Supabase 저장과 함께 다룹니다.
"""

import asyncio
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse


app = FastAPI(title="Streaming Response Practice")


async def generate_words() -> AsyncGenerator[str, None]:
    """단어를 하나씩 천천히 보내는 generator입니다."""

    words = ["FastAPI", "can", "send", "streaming", "responses."]

    for word in words:
        await asyncio.sleep(0.5)
        # 일반 텍스트 스트리밍에서는 문자열 조각을 순서대로 yield합니다.
        # yield는 값을 하나 반환하고 함수 실행 상태를 잠시 멈춰 두는 동작입니다.
        yield word + " "


@app.get("/stream")
async def stream_text():
    """텍스트를 한 번에 보내지 않고 조금씩 나누어 보냅니다."""

    return StreamingResponse(generate_words(), media_type="text/plain")
