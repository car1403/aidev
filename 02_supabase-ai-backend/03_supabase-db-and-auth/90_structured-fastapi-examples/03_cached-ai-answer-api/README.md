# 03. Cached AI Answer API

Upstash Redis에 mock AI 답변을 TTL로 캐시하는 구조화 예제입니다.

이 예제는 Supabase 테이블을 사용하지 않습니다. 따라서 `schema.sql`이 없습니다.

## 실행 전 준비

`.env.example`을 참고해 같은 폴더에 `.env`를 만듭니다.

```text
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
```

## 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\03_cached-ai-answer-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8013
```

Swagger UI:

```text
http://127.0.0.1:8013/docs
```

## 확인할 endpoint

| Method | URL | 설명 |
|---|---|---|
| GET | `/health` | 서버와 Redis 환경변수 상태 확인 |
| GET | `/ai/mock-answer` | 질문 답변을 Redis에 캐시 |
| DELETE | `/ai/mock-answer-cache` | 질문 캐시 삭제 |

## 테스트 흐름

1. 같은 질문으로 `/ai/mock-answer`를 두 번 호출합니다.
2. 첫 번째는 `cached: false`입니다.
3. 두 번째는 `cached: true`입니다.
4. `/ai/mock-answer-cache`로 삭제 후 다시 호출하면 `cached: false`입니다.
