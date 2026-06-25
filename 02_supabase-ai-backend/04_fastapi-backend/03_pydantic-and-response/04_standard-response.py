"""표준 응답 구조 예제입니다.

이 파일은 표준 응답 구조 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

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


@app.get("/memos", response_model=ApiResponse)
def list_memos():
    """메모 목록을 표준 응답 구조로 반환합니다."""

    memos = [
        {
            "id": 1,
            "title": "표준 응답 구조",
            "content": "success, message, data 구조를 연습합니다.",
            "tags": ["api", "response"],
        }
    ]

    return ApiResponse(
        success=True,
        message="memos loaded",
        data=memos,
    )


@app.get("/empty", response_model=ApiResponse)
def empty_response():
    """데이터가 없어도 응답 구조는 유지합니다."""

    return ApiResponse(
        success=True,
        message="no data yet",
        data=None,
    )
