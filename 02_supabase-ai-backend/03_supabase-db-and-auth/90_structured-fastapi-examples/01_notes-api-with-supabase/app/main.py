r"""Notes API 구조화 예제의 시작 파일입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8011
"""

from fastapi import FastAPI

from app.routers.notes_router import router as notes_router


app = FastAPI(title="Example 01 - Notes API With Supabase")
app.include_router(notes_router)
