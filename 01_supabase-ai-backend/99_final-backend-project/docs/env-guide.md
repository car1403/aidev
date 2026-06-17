# Environment Guide

`.env`에 필요한 환경변수와 보안 주의사항을 작성합니다. 실제 key 값은 적지 않습니다.

## 필수 환경변수

```env
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
```

## LLM API 환경변수

```env
GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
```

최종 프로젝트의 기본 LLM API는 Gemini입니다. OpenAI API는 선택/비교 실습으로 사용할 때만 설정합니다.

실제 LLM API를 사용하지 않고 mock 답변만 구현한 경우, 그 이유를 작성합니다.

```text
예:
수업 단계에서는 비용 발생을 막기 위해 mock LLM으로 구현했습니다.
실제 API 연동 위치는 main_supabase.py의 create_qa 함수 내부입니다.
```

## Upstash Redis 선택 환경변수

```env
UPSTASH_REDIS_REST_URL=
UPSTASH_REDIS_REST_TOKEN=
```

Upstash Redis를 사용한다면 캐시, TTL, 요청 제한 중 어떤 용도로 사용하는지 작성합니다.

## 보안 주의사항

- `.env` 파일은 GitHub에 올리지 않습니다.
- `.env.example`에는 실제 값이 아닌 예시 값만 둡니다.
- service role key는 서버 코드에서만 사용합니다.
- Streamlit, 브라우저 코드, README 캡처에 secret을 노출하지 않습니다.
- 로그에 API key나 token을 남기지 않습니다.
