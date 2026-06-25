"""오류가 발생했을 때 서비스 로그를 남기는 예제.

실제 서비스에서는 오류가 생겨도 조용히 실패하면 안 됩니다.
어떤 기능에서 어떤 오류가 발생했는지 기록해야 나중에 원인을 찾을 수 있습니다.
"""

from __future__ import annotations

import os
from pathlib import Path
import traceback

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


def save_error_log(supabase: Client, error: Exception) -> dict:
    """예외 정보를 service_logs 테이블에 저장합니다."""

    # traceback은 개발자가 오류 위치를 찾을 때 유용합니다.
    # 실제 운영 서비스에서는 민감한 정보가 포함되지 않도록 로그 정책을 정해야 합니다.
    metadata = {
        "endpoint": "script",
        "status_code": 500,
        "error_type": type(error).__name__,
        "traceback": traceback.format_exc(limit=3),
        "retryable": False,
    }

    payload = {
        "event_type": "practice.error",
        "message": str(error),
        "metadata": metadata,
    }

    result = supabase.table("service_logs").insert(payload).execute()

    if not result.data:
        raise RuntimeError("오류 로그 저장 결과가 비어 있습니다.")

    return result.data[0]


def risky_operation() -> None:
    """일부러 오류를 발생시키는 함수입니다."""

    raise ValueError("실습용으로 발생시킨 예외입니다.")


def print_schema_help() -> None:
    """테이블이 없을 때 실행해야 할 SQL 파일 위치를 안내합니다."""

    print("\nservice_logs 테이블이 없다면 Supabase SQL Editor에서 아래 파일을 먼저 실행하세요.")
    print(
        r"C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql"
    )


def main() -> None:
    """오류를 일부러 발생시키고 오류 로그를 저장합니다."""

    supabase = get_supabase()

    try:
        risky_operation()
    except Exception as error:
        try:
            log = save_error_log(supabase, error)
        except APIError as api_error:
            print("Supabase 오류 로그 저장 중 오류가 발생했습니다.")
            print(f"오류 내용: {api_error}")
            print_schema_help()
            return

        print("오류 로그를 저장했습니다.")
        print(log)


if __name__ == "__main__":
    main()
