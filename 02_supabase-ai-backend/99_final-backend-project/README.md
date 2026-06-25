# 99. Final Backend Project

이 단원은 `02_supabase-ai-backend`의 최종 백엔드 프로젝트입니다.

Python, FastAPI, Pydantic, Gemini SDK, Supabase, Upstash Redis, 서비스 로그, Codex 기반 코드 리뷰를 하나의 결과물로 정리합니다. 앞에서 만든 `08_backend-mini-service-practice`의 미니 서비스를 바탕으로, 직접 요구사항을 정리하고 API, 데이터베이스, 환경 변수, 테스트 결과, 보안 점검 문서를 완성합니다.

## 프로젝트 주제 예시

```text
Supabase 기반 AI 질문 응답 백엔드 서비스
```

## 프로젝트 목표

- FastAPI 기반 REST API를 설계하고 구현합니다.
- Pydantic 모델로 요청/응답 데이터를 검증합니다.
- Gemini SDK를 기본 LLM 연동 방식으로 사용합니다.
- REST 호출 예제는 구조 이해용 보충으로만 다룹니다.
- OpenAI API는 선택 또는 비교 실습으로만 다룹니다.
- Supabase에 질문, 답변, 서비스 로그를 저장합니다.
- Upstash Redis는 선택 기능으로 캐시, 세션, 요청 횟수 제한 중 하나에 적용할 수 있습니다.
- Codex를 활용해 코드 리뷰, 디버깅, 보안/비용 점검 기록을 남깁니다.

## 필수 포함 요소

| 항목 | 설명 |
| --- | --- |
| FastAPI | REST API endpoint를 구현합니다. |
| Pydantic | 요청/응답 데이터를 검증합니다. |
| Supabase | 사용자 데이터, 질문/응답, 서비스 로그를 저장합니다. |
| Gemini SDK | 기본 LLM 연동 방식으로 사용합니다. |
| REST 호출 | LLM API 구조를 이해하기 위한 보충 예제로만 사용합니다. |
| Mock-first | 실제 API key가 없거나 비용을 아끼기 위해 먼저 검증하는 응답 흐름입니다. |
| 서비스 로그 | 성공/실패, 오류, 모델명, 처리 결과를 Supabase에 저장합니다. |
| 보안/비용 점검 | API key 노출, service role key 사용 위치, LLM 비용 제한을 확인합니다. |
| Codex 리뷰 | 코드 설명, 오류 분석, 리팩토링, 리뷰 기록을 남깁니다. |

## 선택 포함 요소

| 항목 | 설명 |
| --- | --- |
| Supabase Auth/RLS | 사용자별 데이터 접근 제어를 확장합니다. |
| Upstash Redis | TTL 캐시, 요청 횟수 제한, 임시 세션 상태 중 하나를 구현합니다. |
| OpenAI API | Gemini SDK와 비교하거나 선택 기능으로 호출합니다. |
| Feedback API | AI 답변에 대한 사용자 평가를 저장합니다. |

## 제출 문서

```text
README.md
docs/api-design.md
docs/database-design.md
docs/env-guide.md
docs/service-data-flow.md
docs/security-cost-check.md
docs/test-result.md
docs/codex-review-log.md
```

## 권장 구현 범위

최소 구현:

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
GET /service-logs
```

선택 구현:

```text
POST /feedback
GET /profiles/{user_id}
Upstash Redis 기반 요청 횟수 제한
Upstash Redis 기반 30초 응답 캐시
```

이 과정에서는 Docker 배포와 SSE 스트리밍을 필수로 요구하지 않습니다.

- SSE 기반 실시간 응답 스트리밍은 `04_supabase-ai-mini-project`에서 백엔드, 프론트엔드, Supabase 저장 흐름을 함께 연결하며 다룹니다.
- Docker, Docker Compose, AWS, GitHub Actions 기반 운영은 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 권장 프로젝트 흐름

```text
1. 요구사항 정리
2. API 설계
3. Supabase 테이블 설계
4. mock-first로 FastAPI endpoint 구현
5. Gemini SDK 연동 설계 또는 구현
6. Supabase 저장 연결
7. 서비스 로그 저장 연결
8. Upstash Redis 선택 기능 설계 또는 구현
9. 보안/비용 점검
10. Codex 코드 리뷰
11. Swagger UI 또는 TestClient 실행 결과 정리
```

## 평가 기준

- API endpoint가 리소스 중심으로 설계되어 있는가?
- HTTP Method가 의미에 맞게 사용되었는가?
- Pydantic 요청/응답 모델이 명확한가?
- Supabase 테이블 구조가 서비스 요구사항과 맞는가?
- `.env`와 API key를 안전하게 관리하는가?
- Gemini SDK 기본 호출, REST 보충 호출, mock-first 호출 흐름이 구분되어 있는가?
- `provider`, `model`, `actual_api_called`, `llm_call_mode`로 LLM 호출 상태를 기록하는가?
- OpenAI 호출은 선택 또는 비교 실습으로 분리되어 있는가?
- Upstash Redis를 사용한다면 Supabase와 역할이 명확히 구분되는가?
- 서비스 로그에 민감 정보가 들어가지 않는가?
- Swagger UI 또는 테스트 결과를 문서에 포함했는가?
- Codex가 생성하거나 제안한 내용을 직접 검토했는가?

## 제출 전 체크리스트

- [ ] `.env`에는 실제 key를 넣고, `.env.example`에는 예시 값만 남겼습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`를 프론트엔드나 README에 노출하지 않았습니다.
- [ ] 실제 LLM API 호출 전 mock-first 버전으로 먼저 테스트했습니다.
- [ ] Gemini SDK를 기본 LLM 연동 방식으로 사용하고, REST는 보충, OpenAI는 선택/비교 흐름으로 분리했습니다.
- [ ] `provider`, `model`, `actual_api_called`, `llm_call_mode` 기준을 API 응답, Supabase 저장, 서비스 로그에 반영했습니다.
- [ ] 실제 LLM API를 사용한다면 최대 출력 길이 같은 비용 제한을 설정했습니다.
- [ ] Supabase update/delete 코드에는 조건이 있습니다.
- [ ] 서비스 로그에 API key, token, 개인정보가 들어가지 않습니다.
- [ ] Swagger UI 또는 TestClient 결과를 문서에 포함했습니다.
- [ ] Codex 리뷰 결과를 그대로 붙이지 않고 본인 판단과 함께 기록했습니다.

## 다음 과정 연결

이 프로젝트 이후에는 `03_supabase-ai-frontend`에서 Streamlit 기반 화면을 만들고, `04_supabase-ai-mini-project`에서 백엔드, 프론트엔드, Supabase 저장 흐름을 통합합니다.
