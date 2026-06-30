# 05. Integrated AI Backend API

Auth, Supabase DB 저장, Upstash Redis TTL 캐시, Gemini 선택 호출을 하나로 연결한 통합 참고 예제입니다.

이 예제는 완성 서비스가 아니라, `01`~`04`에서 배운 구조가 한 요청 흐름 안에서 어떻게 연결되는지 보여주는 작은 예제입니다.

기본값은 mock 응답입니다. Gemini API key, 비용, 쿼터 문제로 막히지 않도록 먼저 mock으로 전체 흐름을 확인하고, 준비가 되면 `USE_GEMINI=true`로 바꾸어 실제 Gemini SDK 호출을 확인합니다.

## 1. Supabase 테이블 만들기

Supabase SQL Editor에서 `schema.sql`을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\05_integrated-ai-backend-api\schema.sql
```

## 2. 환경변수 준비

`.env.example`을 참고해 같은 폴더에 `.env`를 만듭니다.

```text
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
USE_GEMINI=false
GEMINI_API_KEY=...
GEMINI_MODEL=gemini-2.5-flash-lite
```

처음 실행할 때는 `USE_GEMINI=false`를 권장합니다.

## 3. 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\05_integrated-ai-backend-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8015
```

Swagger UI:

```text
http://127.0.0.1:8015/docs
```

## 테스트 순서

1. `POST /auth/signup`
2. `POST /auth/signin`
3. Swagger `Authorize`에 access token 입력
4. `GET /me`
5. `POST /chat`
6. 같은 질문으로 `POST /chat` 다시 실행
7. `GET /logs`

두 번째 `POST /chat`에서는 Redis 캐시가 있으면 `cached: true`가 됩니다.

## 요청 흐름

```text
Bearer token 확인
-> Redis에서 같은 질문 캐시 확인
-> 캐시가 있으면 Redis 답변 반환
-> 캐시가 없으면 USE_GEMINI 확인
-> USE_GEMINI=false면 mock 답변 생성
-> USE_GEMINI=true면 Gemini SDK 호출
-> Supabase ex90_user_chat_logs에 저장
-> Redis에 TTL과 함께 답변 저장
-> 응답 반환
```

## Gemini 호출 기준

| 설정 | 동작 |
|---|---|
| `USE_GEMINI=false` | mock 답변을 사용합니다. 기본값입니다. |
| `USE_GEMINI=true` | Gemini SDK를 호출합니다. |
| `GEMINI_API_KEY` 없음 | Gemini 호출을 하지 못하므로 오류 로그를 남깁니다. |
| Gemini 503/쿼터 오류 | 오류 로그를 남기고 HTTP 오류를 반환합니다. |

이 예제는 Gemini 실패 시 자동으로 mock fallback을 하지 않습니다. 실패 원인을 수강생이 확인할 수 있도록 `status='error'`, `error_message`를 로그에 남깁니다.
