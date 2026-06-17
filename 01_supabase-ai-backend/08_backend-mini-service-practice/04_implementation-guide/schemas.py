"""미니 서비스에서 사용하는 Pydantic 모델 모음.

Pydantic 모델은 FastAPI에서 요청 데이터를 검증하고,
Swagger UI에 문서 형태로 보여주는 역할을 합니다.
"""

from pydantic import BaseModel, Field


class QaCreate(BaseModel):
    """사용자가 질문을 보낼 때 사용하는 요청 모델입니다."""

    # user_id는 로그인 기능을 완성하기 전까지 문자열로 간단히 받습니다.
    # 이후 Supabase Auth를 연결하면 auth.users.id와 연결할 수 있습니다.
    user_id: str | None = Field(default=None, examples=["student01"])

    # question은 비어 있으면 안 됩니다.
    # max_length를 두면 너무 긴 요청으로 인한 비용/성능 문제를 줄일 수 있습니다.
    question: str = Field(
        min_length=1,
        max_length=1000,
        examples=["FastAPI에서 Pydantic은 왜 사용하나요?"],
    )

    # 처음에는 mock 모델명을 사용합니다.
    # 실제 LLM API를 연결하면 Gemini 모델명을 기본으로 사용합니다.
    # OpenAI 모델명은 선택/비교 실습 때 사용할 수 있습니다.
    model: str = Field(default="mock-teacher", examples=["mock-teacher"])


class QaItem(BaseModel):
    """질문/답변 저장 결과를 표현하는 응답 모델입니다."""

    id: str
    user_id: str | None = None
    question: str
    answer: str
    model: str
    created_at: str | None = None


class ServiceLogItem(BaseModel):
    """서비스 로그 응답 모델입니다."""

    id: str
    event_type: str
    message: str
    metadata: dict
    created_at: str | None = None


class ItemResponse(BaseModel):
    """단일 객체 응답을 통일하기 위한 모델입니다."""

    item: dict


class ListResponse(BaseModel):
    """목록 응답을 통일하기 위한 모델입니다."""

    items: list[dict]
