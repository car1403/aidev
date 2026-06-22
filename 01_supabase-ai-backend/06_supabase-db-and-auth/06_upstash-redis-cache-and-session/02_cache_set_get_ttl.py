"""Upstash Redis에 값을 저장하고 TTL을 적용하는 예제.

Redis는 key와 value를 사용합니다.

예를 들어 `cache:greeting`이라는 key에 "안녕하세요"라는 value를
저장할 수 있습니다. TTL을 30초로 설정하면 30초 뒤에 값이 사라집니다.
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
    """Upstash Redis REST API에 Redis 명령을 보냅니다.

    Upstash REST API는 URL 경로에 Redis 명령을 적는 방식으로 사용할 수 있습니다.
    예를 들어 SET cache:greeting hello EX 30 명령은 아래 주소로 호출됩니다.

    /set/cache:greeting/hello/ex/30
    """

    if not UPSTASH_REDIS_REST_URL or not UPSTASH_REDIS_REST_TOKEN:
        raise RuntimeError(".env에 Upstash Redis URL과 Token을 먼저 설정해 주세요.")

    # parts로 받은 Redis 명령 조각을 URL 경로로 조립합니다.
    # 예: ("get", "course:01:greeting") -> /get/course:01:greeting
    url = f"{UPSTASH_REDIS_REST_URL}/{'/'.join(parts)}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}

    # Upstash REST API는 HTTP 요청으로 Redis 명령을 실행합니다.
    # Docker Redis client를 직접 연결하지 않아도 되므로 초보 실습에 적합합니다.
    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


# 수업용 key에는 과정 이름을 앞에 붙여 다른 실습 데이터와 섞이지 않게 합니다.
cache_key = "course:01:greeting"
cache_value = "hello-upstash-redis"
ttl_seconds = "30"


print("Redis SET 명령 실행")
# SET key value EX seconds는 값을 저장하면서 TTL을 함께 설정하는 명령입니다.
set_result = upstash_command("set", cache_key, cache_value, "ex", ttl_seconds)
print(set_result)

print("\nRedis GET 명령 실행")
# GET key는 key에 저장된 값을 조회합니다.
get_result = upstash_command("get", cache_key)
print(get_result)

print("\nRedis TTL 명령 실행")
# TTL key는 key가 몇 초 뒤에 사라지는지 확인합니다.
ttl_result = upstash_command("ttl", cache_key)
print(ttl_result)

print("\n30초가 지나면 이 key는 자동으로 사라집니다.")
