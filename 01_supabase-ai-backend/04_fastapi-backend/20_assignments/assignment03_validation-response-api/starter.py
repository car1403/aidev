"""Assignment 03 starter: Validation And Response API.

요구사항:
1. Pydantic으로 요청 데이터 검증
2. 표준 응답 구조 사용
3. 잘못된 요청에서 422 확인
"""

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Validation Response Assignment")


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None


class ScoreRequest(BaseModel):
    student_name: str = Field(min_length=2)
    subject: str = Field(min_length=1)
    score: int = Field(ge=0, le=100)


@app.post("/scores", response_model=ApiResponse)
def create_score(request: ScoreRequest):
    # TODO: 점수 등급을 계산해 data에 포함하세요.
    return ApiResponse(
        success=True,
        message="score accepted",
        data=request.model_dump(),
    )
