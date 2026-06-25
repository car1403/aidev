from fastapi import FastAPI  # FastAPI 서버 객체와 API 경로를 만들기 위해 가져옵니다.
from pydantic import BaseModel, Field  # 요청 JSON의 구조와 검증 규칙을 정의하기 위해 가져옵니다.

app = FastAPI(title="Frontend Practice Backend")  # Streamlit 연동 실습용 최소 백엔드 앱을 만듭니다.


class MessageRequest(BaseModel):  # /api/message 요청 본문 구조를 정의합니다.
    name: str = Field(..., min_length=1, description="메시지를 보낸 사용자 이름")
    message: str = Field(..., min_length=1, description="프론트엔드에서 보낸 메시지")


class ScoreRequest(BaseModel):  # /api/score-feedback 요청 본문 구조를 정의합니다.
    name: str = Field(..., min_length=1, description="점수를 입력한 사용자 이름")
    score: int = Field(..., ge=0, le=100, description="0부터 100 사이의 점수")


class ChatRequest(BaseModel):  # /api/chat/mock 요청 본문 구조를 정의합니다.
    question: str = Field(..., min_length=1, description="사용자가 입력한 질문")


@app.get("/")  # 브라우저에서 루트 주소를 열었을 때 확인할 기본 API입니다.
def read_root():
    return {"message": "Frontend Practice Backend is running"}


@app.get("/health")  # 프론트엔드가 서버 실행 상태를 확인할 때 호출하는 API입니다.
def health_check():
    return {"status": "ok", "service": "frontend-practice-backend"}


@app.get("/api/courses")  # 과정 목록처럼 서버에서 데이터를 조회하는 GET 예제입니다.
def get_courses():
    return {
        "courses": ["Python", "Streamlit", "FastAPI", "Supabase"],
        "count": 4,
    }


@app.post("/api/message")  # 프론트엔드가 JSON 데이터를 보내는 POST 예제입니다.
def create_message(request: MessageRequest):
    return {
        "name": request.name,
        "message": request.message,
        "reply": f"{request.name}님, 메시지를 받았습니다: {request.message}",
    }


@app.post("/api/score-feedback")  # 점수를 받아 조건문으로 피드백을 만드는 POST 예제입니다.
def create_score_feedback(request: ScoreRequest):
    if request.score >= 80:
        feedback = "좋습니다. 다음 단계로 넘어갈 준비가 되어 있습니다."
    elif request.score >= 50:
        feedback = "기본 흐름은 이해했습니다. 예제를 한 번 더 수정해 보세요."
    else:
        feedback = "기초 예제를 다시 실행해 보세요."

    return {
        "name": request.name,
        "score": request.score,
        "feedback": feedback,
    }


@app.post("/api/chat/mock")  # 04 챗봇 UI 단원으로 이어지는 mock AI 응답 예제입니다.
def create_mock_chat(request: ChatRequest):
    return {
        "answer": f"'{request.question}'에 대한 mock 응답입니다.",
        "provider": "mock",
        "model": "mock-chat",
        "actual_api_called": False,
    }
