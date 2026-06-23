"""Redis cache-aside 패턴을 mock 데이터로 이해하는 예제입니다."""

from __future__ import annotations

import json
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
    encoded_parts = [quote(part, safe="") for part in parts]
    url = f"{base_url}/{'/'.join(encoded_parts)}"
    headers = {"Authorization": f"Bearer {token}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_profile_from_supabase_mock(user_id: str) -> dict:
    """Supabase 조회를 흉내 내는 함수입니다."""

    print("Supabase에서 사용자 프로필을 조회한다고 가정합니다.")
    return {
        "user_id": user_id,
        "display_name": "사용자 A",
        "course": "01_supabase-ai-backend",
    }


def get_profile_with_cache(user_id: str) -> dict:
    """Redis 캐시를 먼저 확인하고, 없으면 Supabase 조회 결과를 저장합니다."""

    cache_key = f"course:01:cache:profile:{user_id}"

    cached = upstash_command("get", cache_key)
    if cached.get("result"):
        print("Redis cache hit")
        return json.loads(cached["result"])

    print("Redis cache miss")
    profile = fetch_profile_from_supabase_mock(user_id)

    # 조회 결과를 60초 동안 Redis에 저장합니다.
    upstash_command("set", cache_key, json.dumps(profile, ensure_ascii=False), "ex", "60")
    return profile


def main() -> None:
    """cache-aside 흐름을 실행합니다."""

    try:
        profile = get_profile_with_cache("student01")
        print(profile)
    except (RuntimeError, httpx.HTTPError) as error:
        print("[Upstash Redis 실행 오류]")
        print(error)
        print("\n.env의 UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN을 확인하세요.")


if __name__ == "__main__":
    main()
