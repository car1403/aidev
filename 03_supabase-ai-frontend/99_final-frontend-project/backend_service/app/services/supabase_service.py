from fastapi import HTTPException

from app.core.config import (
    SUPABASE_ANON_KEY,
    SUPABASE_SERVICE_ROLE_KEY,
    SUPABASE_URL,
)


def _require_supabase_package():
    try:
        from supabase import create_client
    except ImportError as exc:
        raise HTTPException(
            status_code=500,
            detail="supabase 패키지가 설치되어 있지 않습니다. pip install -r requirements.txt를 실행하세요.",
        ) from exc

    return create_client


def get_auth_client():
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        raise HTTPException(
            status_code=500,
            detail="SUPABASE_URL 또는 SUPABASE_ANON_KEY가 설정되어 있지 않습니다.",
        )

    create_client = _require_supabase_package()
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


def get_service_client():
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise HTTPException(
            status_code=500,
            detail="SUPABASE_URL 또는 SUPABASE_SERVICE_ROLE_KEY가 설정되어 있지 않습니다.",
        )

    create_client = _require_supabase_package()
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


def normalize_user(user) -> dict[str, str]:
    metadata = getattr(user, "user_metadata", None) or {}
    return {
        "id": str(user.id),
        "email": user.email,
        "display_name": metadata.get("display_name") or user.email,
    }
