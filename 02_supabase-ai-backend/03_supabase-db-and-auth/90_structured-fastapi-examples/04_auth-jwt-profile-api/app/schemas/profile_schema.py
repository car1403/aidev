"""Profile 요청/응답 모델입니다."""

from pydantic import BaseModel, Field


class ProfileUpdate(BaseModel):
    display_name: str = Field(min_length=1, examples=["홍길동"])


class ProfilePublic(BaseModel):
    id: str
    display_name: str
    created_at: str | None = None
    updated_at: str | None = None
