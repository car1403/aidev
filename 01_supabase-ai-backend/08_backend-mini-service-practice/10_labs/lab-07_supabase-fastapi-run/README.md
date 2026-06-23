# Lab 07. Supabase FastAPI Run

## 목표

`main_supabase.py`를 실행해서 실제 Supabase 테이블에 데이터가 저장되는지 확인합니다.

## 사전 준비

- Supabase 프로젝트가 준비되어 있어야 합니다.
- `.env`에 Supabase URL과 Key가 설정되어 있어야 합니다.
- `mini-service-schema.sql` 실행이 완료되어 있어야 합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

## Swagger UI

```text
http://127.0.0.1:8005/docs
```

## 테스트 순서

1. `GET /health`
2. `POST /questions`
3. Supabase Table Editor에서 `mini_questions` 확인
4. `GET /questions`
5. `GET /service-logs`
6. Supabase Table Editor에서 `mini_service_logs` 확인

## 확인할 내용

- Swagger UI에서 만든 질문이 Supabase에 저장되나요?
- `mini_questions`에 `question`, `answer`, `provider`, `model`, `actual_api_called`, `llm_call_mode`가 저장되나요?
- `mini_service_logs`에 `question_created` 로그가 저장되나요?
- 오류가 발생하면 메시지를 보고 원인을 추적할 수 있나요?
