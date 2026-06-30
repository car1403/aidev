r"""Auth JWT Profile API 구조화 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\04_auth-jwt-profile-api
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8014
"""

from fastapi import FastAPI

from app.routers.auth_router import router as auth_router
from app.routers.profile_router import router as profile_router


app = FastAPI(title="Example 04 - Auth JWT Profile API")
app.include_router(auth_router)
app.include_router(profile_router)
