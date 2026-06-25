# Lab 06 - Mock FastAPI 서비스 API

이 실습은 Supabase 없이 메모리 저장소로 FastAPI 서비스 API 구조를 먼저 확인합니다.

## 목표

- Swagger UI에서 서비스 데이터 API를 테스트할 수 있습니다.
- 사용자 프로필, 대화, 메시지, 서비스 로그 endpoint 흐름을 확인합니다.
- mock 서버는 재시작하면 데이터가 사라진다는 점을 이해합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

Swagger UI:

```text
http://127.0.0.1:8003/docs
```

## 실습 순서

1. `GET /health`
2. `GET /profiles/student01`
3. `POST /conversations`
4. `POST /conversations/{conversation_id}/messages`
5. `GET /conversations/{conversation_id}/messages`
6. `POST /service-logs`

## 확인 기준

- 모든 endpoint가 Swagger UI에 보입니다.
- `POST /conversations` 응답의 `id`를 메시지 저장에 사용할 수 있습니다.
- 메시지 조회 결과에 방금 저장한 메시지가 보입니다.
