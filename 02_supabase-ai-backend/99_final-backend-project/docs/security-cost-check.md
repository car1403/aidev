# Security And Cost Check

최종 프로젝트 제출 전 보안과 비용 위험을 점검합니다.

기능이 정상 동작하더라도 API key가 노출되거나 실제 LLM API가 반복 호출되면 안전한 프로젝트라고 보기 어렵습니다.

## Secret 관리

- [ ] `.env` 파일을 GitHub에 올리지 않았습니다.
- [ ] `.env.example`에는 실제 key가 없습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`를 프론트엔드에 넣지 않았습니다.
- [ ] `GEMINI_API_KEY`, `OPENAI_API_KEY`, `UPSTASH_REDIS_REST_TOKEN`을 print하지 않았습니다.
- [ ] Codex 요청문이나 문서에 실제 key를 붙여 넣지 않았습니다.

## LLM API 비용 관리

- [ ] 기본 LLM 연동 방식은 Gemini SDK로 사용합니다.
- [ ] REST 호출 예제는 구조 이해용 보충으로 분리합니다.
- [ ] OpenAI 호출은 선택 또는 비교 실습으로만 실행합니다.
- [ ] 실제 API 호출 전 mock-first로 먼저 테스트했습니다.
- [ ] `actual_api_called`, `llm_call_mode`로 실제 호출 여부를 구분합니다.
- [ ] 반복문 안에서 실제 LLM API를 무제한 호출하지 않습니다.
- [ ] 최대 출력 길이 또는 요청 횟수 제한을 고려했습니다.
- [ ] 오류 발생 시 무한 재시도하지 않습니다.

## Supabase 보안

- [ ] service role key는 FastAPI 백엔드에서만 사용합니다.
- [ ] 사용자별 데이터 조회 시 `user_id` 또는 `owner_id` 기준을 고려했습니다.
- [ ] update/delete에는 `.eq(...)` 조건이 있습니다.
- [ ] 로그 테이블에 key, token, 비밀번호가 저장되지 않습니다.
- [ ] RLS 적용 여부를 문서에 기록했습니다.

## Upstash Redis 보안

- [ ] Redis token은 코드나 로그에 출력하지 않습니다.
- [ ] key 이름에 이메일, 전화번호 같은 민감 정보를 그대로 넣지 않습니다.
- [ ] TTL이 필요한 key에 만료 시간을 설정했습니다.
- [ ] 장기 보관 데이터는 Redis가 아니라 Supabase에 저장합니다.

## 점검 결과 작성

```text
점검한 파일:
발견한 보안 위험:
발견한 비용 위험:
수정한 내용:
보류한 내용과 이유:
추가로 확인할 내용:
```
