"""Upstash Redis에 임시 세션 상태를 저장하는 예제입니다."""

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


def main() -> None:
    """사용자별 임시 상태를 JSON 문자열로 저장하고 다시 읽습니다."""

    student_id = "student01"
    session_key = f"course:01:session:{student_id}"
    ttl_seconds = "300"

    session_state = {
        "current_step": "supabase-db-auth",
        "last_action": "opened-redis-practice",
        "is_generating_answer": False,
    }

    session_value = json.dumps(session_state, ensure_ascii=False)

    try:
        print("[session SET]")
        print(upstash_command("set", session_key, session_value, "ex", ttl_seconds))

        print("\n[session GET]")
        stored = upstash_command("get", session_key)
        print(stored)

        if stored.get("result"):
            restored = json.loads(stored["result"])
            print("\n[restored Python dict]")
            print(restored)

        print("\n[session TTL]")
        print(upstash_command("ttl", session_key))
    except (RuntimeError, httpx.HTTPError) as error:
        print("[Upstash Redis 실행 오류]")
        print(error)
        print("\n.env의 UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN을 확인하세요.")


if __name__ == "__main__":
    main()
