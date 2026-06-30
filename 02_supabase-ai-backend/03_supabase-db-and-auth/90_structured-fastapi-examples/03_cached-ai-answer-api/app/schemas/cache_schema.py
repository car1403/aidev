"""Redis 캐시 응답 모델입니다."""

from pydantic import BaseModel


class CachedAnswerResponse(BaseModel):
    question: str
    answer: str
    cached: bool
    ttl_seconds: int
