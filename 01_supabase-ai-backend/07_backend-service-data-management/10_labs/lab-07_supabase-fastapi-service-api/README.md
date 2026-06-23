# Lab 07 - Supabase FastAPI 서비스 API

이 실습은 FastAPI endpoint가 실제 Supabase 테이블에 데이터를 저장하고 조회하는 흐름을 확인합니다.

## 목표

- mock 서버와 Supabase 서버의 차이를 설명할 수 있습니다.
- FastAPI endpoint를 통해 Supabase 테이블에 데이터가 저장되는지 확인합니다.
- API 오류가 발생했을 때 `.env`와 schema 준비 상태를 점검할 수 있습니다.

## 실행 전 확인

```text
C:\aidev\01_supabase-ai-backend\.env
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql
```

## 실행 방법

```powershell
cd C:\aidev\01_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

## 확인 기준

- `GET /health` 응답의 `storage`가 `supabase`입니다.
- `POST /conversations`로 만든 데이터가 Supabase `conversations` 테이블에 저장됩니다.
- `POST /conversations/{conversation_id}/messages`로 만든 데이터가 `messages` 테이블에 저장됩니다.
- `POST /service-logs`로 만든 로그가 `service_logs` 테이블에 저장됩니다.

## 오류 확인

- 500 오류가 나오면 `.env` 값과 Supabase 테이블 생성 여부를 확인합니다.
- 404 오류가 나오면 요청한 `user_id` 또는 `conversation_id`가 실제로 존재하는지 확인합니다.
