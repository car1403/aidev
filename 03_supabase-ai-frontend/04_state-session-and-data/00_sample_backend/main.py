r"""04_state-session-and-data 전용 FastAPI 샘플 백엔드입니다.

이 백엔드는 Supabase Auth를 대신하는 실습용 mock 서버입니다.
수강생은 이 파일을 실행한 뒤 Streamlit 화면에서 회원가입, 로그인,
로그아웃, Authorization header, 사용자별 데이터 조회 흐름을 연습합니다.

실행 순서:
    1. PowerShell에서 03_supabase-ai-frontend 폴더로 이동합니다.

       cd C:\aidev\03_supabase-ai-frontend

    2. 03 과정 가상환경을 활성화합니다.

       .\.venv\Scripts\Activate.ps1

    3. 샘플 백엔드 폴더로 이동합니다.

       cd .\04_state-session-and-data\00_sample_backend

    4. FastAPI 서버를 실행합니다.

       uvicorn main:app --reload --host 127.0.0.1 --port 8000

    5. 브라우저에서 Swagger 문서를 확인합니다.

       http://127.0.0.1:8000/docs

주의:
    - 이 서버는 메모리 안에만 데이터를 저장합니다.
    - 서버를 껐다 켜면 수업 중 새로 가입한 계정은 사라집니다.
    - 실제 서비스의 회원가입/로그인/Supabase Auth/RLS는 백엔드 과정에서 다룹니다.
"""

from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="State Session Sample API")


class SignupRequest(BaseModel):
    """회원가입 요청 본문입니다.

    Streamlit 화면은 사용자가 입력한 username, password, display_name을
    JSON으로 만들어 이 구조에 맞게 백엔드로 보냅니다.
    """

    username: str = Field(min_length=3, examples=["student"])
    password: str = Field(min_length=4, examples=["1234"])
    display_name: str = Field(min_length=1, examples=["수강생"])


class LoginRequest(BaseModel):
    """로그인 요청 본문입니다."""

    username: str = Field(examples=["student"])
    password: str = Field(examples=["1234"])


class ConversationRequest(BaseModel):
    """새 대화 메시지 저장 요청 본문입니다."""

    message: str = Field(min_length=1, examples=["오늘 학습한 내용을 요약해 주세요."])


# 실제 서비스라면 사용자 정보는 Supabase Auth 또는 별도 users 테이블에 저장합니다.
# 여기서는 초보자 실습을 위해 Python 딕셔너리에 임시 저장합니다.
USERS: dict[str, dict] = {
    "student": {
        "username": "student",
        "password": "1234",
        "display_name": "수강생",
        "role": "learner",
    }
}


# token과 username의 관계를 저장합니다.
# 실제 서비스에서는 JWT를 검증하거나 세션 저장소를 사용합니다.
# 기존 단독 예제들이 바로 동작하도록 sample-access-token도 미리 등록해 둡니다.
TOKENS: dict[str, str] = {"sample-access-token": "student"}


CONVERSATIONS = [
    {"id": 1, "role": "user", "content": "오늘 학습한 내용을 요약해 주세요."},
    {"id": 2, "role": "assistant", "content": "Streamlit 상태 관리와 인증 흐름을 학습했습니다."},
]


SERVICE_LOGS = [
    {
        "id": 1,
        "event": "sample_backend_started",
        "status": "ok",
        "message": "04_state-session-and-data 샘플 백엔드 준비",
        "created_at": "2026-06-15T09:00:00",
    },
    {
        "id": 2,
        "event": "login_success",
        "status": "ok",
        "message": "student 계정 로그인 성공 예시",
        "created_at": "2026-06-15T09:05:00",
    },
]


def now_iso() -> str:
    """로그에 기록할 현재 시각 문자열을 만듭니다."""

    return datetime.now().isoformat(timespec="seconds")


def add_service_log(event: str, status_text: str, message: str) -> None:
    """화면에서 확인할 수 있도록 간단한 서비스 로그를 추가합니다."""

    SERVICE_LOGS.append(
        {
            "id": len(SERVICE_LOGS) + 1,
            "event": event,
            "status": status_text,
            "message": message,
            "created_at": now_iso(),
        }
    )


def get_username_from_header(authorization: str | None) -> str:
    """Authorization header에서 token을 꺼내 사용자 이름을 찾습니다.

    프론트엔드는 보호된 API를 호출할 때 아래 형식의 header를 보냅니다.

        Authorization: Bearer sample-token-...

    백엔드는 이 값을 확인해서 요청한 사용자가 누구인지 판단합니다.
    """

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header가 없습니다. Bearer token을 보내야 합니다.",
        )

    token = authorization.removeprefix("Bearer ").strip()
    username = TOKENS.get(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 token입니다. 다시 로그인하세요.",
        )

    return username


@app.get("/")
def root() -> dict:
    """백엔드 서버가 실행 중인지 간단히 확인합니다."""

    return {
        "message": "04_state-session-and-data sample backend is running",
        "docs": "http://127.0.0.1:8000/docs",
    }


@app.get("/health")
def health() -> dict:
    """헬스 체크용 API입니다."""

    return {"status": "ok"}


@app.post("/api/signup", status_code=status.HTTP_201_CREATED)
def signup(request: SignupRequest) -> dict:
    """회원가입 API입니다.

    같은 username이 이미 있으면 409 오류를 반환합니다.
    새 계정은 USERS 딕셔너리에 저장됩니다.
    """

    if request.username in USERS:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 가입된 사용자 이름입니다.",
        )

    USERS[request.username] = {
        "username": request.username,
        "password": request.password,
        "display_name": request.display_name,
        "role": "learner",
    }
    add_service_log("signup_success", "ok", f"{request.username} 회원가입")

    return {
        "message": "회원가입이 완료되었습니다. 이제 로그인할 수 있습니다.",
        "username": request.username,
        "display_name": request.display_name,
    }


@app.post("/api/login")
def login(request: LoginRequest) -> dict:
    """로그인 API입니다.

    username과 password가 맞으면 access_token을 반환합니다.
    Streamlit은 이 token을 st.session_state에 저장합니다.
    """

    user = USERS.get(request.username)
    if user is None or user["password"] != request.password:
        add_service_log("login_failed", "warning", f"{request.username} 로그인 실패")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자 이름 또는 비밀번호가 올바르지 않습니다.",
        )

    token = f"sample-token-{request.username}-{uuid4().hex[:8]}"
    TOKENS[token] = request.username
    add_service_log("login_success", "ok", f"{request.username} 로그인 성공")

    return {
        "access_token": token,
        "token_type": "bearer",
        "username": request.username,
        "display_name": user["display_name"],
    }


@app.get("/api/me")
def get_me(authorization: str | None = Header(default=None)) -> dict:
    """로그인한 사용자 정보를 반환하는 보호된 API입니다."""

    username = get_username_from_header(authorization)
    user = USERS[username]
    return {
        "username": user["username"],
        "display_name": user["display_name"],
        "role": user["role"],
    }


@app.get("/api/conversations")
def get_conversations(authorization: str | None = Header(default=None)) -> dict:
    """대화 이력 목록을 반환하는 보호된 API입니다."""

    username = get_username_from_header(authorization)
    add_service_log("conversation_fetch", "ok", f"{username} 대화 이력 조회")
    return {"items": CONVERSATIONS}


@app.post("/api/conversations")
def create_conversation(
    request: ConversationRequest,
    authorization: str | None = Header(default=None),
) -> dict:
    """새 대화 메시지를 저장하는 보호된 API입니다."""

    username = get_username_from_header(authorization)
    item = {"id": len(CONVERSATIONS) + 1, "role": "user", "content": request.message}
    CONVERSATIONS.append(item)
    add_service_log("conversation_create", "ok", f"{username} 대화 메시지 저장")
    return item


@app.get("/api/service-logs")
def get_service_logs(authorization: str | None = Header(default=None)) -> dict:
    """서비스 로그 목록을 반환하는 보호된 API입니다."""

    get_username_from_header(authorization)
    return {"items": SERVICE_LOGS}
