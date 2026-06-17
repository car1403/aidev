"""Supabase service_logs 테이블에 로그를 저장하는 예제."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_supabase() -> Client:
    """Supabase client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요.")

    return create_client(url, key)


def insert_service_log(supabase: Client, event_type: str, message: str, metadata: dict) -> dict:
    """service_logs 테이블에 로그 1개를 저장합니다."""

    # metadata는 jsonb 컬럼입니다.
    # endpoint, status_code, duration_ms처럼 구조가 조금씩 달라질 수 있는 값을 담기 좋습니다.
    result = (
        supabase.table("service_logs")
        .insert(
            {
                "event_type": event_type,
                "message": message,
                "metadata": metadata,
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("서비스 로그 저장 결과가 비어 있습니다.")

    return result.data[0]


def main() -> None:
    supabase = get_supabase()

    log = insert_service_log(
        supabase,
        event_type="practice.success",
        message="서비스 로그 저장 실습이 완료되었습니다.",
        metadata={
            "endpoint": "script",
            "status_code": 200,
            "duration_ms": 10,
        },
    )

    print("저장된 로그:")
    print(log)


if __name__ == "__main__":
    main()
