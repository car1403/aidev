"""Pydantic 모델 기초 예제입니다.

이 파일은 Pydantic 모델 개념을 나누어 읽고 실행해 보기 위한 학습용 파일입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\01_fastapi-backend\03_pydantic-and-response
    python .\01_pydantic-models.py

Pydantic 모델은 API가 주고받는 데이터의 모양을 정의합니다.
FastAPI는 이 모델을 사용해서 요청 JSON을 검증하고 Swagger 문서도 만듭니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


# FastAPI 앱 객체입니다.
# 아래 __main__ 블록의 uvicorn.run(app, ...)에서 사용하는 app이 이 변수입니다.
app = FastAPI(title="Pydantic Model Practice")


# BaseModel을 상속한 클래스는 요청/응답 데이터의 설계도 역할을 합니다.
# FastAPI는 이 설계도를 보고 요청 JSON이 올바른지 자동으로 검사합니다.
class MemoCreate(BaseModel):
    """새 메모를 만들 때 클라이언트가 보내야 하는 데이터입니다."""

    # title은 문자열이어야 하며, 비어 있으면 안 됩니다.
    # max_length를 사용하면 너무 긴 제목이 들어오는 것을 막을 수 있습니다.
    title: str = Field(min_length=1, max_length=50, examples=["FastAPI 복습"])

    # content도 문자열이어야 하며, 비어 있으면 안 됩니다.
    # API는 이 조건을 기준으로 잘못된 요청을 자동으로 거절합니다.
    content: str = Field(min_length=1, max_length=500, examples=["Pydantic 모델을 정리합니다."])

    # tags는 문자열 목록입니다.
    # default_factory=list는 값이 없을 때 빈 목록을 새로 만들어 줍니다.
    tags: list[str] = Field(default_factory=list, max_length=5, examples=[["fastapi", "pydantic"]])


@app.post("/memos")
def create_memo(memo: MemoCreate):
    """Pydantic 모델을 사용해 요청 JSON을 검증합니다."""

    # FastAPI는 클라이언트가 보낸 JSON을 MemoCreate 규칙으로 먼저 검사합니다.
    # 검증에 성공하면 이 함수가 실행되고, 실패하면 자동으로 422 오류가 반환됩니다.
    # memo는 dict가 아니라 MemoCreate 객체입니다.
    # JSON으로 응답하려면 model_dump()로 dict 형태로 바꿀 수 있습니다.
    return {
        "message": "memo data is valid",
        "data": memo.model_dump(),
    }

if __name__ == "__main__":
    # 파일명에 하이픈(-)이 들어 있으면 uvicorn 파일명:app 방식이 헷갈릴 수 있습니다.
    # 그래서 이 예제는 `python .\01_pydantic-models.py` 명령으로 직접 실행합니다.
    # 서버가 실행되면 브라우저에서 http://127.0.0.1:8000/docs 를 열어 Swagger UI를 확인합니다.
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
