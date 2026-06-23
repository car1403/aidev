"""Supabase service_logs 테이블에 성공 로그를 저장하는 예제.

실행 전 확인할 것:
1. C:\\aidev\\01_supabase-ai-backend\\.env 파일에 Supabase 값이 들어 있어야 합니다.
2. Supabase SQL Editor에서 06_supabase-db-and-auth/00_references/supabase-schema.sql을 실행해야 합니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from postgrest.exceptions import APIError
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_supabase() -> Client:
    """환경변수에서 Supabase 접속 정보를 읽어 client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError(
            "SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요."
        )

    return create_client(url, key)


def insert_service_log(
    supabase: Client,
    event_type: str,
    message: str,
    metadata: dict,
    user_id: str | None = None,
) -> dict:
    """service_logs 테이블에 로그 1개를 저장합니다."""

    # metadata는 jsonb 컬럼입니다.
    # endpoint, status_code, duration_ms처럼 상황마다 달라지는 값을 담기에 좋습니다.
    payload = {
        "user_id": user_id,
        "event_type": event_type,
        "message": message,
        "metadata": metadata,
    }

    result = supabase.table("service_logs").insert(payload).execute()

    if not result.data:
        raise RuntimeError("서비스 로그 저장 결과가 비어 있습니다.")

    return result.data[0]


def print_schema_help() -> None:
    """테이블이 없을 때 실행해야 할 SQL 파일 위치를 안내합니다."""

    print("\nservice_logs 테이블이 없다면 Supabase SQL Editor에서 아래 파일을 먼저 실행하세요.")
    print(
        r"C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql"
    )


def main() -> None:
    """성공 로그 1개를 Supabase에 저장합니다."""

    supabase = get_supabase()

    try:
        log = insert_service_log(
            supabase=supabase,
            event_type="practice.success",
            message="서비스 로그 저장 실습이 완료되었습니다.",
            metadata={
                "endpoint": "script",
                "status_code": 200,
                "duration_ms": 10,
                "source": "07_backend-service-data-management",
                "provider": "gemini",
                "model": "gemini-2.5-flash-lite",
                "actual_api_called": False,
                "llm_call_mode": "mock-first",
            },
        )
    except APIError as error:
        print("Supabase 서비스 로그 저장 중 오류가 발생했습니다.")
        print(f"오류 내용: {error}")
        print_schema_help()
        return

    print("저장된 로그:")
    print(log)


if __name__ == "__main__":
    main()
