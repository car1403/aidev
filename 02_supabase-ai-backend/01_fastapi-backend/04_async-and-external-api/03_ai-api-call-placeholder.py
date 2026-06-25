"""AI API 호출 구조를 미리 이해하는 예제입니다.

이 파일은 AI API 호출 흐름을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
API key 없이도 LLM API 흐름을 먼저 이해하기 위한 placeholder 예제입니다.

실제 LLM API 호출은 `02_llm-api-integration`에서 다룹니다.
"""

import asyncio

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="AI API Placeholder Practice")


class ChatRequest(BaseModel):
    """사용자가 보낸 질문 데이터입니다."""

    message: str = Field(min_length=1, examples=["FastAPI가 무엇인가요?"])
    tone: str = Field(default="friendly", examples=["friendly"])


async def call_fake_ai_model(message: str, tone: str) -> str:
    """실제 AI 모델 호출 대신 가짜 응답을 반환합니다."""

    # 실제 서비스라면 이 부분에서 Gemini API를 기본으로 호출합니다.
    # OpenAI API는 선택/비교 실습을 진행할 때 연결할 수 있습니다.
    # 지금은 API key 없이도 흐름을 이해할 수 있도록 1초 기다린 뒤 샘플 응답을 만듭니다.
    await asyncio.sleep(1)
    return f"[{tone}] 질문 '{message}'에 대한 샘플 AI 응답입니다."


@app.post("/ai/chat")
async def chat(request: ChatRequest):
    """AI 챗봇 API의 기본 흐름을 보여줍니다."""

    answer = await call_fake_ai_model(request.message, request.tone)

    return {
        "message": "ai response generated",
        "data": {
            "question": request.message,
            "answer": answer,
        },
    }
