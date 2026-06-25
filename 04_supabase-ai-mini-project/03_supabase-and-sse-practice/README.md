# 63_supabase-and-sse-practice

이 단원은 팀 프로젝트에 필요한 핵심 기능을 단계별로 실습하는 공간입니다.

`61_local-dev-basic`에서는 로컬 실행 감각을 익히고, `62_instructor-sample-project`에서는 완성된 샘플을 먼저 확인했습니다. 이제 이 단원에서는 Supabase 테이블 설계, FastAPI API, Streamlit 화면, 서비스 로그, SSE 기반 실시간 응답 흐름을 작은 단계로 나누어 직접 구성합니다.

## 이 단원에서 만드는 흐름

```text
Supabase 테이블 준비
-> FastAPI에서 Supabase 데이터 조회/저장 API 구현
-> Streamlit에서 FastAPI API 호출
-> 서비스 로그와 사용자 피드백 저장
-> SSE로 AI 응답 생성 과정을 실시간 표시
```

## 폴더 구성

```text
63_supabase-and-sse-practice
├─ README.md
├─ 61_supabase-project-and-schema
├─ 62_fastapi-supabase-api
├─ 63_streamlit-dashboard-ui
├─ 64_service-log-and-feedback
└─ 65_sse-streaming-ai-response
```

## 학습 순서

1. `61_supabase-project-and-schema`
   - Supabase 프로젝트, API key, `.env`, 테이블 구조를 정리합니다.
   - 처음에는 테이블을 많이 만들기보다 `profiles`, `conversations`, `messages`, `service_logs`, `feedbacks` 정도로 시작합니다.

2. `62_fastapi-supabase-api`
   - FastAPI가 Supabase와 통신하는 백엔드 역할을 하도록 구성합니다.
   - Streamlit이 Supabase에 직접 접근하지 않고 FastAPI를 호출하는 구조를 익힙니다.

3. `63_streamlit-dashboard-ui`
   - Streamlit에서 FastAPI API를 호출해 데이터를 화면에 표시합니다.
   - 로그 목록, 간단한 통계, 사용자 피드백 입력 화면을 구성합니다.

4. `64_service-log-and-feedback`
   - API 호출 결과, 오류, 사용자 피드백을 Supabase에 저장하는 흐름을 정리합니다.
   - 프로젝트 산출물에서 서비스 품질을 설명할 수 있도록 로그 기준을 문서화합니다.

5. `65_sse-streaming-ai-response`
   - FastAPI의 `StreamingResponse`와 Streamlit 화면 표시를 연결합니다.
   - AI 응답 chunk는 화면에 실시간 표시하고, 최종 assistant 응답만 Supabase에 저장하는 흐름을 설계합니다.

## 중요한 기준

- 63 과정의 기본 데이터 저장소는 Supabase입니다.
- FastAPI는 Supabase와 AI API를 연결하는 백엔드 역할을 합니다.
- Streamlit은 FastAPI API를 호출하는 화면 역할을 합니다.
- SSE는 필수 구현이 아니라 선택 확장입니다.
- 배포도 필수는 아니며, 로컬에서 FastAPI와 Streamlit이 정상 동작하면 기본 제출 기준을 충족합니다.
- Docker, Docker Compose, AWS, GitHub Actions 기반 운영 자동화는 07 과정에서 본격적으로 다룹니다.

## 팀 프로젝트에 연결하는 방법

이 단원의 각 단계는 `99_team-projects`의 팀 프로젝트 문서와 연결됩니다.

```text
61_supabase-project-and-schema
-> docs/supabase-schema.md

62_fastapi-supabase-api
-> docs/api-spec.md

63_streamlit-dashboard-ui
-> docs/ui-design.md

64_service-log-and-feedback
-> docs/dashboard-result.md, docs/test-checklist.md

65_sse-streaming-ai-response
-> docs/streaming-response-design.md
```

## 최종 확인 체크리스트

- [ ] Supabase 프로젝트 URL과 key를 `.env`에 정리했다.
- [ ] `.env`는 GitHub에 올리지 않는다.
- [ ] 테이블 구조를 문서화했다.
- [ ] FastAPI에서 Supabase 데이터를 조회하거나 저장할 수 있다.
- [ ] Streamlit에서 FastAPI API를 호출할 수 있다.
- [ ] 서비스 로그와 사용자 피드백 저장 기준을 정했다.
- [ ] SSE를 적용하는 경우 일반 응답 API와 스트리밍 응답 API의 차이를 설명할 수 있다.
- [ ] 최종 프로젝트 문서에 API, 화면, DB, 로그, 테스트 기준이 정리되어 있다.