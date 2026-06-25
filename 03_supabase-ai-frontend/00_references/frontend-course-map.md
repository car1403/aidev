# Frontend Course Map

이 문서는 `03_supabase-ai-frontend` 과정의 전체 흐름을 한눈에 보기 위한 참고 자료입니다.

## 과정 흐름

```text
00_references
-> 01_streamlit-basic
-> 02_streamlit-ui-components
-> 03_api-integration
-> 04_ai-chatbot-interface
-> 05_state-session-and-data
-> 90_ai-assisted-ui-review-and-debugging
-> 99_final-frontend-project
```

## 단원별 핵심 질문

| 단원 | 핵심 질문 |
| --- | --- |
| `00_references` | 프론트엔드는 전체 AI 서비스에서 어떤 역할을 하나요? |
| `01_streamlit-basic` | Streamlit 앱은 어떻게 실행하고 화면은 어떻게 구성하나요? |
| `02_streamlit-ui-components` | 버튼, 입력창, 테이블, 차트 같은 UI 요소를 어떻게 구성하나요? |
| `03_api-integration` | Streamlit 화면에서 FastAPI API를 어떻게 호출하나요? |
| `04_ai-chatbot-interface` | 사용자 질문과 AI 응답을 대화형 UI로 어떻게 표현하나요? |
| `05_state-session-and-data` | 로그인 상태, 대화 이력, 서비스 로그를 화면에서 어떻게 관리하나요? |
| `90_ai-assisted-ui-review-and-debugging` | AI 보조 도구로 UI 코드 오류와 개선점을 어떻게 찾나요? |
| `99_final-frontend-project` | Streamlit 화면, FastAPI 호출, 서비스 로그, 무료 배포 흐름을 어떻게 하나로 연결하나요? |

## 백엔드 과정과의 연결

`03_supabase-ai-frontend`는 독립적으로 완성되는 과정이 아닙니다. `02_supabase-ai-backend`에서 만든 API를 호출하면서 완성됩니다.

```text
02_supabase-ai-backend
-> FastAPI
-> Supabase Auth / Database
-> Upstash Redis
-> LLM API 호출

03_supabase-ai-frontend
-> Streamlit 화면
-> API 호출
-> 로그인 상태 표시
-> 대화 이력 표시
-> 서비스 로그 조회
```

## 03 미니 프로젝트와의 연결

`04_supabase-ai-mini-project`에서는 01과 02에서 배운 내용을 묶어 통합 프로젝트를 진행합니다.

특히 다음 내용은 03에서 본격적으로 다룹니다.

```text
SSE 기반 실시간 AI 응답 스트리밍
백엔드 스트리밍 응답
Streamlit 실시간 표시
Supabase 최종 메시지 저장
통합 대시보드 산출물
```

02 과정에서는 SSE를 깊게 구현하기보다, 프론트엔드가 백엔드 API를 호출하고 응답을 화면에 표시하는 기본 흐름을 확실히 익히는 데 집중합니다.

## 06 운영 과정과의 연결

`02`에서는 무료 배포 서비스 기반의 간단한 배포 흐름만 안내합니다.

```text
FastAPI -> Render
Redis -> Upstash
Streamlit -> Streamlit Community Cloud
```

Docker Compose, AWS, GitHub Actions, 모니터링, Auto Healing은 `07_multi-agent-service-ops`에서 더 깊게 다룹니다.

## 99 최종 프론트엔드 프로젝트

`99_final-frontend-project`는 02 과정에서 배운 화면 구성, API 호출, 대화 이력 조회, 서비스 로그 조회를 하나의 작은 서비스 예제로 연결합니다.

```text
Streamlit 프론트엔드
-> FastAPI 백엔드
-> 대화 이력 조회
-> 서비스 로그 조회
-> 무료 배포 흐름 점검
```

이 프로젝트는 기본 단원용 `.env`가 아니라 자기 폴더 안의 `.env`를 사용합니다.

```text
C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\.env
```

03 미니 프로젝트에서는 이 흐름을 Supabase 테이블 저장, Gemini 응답 생성, SSE 스트리밍, 프로젝트 산출물 작성으로 확장합니다.
