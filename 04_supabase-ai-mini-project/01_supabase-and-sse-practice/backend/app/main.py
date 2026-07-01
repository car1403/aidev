r"""01_supabase-and-sse-practice backend.

실행:
    cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
    C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, CORS_ALLOW_ORIGINS, is_redis_configured, is_supabase_configured
from app.routers.log_router import router as log_router


app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(log_router)


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "supabase_configured": is_supabase_configured(),
        "redis_configured": is_redis_configured(),
        "message": "04 mini project realtime backend is running",
    }
