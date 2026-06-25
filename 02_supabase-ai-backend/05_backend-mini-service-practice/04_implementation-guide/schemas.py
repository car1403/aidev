"""미니 서비스에서 사용하는 Pydantic 모델 모음.

FastAPI는 Pydantic 모델을 이용해 요청 JSON을 검사합니다.
예를 들어 question이 비어 있으면 API 함수가 실행되기 전에 검증 오류가 발생합니다.
"""

from pydantic import BaseModel, Field


class QuestionCreateRequest(BaseModel):
    """POST /questions 요청에서 사용하는 모델입니다."""

    # user_id는 질문을 보낸 사용자를 구분하는 값입니다.
    # 실제 로그인 기능을 붙이면 Supabase Auth 사용자 id와 연결할 수 있습니다.
    user_id: str = Field(
        min_length=1,
        examples=["student01"],
        description="질문을 보낸 사용자 id",
    )

    # question은 사용자가 입력한 질문입니다.
    # max_length를 두면 너무 긴 입력으로 인한 비용과 처리 시간을 줄일 수 있습니다.
    question: str = Field(
        min_length=1,
        max_length=500,
        examples=["FastAPI에서 Pydantic은 왜 사용하나요?"],
        description="사용자 질문",
    )

    # 처음에는 실제 LLM이 아니라 mock 답변 생성 함수를 사용합니다.
    # 다만 모델 이름은 이후 실제 Gemini SDK로 교체할 때와 맞추기 위해 기본값을 Gemini 기준으로 둡니다.
    model: str = Field(
        default="gemini-2.5-flash-lite",
        examples=["gemini-2.5-flash-lite"],
        description="답변 생성에 사용할 모델 이름",
    )

    # provider는 어떤 LLM 서비스 계열을 기준으로 설계했는지 표시합니다.
    # 01~03 과정에서는 Gemini를 기본으로 사용하고, OpenAI는 선택 비교용으로 유지합니다.
    provider: str = Field(
        default="gemini",
        examples=["gemini"],
        description="답변 생성에 사용할 LLM 제공자",
    )


class ServiceLogCreateRequest(BaseModel):
    """POST /service-logs 요청에서 사용하는 모델입니다."""

    event_type: str = Field(
        min_length=1,
        examples=["question_created"],
        description="로그 종류",
    )
    message: str = Field(
        min_length=1,
        examples=["질문 답변 생성 성공"],
        description="사람이 읽을 수 있는 로그 메시지",
    )
    metadata: dict = Field(
        default_factory=dict,
        examples=[{"user_id": "student01", "duration_ms": 120}],
        description="로그에 함께 저장할 추가 정보",
    )


class QuestionItem(BaseModel):
    """질문/답변 저장 결과를 표현하는 모델입니다."""

    id: str
    user_id: str
    question: str
    answer: str
    model: str
    provider: str = "gemini"
    actual_api_called: bool = False
    llm_call_mode: str = "mock-first"
    created_at: str | None = None


class ServiceLogItem(BaseModel):
    """서비스 로그 응답 모델입니다."""

    id: str
    event_type: str
    message: str
    metadata: dict
    created_at: str | None = None


class ErrorBody(BaseModel):
    """오류 응답 안에 들어가는 error 객체입니다."""

    code: str
    message: str


class ErrorResponse(BaseModel):
    """오류 응답 구조입니다."""

    ok: bool = False
    error: ErrorBody
