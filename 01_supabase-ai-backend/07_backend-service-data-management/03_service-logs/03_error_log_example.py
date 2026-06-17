"""오류가 발생했을 때 서비스 로그를 남기는 예제.

실제 서비스에서는 오류가 나더라도 조용히 실패하면 안 됩니다.
어떤 endpoint에서 어떤 오류가 발생했는지 기록해야 나중에 원인을 찾을 수 있습니다.
"""

from __future__ import annotations

import os
from pathlib import Path
import traceback

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


def save_error_log(supabase: Client, error: Exception) -> dict:
    """예외 정보를 service_logs 테이블에 저장합니다."""

    # traceback은 개발자가 오류 위치를 찾을 때 유용합니다.
    # 운영 서비스에서는 민감 정보가 포함되지 않도록 로그 정책을 정해야 합니다.
    metadata = {
        "error_type": type(error).__name__,
        "traceback": traceback.format_exc(limit=3),
    }

    result = (
        supabase.table("service_logs")
        .insert(
            {
                "event_type": "practice.error",
                "message": str(error),
                "metadata": metadata,
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("오류 로그 저장 결과가 비어 있습니다.")

    return result.data[0]


def risky_operation() -> None:
    """일부러 오류를 발생시키는 함수입니다."""

    raise ValueError("수업용으로 발생시킨 예외입니다.")


def main() -> None:
    supabase = get_supabase()

    try:
        risky_operation()
    except Exception as error:
        log = save_error_log(supabase, error)
        print("오류 로그를 저장했습니다:")
        print(log)


if __name__ == "__main__":
    main()
