from pathlib import Path
import os

from dotenv import load_dotenv


BACKEND_ROOT = Path(__file__).resolve().parents[2]
COURSE_ROOT = Path(__file__).resolve().parents[4]

load_dotenv(COURSE_ROOT / ".env")
load_dotenv(BACKEND_ROOT / ".env")

APP_NAME = "04 Mini Project Final Starter Backend"
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
REDIS_URL = os.getenv("REDIS_URL", "").strip()

raw_origins = os.getenv(
    "CORS_ALLOW_ORIGINS",
    "http://localhost:8501,http://127.0.0.1:8501",
)
CORS_ALLOW_ORIGINS = [item.strip() for item in raw_origins.split(",") if item.strip()]

REDIS_CHANNEL = "mini-project:service-logs"


def is_real_value(value: str) -> bool:
    """환경변수가 비어 있지 않고 `.env.example`의 예시 값도 아닌지 확인합니다."""

    return bool(value) and not value.startswith(("your-", "https://your-"))


def is_supabase_configured() -> bool:
    """Supabase URL과 service role key가 모두 실제 값인지 확인합니다."""

    return is_real_value(SUPABASE_URL) and is_real_value(SUPABASE_SERVICE_ROLE_KEY)


def is_redis_configured() -> bool:
    """Redis URL이 실제 값으로 설정되었는지 확인합니다."""

    return is_real_value(REDIS_URL)
