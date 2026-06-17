"""표준 응답 구조 예제.

API가 많아질수록 응답 모양이 제각각이면 프론트엔드에서 처리하기 어렵습니다.
이 예제에서는 success, message, data 형태로 응답을 통일합니다.
"""

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Standard Response Practice")


class ApiResponse(BaseModel):
    """수업용 표준 응답 모델입니다."""

    success: bool
    message: str
    data: Any | None = None


@app.get("/courses", response_model=ApiResponse)
def list_courses():
    """강의 목록을 표준 응답 구조로 반환합니다."""

    courses = [
        {"id": 1, "title": "Python Basic"},
        {"id": 2, "title": "FastAPI Backend"},
    ]

    return ApiResponse(
        success=True,
        message="courses loaded",
        data=courses,
    )


@app.get("/empty", response_model=ApiResponse)
def empty_response():
    """데이터가 없어도 응답 구조는 유지합니다."""

    return ApiResponse(
        success=True,
        message="no data yet",
        data=None,
    )
