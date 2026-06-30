"""Upstash Redis 환경변수를 읽습니다."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    redis_rest_url: str
    redis_rest_token: str


def get_settings() -> Settings:
    return Settings(
        redis_rest_url=os.getenv("UPSTASH_REDIS_REST_URL", "").strip().rstrip("/"),
        redis_rest_token=os.getenv("UPSTASH_REDIS_REST_TOKEN", "").strip(),
    )


def is_configured() -> bool:
    settings = get_settings()
    return bool(settings.redis_rest_url and settings.redis_rest_token)
