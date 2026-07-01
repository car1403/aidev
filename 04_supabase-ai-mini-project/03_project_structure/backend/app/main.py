r"""03_project_structure backend starter.

실행:
    cd C:\aidev\04_supabase-ai-mini-project\03_project_structure\backend
    C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

이 파일은 학생들이 프로젝트를 시작할 수 있도록 health endpoint만 제공합니다.
로그 API, 피드백 API, SSE endpoint는 routers 폴더에 직접 구현합니다.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, CORS_ALLOW_ORIGINS, is_redis_configured, is_supabase_configured


app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO:
# 1. app.routers.log_router를 만들고 app.include_router(log_router)를 추가합니다.
# 2. app.routers.feedback_router를 만들고 app.include_router(feedback_router)를 추가합니다.
# 3. app.routers.stream_router 또는 log_router 안에 /stream/logs SSE endpoint를 추가합니다.
# 4. 구현 예시는 01_supabase-and-sse-practice/backend/app 폴더를 참고합니다.


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "supabase_configured": is_supabase_configured(),
        "redis_configured": is_redis_configured(),
        "message": "04 mini project starter backend is running",
    }
