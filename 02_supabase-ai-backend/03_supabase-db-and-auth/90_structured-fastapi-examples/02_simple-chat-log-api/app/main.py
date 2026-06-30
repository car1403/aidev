r"""Simple Chat Log API 구조화 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\02_simple-chat-log-api
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8012
"""

from fastapi import FastAPI

from app.routers.chat_router import router as chat_router


app = FastAPI(title="Example 02 - Simple Chat Log API")
app.include_router(chat_router)
