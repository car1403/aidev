"""Lab 05 solution - 인증이 필요한 API 만들기.

실제 Supabase Auth를 붙이기 전, 보호 API가 어떤 순서로 동작하는지 확인합니다.

흐름:
1. 클라이언트가 Authorization 헤더를 보냅니다.
2. FastAPI가 endpoint 실행 전에 get_current_user 함수를 먼저 실행합니다.
3. 토큰이 없거나 틀리면 endpoint 본문은 실행되지 않고 401 오류가 반환됩니다.
4. 토큰이 맞으면 사용자 정보가 endpoint로 전달됩니다.
"""

from __future__ import annotations

from fastapi import Depends, FastAPI, Header, HTTPException


app = FastAPI(title="Auth and RLS Policy Check Lab")


def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    """Authorization 헤더를 확인해서 현재 사용자 정보를 반환합니다."""

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization 헤더가 필요합니다.")

    if authorization != "Bearer demo-token":
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")

    return {
        "id": "student01",
        "email": "student@example.com",
        "role": "authenticated",
    }


@app.get("/health")
def health() -> dict[str, str]:
    """서버가 실행 중인지 확인하는 공개 endpoint입니다."""

    return {"status": "ok"}


@app.get("/me")
def me(user: dict = Depends(get_current_user)) -> dict:
    """인증된 사용자만 접근할 수 있는 보호 endpoint입니다."""

    return {"user": user}
