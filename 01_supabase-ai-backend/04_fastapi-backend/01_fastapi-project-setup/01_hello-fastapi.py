"""FastAPI 첫 번째 예제.

이 파일은 학습 순서를 보여주기 위해 파일명에 번호와 하이픈을 사용합니다.
실제 실행은 같은 폴더의 main.py를 사용합니다.

실행 방법:
    cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\01_fastapi-project-setup
    uvicorn main:app --reload

주의:
    파일명에 하이픈(-)이 들어 있으면 일부 환경에서 import가 불편할 수 있습니다.
    실제 프로젝트에서는 보통 `main.py` 같은 단순한 파일명을 사용합니다.
"""

from fastapi import FastAPI


# FastAPI 객체는 API 서버의 중심입니다.
# 이 객체에 GET, POST 같은 엔드포인트를 하나씩 등록합니다.
app = FastAPI(
    title="Hello FastAPI",
    description="FastAPI 서버가 어떻게 시작되는지 확인하는 첫 예제입니다.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """브라우저에서 http://127.0.0.1:8000/ 로 접속했을 때 실행됩니다."""

    # FastAPI는 Python dict를 자동으로 JSON 응답으로 변환합니다.
    return {
        "message": "Hello, FastAPI",
        "next": "Open /docs to see Swagger UI",
    }


@app.get("/health")
def health_check():
    """서버가 살아 있는지 확인하는 가장 기본적인 점검용 API입니다."""

    return {"status": "ok"}
