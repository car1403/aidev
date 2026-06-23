r"""FastAPI + OpenAI optional endpoint 예제입니다.

OPENAI_API_KEY가 없으면 실제 API를 호출하지 않고 안내 메시지를 반환합니다.
OPENAI_API_KEY가 있으면 실제 호출을 수행하므로 비용이 발생할 수 있습니다.

실행:
    cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
    ..\..\.venv\Scripts\Activate.ps1
    uvicorn 04_openai_optional_endpoint:app --reload
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field


# FastAPI 서버가 어느 위치에서 실행되더라도 같은 .env 파일을 읽기 위해 절대 경로를 계산합니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


app = FastAPI(title="OpenAI Optional LLM Endpoint")


class ChatRequest(BaseModel):
    """실제 API 호출에 사용할 요청 모델입니다."""

    # 프론트엔드가 보낸 질문입니다. 빈 질문은 FastAPI/Pydantic이 자동으로 422 오류 처리합니다.
    message: str = Field(min_length=1, max_length=500, examples=["FastAPI에서 Pydantic을 왜 사용하나요?"])
    memo_context: str = Field(default="", max_length=1000, examples=["Pydantic은 요청 데이터를 검증합니다."])
    # API 사용자가 너무 큰 값을 보내지 못하도록 범위를 제한합니다.
    temperature: float = Field(default=0.3, ge=0.0, le=1.0)
    # max_tokens 상한을 두면 실수로 매우 긴 응답을 생성하는 것을 방지할 수 있습니다.
    max_tokens: int = Field(default=300, ge=50, le=1000)


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 API key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def build_user_content(request: ChatRequest) -> str:
    """OpenAI messages에 넣을 user content를 만듭니다."""

    parts = []
    if request.memo_context:
        parts.append(f"참고 메모:\n{request.memo_context}")
    parts.append(f"사용자 질문:\n{request.message}")
    return "\n\n".join(parts)


@app.get("/health")
def health_check():
    # 배포 후에도 서버가 살아 있는지 확인할 때 사용하는 endpoint입니다.
    return {"status": "ok"}


@app.post("/ai/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not is_real_api_key(api_key):
        # key가 없을 때도 서버가 오류로 죽지 않고 안내 응답을 반환하게 합니다.
        # 이 구조는 학습, 데모, 로컬 개발에서 특히 유용합니다.
        return {
            "provider": "openai",
            "model": model,
            "actual_api_called": False,
            "answer": "OPENAI_API_KEY가 없거나 placeholder 값입니다. mock 예제로 먼저 실습하세요.",
        }

    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    # 이 부분부터 실제 비용이 발생할 수 있는 외부 API 호출입니다.
    # 운영 서비스에서는 호출 전 사용자 권한, rate limit, 로그 정책을 함께 적용합니다.
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다."},
            {"role": "user", "content": build_user_content(request)},
        ],
        temperature=request.temperature,
        max_tokens=request.max_tokens,
    )

    # 프론트엔드가 실제 호출 여부를 구분할 수 있도록 actual_api_called를 함께 반환합니다.
    return {
        "provider": "openai",
        "model": model,
        "actual_api_called": True,
        "answer": response.choices[0].message.content,
    }
