r"""99_final-backend-project solution 구조화 예제입니다.

실행:
    cd C:\aidev\02_supabase-ai-backend\99_final-backend-project\solution
    ..\..\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
"""

from fastapi import FastAPI

from app.routers.product_router import router as product_router


app = FastAPI(title="Final Backend Project Solution")
app.include_router(product_router)
