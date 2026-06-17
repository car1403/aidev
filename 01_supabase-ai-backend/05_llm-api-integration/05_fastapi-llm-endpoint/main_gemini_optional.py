"""FastAPI + Gemini optional endpoint 예제.

01~03 과정에서는 Gemini API를 기본 LLM 실습 모델로 사용합니다.
GEMINI_API_KEY가 없으면 실제 API를 호출하지 않고 안내 메시지를 반환합니다.
GEMINI_API_KEY가 있으면 실제 호출을 수행하므로 무료 범위와 호출 제한을 먼저 확인합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from fastapi import FastAPI
import httpx
from pydantic import BaseModel, Field


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


app = FastAPI(title="Gemini Optional LLM Endpoint")


class ChatRequest(BaseModel):
    """Gemini API 호출에 사용할 요청 모델입니다."""

    message: str = Field(min_length=1, examples=["FastAPI에서 Pydantic을 왜 사용하나요?"])
    temperature: float = Field(default=0.3, ge=0.0, le=1.0)
    max_output_tokens: int = Field(default=300, ge=50, le=1000)


@app.get("/health")
def health_check():
    """서버 상태 확인용 API입니다."""

    return {"status": "ok"}


@app.post("/ai/chat")
def chat(request: ChatRequest):
    """FastAPI 요청을 받아 Gemini REST API 호출 흐름으로 연결합니다."""

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not api_key:
        return {
            "provider": "gemini",
            "model": model,
            "actual_api_called": False,
            "answer": "GEMINI_API_KEY가 없어 실제 API를 호출하지 않았습니다. mock 예제로 먼저 실습하세요.",
        }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": request.message},
                ]
            }
        ],
        "generationConfig": {
            "temperature": request.temperature,
            "maxOutputTokens": request.max_output_tokens,
        },
    }

    response = httpx.post(url, params=params, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]

    return {
        "provider": "gemini",
        "model": model,
        "actual_api_called": True,
        "answer": answer,
    }
