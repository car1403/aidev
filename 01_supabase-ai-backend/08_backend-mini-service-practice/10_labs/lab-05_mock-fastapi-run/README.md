# Lab 05. Mock FastAPI Run

## 목표

Supabase 없이 메모리 저장소로 FastAPI 서버를 실행하고 API 흐름을 확인합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

## Swagger UI

```text
http://127.0.0.1:8004/docs
```

## 테스트 순서

1. `GET /health`
2. `POST /questions`
3. `GET /questions`
4. `GET /questions/{question_id}`
5. `POST /service-logs`
6. `GET /service-logs`

## POST /questions 요청 예시

```json
{
  "user_id": "student01",
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
  "model": "mock-teacher"
}
```

## 확인할 내용

- `POST /questions` 실행 후 `id`가 생성되나요?
- `GET /questions`에서 방금 만든 데이터가 보이나요?
- `GET /service-logs`에서 `question_created` 로그가 보이나요?
- 서버를 재시작하면 메모리 데이터가 사라지는지 이해했나요?
