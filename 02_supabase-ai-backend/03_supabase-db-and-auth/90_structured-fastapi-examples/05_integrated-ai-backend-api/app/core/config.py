"""통합 예제의 환경변수 설정입니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str
    redis_rest_url: str
    redis_rest_token: str
    use_gemini: bool
    gemini_api_key: str
    gemini_model: str


def parse_bool(value: str | None) -> bool:
    """환경변수 문자열을 bool 값으로 변환합니다."""

    return (value or "").strip().lower() in {"1", "true", "yes", "y"}


def get_settings() -> Settings:
    return Settings(
        supabase_url=os.getenv("SUPABASE_URL", "").strip().rstrip("/"),
        supabase_anon_key=os.getenv("SUPABASE_ANON_KEY", "").strip(),
        supabase_service_role_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip(),
        redis_rest_url=os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/"),
        redis_rest_token=os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip(),
        use_gemini=parse_bool(os.getenv("USE_GEMINI")),
        gemini_api_key=os.getenv("GEMINI_API_KEY", "").strip(),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite").strip(),
    )


def config_status() -> dict[str, bool]:
    settings = get_settings()
    return {
        "supabase_url": bool(settings.supabase_url),
        "supabase_anon_key": bool(settings.supabase_anon_key),
        "supabase_service_role_key": bool(settings.supabase_service_role_key),
        "redis_rest_url": bool(settings.redis_rest_url),
        "redis_rest_token": bool(settings.redis_rest_token),
        "use_gemini": settings.use_gemini,
        "gemini_api_key": bool(settings.gemini_api_key),
    }
