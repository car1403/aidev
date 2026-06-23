# Security And Cost Checklist

AI 백엔드 과정에서 보안과 비용 문제를 줄이기 위한 체크리스트입니다.

## 민감 정보

- [ ] `.env` 파일은 GitHub에 올리지 않습니다.
- [ ] `.env.example`에는 실제 key가 아닌 예시 값만 둡니다.
- [ ] `GEMINI_API_KEY`, `OPENAI_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `UPSTASH_REDIS_REST_TOKEN`을 print하지 않습니다.
- [ ] 01~03 과정에서는 Gemini SDK를 기본으로 사용하고, REST 호출은 구조 이해용 보충, OpenAI API는 선택/비교 실습일 때만 호출합니다.
- [ ] service role key는 FastAPI 서버 코드에서만 사용합니다.
- [ ] Streamlit, 브라우저 JavaScript, README 캡처에 secret이 노출되지 않게 합니다.
- [ ] Codex 요청문에 실제 key나 token을 붙여 넣지 않습니다.

## 비용

- [ ] mock-first 예제로 먼저 API 구조와 저장 구조를 검증합니다.
- [ ] 실제 Gemini SDK 호출 여부를 `actual_api_called`, `llm_call_mode`로 구분합니다.
- [ ] 실제 LLM API 호출 전 계정의 사용량과 결제 상태를 확인합니다.
- [ ] 최대 출력 길이를 너무 크게 설정하지 않습니다.
- [ ] 반복문 안에서 실제 LLM API를 무제한 호출하지 않습니다.
- [ ] 실패 재시도 로직이 무한 반복되지 않도록 제한합니다.
- [ ] 테스트 코드가 실제 LLM API를 자동으로 반복 호출하지 않도록 합니다.

## Supabase

- [ ] service role key는 백엔드에서만 사용합니다.
- [ ] 사용자별 데이터에는 user_id 또는 owner_id 조건이 있습니다.
- [ ] update/delete에는 `.eq(...)` 조건이 있습니다.
- [ ] RLS가 필요한 테이블인지 판단했습니다.

## Upstash Redis

- [ ] Redis token은 코드나 로그에 출력하지 않습니다.
- [ ] key 이름에 이메일이나 전화번호 같은 민감 정보를 그대로 넣지 않습니다.
- [ ] TTL이 필요한 key에는 만료 시간을 설정합니다.
- [ ] 오래 보관해야 하는 데이터는 Supabase에 저장합니다.

## 로그

- [ ] 로그에는 key/token을 남기지 않습니다.
- [ ] 오류 로그에는 필요한 최소 정보만 남깁니다.
- [ ] 사용자 질문을 로그로 남길 경우 개인정보 포함 가능성을 고려합니다.
- [ ] 운영 로그와 사용자 대화 이력을 구분합니다.
