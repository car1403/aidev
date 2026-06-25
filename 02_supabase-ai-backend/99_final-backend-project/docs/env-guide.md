# Environment Guide

최종 프로젝트에 필요한 환경 변수와 보안 주의사항을 작성합니다. 실제 key 값은 문서에 적지 않습니다.

## Supabase 환경 변수

```env
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
```

`SUPABASE_SERVICE_ROLE_KEY`는 강한 권한을 가진 key입니다. FastAPI 백엔드에서만 사용하고, Streamlit, React, 브라우저 JavaScript, README 문서에 노출하지 않습니다.

## LLM API 환경 변수

```env
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

최종 프로젝트의 기본 LLM 연동 방식은 Gemini SDK입니다. REST 호출은 API 구조를 이해하기 위한 보충 예제로만 사용하고, OpenAI API는 선택 또는 비교 실습으로 사용할 때만 설정합니다.

## Upstash Redis 선택 환경 변수

```env
UPSTASH_REDIS_REST_URL=your-upstash-redis-rest-url
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
```

Upstash Redis는 필수 기능이 아닙니다. 캐시, 임시 세션, 요청 횟수 제한 중 하나를 구현할 때 사용합니다.

## `.env.example` 작성 기준

- 실제 key 값을 넣지 않습니다.
- 필요한 변수 이름만 보여줍니다.
- 값에는 `your-...` 형식의 예시 문구를 사용합니다.
- `.env` 파일은 GitHub에 올리지 않습니다.

## 확인 체크리스트

- [ ] `.env`는 로컬에만 존재합니다.
- [ ] `.env.example`에는 실제 key가 없습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`는 백엔드에서만 사용합니다.
- [ ] Gemini SDK를 기본 LLM 연동 방식으로 사용합니다.
- [ ] REST 호출 예제는 보충 자료로 분리했습니다.
- [ ] OpenAI는 선택 또는 비교 실습으로 분리했습니다.
- [ ] Redis token을 print하거나 로그에 남기지 않습니다.
