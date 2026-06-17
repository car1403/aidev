# Security And Cost Check

최종 프로젝트 제출 전 보안과 비용 위험을 점검합니다.

## Secret 관리

- [ ] `.env` 파일을 GitHub에 올리지 않았습니다.
- [ ] `.env.example`에는 실제 key가 없습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`를 프론트엔드에 넣지 않았습니다.
- [ ] `GEMINI_API_KEY`, `OPENAI_API_KEY`, `UPSTASH_REDIS_REST_TOKEN`을 print하지 않았습니다.
- [ ] 기본 LLM API는 Gemini로 사용하고, OpenAI 호출은 선택/비교 실습일 때만 실행합니다.
- [ ] README, 캡처 이미지, 로그에 key/token이 없습니다.

## LLM API 비용

- [ ] mock LLM으로 먼저 테스트했습니다.
- [ ] Gemini 무료 범위와 호출 제한을 확인했습니다.
- [ ] 실제 LLM API 호출 위치를 설명할 수 있습니다.
- [ ] `max_tokens` 제한을 설정했습니다.
- [ ] 반복문에서 실제 LLM API를 과도하게 호출하지 않습니다.
- [ ] 실제 API를 호출했다면 호출 횟수를 기록했습니다.

## Supabase

- [ ] service role key는 FastAPI 서버 코드에서만 사용합니다.
- [ ] update/delete 코드에는 조건이 있습니다.
- [ ] RLS 적용 계획을 문서화했습니다.
- [ ] 사용자별 접근 제어가 필요한 데이터를 구분했습니다.

## Upstash Redis

- [ ] Redis token을 노출하지 않았습니다.
- [ ] TTL이 필요한 key에는 만료 시간을 설정했습니다.
- [ ] Redis에 오래 보관해야 할 데이터를 저장하지 않았습니다.
- [ ] 사용하지 않았다면 이유를 작성했습니다.

## Service Logs

- [ ] 성공/실패 로그를 남깁니다.
- [ ] 로그 metadata에 API key나 token이 없습니다.
- [ ] 오류 원인을 추적할 수 있는 정보가 있습니다.
- [ ] 개인정보가 들어갈 가능성을 확인했습니다.
