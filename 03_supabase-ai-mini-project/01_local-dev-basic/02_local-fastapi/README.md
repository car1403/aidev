# 02_local-fastapi

FastAPI 앱을 로컬 Python 환경에서 실행하는 실습입니다.

## 실행 방법

```powershell
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\02_local-fastapi\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 확인

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

