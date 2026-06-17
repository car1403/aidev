"""Response Model 예제.

response_model은 API 응답으로 내보낼 데이터의 모양을 제한합니다.
내부 데이터에 password 같은 값이 있어도 응답 모델에 없으면 밖으로 나가지 않습니다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Response Model Practice")


class UserPublic(BaseModel):
    """외부에 공개해도 되는 사용자 응답 모델입니다."""

    id: int
    name: str
    email: str


users = {
    1: {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "password": "do-not-return-this-value",
    }
}


@app.get("/users/{user_id}", response_model=UserPublic)
def get_user(user_id: int):
    """사용자 정보를 반환하지만 password는 응답에서 제외됩니다."""

    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return users[user_id]
