r"""FastAPI + mock LLM endpoint 예제입니다.

실제 LLM API를 호출하지 않으므로 비용이 발생하지 않습니다.
FastAPI에서 요청을 받고, 모델 호출 결과처럼 응답하는 흐름을 연습합니다.

실행:
    cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
    ..\..\.venv\Scripts\Activate.ps1
    uvicorn main_mock:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Mock LLM Endpoint")


class ChatRequest(BaseModel):
    """프론트엔드나 API client가 보낼 채팅 요청 모델입니다."""

    # message는 사용자가 입력한 질문입니다.
    # min_length=1은 빈 문자열 요청을 막는 가장 기본적인 검증입니다.
    message: str = Field(min_length=1, max_length=500, examples=["FastAPI가 무엇인가요?"])
    memo_context: str = Field(default="", max_length=1000, examples=["FastAPI는 Python API 서버 프레임워크입니다."])
    # temperature는 0.0부터 1.0까지만 허용해서 잘못된 값이 들어오지 않게 합니다.
    temperature: float = Field(default=0.3, ge=0.0, le=1.0)


class ChatResponse(BaseModel):
    """AI 응답을 클라이언트에 돌려줄 때 사용할 응답 모델입니다."""

    # provider/model을 응답에 포함하면 프론트엔드와 로그에서 어떤 모델을 썼는지 확인하기 쉽습니다.
    provider: str
    model: str
    answer: str


def generate_mock_answer(message: str, memo_context: str, temperature: float) -> str:
    """실제 모델 응답 대신 수업용 가짜 응답을 생성합니다."""

    context_text = f"참고 메모 '{memo_context}'를 함께 사용했습니다. " if memo_context else ""
    return (
        f"질문 '{message}'에 대한 mock 응답입니다. "
        f"{context_text}"
        f"temperature={temperature} 설정을 사용했다고 가정합니다."
    )


@app.get("/health")
def health_check():
    """서버 상태 확인용 API입니다."""

    return {"status": "ok"}


@app.post("/ai/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """AI 챗봇 endpoint의 기본 구조입니다."""

    # 실제 서비스라면 이 위치에서 Gemini API 같은 외부 LLM API를 호출합니다.
    # OpenAI API는 선택/비교 실습으로 연결할 수 있습니다.
    # 지금은 비용 없는 수업을 위해 mock 함수를 호출합니다.
    answer = generate_mock_answer(request.message, request.memo_context, request.temperature)

    # response_model=ChatResponse와 같은 구조로 반환하면 Swagger 문서도 명확해집니다.
    return ChatResponse(
        provider="mock",
        model="mock-teacher",
        answer=answer,
    )
