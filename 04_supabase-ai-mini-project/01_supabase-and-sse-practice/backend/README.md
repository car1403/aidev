# Backend

FastAPI로 로그 생성, 최근 로그 조회, SSE 실시간 로그 스트림을 제공합니다.

## 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## API

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | backend 상태 확인 |
| POST | `/logs` | 로그 생성, DB 저장, Redis publish |
| GET | `/logs` | 최근 로그 조회 |
| GET | `/logs/summary` | level별 로그 수 조회 |
| GET | `/stream/logs` | SSE 실시간 로그 스트림 |

## 환경변수

기본값은 04 과정 최상위 `.env`에서 읽습니다.

```text
C:\aidev\04_supabase-ai-mini-project\.env
```

`backend/.env.example`은 backend만 따로 배포할 때 참고합니다.

## 테스트

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
pytest tests -q
```
