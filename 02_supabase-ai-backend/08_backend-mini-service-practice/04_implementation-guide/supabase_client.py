"""Supabase client 생성 함수.

Supabase 연결 코드를 별도 파일로 분리하면 여러 endpoint에서 재사용하기 쉽습니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_supabase() -> Client:
    """환경변수에서 Supabase URL/key를 읽고 client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요.")

    # create_client는 Python 코드에서 Supabase REST API를 쉽게 호출하게 해줍니다.
    return create_client(url, key)
