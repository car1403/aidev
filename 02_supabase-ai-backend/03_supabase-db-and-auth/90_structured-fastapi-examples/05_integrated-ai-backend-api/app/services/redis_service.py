"""Upstash Redis helper입니다."""

from __future__ import annotations

from urllib.parse import quote

import httpx
from fastapi import HTTPException

from app.core.config import get_settings


TTL_SECONDS = 60


def redis_command(*parts: str) -> dict:
    settings = get_settings()
    if not settings.redis_rest_url or not settings.redis_rest_token:
        raise HTTPException(status_code=500, detail="Upstash Redis 환경변수를 확인하세요.")
    encoded = [quote(part, safe="") for part in parts]
    url = f"{settings.redis_rest_url}/{'/'.join(encoded)}"
    headers = {"Authorization": f"Bearer {settings.redis_rest_token}"}
    try:
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"Redis 호출 실패: {error}") from error
    return response.json()


def get_answer(key: str) -> str | None:
    return redis_command("get", key).get("result")


def set_answer(key: str, answer: str) -> None:
    redis_command("set", key, answer, "ex", str(TTL_SECONDS))
