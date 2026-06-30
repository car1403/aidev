"""RLS가 적용된 `ex90_profiles`를 REST API로 호출합니다."""

from __future__ import annotations

import httpx
from fastapi import HTTPException

from app.core.config import get_settings
from app.schemas.profile_schema import ProfilePublic, ProfileUpdate


TABLE_NAME = "ex90_profiles"


def auth_headers(access_token: str | None) -> dict[str, str]:
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_anon_key or not access_token:
        raise HTTPException(status_code=500, detail="Supabase 환경변수 또는 token을 확인하세요.")

    return {
        "apikey": settings.supabase_anon_key,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def table_url() -> str:
    return f"{get_settings().supabase_url}/rest/v1/{TABLE_NAME}"


def to_profile(row: dict) -> ProfilePublic:
    return ProfilePublic(
        id=str(row["id"]),
        display_name=row["display_name"],
        created_at=row.get("created_at"),
        updated_at=row.get("updated_at"),
    )


def get_profile(access_token: str | None) -> ProfilePublic:
    try:
        response = httpx.get(
            table_url(),
            headers=auth_headers(access_token),
            params={"select": "*"},
            timeout=10,
        )
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"profile 조회 실패: {error}") from error

    data = response.json()
    if not data:
        raise HTTPException(status_code=404, detail="profile이 없습니다. PUT /profile을 먼저 실행하세요.")
    return to_profile(data[0])


def upsert_profile(
    user_id: str,
    access_token: str | None,
    request: ProfileUpdate,
) -> ProfilePublic:
    payload = {"id": user_id, "display_name": request.display_name}
    try:
        response = httpx.post(
            f"{table_url()}?on_conflict=id",
            headers=auth_headers(access_token),
            json=payload,
            timeout=10,
        )
        response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail=f"profile 저장 실패: {error}") from error

    return to_profile(response.json()[0])
