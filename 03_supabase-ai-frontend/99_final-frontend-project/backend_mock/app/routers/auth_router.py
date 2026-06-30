from fastapi import APIRouter, Depends

from app.core.security import parse_bearer_token
from app.schemas.auth_schema import (
    AuthResponse,
    MessageResponse,
    SigninRequest,
    SignupRequest,
    UserResponse,
)
from app.services.auth_service import get_user_by_token, signin, signout, signup


router = APIRouter(tags=["auth"])


@router.post("/auth/signup", response_model=UserResponse)
def signup_endpoint(payload: SignupRequest) -> dict:
    return signup(payload)


@router.post("/auth/signin", response_model=AuthResponse)
def signin_endpoint(payload: SigninRequest) -> dict:
    return signin(payload)


@router.post("/auth/signout", response_model=MessageResponse)
def signout_endpoint(token: str = Depends(parse_bearer_token)) -> dict:
    return signout(token)


@router.get("/me", response_model=UserResponse)
def me_endpoint(token: str = Depends(parse_bearer_token)) -> dict:
    return get_user_by_token(token)
