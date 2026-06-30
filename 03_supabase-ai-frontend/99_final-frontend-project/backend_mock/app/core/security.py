from uuid import uuid4

from fastapi import Header, HTTPException, status

from app.core.config import MOCK_TOKEN_PREFIX


def create_access_token() -> str:
    return f"{MOCK_TOKEN_PREFIX}_{uuid4().hex}"


def parse_bearer_token(authorization: str | None = Header(default=None)) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header가 필요합니다.",
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header는 Bearer token 형식이어야 합니다.",
        )

    return token
