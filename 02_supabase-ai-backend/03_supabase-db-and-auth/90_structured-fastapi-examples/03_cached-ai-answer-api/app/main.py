r"""Cached AI Answer API 구조화 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\03_cached-ai-answer-api
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8013
"""

from fastapi import FastAPI

from app.routers.cache_router import router as cache_router


app = FastAPI(title="Example 03 - Cached AI Answer API")
app.include_router(cache_router)
