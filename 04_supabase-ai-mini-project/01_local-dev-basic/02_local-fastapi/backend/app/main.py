import os  # 운영체제 환경변수에서 설정값을 읽기 위해 사용합니다.
from pathlib import Path  # 현재 파일 위치를 기준으로 .env 파일 경로를 계산하기 위해 사용합니다.

from dotenv import load_dotenv  # .env 파일의 값을 Python 환경변수로 불러오기 위해 사용합니다.
from fastapi import FastAPI  # FastAPI 서버 객체와 API 경로를 만들기 위해 사용합니다.


# 이 예제는 backend/app 폴더 안에서 실행되지만,
# 환경변수 파일은 04_supabase-ai-mini-project 최상위에 둡니다.
# parents[4]는 현재 파일(main.py)에서 04_supabase-ai-mini-project 폴더까지 올라가는 경로입니다.
PROJECT_ENV = Path(__file__).resolve().parents[4] / ".env"
load_dotenv(PROJECT_ENV)

# APP_NAME은 선택 환경변수입니다.
# .env에 값이 없으면 기본 이름인 "FastAPI App"을 사용합니다.
APP_NAME = os.getenv("APP_NAME", "FastAPI App")

# FastAPI 서버 객체를 생성합니다.
# title 값은 Swagger UI(/docs) 화면 제목으로도 표시됩니다.
app = FastAPI(title=APP_NAME)


@app.get("/health")
def health_check():
    """FastAPI 서버가 정상 실행 중인지 확인하는 가장 단순한 API입니다."""
    return {
        "status": "ok",
        "app": APP_NAME,
        "env_file": str(PROJECT_ENV),
    }


@app.get("/api/message")
def get_message():
    """Streamlit 화면에서 호출해 볼 수 있는 간단한 JSON 응답 API입니다."""
    return {
        "message": "FastAPI is running locally.",
        "next_step": "04_local-full-stack에서 Supabase 저장과 Streamlit 화면을 연결합니다.",
    }
