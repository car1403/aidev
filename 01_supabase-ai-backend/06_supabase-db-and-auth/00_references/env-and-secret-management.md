# 환경변수와 비밀정보 관리

`01_supabase-ai-backend`는 Supabase 중심으로 진행합니다.

## 원칙

- API Key를 코드에 직접 쓰지 않습니다.
- `.env`는 GitHub에 올리지 않습니다.
- 공유용 예시는 `.env.example`로 만듭니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 강한 권한을 가진 key이므로 FastAPI 같은 서버 코드에서만 사용합니다.
- Streamlit 화면이나 브라우저 코드에는 service role key를 넣지 않습니다.

## Supabase 환경변수 예시

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

## key 역할

```text
SUPABASE_URL
-> Supabase 프로젝트 API 주소

SUPABASE_ANON_KEY
-> 클라이언트에서도 사용할 수 있는 공개용 key
-> RLS 정책과 함께 사용해야 안전함

SUPABASE_SERVICE_ROLE_KEY
-> RLS를 우회할 수 있는 서버 전용 key
-> FastAPI 서버에서만 사용

GEMINI_API_KEY
-> 기본 선택 사항
-> 01~03 과정의 실제 AI 응답 생성 실습에서 우선 사용

OPENAI_API_KEY
-> 선택 사항
-> OpenAI 예제를 활용한 모델 비교 또는 추가 강의 때 사용

UPSTASH_REDIS_REST_URL
-> 선택 사항
-> Upstash Redis REST API 주소
-> 캐시, TTL, 요청 제한 실습에서 사용

UPSTASH_REDIS_REST_TOKEN
-> 선택 사항
-> Upstash Redis REST API 호출에 필요한 token
-> FastAPI 서버 코드에서만 사용
```

## Docker 관련 환경변수

`DATABASE_URL`, `REDIS_URL` 같은 로컬 DB/Redis 환경변수는 이 과정의 기본 흐름에서 사용하지 않습니다.

`01_supabase-ai-backend`에서 Redis가 필요할 때는 로컬 Redis 주소 대신 Upstash Redis의 REST URL과 token을 사용합니다.

Docker, PostgreSQL, Redis 운영은 `C:\aidev\06_multi-agent-service-ops`에서 다룹니다.
