# Lab 09 - 보안과 비용 체크

이 lab에서는 AI 백엔드 코드에서 민감 정보 노출 위험과 LLM API 비용 위험을 점검합니다.

기능이 정상 동작하더라도 API key가 노출되거나 실제 LLM API가 반복 호출되면 안전한 서비스라고 보기 어렵습니다. 이 lab에서는 최종 점검 관점으로 보안과 비용을 확인합니다.

## 실습 목표

- API key, token, service role key 노출 위험을 찾을 수 있다.
- `.env`와 `.env.example` 관리 기준을 확인할 수 있다.
- 실제 LLM API 호출과 mock-first 호출을 구분할 수 있다.
- mock-first, Gemini SDK 최소/안내형 예제, OpenAI 선택 사용 흐름의 비용 위험을 설명할 수 있다.
- Upstash Redis TTL과 key 설계를 점검할 수 있다.
- 서비스 로그에 민감 정보가 들어가지 않도록 확인할 수 있다.

## 사용할 체크리스트

```text
../../00_references/security-cost-checklist.md
../../00_references/backend-review-checklist.md
```

## 점검 대상 예시

```text
C:\aidev\02_supabase-ai-backend\02_llm-api-integration
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice
```

## 실습 절차

1. 실제 API 호출 파일과 mock-first 파일을 구분합니다.
2. API key, Supabase key, Redis token이 코드에 직접 적혀 있는지 찾습니다.
3. key 또는 token을 print하거나 로그에 남기는 코드가 있는지 확인합니다.
4. `.env.example`에 실제 key가 들어가 있지 않은지 확인합니다.
5. LLM API 호출이 반복문이나 테스트에서 과도하게 실행될 가능성이 있는지 확인합니다.
6. Gemini SDK, REST 호출, OpenAI 예제가 어떤 목적으로 분리되어 있는지 확인합니다.
7. Redis key에 TTL이 설정되어 있는지 확인합니다.
8. 서비스 로그에 민감 정보가 들어갈 가능성이 있는지 확인합니다.
9. Codex에게 보안과 비용 관점의 리뷰를 요청합니다.

## Codex 요청 예시

```text
다음 백엔드 코드를 보안과 비용 관점에서 리뷰해주세요.

리뷰 대상:
02_llm-api-integration
03_supabase-db-and-auth
05_backend-mini-service-practice

중점 확인:
1. API key, Supabase key, Redis token이 코드에 직접 적혀 있는가?
2. key나 token을 print 또는 로그로 출력하는 부분이 있는가?
3. 실제 LLM API 호출이 반복문이나 테스트에서 과도하게 실행될 수 있는가?
4. mock-first, Gemini SDK 최소/안내형 예제, OpenAI 선택 사용 흐름이 구분되어 있는가?
5. Redis TTL이 필요한 곳에 설정되어 있는가?
6. 서비스 로그에 민감 정보가 들어갈 가능성이 있는가?

출력 형식:
- 즉시 수정해야 할 보안 위험
- 비용 증가 가능성이 있는 부분
- Redis/로그 점검 항목
- 수정 전 확인 질문
- 안전하게 고치는 순서

아직 코드를 수정하지 말고 점검 결과만 정리해주세요.
```

## 결과 정리

```md
## Lab 09 결과

- 점검한 파일:
- 발견한 보안 위험:
- 발견한 비용 위험:
- Redis TTL 또는 key 설계 문제:
- 로그에 민감 정보가 들어갈 가능성:
- 수정 제안:
- 직접 확인한 실행 결과:
```

## 완료 체크리스트

- [ ] 실제 API 호출 파일과 mock-first 파일을 구분했다.
- [ ] key와 token이 코드에 직접 적혀 있지 않은지 확인했다.
- [ ] `.env.example`에 실제 key가 없는지 확인했다.
- [ ] LLM API 과도 호출 가능성을 확인했다.
- [ ] Redis TTL 설정 여부를 확인했다.
- [ ] 서비스 로그의 민감 정보 위험을 확인했다.
- [ ] 보안과 비용 점검 결과를 정리했다.
