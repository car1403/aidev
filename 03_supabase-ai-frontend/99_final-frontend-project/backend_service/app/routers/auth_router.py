from fastapi import APIRouter, Depends

from app.core.security import get_bearer_token
from app.schemas.auth_schema import AuthResponse, SigninRequest, SignupRequest, UserResponse
from app.services.auth_service import get_user_by_token, signin, signout, signup


router = APIRouter(tags=["auth"])


@router.post("/auth/signup", response_model=UserResponse)
def signup_api(payload: SignupRequest) -> dict:
    return signup(payload)


@router.post("/auth/signin", response_model=AuthResponse)
def signin_api(payload: SigninRequest) -> dict:
    return signin(payload)


@router.post("/auth/signout")
def signout_api(token: str = Depends(get_bearer_token)) -> dict[str, str]:
    user = get_user_by_token(token)
    return signout(token, user)


@router.get("/me", response_model=UserResponse)
def me_api(token: str = Depends(get_bearer_token)) -> dict[str, str]:
    return get_user_by_token(token)
