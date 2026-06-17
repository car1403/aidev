"""기술 지원 워크플로우 API에서 사용하는 데이터 모델입니다."""

from pydantic import BaseModel, Field


class TicketRequest(BaseModel):
    """사용자가 입력하는 기술 지원 문의입니다."""

    customer_name: str = Field(..., min_length=1)
    customer_tier: str = Field(default="basic")
    title: str = Field(..., min_length=1)
    message: str = Field(..., min_length=10)


class TicketAnalysis(BaseModel):
    """워크플로우 실행 결과입니다."""

    ticket_id: str
    category: str
    urgency: str
    matched_documents: list[str]
    draft_answer: str
    validation_status: str
    next_action: str
    estimated_cost_usd: float
