"""Lab 05 starter - 인증이 필요한 API 만들기.

이 starter는 FastAPI의 Depends와 Header를 사용해 보호 API 흐름을 연습합니다.
TODO 부분을 채운 뒤 solution.py와 비교합니다.
"""

from __future__ import annotations

from fastapi import Depends, FastAPI, Header, HTTPException


app = FastAPI(title="Auth and RLS Policy Check Starter")


def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    """Authorization 헤더에서 현재 사용자 정보를 확인합니다."""

    # TODO: authorization 값이 없으면 401 오류를 발생시킵니다.
    # TODO: authorization 값이 "Bearer demo-token"이 아니면 401 오류를 발생시킵니다.
    # TODO: 인증에 성공하면 사용자 dict를 반환합니다.
    return {}


@app.get("/health")
def health() -> dict[str, str]:
    """서버가 실행 중인지 확인합니다."""

    return {"status": "ok"}


@app.get("/me")
def me(user: dict = Depends(get_current_user)) -> dict:
    """인증된 사용자만 접근할 수 있는 endpoint입니다."""

    return {"user": user}
