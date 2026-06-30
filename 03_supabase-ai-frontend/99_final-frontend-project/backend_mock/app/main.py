r"""99_final-frontend-project 프론트 개발용 mock backend입니다.

실행:
    cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_mock
    C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
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
        "mode": "mock-memory",
        "message": "99 final frontend project backend is running",
    }
