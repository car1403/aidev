from pathlib import Path
import os

from dotenv import load_dotenv


BACKEND_ROOT = Path(__file__).resolve().parents[2]
COURSE_ROOT = Path(__file__).resolve().parents[4]

load_dotenv(COURSE_ROOT / ".env")
load_dotenv(BACKEND_ROOT / ".env")

APP_NAME = "04 Mini Project Realtime Log Backend"
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
REDIS_URL = os.getenv("REDIS_URL", "")

raw_origins = os.getenv(
    "CORS_ALLOW_ORIGINS",
    "http://localhost:8501,http://127.0.0.1:8501",
)
CORS_ALLOW_ORIGINS = [item.strip() for item in raw_origins.split(",") if item.strip()]

REDIS_CHANNEL = "mini-project:service-logs"
