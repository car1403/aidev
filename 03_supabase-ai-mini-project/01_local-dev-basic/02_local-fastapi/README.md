# 02_local-fastapi

FastAPI 앱을 로컬 Python 환경에서 실행하는 실습입니다.

이 실습은 `03_supabase-ai-mini-project` 최상위 `.venv`와 `.env`를 사용합니다. `backend` 폴더 안에 `.venv`를 새로 만들지 않습니다.

```text
가상환경:
C:\aidev\03_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\03_supabase-ai-mini-project\.env
```

## 실행 방법

첫 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\02_local-fastapi\backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 확인

브라우저에서 아래 주소를 확인합니다.

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

PowerShell에서 직접 확인할 수도 있습니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod http://127.0.0.1:8000/api/message
```

## 확인할 점

- `/health`에서 FastAPI 서버가 정상 실행되는지 확인합니다.
- `/api/message`에서 프론트엔드가 받을 수 있는 JSON 응답을 확인합니다.
- 이 단계는 Supabase 저장 전, FastAPI 서버 실행 감각을 확인하는 기본 단계입니다.
- 실제 Supabase 저장과 조회는 `04_local-full-stack`에서 연결합니다.
