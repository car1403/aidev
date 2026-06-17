"""Lab 04 starter: Response Model."""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Lab 04 Starter")


class UserPublic(BaseModel):
    id: int
    name: str
    # TODO: email 필드를 추가해 보세요.


@app.get("/users/1", response_model=UserPublic)
def get_user():
    """TODO: password가 응답에 포함되지 않도록 확인해 보세요."""

    return {"id": 1, "name": "Alice", "password": "secret"}
