# Assignment 05 - Security And Cost Review Report

이 과제에서는 AI 백엔드 코드의 보안 위험과 비용 위험을 점검하고 개선안을 작성합니다.

보안과 비용 점검은 최종 프로젝트 전에 반드시 필요한 과정입니다. 기능이 잘 동작하더라도 API key가 노출되거나 실제 LLM API가 과도하게 호출되면 운영하기 어렵습니다.

## 목표

- API key, token, service role key 노출 위험을 찾을 수 있다.
- `.env`와 `.env.example` 관리 상태를 점검할 수 있다.
- 실제 LLM API 호출 위치와 비용 위험을 확인할 수 있다.
- Gemini SDK 기본 사용 흐름, REST 보충 예제, OpenAI 선택 사용 흐름을 구분할 수 있다.
- Supabase service role key 사용 위치를 확인할 수 있다.
- Upstash Redis token과 TTL 설정을 점검할 수 있다.
- 서비스 로그에 민감 정보가 들어갈 가능성을 확인할 수 있다.

## 점검 대상 예시

```text
C:\aidev\01_supabase-ai-backend\05_llm-api-integration
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth
C:\aidev\01_supabase-ai-backend\07_backend-service-data-management
C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice
```

## 제출 파일

```text
security-cost-review-report.md
```

## Codex 요청 예시

```text
다음 AI 백엔드 코드를 보안과 비용 관점에서 점검해주세요.

점검 대상:
여기에 파일 또는 폴더 경로를 적습니다.

중점 확인:
1. API key, Supabase key, Redis token이 코드에 직접 적혀 있는가?
2. key나 token을 print 또는 로그로 출력하는 부분이 있는가?
3. .env와 .env.example이 안전하게 구분되어 있는가?
4. 실제 LLM API 호출이 반복문이나 테스트에서 과도하게 실행될 수 있는가?
5. Gemini SDK 기본 사용 흐름, REST 보충 예제, OpenAI 선택 사용 흐름이 구분되어 있는가?
6. Supabase service role key가 백엔드에서만 사용되는가?
7. Upstash Redis token과 TTL 설정이 안전한가?
8. 서비스 로그에 민감 정보가 들어갈 가능성이 있는가?

출력 형식:
- 즉시 수정해야 할 보안 위험
- 비용 증가 가능성이 있는 부분
- 환경 변수 관리 문제
- Supabase/Redis 권한 문제
- 로그 민감 정보 위험
- 안전하게 고치는 순서

아직 코드를 수정하지 말고 점검 결과만 정리해주세요.
```

## 보고서 템플릿

```md
# Security And Cost Review Report

## 1. 점검 대상

- 파일 또는 폴더:
- 코드 목적:

## 2. 사용한 Codex 요청문

```text
여기에 사용한 요청문을 작성합니다.
```

## 3. 민감 정보 점검

- API key 노출 가능성:
- Supabase key 노출 가능성:
- Upstash Redis token 노출 가능성:
- `.env`와 `.env.example` 관리 상태:

## 4. 비용 위험 점검

- 실제 LLM API 호출 위치:
- 반복 호출 가능성:
- Gemini SDK 기본 사용 흐름:
- REST 보충 예제 사용 흐름:
- OpenAI 선택 사용 흐름:
- 비용 제한 장치:

## 5. Supabase와 Redis 점검

- service role key 사용 위치:
- 사용자별 데이터 접근 조건:
- Redis TTL 설정:
- Redis key 설계:

## 6. 서비스 로그 점검

- 로그에 남는 정보:
- 민감 정보 포함 가능성:
- 개선 방향:

## 7. 개선 계획

- 즉시 수정할 항목:
- 이후 개선할 항목:
- 보류한 항목과 이유:

## 8. 최종 확인

- 직접 확인한 방법:
- 남은 질문:
```

## 평가 체크리스트

- [ ] 점검 대상 파일 또는 폴더를 명확히 적었다.
- [ ] 실제 key나 token을 제출물에 포함하지 않았다.
- [ ] `.env`와 `.env.example` 상태를 확인했다.
- [ ] LLM API 비용 위험을 점검했다.
- [ ] Supabase service role key 사용 위치를 확인했다.
- [ ] Upstash Redis token과 TTL을 확인했다.
- [ ] 서비스 로그의 민감 정보 위험을 확인했다.
- [ ] 개선 계획을 우선순위별로 정리했다.
