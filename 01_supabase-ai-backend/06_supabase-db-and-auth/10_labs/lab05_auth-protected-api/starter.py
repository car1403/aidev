"""Lab 05 - 인증 보호 API starter.

이 파일은 실제 Supabase Auth를 호출하지 않고, 보호된 API의 구조를 먼저 연습합니다.
초보자는 "토큰이 없으면 401", "토큰이 있으면 사용자 정보를 반환"하는 흐름부터
이해한 뒤 Supabase Auth JWT 검증으로 확장하면 됩니다.
"""

from fastapi import Depends, FastAPI, Header, HTTPException


app = FastAPI(title="Auth Protected API Lab")


def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    """Authorization 헤더에서 사용자 정보를 확인하는 연습용 함수입니다.

    실제 서비스에서는 여기서 Supabase JWT를 검증해야 합니다.
    지금은 수업용으로 `Bearer demo-token`만 허용합니다.
    """

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
    """서버 상태 확인용 endpoint입니다."""

    return {"status": "ok"}


@app.get("/me")
def me(user: dict = Depends(get_current_user)) -> dict:
    """토큰이 있는 사용자만 접근할 수 있는 보호 endpoint입니다.

    Depends(get_current_user)는 /me 함수가 실행되기 전에 get_current_user를 먼저 실행합니다.
    get_current_user에서 401 오류가 발생하면 /me 본문은 실행되지 않습니다.
    """

    return {"user": user}
