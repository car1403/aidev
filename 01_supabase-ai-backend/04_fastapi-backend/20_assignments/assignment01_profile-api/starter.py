"""Assignment 01 starter: Profile API.

요구사항:
1. GET /health
2. GET /profile
3. POST /profile
4. 이름, 나이, 관심 기술을 관리
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Profile API Assignment")


class ProfileRequest(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=1, le=120)
    interests: list[str] = Field(default_factory=list)


profile = {
    "name": "Student",
    "age": 20,
    "interests": ["Python"],
}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/profile")
def get_profile():
    # TODO: 현재 profile 데이터를 반환하세요.
    return {"data": profile}


@app.post("/profile")
def update_profile(request: ProfileRequest):
    # TODO: request 값으로 profile을 수정하세요.
    profile["name"] = request.name
    profile["age"] = request.age
    profile["interests"] = request.interests
    return {"message": "profile updated", "data": profile}
