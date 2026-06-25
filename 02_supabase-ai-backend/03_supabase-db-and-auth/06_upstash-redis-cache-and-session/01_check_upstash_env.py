"""Upstash Redis 환경 변수를 확인하는 예제입니다."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다."""

    if value is None:
        return False

    return value.strip().startswith(("your-", "https://your-"))


def mask_secret(value: str | None) -> str:
    """token 전체가 노출되지 않도록 일부만 보여줍니다."""

    if not value:
        return "(not set)"

    cleaned = value.strip()
    if is_placeholder(cleaned):
        return "(placeholder value)"

    if len(cleaned) <= 12:
        return "(set, but too short to verify safely)"

    return f"{cleaned[:6]}...{cleaned[-4:]}"


def main() -> None:
    """Upstash Redis 실습에 필요한 환경 변수 설정 상태를 출력합니다."""

    load_dotenv(ENV_PATH)

    redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
    redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

    url_ready = bool(redis_url and not is_placeholder(redis_url))
    token_ready = bool(redis_token and not is_placeholder(redis_token))

    print("[Upstash Redis environment check]")
    print(f".env path: {ENV_PATH}")
    print(f"UPSTASH_REDIS_REST_URL: {redis_url if url_ready else '(not ready)'}")
    print(f"UPSTASH_REDIS_REST_TOKEN: {mask_secret(redis_token)}")

    if not (url_ready and token_ready):
        print("\n[Next step]")
        print("1. Upstash Dashboard에서 Redis database를 생성합니다.")
        print("2. REST API 섹션에서 REST URL과 REST TOKEN을 복사합니다.")
        print("3. C:\\aidev\\02_supabase-ai-backend\\.env 파일에 값을 입력합니다.")
        print("4. 이 파일을 다시 실행합니다.")
        return

    print("\nResult: Upstash Redis 환경 변수가 준비되었습니다.")


if __name__ == "__main__":
    main()
