"""Upstash Redis에 임시 세션 상태를 저장하는 예제.

Supabase는 오래 보관할 사용자 정보와 대화 이력을 저장합니다.
Redis는 "잠깐만 필요한 상태"를 저장하기 좋습니다.

예:
- 사용자가 현재 어떤 단계의 질문을 보고 있는지
- AI 응답 생성 중인지 여부
- 짧은 시간 동안 유지할 임시 설정
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
    """Upstash Redis REST API로 Redis 명령을 실행합니다."""

    if not UPSTASH_REDIS_REST_URL or not UPSTASH_REDIS_REST_TOKEN:
        raise RuntimeError(".env에 Upstash Redis URL과 Token을 먼저 설정해 주세요.")

    url = f"{UPSTASH_REDIS_REST_URL}/{'/'.join(parts)}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}

    response = httpx.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


student_id = "student01"
session_key = f"course:01:session:{student_id}"

# Redis value는 문자열로 저장하는 것이 가장 단순합니다.
# 여러 필드를 저장하고 싶으면 dict를 JSON 문자열로 바꾸어 저장합니다.
session_state = {
    "current_step": "supabase-db-auth",
    "last_action": "opened-redis-practice",
    "is_generating_answer": False,
}

session_value = json.dumps(session_state, ensure_ascii=False)
ttl_seconds = "300"

print("세션 상태 저장")
print(upstash_command("set", session_key, session_value, "ex", ttl_seconds))

print("\n세션 상태 조회")
stored = upstash_command("get", session_key)
print(stored)

if stored.get("result"):
    # Redis에서 꺼낸 문자열을 다시 dict로 복원합니다.
    restored = json.loads(stored["result"])
    print("\n복원된 Python dict:")
    print(restored)

print("\nTTL 확인")
print(upstash_command("ttl", session_key))
