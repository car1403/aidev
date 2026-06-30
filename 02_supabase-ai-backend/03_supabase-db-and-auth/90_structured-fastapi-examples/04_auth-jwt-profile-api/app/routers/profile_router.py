"""Profile 관련 API 경로입니다."""

from fastapi import APIRouter

from app.schemas.auth_schema import UserPublic
from app.schemas.profile_schema import ProfilePublic, ProfileUpdate
from app.services import auth_service, profile_service


router = APIRouter(prefix="/profile")


@router.get("", response_model=ProfilePublic)
def get_profile(user: auth_service.CurrentUser) -> ProfilePublic:
    return profile_service.get_profile(user.access_token)


@router.put("", response_model=ProfilePublic)
def upsert_profile(
    request: ProfileUpdate,
    user: auth_service.CurrentUser,
) -> ProfilePublic:
    return profile_service.upsert_profile(user.id, user.access_token, request)
