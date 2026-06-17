import os  # 운영체제 환경변수에서 API 주소나 비밀 키를 읽기 위해 os 모듈을 가져옵니다.

from dotenv import load_dotenv  # .env 파일에 저장한 환경변수를 Python 실행 환경으로 불러오기 위해 가져옵니다.
from fastapi import FastAPI, HTTPException  # FastAPI 서버 생성, 라우팅, HTTP 오류 응답에 필요한 클래스를 가져옵니다.
from pydantic import BaseModel, Field  # API 요청 데이터의 타입과 검증 규칙을 정의하기 위해 Pydantic 도구를 가져옵니다.
from supabase import create_client  # Supabase REST API와 통신할 클라이언트 객체를 만들기 위해 가져옵니다.

load_dotenv()  # .env 파일의 값을 os.getenv로 읽을 수 있도록 현재 프로세스 환경변수에 등록합니다.

SUPABASE_URL = os.getenv("SUPABASE_URL")  # Supabase 프로젝트 REST API 주소를 환경변수에서 읽어 저장합니다.
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # Supabase API key를 환경변수에서 읽어 저장합니다. 실제 값은 .env에만 둡니다.

app = FastAPI(title="Supabase Learning Log API")  # FastAPI 서버 객체를 생성합니다. 이후 데코레이터로 API 경로를 이 객체에 등록합니다.


class LearningLogCreate(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    learner_name: str = Field(min_length=1, max_length=50)  # learner_name 필드에 허용할 값의 길이, 범위, 형식 같은 검증 조건을 지정합니다.
    topic: str = Field(min_length=1, max_length=100)  # topic 필드에 허용할 값의 길이, 범위, 형식 같은 검증 조건을 지정합니다.
    minutes: int = Field(gt=0, le=600)  # minutes 필드에 허용할 값의 길이, 범위, 형식 같은 검증 조건을 지정합니다.
    memo: str = Field(default="", max_length=500)  # memo 필드에 허용할 값의 길이, 범위, 형식 같은 검증 조건을 지정합니다.


class LearningLogUpdate(BaseModel):  # Pydantic 모델을 정의합니다. FastAPI가 요청 본문을 이 구조로 검증합니다.
    status: str = Field(pattern="^(created|doing|done)$")  # status 필드에 허용할 값의 길이, 범위, 형식 같은 검증 조건을 지정합니다.


def get_supabase_client():  # Supabase 연결 객체를 만드는 함수입니다. 여러 API에서 같은 연결 방식을 재사용합니다.
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:  # Supabase 연결에 필요한 환경변수가 비어 있는지 검사합니다.
        raise HTTPException(status_code=500, detail="Supabase environment variables are missing.")  # API 요청을 정상 처리할 수 없을 때 HTTP 오류 응답을 반환합니다.
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)  # 환경변수로 읽은 URL과 key를 사용해 Supabase 클라이언트를 생성합니다.


@app.get("/health")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def health_check():  # 서버와 외부 연결 상태를 확인하는 health check 요청을 처리합니다.
    supabase = get_supabase_client()  # Supabase 테이블 조회와 저장에 사용할 클라이언트 객체를 가져옵니다.
    response = supabase.table("learning_logs").select("id").limit(1).execute()  # Supabase 테이블에서 데이터를 조회하고 응답 객체에 저장합니다.
    return {"api": "ok", "supabase": "ok", "sample_count": len(response.data)}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.get("/api/logs")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def list_logs():  # 저장된 데이터를 조회하는 요청을 처리합니다.
    supabase = get_supabase_client()  # Supabase 테이블 조회와 저장에 사용할 클라이언트 객체를 가져옵니다.
    response = supabase.table("learning_logs").select("*").order("id", desc=True).execute()  # Supabase 테이블에서 데이터를 조회하고 응답 객체에 저장합니다.
    return {"items": response.data}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.post("/api/logs")  # HTTP POST 요청을 처리할 API 엔드포인트를 등록합니다.
def create_log(payload: LearningLogCreate):  # 요청 본문으로 받은 데이터를 새 항목으로 저장합니다.
    supabase = get_supabase_client()  # Supabase 테이블 조회와 저장에 사용할 클라이언트 객체를 가져옵니다.
    response = supabase.table("learning_logs").insert(payload.model_dump()).execute()  # Supabase 테이블에 새 행을 추가하고 저장 결과를 응답 객체에 저장합니다.
    return {"item": response.data[0] if response.data else None}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.patch("/api/logs/{log_id}")  # HTTP PATCH 요청을 처리할 API 엔드포인트를 등록합니다.
def update_log(log_id: int, payload: LearningLogUpdate):  # 경로 변수와 요청 본문을 사용해 기존 데이터를 수정합니다.
    supabase = get_supabase_client()  # Supabase 테이블 조회와 저장에 사용할 클라이언트 객체를 가져옵니다.
    response = supabase.table("learning_logs").update(payload.model_dump()).eq("id", log_id).execute()  # Supabase 테이블의 기존 행을 수정하고 결과를 응답 객체에 저장합니다.
    if not response.data:  # Supabase 작업 결과가 비어 있으면 대상 데이터를 찾지 못한 상황으로 처리합니다.
        raise HTTPException(status_code=404, detail="Learning log not found")  # API 요청을 정상 처리할 수 없을 때 HTTP 오류 응답을 반환합니다.
    return {"item": response.data[0]}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.

