r"""FastAPI에서 Supabase Auth를 호출하는 최소 예제입니다.

이 예제는 Swagger UI에서 회원가입, 로그인, 현재 사용자 확인 흐름을 확인합니다.

실행 전 준비:
    C:\aidev\02_supabase-ai-backend\.env 파일에
    SUPABASE_URL, SUPABASE_ANON_KEY 값을 입력합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\04_supabase-auth-and-rls
    ..\..\.venv\Scripts\Activate.ps1
    uvicorn 01_fastapi_supabase_auth:app --reload --host 127.0.0.1 --port 8002

Swagger 확인:
    http://127.0.0.1:8002/docs
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field
from supabase import create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"

# HTTPBearer를 사용하면 Swagger UI 오른쪽 위에 Authorize 버튼이 생깁니다.
# 수강생은 /auth/signin에서 받은 access_token을 Authorize에 붙여 넣고 /me를 호출할 수 있습니다.
bearer_security = HTTPBearer(auto_error=False)

app = FastAPI(
    title="Supabase Auth FastAPI Example",
    description="Supabase Auth sign up/sign in과 Bearer token 확인 흐름을 Swagger에서 실습합니다.",
)


class AuthRequest(BaseModel):
    """회원가입과 로그인 요청 Body입니다."""

    email: str = Field(
        examples=["student-auth-test@example.com"],
        description="Supabase Auth에 사용할 테스트 이메일입니다.",
    )
    password: str = Field(
        min_length=6,
        examples=["test-password-123"],
        description="Supabase Auth에 사용할 테스트 비밀번호입니다.",
    )


class UserInfo(BaseModel):
    """응답에서 보여 줄 사용자 정보입니다."""

    id: str
    email: str | None = None


class SignUpResponse(BaseModel):
    """회원가입 요청 결과입니다."""

    message: str
    user: UserInfo | None = None


class SignInResponse(BaseModel):
    """로그인 성공 결과입니다.

    access_token은 Swagger에서 /me를 호출할 때 필요합니다.
    수업 중 화면 공유나 GitHub에는 실제 token 값을 노출하지 않습니다.
    """

    access_token: str
    token_type: str = "bearer"
    user: UserInfo


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다."""

    if value is None:
        return False

    cleaned = value.strip()
    return cleaned.startswith(("your-", "https://your-")) or "example.com" in cleaned


def read_required_env(name: str) -> str:
    """필수 환경 변수를 읽습니다.

    값이 없거나 .env.example의 예시 값 그대로라면 수강생이 바로 원인을 알 수 있도록
    500 오류와 함께 안내 메시지를 반환합니다.
    """

    value = os.getenv(name)
    if value is None or not value.strip() or is_placeholder(value):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{name} 값이 없습니다. C:\\aidev\\02_supabase-ai-backend\\.env 파일을 확인하세요.",
        )

    return value.strip()


def get_supabase():
    """Supabase client를 만듭니다.

    Auth API는 사용자를 대신해 호출하는 흐름이므로 service role key가 아니라 anon key를 사용합니다.
    """

    load_dotenv(ENV_PATH)

    supabase_url = read_required_env("SUPABASE_URL")
    anon_key = read_required_env("SUPABASE_ANON_KEY")

    return create_client(supabase_url, anon_key)


@app.get("/health")
def health_check() -> dict[str, str]:
    """서버가 실행 중인지 확인합니다."""

    return {"status": "ok"}


@app.post("/auth/signup", response_model=SignUpResponse)
def sign_up(request: AuthRequest) -> SignUpResponse:
    """Supabase Auth에 회원가입 요청을 보냅니다."""

    supabase = get_supabase()

    try:
        response = supabase.auth.sign_up(
            {
                "email": request.email,
                "password": request.password,
            }
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Supabase sign up 실패: {error}",
        ) from error

    user = response.user
    return SignUpResponse(
        message="sign up request sent",
        user=UserInfo(id=user.id, email=user.email) if user else None,
    )


@app.post("/auth/signin", response_model=SignInResponse)
def sign_in(request: AuthRequest) -> SignInResponse:
    """Supabase Auth에 로그인 요청을 보내고 access token을 반환합니다."""

    supabase = get_supabase()

    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": request.email,
                "password": request.password,
            }
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Supabase sign in 실패: {error}",
        ) from error

    if response.user is None or response.session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="로그인 응답에 user 또는 session이 없습니다. 이메일 인증 설정을 확인하세요.",
        )

    return SignInResponse(
        access_token=response.session.access_token,
        user=UserInfo(id=response.user.id, email=response.user.email),
    )


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_security),
) -> UserInfo:
    """Authorization 헤더의 Bearer token으로 현재 사용자를 확인합니다."""

    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization 헤더가 필요합니다. 예: Bearer <access_token>",
        )

    supabase = get_supabase()

    try:
        response = supabase.auth.get_user(credentials.credentials)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"token 확인 실패: {error}",
        ) from error

    if response.user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token에서 사용자를 확인할 수 없습니다.",
        )

    return UserInfo(id=response.user.id, email=response.user.email)


@app.get("/me", response_model=UserInfo)
def read_me(current_user: UserInfo = Depends(get_current_user)) -> UserInfo:
    """현재 access token이 가리키는 사용자를 반환합니다."""

    return current_user
