# Lab 11 - FastAPI Rate Limit Dependency

이 실습은 FastAPI `Depends`를 사용해 endpoint 실행 전에 요청 제한을 적용하는 구조를 확인합니다.

## 학습 목표

- FastAPI 의존성 함수가 endpoint 실행 전에 동작한다는 것을 이해합니다.
- Redis 기반 rate limit을 API 보호 기능으로 연결할 수 있습니다.
- 요청 제한 초과 시 HTTP 429를 반환하는 흐름을 확인합니다.

## 실행 방법

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\06_upstash-redis-cache-and-session
..\..\.venv\Scripts\Activate.ps1
uvicorn 06_fastapi_rate_limit_dependency:app --reload --host 127.0.0.1 --port 8001
```

Swagger UI:

```text
http://127.0.0.1:8001/docs
```

## 확인 기준

- `/health`는 서버 상태를 반환합니다.
- 보호된 endpoint를 여러 번 호출하면 요청 횟수가 증가합니다.
- 제한 횟수를 넘으면 HTTP 429가 반환됩니다.

## 정리 질문

- rate limit은 인증 기능과 어떤 차이가 있나요?
- API 비용 관리 관점에서 rate limit은 왜 중요한가요?
- Redis가 없다면 요청 횟수 제한을 어디에 저장할 수 있을까요?
