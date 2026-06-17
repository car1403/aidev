"""Lab 03 solution: Request Body와 Pydantic 검증."""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Lab 03 Request Body Validation")


class UserCreate(BaseModel):
    """사용자 생성 요청 모델입니다."""

    name: str = Field(min_length=2, examples=["Alice"])
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$", examples=["alice@example.com"])
    age: int = Field(ge=1, le=120, examples=[25])


@app.post("/users")
def create_user(user: UserCreate):
    """요청 body를 검증한 뒤 사용자 데이터를 반환합니다."""

    return {
        "message": "user created",
        "data": user.model_dump(),
    }
