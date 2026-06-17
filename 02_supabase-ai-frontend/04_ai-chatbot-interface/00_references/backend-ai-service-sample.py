from fastapi import FastAPI  # FastAPI 서버 생성, 라우팅, HTTP 오류 응답에 필요한 클래스를 가져옵니다.
from pydantic import BaseModel  # API 요청 데이터의 타입과 검증 규칙을 정의하기 위해 Pydantic 도구를 가져옵니다.

app = FastAPI(title="AI Chat Service Sample")  # FastAPI 서버 객체를 생성합니다. 이후 데코레이터로 API 경로를 이 객체에 등록합니다.


class ChatRequest(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    message: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.


@app.get("/health")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def health_check():  # 서버와 외부 연결 상태를 확인하는 health check 요청을 처리합니다.
    return {"status": "ok"}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.post("/api/chat")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def chat(request: ChatRequest):  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    reply = f"임시 AI 응답입니다. 입력한 메시지: {request.message}"  # 백엔드 또는 AI 서비스가 만든 응답 문자열을 화면 출력용 변수에 저장합니다.
    return {"reply": reply}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


