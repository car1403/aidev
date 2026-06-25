"""요청 데이터 검증 예제입니다.

이 파일은 요청 검증 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

잘못된 요청이 들어오면 FastAPI는 자동으로 422 응답을 반환합니다.
이 예제에서는 필수값, 문자열 길이, 목록 길이를 검증합니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Request Validation Practice")


class MemoCreate(BaseModel):
    """메모 생성 요청 데이터입니다."""

    # min_length=1은 빈 문자열을 막기 위한 조건입니다.
    title: str = Field(min_length=1, max_length=50, examples=["검증 연습"])

    # content도 최소 1글자 이상이어야 합니다.
    content: str = Field(min_length=1, max_length=500, examples=["잘못된 요청을 일부러 보내 봅니다."])

    # 태그는 5개까지만 받습니다.
    tags: list[str] = Field(default_factory=list, max_length=5, examples=[["validation"]])


@app.post("/memos")
def create_memo(memo: MemoCreate):
    """요청 데이터가 조건을 만족하면 이 함수가 실행됩니다."""

    return {
        "message": "request validation passed",
        "title_length": len(memo.title),
        "content_length": len(memo.content),
        "tag_count": len(memo.tags),
    }
