"""Supabase Auth와 Bearer token 확인입니다."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, Header, HTTPException, status

from app.core.config import get_settings
from app.schemas.auth_schema import AuthRequest, AuthResponse, UserPublic


def get_supabase_client():
    from supabase import create_client

    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        raise HTTPException(status_code=500, detail="Supabase 환경변수를 확인하세요.")
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def signup(request: AuthRequest) -> UserPublic:
    try:
        response = get_supabase_client().auth.sign_up(
            {"email": request.email, "password": request.password}
        )
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"sign up 실패: {error}") from error
    if response.user is None:
        raise HTTPException(status_code=400, detail="user가 없는 signup 응답입니다.")
    return UserPublic(id=response.user.id, email=response.user.email)


def signin(request: AuthRequest) -> AuthResponse:
    try:
        response = get_supabase_client().auth.sign_in_with_password(
            {"email": request.email, "password": request.password}
        )
    except Exception as error:
        raise HTTPException(status_code=401, detail=f"sign in 실패: {error}") from error
    if response.user is None or response.session is None:
        raise HTTPException(status_code=401, detail="로그인 응답에 user/session이 없습니다.")
    user = UserPublic(
        id=response.user.id,
        email=response.user.email,
        access_token=response.session.access_token,
    )
    return AuthResponse(user=user, access_token=response.session.access_token)


def get_current_user(authorization: str | None = Header(default=None)) -> UserPublic:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization: Bearer <access_token> 헤더가 필요합니다.",
        )
    token = authorization.removeprefix("Bearer ").strip()
    try:
        response = get_supabase_client().auth.get_user(token)
    except Exception as error:
        raise HTTPException(status_code=401, detail=f"token 확인 실패: {error}") from error
    if response.user is None:
        raise HTTPException(status_code=401, detail="유효하지 않은 token입니다.")
    return UserPublic(id=response.user.id, email=response.user.email, access_token=token)


CurrentUser = Annotated[UserPublic, Depends(get_current_user)]
