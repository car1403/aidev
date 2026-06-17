"""Pydantic 모델 기초 예제.

Pydantic 모델은 API가 주고받는 데이터의 모양을 정의합니다.
FastAPI는 이 모델을 사용해서 JSON 요청을 검증하고 Swagger 문서도 만듭니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Pydantic Model Practice")


class UserCreate(BaseModel):
    """회원가입 요청 데이터의 형식을 정의합니다."""

    name: str = Field(min_length=2, max_length=30, examples=["Alice"])
    # EmailStr을 사용하면 email-validator 패키지가 추가로 필요할 수 있습니다.
    # 이 과정에서는 별도 패키지 없이 실행되도록 문자열 패턴으로 이메일 형식을 간단히 검증합니다.
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$", examples=["alice@example.com"])
    age: int = Field(ge=14, le=120, examples=[25])


@app.post("/users")
def create_user(user: UserCreate):
    """Pydantic 모델을 사용해 요청 JSON을 검증합니다."""

    # user는 dict가 아니라 UserCreate 객체입니다.
    # JSON으로 응답하려면 model_dump()로 dict 형태로 바꿀 수 있습니다.
    return {
        "message": "user data is valid",
        "data": user.model_dump(),
    }
