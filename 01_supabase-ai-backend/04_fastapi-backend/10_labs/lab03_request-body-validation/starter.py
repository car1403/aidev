"""Lab 03 starter: Request Body와 Pydantic 검증."""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Lab 03 Starter")


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    # TODO: age 필드를 추가하고 1 이상 120 이하로 검증해 보세요.


@app.post("/users")
def create_user(user: UserCreate):
    """TODO: user 데이터를 응답으로 반환해 보세요."""

    return {"message": "TODO"}
