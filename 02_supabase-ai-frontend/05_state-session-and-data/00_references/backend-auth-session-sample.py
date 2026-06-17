from fastapi import FastAPI, Header, HTTPException  # FastAPI 서버 생성, 라우팅, HTTP 오류 응답에 필요한 클래스를 가져옵니다.
from pydantic import BaseModel  # API 요청 데이터의 타입과 검증 규칙을 정의하기 위해 Pydantic 도구를 가져옵니다.

app = FastAPI(title="Auth Session Sample API")  # FastAPI 서버 객체를 생성합니다. 이후 데코레이터로 API 경로를 이 객체에 등록합니다.

VALID_TOKEN = "sample-access-token"  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.


class LoginRequest(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    username: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    password: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.


class ConversationRequest(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    message: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.


CONVERSATIONS = [  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    {"id": 1, "role": "user", "content": "오늘 학습한 내용을 요약해 주세요."},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    {"id": 2, "role": "assistant", "content": "Streamlit 상태 관리와 인증 흐름을 학습했습니다."},  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
]


SERVICE_LOGS = [
    {
        "id": 1,
        "event": "login_success",
        "status": "ok",
        "message": "student 계정 로그인 성공",
        "created_at": "2026-06-15T09:00:00",
    },
    {
        "id": 2,
        "event": "chat_request",
        "status": "ok",
        "message": "AI 응답 요청 처리",
        "created_at": "2026-06-15T09:05:00",
    },
    {
        "id": 3,
        "event": "conversation_fetch",
        "status": "warning",
        "message": "대화 이력 조회 지연",
        "created_at": "2026-06-15T09:10:00",
    },
]


def verify_token(authorization: str | None):  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    if authorization != f"Bearer {VALID_TOKEN}":  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        raise HTTPException(status_code=401, detail="Invalid token")  # API 요청을 정상 처리할 수 없을 때 HTTP 오류 응답을 반환합니다.


@app.post("/api/login")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def login(request: LoginRequest):  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    if request.username == "student" and request.password == "1234":  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        return {"access_token": VALID_TOKEN, "username": request.username}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.
    raise HTTPException(status_code=401, detail="Login failed")  # API 요청을 정상 처리할 수 없을 때 HTTP 오류 응답을 반환합니다.


@app.get("/api/me")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def get_me(authorization: str | None = Header(default=None)):  # 저장된 데이터를 조회하는 요청을 처리합니다.
    verify_token(authorization)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    return {"username": "student", "role": "learner"}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.get("/api/conversations")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def get_conversations(authorization: str | None = Header(default=None)):  # 저장된 데이터를 조회하는 요청을 처리합니다.
    verify_token(authorization)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    return {"items": CONVERSATIONS}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.post("/api/conversations")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def create_conversation(request: ConversationRequest, authorization: str | None = Header(default=None)):  # 요청 본문으로 받은 데이터를 새 항목으로 저장합니다.
    verify_token(authorization)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    item = {"id": len(CONVERSATIONS) + 1, "role": "user", "content": request.message}  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    CONVERSATIONS.append(item)  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    return item  # 함수 실행 결과를 호출한 위치로 돌려줍니다.


@app.get("/api/service-logs")
def get_service_logs(authorization: str | None = Header(default=None)):
    """프론트엔드가 서비스 로그 조회 화면을 연습할 수 있도록 샘플 로그를 반환합니다."""

    verify_token(authorization)
    return {"items": SERVICE_LOGS}

