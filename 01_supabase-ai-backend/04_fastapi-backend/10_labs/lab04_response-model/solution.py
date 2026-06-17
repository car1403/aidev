"""Lab 04 solution: Response Model."""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Lab 04 Response Model")


class UserPublic(BaseModel):
    """외부로 공개할 사용자 응답 모델입니다."""

    id: int
    name: str
    email: str


@app.get("/users/1", response_model=UserPublic)
def get_user():
    """내부 데이터에 password가 있어도 응답에서는 제외됩니다."""

    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "password": "secret-password",
    }
