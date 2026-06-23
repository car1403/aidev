"""Supabase profiles 테이블 CRUD 예제.

이 파일은 실제 Supabase에 프로필 데이터를 저장하고 다시 조회합니다.

실행 전 확인할 것:
1. C:\\aidev\\01_supabase-ai-backend\\.env 파일에 Supabase 값이 들어 있어야 합니다.
2. Supabase SQL Editor에서 06_supabase-db-and-auth/00_references/supabase-schema.sql을 실행해야 합니다.
3. preferred_language, course_level까지 저장하려면 README의 alter table SQL도 실행해야 합니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from postgrest.exceptions import APIError
from supabase import Client, create_client


# 현재 파일 위치:
# C:\aidev\01_supabase-ai-backend\07_backend-service-data-management\01_user-profile-data\02_profile_crud_supabase.py
# parents[2]는 C:\aidev\01_supabase-ai-backend 폴더입니다.
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


def upsert_profile(
    supabase: Client,
    profile_id: str,
    display_name: str,
    preferred_language: str = "ko",
    course_level: str = "beginner",
) -> dict:
    """profiles 테이블에 사용자 프로필을 저장하거나 갱신합니다.

    upsert는 insert와 update를 합친 개념입니다.
    같은 id가 없으면 새로 만들고, 같은 id가 있으면 기존 데이터를 갱신합니다.
    """

    profile_payload = {
        "id": profile_id,
        "display_name": display_name,
        "preferred_language": preferred_language,
        "course_level": course_level,
    }

    result = supabase.table("profiles").upsert(profile_payload).execute()

    if not result.data:
        raise RuntimeError("profiles upsert 결과가 비어 있습니다.")

    return result.data[0]


def get_profile(supabase: Client, profile_id: str) -> dict | None:
    """id로 사용자 프로필 1개를 조회합니다."""

    result = supabase.table("profiles").select("*").eq("id", profile_id).limit(1).execute()

    if not result.data:
        return None

    return result.data[0]


def print_table_column_help() -> None:
    """profiles 테이블 컬럼이 부족할 때 실행할 SQL을 안내합니다."""

    print("\nprofiles 테이블에 확장 컬럼이 없다면 Supabase SQL Editor에서 아래 SQL을 실행하세요.")
    print(
        """
alter table profiles
add column if not exists preferred_language text not null default 'ko';

alter table profiles
add column if not exists course_level text not null default 'beginner';
""".strip()
    )


def main() -> None:
    """프로필 저장과 조회 흐름을 실행합니다."""

    supabase = get_supabase()

    # 학습용 고정 UUID입니다.
    # 실제 서비스에서는 로그인한 사용자의 Supabase Auth user id를 사용합니다.
    profile_id = "00000000-0000-0000-0000-000000000001"

    try:
        saved = upsert_profile(
            supabase=supabase,
            profile_id=profile_id,
            display_name="수강생 A",
            preferred_language="ko",
            course_level="beginner",
        )
    except APIError as error:
        print("Supabase profiles 저장 중 오류가 발생했습니다.")
        print(f"오류 내용: {error}")
        print_table_column_help()
        return

    print("저장된 프로필:")
    print(saved)

    loaded = get_profile(supabase, profile_id)
    print("\n조회한 프로필:")
    print(loaded)


if __name__ == "__main__":
    main()
