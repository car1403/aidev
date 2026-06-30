"""Auth 모델입니다."""

from pydantic import BaseModel, Field


class AuthRequest(BaseModel):
    email: str = Field(min_length=3, examples=["student@example.com"])
    password: str = Field(min_length=6, examples=["password123"])


class UserPublic(BaseModel):
    id: str
    email: str | None = None
    access_token: str | None = None


class AuthResponse(BaseModel):
    user: UserPublic
    access_token: str
    token_type: str = "bearer"
