from fastapi import Header, HTTPException


def get_bearer_token(authorization: str | None = Header(default=None)) -> str:
    """Authorization: Bearer <token> header에서 token만 꺼냅니다."""

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header가 없습니다.")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Bearer token 형식이 아닙니다.")

    return token
