r"""99_final-frontend-project 실제 서비스 연결용 backend입니다.

실행:
    cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_service
    C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

이 backend는 Supabase Auth, Supabase DB, Gemini API를 사용합니다.
Upstash Redis는 같은 질문에 대한 응답을 캐시하는 선택 확장입니다.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, CORS_ALLOW_ORIGINS
from app.routers.auth_router import router as auth_router
from app.routers.chat_router import router as chat_router
from app.routers.log_router import router as log_router


app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(log_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "mode": "supabase-gemini-upstash-optional",
        "message": "99 final frontend project service backend is running",
    }
