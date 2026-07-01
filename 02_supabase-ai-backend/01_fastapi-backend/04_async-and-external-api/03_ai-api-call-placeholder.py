"""AI API 호출 구조를 미리 이해하는 예제입니다.

이 파일은 AI API 호출 흐름을 나누어 읽고 실행해 보기 위한 학습용 파일입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\01_fastapi-backend\04_async-and-external-api
    python .\03_ai-api-call-placeholder.py

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
API key 없이도 LLM API 흐름을 먼저 이해하기 위한 placeholder 예제입니다.

실제 LLM API 호출은 `02_llm-api-integration`에서 다룹니다.
"""

# 실제 AI API 호출은 네트워크 시간이 걸리는 작업입니다.
# 여기서는 그 시간을 흉내 내기 위해 asyncio.sleep()을 사용합니다.
import asyncio

from fastapi import FastAPI
from pydantic import BaseModel, Field


# FastAPI 앱 객체입니다.
# 아래 __main__ 블록의 uvicorn.run(app, ...)에서 사용하는 app이 이 변수입니다.
app = FastAPI(title="AI API Placeholder Practice")


class ChatRequest(BaseModel):
    """사용자가 보낸 질문 데이터입니다."""

    # message는 사용자의 질문입니다. 최소 1글자 이상이어야 합니다.
    message: str = Field(min_length=1, examples=["FastAPI가 무엇인가요?"])
    # tone은 답변 말투를 고르는 값입니다.
    # 사용자가 보내지 않으면 기본값 friendly를 사용합니다.
    tone: str = Field(default="friendly", examples=["friendly"])


async def call_fake_ai_model(message: str, tone: str) -> str:
    """실제 AI 모델 호출 대신 가짜 응답을 반환합니다."""

    # 실제 서비스라면 이 부분에서 Gemini API를 기본으로 호출합니다.
    # OpenAI API는 선택/비교 실습을 진행할 때 연결할 수 있습니다.
    # 지금은 API key 없이도 흐름을 이해할 수 있도록 1초 기다린 뒤 샘플 응답을 만듭니다.
    await asyncio.sleep(1)
    return f"[{tone}] 질문 '{message}'에 대한 샘플 AI 응답입니다."


# POST /ai/chat은 사용자의 질문 JSON을 받고 AI 응답 JSON을 돌려주는 형태입니다.
# 아직 실제 AI 모델은 호출하지 않고, call_fake_ai_model()로 전체 흐름만 연습합니다.
@app.post("/ai/chat")
async def chat(request: ChatRequest):
    """AI 챗봇 API의 기본 흐름을 보여줍니다."""

    # request는 이미 ChatRequest 모델로 검증된 값입니다.
    # message가 비어 있으면 이 함수가 실행되기 전에 FastAPI가 422 오류를 반환합니다.
    answer = await call_fake_ai_model(request.message, request.tone)

    return {
        "message": "ai response generated",
        "data": {
            "question": request.message,
            "answer": answer,
        },
    }

if __name__ == "__main__":
    # 파일명에 하이픈(-)이 들어 있으면 uvicorn 파일명:app 방식이 헷갈릴 수 있습니다.
    # 그래서 이 예제는 `python .\03_ai-api-call-placeholder.py` 명령으로 직접 실행합니다.
    # 서버가 실행되면 브라우저에서 http://127.0.0.1:8000/docs 를 열어 Swagger UI를 확인합니다.
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
