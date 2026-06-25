# 04_team-project-guide

이 폴더는 `04_supabase-ai-mini-project`의 팀 프로젝트 진행 가이드입니다.

`01_local-dev-basic`에서 로컬 실행 감각을 익히고, `02_instructor-sample-project`에서 완성된 샘플을 확인한 뒤, `03_supabase-and-sse-practice`에서 핵심 기능을 단계별로 연습합니다. 이 단원에서는 팀 프로젝트의 주제, 역할, 요구사항, 일정, 발표, 제출 기준을 정리합니다.

## 03 과정 안에서의 위치

```text
01_local-dev-basic
-> 로컬 .venv/.env, FastAPI, Streamlit, Supabase 연결 확인

02_instructor-sample-project
-> 완성된 학습 로그 대시보드 샘플 확인

03_supabase-and-sse-practice
-> Supabase 테이블, FastAPI API, Streamlit UI, 로그/피드백, SSE 기능 실습

04_team-project-guide
-> 팀 프로젝트 주제, 역할, 요구사항, 일정, 발표, 제출 기준 정리

05_project-templates
-> 팀 프로젝트에 복사해서 쓸 문서, SQL, 환경 변수, 체크리스트 템플릿 확인

99_team-projects
-> 실제 팀 프로젝트 작업 공간
```

## 프로젝트 기본 주제

이번 미니 프로젝트의 기본 주제는 **실시간 로그 대시보드 인터페이스**입니다.

`02_supabase-ai-backend`와 `03_supabase-ai-frontend`에서 배운 내용을 연결해 Supabase, FastAPI, Streamlit으로 로그를 저장, 조회, 시각화하는 작은 서비스를 완성합니다.

```text
분야:
웹 서비스 기초 및 AI 백엔드 개발

프로젝트:
실시간 로그 대시보드 인터페이스

핵심 설명:
사용자 요청, AI 응답, 오류, 피드백, 처리 시간 같은 로그 데이터를 Supabase에 저장하고,
FastAPI API를 통해 조회하며,
Streamlit 화면에서 대시보드로 시각화합니다.
```

## 프로젝트 진행 방향

이번 프로젝트는 아래 3가지를 목표로 진행합니다.

```text
1. 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습
2. 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작
3. 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화
```

03 과정에서는 Supabase 클라우드 프로젝트와 로컬 FastAPI/Streamlit 실행을 기준으로 합니다.

```text
가상환경:
C:\aidev\04_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\04_supabase-ai-mini-project\.env
```

Docker, Docker Compose, AWS 배포, GitHub Actions 자동화는 `07_multi-agent-service-ops`에서 학습합니다. 03 과정의 배포는 선택 시연이며, 기본 제출 기준은 로컬에서 정상 동작하는 것입니다.

## 필수 산출물

팀은 아래 4가지 산출물을 필수로 제출합니다. 그 외 프로젝트 계획서, 테스트 체크리스트, 발표 자료, 배포 문서, SSE 설계 문서는 선택 보조 산출물입니다.

| 산출물 | 설명 |
| --- | --- |
| API 설계 문서 | FastAPI 엔드포인트, HTTP Method, Request/Response, 오류 응답 규칙 |
| 화면 설계서 | 메인, 상세, 입력, 설정, 오류 화면의 와이어프레임과 사용자 액션 흐름 |
| 데이터베이스 스키마 설계서 | Supabase 테이블, 컬럼, 관계, 제약조건, ERD, RLS 정책 |
| 대시보드 구현 결과물 | 실행 가능한 Streamlit 대시보드와 핵심 기능 시연 |

## 팀 구성

팀 구성은 4~5명을 권장합니다.

```text
Backend/API
-> FastAPI 엔드포인트, Pydantic 모델, Supabase 연동

Database/Supabase
-> 테이블 설계, SQL, RLS, 테스트 데이터

Frontend/UI
-> Streamlit 화면, API 호출, 대시보드 구성

AI/Quality
-> Gemini 연동, 프롬프트, 응답 품질, 피드백 흐름

Docs/Presentation
-> 필수 산출물 문서 정리, 선택적으로 제출 체크리스트와 발표 자료 작성
```

## 제출 전 확인할 것

- 백엔드가 `uvicorn`으로 실행되는가?
- 프론트엔드가 `streamlit run`으로 실행되는가?
- API 설계 문서가 있는가?
- 화면 설계서가 있는가?
- 데이터베이스 스키마 설계서가 있는가?
- 대시보드 구현 결과물이 정리되어 있는가?
- 화면 설계서에 주요 화면과 사용자 액션 흐름이 정리되어 있는가?
- 구현된 대시보드가 로그 수집, 조회, 시각화 기능을 보여주는가?
- `SUPABASE_SERVICE_ROLE_KEY`가 프론트엔드에 노출되지 않았는가?
- README만 보고 실행할 수 있는가?
