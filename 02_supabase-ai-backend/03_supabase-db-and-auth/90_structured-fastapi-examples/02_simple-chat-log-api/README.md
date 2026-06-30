# 02. Simple Chat Log API

사용자 질문과 AI 답변을 `ex90_simple_chat_logs` 테이블에 저장하는 구조화 예제입니다.

본문의 `05_conversation-history-and-service-logs`를 FastAPI 프로젝트 구조로 나누어 봅니다.

## 실행 전 준비

1. Supabase SQL Editor에서 `schema.sql`을 실행합니다.
2. `.env.example`을 참고해 `.env`를 만듭니다.

```text
SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
```

## 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\02_simple-chat-log-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8012
```

Swagger UI:

```text
http://127.0.0.1:8012/docs
```

## 확인할 endpoint

| Method | URL | 설명 |
|---|---|---|
| GET | `/health` | 서버 상태 확인 |
| POST | `/chat` | mock AI 답변 생성 후 로그 저장 |
| GET | `/logs` | 최근 로그 조회 |

## 테스트

```powershell
python -m pytest -s
```
