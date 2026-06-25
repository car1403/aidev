"""Upstash Redis에 값을 저장하고 TTL을 확인하는 예제입니다."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다."""

    if value is None:
        return False

    return value.strip().startswith(("your-", "https://your-"))


def get_upstash_env() -> tuple[str, str]:
    """Upstash Redis REST URL과 token을 읽습니다."""

    load_dotenv(ENV_PATH)

    url = os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/")
    token = os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip()

    if not url or not token or is_placeholder(url) or is_placeholder(token):
        raise RuntimeError("Upstash Redis 환경 변수가 준비되지 않았습니다. 01_check_upstash_env.py를 먼저 실행하세요.")

    return url, token


def upstash_command(*parts: str) -> dict:
    """Upstash Redis REST API로 Redis 명령을 실행합니다."""

    base_url, token = get_upstash_env()

    # Redis 명령 조각을 URL 경로에 넣기 위해 안전하게 인코딩합니다.
    # 공백, 한글, JSON 문자열이 포함되어도 URL이 깨지지 않게 하기 위한 처리입니다.
    encoded_parts = [quote(part, safe="") for part in parts]
    url = f"{base_url}/{'/'.join(encoded_parts)}"
    headers = {"Authorization": f"Bearer {token}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """SET, GET, TTL 명령을 차례대로 실행합니다."""

    cache_key = "course:01:greeting"
    cache_value = "hello-upstash-redis"
    ttl_seconds = "30"

    try:
        print("[Redis SET]")
        print(upstash_command("set", cache_key, cache_value, "ex", ttl_seconds))

        print("\n[Redis GET]")
        print(upstash_command("get", cache_key))

        print("\n[Redis TTL]")
        print(upstash_command("ttl", cache_key))

        print("\nResult: 30초가 지나면 이 key는 자동으로 사라집니다.")
    except (RuntimeError, httpx.HTTPError) as error:
        print("[Upstash Redis 실행 오류]")
        print(error)
        print("\n.env의 UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN을 확인하세요.")


if __name__ == "__main__":
    main()
