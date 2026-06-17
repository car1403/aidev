# 99. Final Backend Project

이 단원은 `01_supabase-ai-backend`의 최종 백엔드 프로젝트입니다.

학생은 Python, FastAPI, Supabase, LLM API 연동, 사용자 데이터 관리, 서비스 로그, Codex 기반 코드 리뷰를 하나의 결과물로 정리합니다.

이 프로젝트는 `08_backend-mini-service-practice`에서 만든 작은 미니 서비스를 바탕으로, 학생이 직접 요구사항과 테이블, API, 로그, 보안 점검을 확장하는 단계입니다.

## 프로젝트 주제 예시

```text
Supabase 기반 AI 질문 응답 백엔드 서비스
```

## 필수 포함 요소

| 항목 | 설명 |
| --- | --- |
| FastAPI | REST API endpoint를 구현합니다. |
| Pydantic | 요청/응답 데이터를 검증합니다. |
| Supabase | 사용자 데이터, 질문/응답, 서비스 로그를 저장합니다. |
| Auth/RLS | 사용자별 데이터 접근 제어를 설계합니다. |
| LLM API | Gemini API 연동 흐름을 기본으로 구현하거나 문서화합니다. OpenAI API는 선택/비교 실습으로 유지합니다. |
| Mock LLM | 실제 API key가 없거나 비용을 아끼기 위해 mock 답변 흐름을 제공합니다. |
| Upstash Redis | 선택 항목입니다. TTL 캐시, 요청 횟수 제한, 임시 세션 상태 중 하나를 설계하거나 구현합니다. |
| 서비스 로그 | 성공/실패, 오류, 모델명, 처리 결과를 Supabase에 저장합니다. |
| 보안/비용 점검 | API key 노출, service role key 사용 위치, LLM 비용 제한을 확인합니다. |
| Codex 리뷰 | 코드 설명, 오류 분석, 리팩토링, 리뷰 기록을 남깁니다. |

## 제출 문서

```text
README.md
docs/api-design.md
docs/database-design.md
docs/env-guide.md
docs/test-result.md
docs/codex-review-log.md
docs/security-cost-check.md
docs/service-data-flow.md
```

## 권장 구현 범위

최소 구현:

```text
GET /health
POST /qa
GET /qa
GET /qa/{id}
GET /service-logs
```

선택 구현:

```text
POST /feedback
GET /profiles/{user_id}
Upstash Redis 기반 요청 횟수 제한
Upstash Redis 기반 30초 캐시
```

이 과정에서는 Docker 배포와 SSE 스트리밍을 필수로 요구하지 않습니다. SSE 통합은 `03_supabase-ai-mini-project`, Docker/AWS 운영은 `06_multi-agent-service-ops`에서 진행합니다.

## 추천 프로젝트 흐름

```text
1. 요구사항 정리
2. API 설계
3. Supabase 테이블 설계
4. mock LLM으로 FastAPI endpoint 구현
5. Supabase 저장 연결
6. 서비스 로그 저장 연결
7. 실제 LLM API 연동 또는 연동 설계 문서화
8. 보안/비용 점검
9. Codex 코드 리뷰
10. 테스트 결과 정리
```

## 평가 기준

- API endpoint가 명확하게 설계되어 있는가?
- Supabase 테이블 구조가 서비스 요구사항과 맞는가?
- `.env`와 API key를 안전하게 관리하는가?
- 사용자별 데이터 접근 제어를 고려했는가?
- LLM API 호출 흐름과 비용/토큰 개념을 설명할 수 있는가?
- mock LLM과 실제 LLM API 호출 흐름을 구분할 수 있는가?
- Upstash Redis를 사용한다면 Supabase와 역할을 명확히 구분했는가?
- 서비스 로그에 민감 정보가 들어가지 않는가?
- Swagger UI 또는 테스트 결과를 제출했는가?
- Codex가 생성한 코드를 학생이 직접 검토했는가?

## 제출 전 체크리스트

- [ ] `.env`에 실제 key를 넣고, `.env.example`에는 예시 값만 남겼습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`를 프론트엔드나 README에 노출하지 않았습니다.
- [ ] 실제 LLM API 호출 전 mock 버전으로 먼저 테스트했습니다.
- [ ] 실제 LLM API를 사용한다면 `max_tokens` 같은 비용 제한을 설정했습니다.
- [ ] Supabase update/delete 코드에 조건이 있습니다.
- [ ] 서비스 로그에 API key, token, 개인정보가 들어가지 않습니다.
- [ ] Swagger UI 또는 TestClient 결과를 문서에 남겼습니다.
- [ ] Codex 리뷰 결과를 그대로 붙이지 않고 본인 판단을 함께 기록했습니다.

## 다음 과정 연결

이 프로젝트 이후에는 `02_supabase-ai-frontend`에서 Streamlit 기반 화면을 만들고, `03_supabase-ai-mini-project`에서 백엔드와 프론트엔드를 통합합니다.
