"""Upstash Redis를 사용한 간단한 요청 횟수 제한 예제.

Rate Limit은 사용자가 짧은 시간 안에 API를 너무 많이 호출하지 못하게
제한하는 기능입니다. AI API는 비용이 발생할 수 있으므로 백엔드에서
요청 횟수를 제한하는 개념이 중요합니다.
"""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


UPSTASH_REDIS_REST_URL = os.getenv("UPSTASH_REDIS_REST_URL", "").rstrip("/")
UPSTASH_REDIS_REST_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")


def upstash_command(*parts: str) -> dict:
    """Upstash Redis REST API로 Redis 명령을 실행합니다."""

    if not UPSTASH_REDIS_REST_URL or not UPSTASH_REDIS_REST_TOKEN:
        raise RuntimeError(".env에 Upstash Redis URL과 Token을 먼저 설정해 주세요.")

    # Upstash는 Redis 명령을 REST URL 경로로 표현할 수 있습니다.
    # 예: INCR rate-limit:student01 -> /incr/rate-limit:student01
    url = f"{UPSTASH_REDIS_REST_URL}/{'/'.join(parts)}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def check_rate_limit(user_id: str, limit: int = 3, window_seconds: int = 60) -> bool:
    """사용자의 요청 횟수를 확인하고 허용 여부를 반환합니다.

    user_id별로 Redis key를 만듭니다. 예를 들어 user_id가 student01이면
    key는 `rate-limit:student01`이 됩니다.

    첫 요청이면 key가 없으므로 1로 만들고 TTL을 설정합니다.
    이후 요청은 INCR 명령으로 숫자를 1씩 증가시킵니다.
    숫자가 limit보다 커지면 요청을 거절합니다.
    """

    key = f"course:01:rate-limit:{user_id}"
    # INCR은 key의 숫자 값을 1 증가시킵니다.
    # key가 없으면 0에서 시작해 1이 됩니다.
    count_result = upstash_command("incr", key)
    request_count = int(count_result["result"])

    if request_count == 1:
        # 첫 요청일 때만 만료 시간을 설정합니다.
        # 60초가 지나면 key가 사라지고 요청 횟수가 다시 0부터 시작됩니다.
        upstash_command("expire", key, str(window_seconds))

    print(f"현재 요청 횟수: {request_count} / 제한: {limit}")
    return request_count <= limit


student_id = "student01"

if check_rate_limit(student_id):
    print("요청 허용: AI API 또는 백엔드 로직을 실행해도 됩니다.")
else:
    print("요청 제한: 잠시 후 다시 시도하도록 안내합니다.")
