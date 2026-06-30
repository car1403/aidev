"""환경변수를 읽는 작은 설정 모듈입니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """Supabase 접속에 필요한 설정입니다."""

    supabase_url: str
    supabase_service_role_key: str


def get_settings() -> Settings:
    """현재 예제 폴더의 `.env` 값을 읽어 Settings로 반환합니다."""

    return Settings(
        supabase_url=os.getenv("SUPABASE_URL", "").strip().rstrip("/"),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip(),
    )


def is_configured() -> bool:
    """필수 환경변수가 준비되었는지 확인합니다."""

    settings = get_settings()
    return bool(settings.supabase_url and settings.supabase_service_role_key)
