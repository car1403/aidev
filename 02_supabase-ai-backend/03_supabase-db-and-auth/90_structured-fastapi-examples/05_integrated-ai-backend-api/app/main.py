r"""Integrated AI Backend API 구조화 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\05_integrated-ai-backend-api
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8015
"""

from fastapi import FastAPI

from app.routers.auth_router import router as auth_router
from app.routers.chat_router import router as chat_router


app = FastAPI(title="Example 05 - Integrated AI Backend API")
app.include_router(auth_router)
app.include_router(chat_router)
