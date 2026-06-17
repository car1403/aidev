"""Supabase profiles 테이블 CRUD 예제.

이 파일은 실제 Supabase에 데이터를 저장할 수 있습니다.
실행 전 `06_supabase-db-and-auth/00_references/supabase-schema.sql`을
Supabase SQL Editor에서 실행했는지 확인합니다.
"""

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


def upsert_profile(supabase: Client, profile_id: str, display_name: str) -> dict:
    """profiles 테이블에 사용자 프로필을 저장하거나 갱신합니다.

    upsert는 insert와 update를 합친 개념입니다.
    같은 id가 없으면 새로 만들고, 같은 id가 있으면 기존 데이터를 갱신합니다.
    """

    result = (
        supabase.table("profiles")
        .upsert(
            {
                "id": profile_id,
                "display_name": display_name,
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("profiles upsert 결과가 비어 있습니다.")

    return result.data[0]


def get_profile(supabase: Client, profile_id: str) -> dict | None:
    """id로 사용자 프로필 1개를 조회합니다."""

    result = supabase.table("profiles").select("*").eq("id", profile_id).limit(1).execute()
    if not result.data:
        return None
    return result.data[0]


def main() -> None:
    supabase = get_supabase()

    # 수업용 고정 uuid입니다. 실제 서비스에서는 로그인한 사용자의 id를 사용합니다.
    profile_id = "00000000-0000-0000-0000-000000000001"

    saved = upsert_profile(supabase, profile_id, "수강생 A")
    print("저장된 프로필:")
    print(saved)

    loaded = get_profile(supabase, profile_id)
    print("\n조회된 프로필:")
    print(loaded)


if __name__ == "__main__":
    main()
