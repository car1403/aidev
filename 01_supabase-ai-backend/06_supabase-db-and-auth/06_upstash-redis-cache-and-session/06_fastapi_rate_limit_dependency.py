"""FastAPI endpoint에 Upstash Redis 기반 Rate Limit을 적용하는 예제입니다."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException, status


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(ENV_PATH)

app = FastAPI(title="FastAPI Upstash Rate Limit Practice")


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다."""

    if value is None:
        return False

    return value.strip().startswith(("your-", "https://your-"))


def get_upstash_env() -> tuple[str, str]:
    """Upstash Redis REST URL과 token을 읽습니다."""

    url = os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/")
    token = os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip()

    if not url or not token or is_placeholder(url) or is_placeholder(token):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Upstash Redis environment values are missing. Check .env first.",
        )

    return url, token


def upstash_command(*parts: str) -> dict:
    """Upstash Redis REST API로 Redis 명령을 실행합니다."""

    base_url, token = get_upstash_env()
    encoded_parts = [quote(part, safe="") for part in parts]
    url = f"{base_url}/{'/'.join(encoded_parts)}"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Upstash Redis request failed: {error}",
        ) from error

    return response.json()


def check_rate_limit(x_user_id: str = Header(default="anonymous")) -> str:
    """요청 처리 전에 사용자별 호출 횟수를 검사합니다."""

    limit = 5
    window_seconds = 60
    key = f"course:01:fastapi-rate-limit:{x_user_id}"

    count_result = upstash_command("incr", key)
    request_count = int(count_result["result"])

    if request_count == 1:
        upstash_command("expire", key, str(window_seconds))

    if request_count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"요청이 너무 많습니다. {window_seconds}초 후 다시 시도해 주세요.",
        )

    return x_user_id


@app.get("/health")
def health() -> dict[str, str | bool]:
    """서버 상태와 Upstash 환경 변수 설정 여부를 확인합니다."""

    redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
    redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

    return {
        "status": "ok",
        "redis": "upstash",
        "redis_url_configured": bool(redis_url and not is_placeholder(redis_url)),
        "redis_token_configured": bool(redis_token and not is_placeholder(redis_token)),
    }


@app.post("/ai/mock-answer")
def mock_answer(user_id: str = Depends(check_rate_limit)) -> dict[str, str | bool]:
    """Rate Limit을 통과한 경우에만 mock AI 응답을 반환합니다."""

    return {
        "user_id": user_id,
        "actual_api_called": False,
        "answer": "요청 제한을 통과했으므로 mock AI 응답 생성을 진행할 수 있습니다.",
    }
