"""Redis cache-aside 패턴을 mock 데이터로 이해하는 예제.

이 파일은 Supabase를 실제로 조회하지 않고, Supabase 조회 함수를 흉내 냅니다.
초보자는 먼저 "캐시가 있으면 Redis, 없으면 DB"라는 흐름을 이해하는 것이 중요합니다.
"""

from __future__ import annotations

from pathlib import Path
import json
import os

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

UPSTASH_REDIS_REST_URL = os.getenv("UPSTASH_REDIS_REST_URL", "").rstrip("/")
UPSTASH_REDIS_REST_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")


def upstash_command(*parts: str) -> dict:
    """Upstash Redis REST API에 명령을 보냅니다."""

    if not UPSTASH_REDIS_REST_URL or not UPSTASH_REDIS_REST_TOKEN:
        raise RuntimeError(".env에 Upstash Redis URL과 Token을 먼저 설정해 주세요.")

    url = f"{UPSTASH_REDIS_REST_URL}/{'/'.join(parts)}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_profile_from_supabase_mock(user_id: str) -> dict:
    """Supabase 조회를 흉내 내는 함수입니다."""

    # 실제 서비스에서는 이 위치에서 supabase.table("profiles").select(...).execute()를 호출합니다.
    print("Supabase에서 사용자 프로필을 조회했다고 가정합니다.")
    return {
        "user_id": user_id,
        "display_name": "수강생 A",
        "course": "01_supabase-ai-backend",
    }


def get_profile_with_cache(user_id: str) -> dict:
    """Redis 캐시를 먼저 확인하고, 없으면 Supabase에서 조회하는 흐름입니다."""

    cache_key = f"course:01:cache:profile:{user_id}"

    cached = upstash_command("get", cache_key)
    if cached.get("result"):
        print("Redis cache hit")
        return json.loads(cached["result"])

    print("Redis cache miss")
    profile = fetch_profile_from_supabase_mock(user_id)

    # 조회 결과를 Redis에 60초 동안 저장합니다.
    # 60초 안에 같은 사용자를 다시 조회하면 Supabase 조회를 생략할 수 있습니다.
    upstash_command("set", cache_key, json.dumps(profile, ensure_ascii=False), "ex", "60")
    return profile


profile = get_profile_with_cache("student01")
print(profile)
