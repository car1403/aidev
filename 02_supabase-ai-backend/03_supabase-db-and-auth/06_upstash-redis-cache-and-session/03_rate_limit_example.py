"""Upstash Redis로 간단한 요청 횟수 제한을 구현하는 예제입니다."""

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
    encoded_parts = [quote(part, safe="") for part in parts]
    url = f"{base_url}/{'/'.join(encoded_parts)}"
    headers = {"Authorization": f"Bearer {token}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def check_rate_limit(user_id: str, limit: int = 3, window_seconds: int = 60) -> bool:
    """사용자별 요청 횟수를 확인하고 허용 여부를 반환합니다."""

    key = f"course:01:rate-limit:{user_id}"

    # INCR는 숫자를 1 증가시킵니다.
    # key가 없으면 Redis가 0에서 시작해 1로 만듭니다.
    count_result = upstash_command("incr", key)
    request_count = int(count_result["result"])

    # 첫 요청일 때만 만료 시간을 설정합니다.
    if request_count == 1:
        upstash_command("expire", key, str(window_seconds))

    print(f"현재 요청 횟수: {request_count} / 제한: {limit}")
    return request_count <= limit


def main() -> None:
    """같은 사용자가 API를 호출할 때 rate limit이 어떻게 동작하는지 확인합니다."""

    student_id = "student01"

    try:
        if check_rate_limit(student_id):
            print("요청 허용: AI API 또는 백엔드 로직을 실행해도 됩니다.")
        else:
            print("요청 제한: 잠시 후 다시 시도하도록 안내합니다.")
    except (RuntimeError, httpx.HTTPError) as error:
        print("[Upstash Redis 실행 오류]")
        print(error)
        print("\n.env의 UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN을 확인하세요.")


if __name__ == "__main__":
    main()
