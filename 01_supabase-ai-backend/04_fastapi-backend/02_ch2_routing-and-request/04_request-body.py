"""Request Body 예제.

Request Body는 클라이언트가 서버로 보내는 JSON 데이터입니다.
보통 POST, PUT 요청에서 사용합니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Request Body Practice")


class FeedbackRequest(BaseModel):
    """사용자 피드백 요청 데이터입니다."""

    user_name: str = Field(min_length=1, examples=["Alice"])
    score: int = Field(ge=1, le=5, examples=[5])
    comment: str = Field(min_length=5, examples=["오늘 수업이 이해하기 쉬웠습니다."])


@app.post("/feedback")
def create_feedback(feedback: FeedbackRequest):
    """사용자 피드백 JSON을 받아 처리합니다."""

    return {
        "message": "feedback received",
        "data": feedback.model_dump(),
    }
