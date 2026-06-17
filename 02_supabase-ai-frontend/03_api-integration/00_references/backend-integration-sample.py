from fastapi import FastAPI  # FastAPI 서버 생성, 라우팅, HTTP 오류 응답에 필요한 클래스를 가져옵니다.
from pydantic import BaseModel  # API 요청 데이터의 타입과 검증 규칙을 정의하기 위해 Pydantic 도구를 가져옵니다.

app = FastAPI(title="Frontend Integration Sample API")  # FastAPI 서버 객체를 생성합니다. 이후 데코레이터로 API 경로를 이 객체에 등록합니다.


class MessageRequest(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    name: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    message: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.


class ScoreRequest(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    name: str  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    score: int  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.


@app.get("/")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def read_root():  # 반복해서 사용할 로직을 함수로 묶어 이름을 붙입니다.
    return {"message": "FastAPI backend is running"}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.get("/health")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def health_check():  # 서버와 외부 연결 상태를 확인하는 health check 요청을 처리합니다.
    return {"status": "ok"}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.get("/api/courses")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def get_courses():  # 저장된 데이터를 조회하는 요청을 처리합니다.
    return {"courses": ["Python", "Streamlit", "FastAPI", "Supabase"]}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.post("/api/message")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def create_message(request: MessageRequest):  # 요청 본문으로 받은 데이터를 새 항목으로 저장합니다.
    return {  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.
        "name": request.name,  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
        "message": request.message,  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
        "reply": f"{request.name}님, 메시지를 받았습니다: {request.message}",  # 이 줄은 예제의 핵심 동작을 단계별로 보여주기 위한 코드입니다.
    }


@app.post("/api/score-feedback")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def create_score_feedback(request: ScoreRequest):  # 요청 본문으로 받은 데이터를 새 항목으로 저장합니다.
    if request.score >= 80:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        feedback = "좋습니다. 다음 단계로 넘어갈 준비가 되어 있습니다."  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    elif request.score >= 50:  # 앞 조건이 False일 때 추가 조건을 검사합니다.
        feedback = "기본 흐름은 이해했습니다. 예제를 한 번 더 수정해 보세요."  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        feedback = "기초 예제를 다시 실행해 보세요."  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

    return {"name": request.name, "score": request.score, "feedback": feedback}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.

