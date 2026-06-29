r"""LLM API 구조 분리 과제의 실행 시작점입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\02_llm-api-integration\20_assignments\assignment-100_llm-api-structure-refactor
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.routers.chat_router import router as chat_router


app = FastAPI(title="LLM API Structure Refactor Assignment")
app.include_router(chat_router)
