"""FastAPI endpoint에 Upstash Redis 기반 Rate Limit을 적용하는 예제.

이 예제는 AI API 비용을 보호하는 백엔드 패턴을 보여줍니다.
실제 서비스에서는 사용자 id를 로그인 정보에서 가져오지만,
초보 실습에서는 `x-user-id` 헤더로 간단히 전달합니다.
"""

from __future__ import annotations

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

UPSTASH_REDIS_REST_URL = os.getenv("UPSTASH_REDIS_REST_URL", "").rstrip("/")
UPSTASH_REDIS_REST_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")

app = FastAPI(title="FastAPI Upstash Rate Limit Practice")


def upstash_command(*parts: str) -> dict:
    """Upstash Redis REST API로 Redis 명령을 실행합니다."""

    if not UPSTASH_REDIS_REST_URL or not UPSTASH_REDIS_REST_TOKEN:
        raise HTTPException(status_code=500, detail="Upstash Redis environment values are missing.")

    url = f"{UPSTASH_REDIS_REST_URL}/{'/'.join(parts)}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def check_rate_limit(x_user_id: str = Header(default="anonymous")) -> str:
    """요청을 처리하기 전에 사용자별 호출 횟수를 검사합니다."""

    # 수업에서는 60초 동안 5번만 허용합니다.
    # AI API 호출 전 이 검사를 통과해야 비용이 발생하는 작업을 실행합니다.
    limit = 5
    window_seconds = 60
    key = f"course:01:fastapi-rate-limit:{x_user_id}"

    count_result = upstash_command("incr", key)
    request_count = int(count_result["result"])

    if request_count == 1:
        upstash_command("expire", key, str(window_seconds))

    if request_count > limit:
        raise HTTPException(
            status_code=429,
            detail=f"요청이 너무 많습니다. {window_seconds}초 뒤에 다시 시도해 주세요.",
        )

    return x_user_id


@app.get("/health")
def health() -> dict[str, str]:
    """서버 상태 확인용 endpoint입니다."""

    return {"status": "ok"}


@app.post("/ai/mock-answer")
def mock_answer(user_id: str = Depends(check_rate_limit)) -> dict[str, str]:
    """Rate Limit을 통과한 경우에만 AI 응답 생성을 실행합니다."""

    return {
        "user_id": user_id,
        "answer": "요청 제한을 통과했으므로 AI 응답 생성을 진행할 수 있습니다.",
    }
