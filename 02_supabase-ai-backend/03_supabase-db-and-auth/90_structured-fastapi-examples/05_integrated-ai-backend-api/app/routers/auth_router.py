"""Auth와 상태 확인 API입니다."""

from fastapi import APIRouter

from app.core.config import config_status
from app.schemas.auth_schema import AuthRequest, AuthResponse, UserPublic
from app.services import auth_service


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | dict[str, bool]]:
    return {"status": "ok", "configured": config_status()}


@router.post("/auth/signup", response_model=UserPublic)
def signup(request: AuthRequest) -> UserPublic:
    return auth_service.signup(request)


@router.post("/auth/signin", response_model=AuthResponse)
def signin(request: AuthRequest) -> AuthResponse:
    return auth_service.signin(request)


@router.get("/me", response_model=UserPublic)
def me(user: auth_service.CurrentUser) -> UserPublic:
    return user
