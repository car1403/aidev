"""Assignment 99 starter: FastAPI Mini Project.

주제 예시:
- 학습 기록 API
- 피드백 수집 API
- 간단한 Todo API

조건:
1. GET/POST를 포함합니다.
2. Pydantic 모델을 사용합니다.
3. 404 또는 400 오류 처리를 포함합니다.
4. README에 실행 방법과 요청/응답 예시를 작성합니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="FastAPI Mini Project")


class ItemCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)


items = {}
next_item_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    # TODO: 전체 item 목록을 반환하세요.
    return {"data": list(items.values())}


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    # TODO: 새 item을 생성하세요.
    return {"message": "TODO"}
