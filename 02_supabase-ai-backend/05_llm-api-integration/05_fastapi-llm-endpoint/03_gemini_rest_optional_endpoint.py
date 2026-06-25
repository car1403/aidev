r"""FastAPI + Gemini REST optional endpoint 예제입니다.

01~03 과정에서는 Gemini API를 기본 LLM 실습 모델로 사용합니다.
GEMINI_API_KEY가 없으면 실제 API를 호출하지 않고 안내 메시지를 반환합니다.
GEMINI_API_KEY가 있으면 실제 호출을 수행하므로 무료 범위와 호출 제한을 먼저 확인합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
    ..\..\.venv\Scripts\Activate.ps1
    uvicorn 03_gemini_rest_optional_endpoint:app --reload
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from fastapi import FastAPI
import httpx
from pydantic import BaseModel, Field


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


app = FastAPI(title="Gemini REST Optional LLM Endpoint")


class ChatRequest(BaseModel):
    """Gemini API 호출에 사용할 요청 모델입니다."""

    message: str = Field(min_length=1, max_length=500, examples=["FastAPI에서 Pydantic을 왜 사용하나요?"])
    memo_context: str = Field(default="", max_length=1000, examples=["Pydantic은 요청 데이터를 검증합니다."])
    temperature: float = Field(default=0.3, ge=0.0, le=1.0)
    max_output_tokens: int = Field(default=300, ge=50, le=1000)


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 API key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def build_prompt(request: ChatRequest) -> str:
    """Gemini에 보낼 질문과 메모 컨텍스트를 하나의 텍스트로 정리합니다."""

    parts = ["당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다."]
    if request.memo_context:
        parts.append(f"참고 메모:\n{request.memo_context}")
    parts.append(f"사용자 질문:\n{request.message}")
    parts.append("답변은 초보자가 이해할 수 있도록 단계별로 작성해 주세요.")
    return "\n\n".join(parts)


@app.get("/health")
def health_check():
    """서버 상태 확인용 API입니다."""

    return {"status": "ok"}


@app.post("/ai/chat")
def chat(request: ChatRequest):
    """FastAPI 요청을 받아 Gemini REST API 호출 흐름으로 연결합니다."""

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not is_real_api_key(api_key):
        return {
            "provider": "gemini",
            "model": model,
            "actual_api_called": False,
            "answer": "GEMINI_API_KEY가 없거나 placeholder 값입니다. mock 예제로 먼저 실습하세요.",
        }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": build_prompt(request)},
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
