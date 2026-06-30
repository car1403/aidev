"""Upstash Redis에 mock AI 답변을 캐시합니다."""

from __future__ import annotations

from urllib.parse import quote

import httpx
from fastapi import HTTPException, status

from app.core.config import get_settings
from app.schemas.cache_schema import CachedAnswerResponse


TTL_SECONDS = 60


def redis_command(*parts: str) -> dict:
    settings = get_settings()
    if not settings.redis_rest_url or not settings.redis_rest_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=".env의 UPSTASH_REDIS_REST_URL, UPSTASH_REDIS_REST_TOKEN을 확인하세요.",
        )

    encoded = [quote(part, safe="") for part in parts]
    url = f"{settings.redis_rest_url}/{'/'.join(encoded)}"
    headers = {"Authorization": f"Bearer {settings.redis_rest_token}"}

    try:
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"Redis 호출 실패: {error}") from error

    return response.json()


def cache_key(question: str) -> str:
    return f"ex90:answer:{question}"


def create_mock_answer(question: str) -> str:
    return f"'{question}'에 대한 Redis 캐시 예제용 mock 답변입니다."


def get_or_create_answer(question: str) -> CachedAnswerResponse:
    key = cache_key(question)
    cached_result = redis_command("get", key)
    cached_answer = cached_result.get("result")

    if cached_answer:
        return CachedAnswerResponse(
            question=question,
            answer=cached_answer,
            cached=True,
            ttl_seconds=TTL_SECONDS,
        )

    answer = create_mock_answer(question)
    redis_command("set", key, answer, "ex", str(TTL_SECONDS))
    return CachedAnswerResponse(
        question=question,
        answer=answer,
        cached=False,
        ttl_seconds=TTL_SECONDS,
    )


def clear_answer(question: str) -> int:
    result = redis_command("del", cache_key(question))
    return int(result.get("result", 0))
