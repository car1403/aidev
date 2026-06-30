"""Redis 캐시 API 경로를 정의합니다."""

from fastapi import APIRouter, Query

from app.core.config import is_configured
from app.schemas.cache_schema import CachedAnswerResponse
from app.services import cache_service


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    return {"status": "ok", "redis_configured": is_configured()}


@router.get("/ai/mock-answer", response_model=CachedAnswerResponse)
def mock_answer(question: str = Query(min_length=1)) -> CachedAnswerResponse:
    return cache_service.get_or_create_answer(question)


@router.delete("/ai/mock-answer-cache")
def clear_cache(question: str = Query(min_length=1)) -> dict[str, str | int]:
    deleted_count = cache_service.clear_answer(question)
    return {"question": question, "deleted_count": deleted_count}
