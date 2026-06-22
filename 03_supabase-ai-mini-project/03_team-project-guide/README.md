# 03_team-project-guide

이 폴더는 `03_supabase-ai-mini-project`의 팀 프로젝트 진행 가이드입니다.

이번 미니 프로젝트의 기준 주제는 **실시간 로그 대시보드 인터페이스**입니다. `01_supabase-ai-backend`와 `02_supabase-ai-frontend`에서 배운 내용을 연결해, Supabase, FastAPI, Streamlit으로 로그를 저장, 조회, 시각화하는 작은 웹 서비스를 완성합니다.

## 프로젝트 큰 방향

이번 프로젝트는 아래 3가지를 목표로 진행합니다.

```text
1. 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습
2. 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작
3. 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화
```

03 과정에서는 Supabase 클라우드 프로젝트와 로컬 FastAPI/Streamlit 실행을 기준으로 합니다. Docker, Docker Compose, AWS 배포, GitHub Actions 자동화는 `06_multi-agent-service-ops`에서 학습합니다.

## 최종 프로젝트 주제

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

## 필수 산출물

팀은 아래 4가지 산출물을 반드시 제출합니다.

| 산출물 | 설명 |
| --- | --- |
| API 설계 문서 | FastAPI 엔드포인트, HTTP Method, Request/Response, 에러 응답 규칙 |
| 화면 설계서 | 메인, 상세, 입력, 설정, 오류 화면의 와이어프레임과 사용자 액션 흐름 |
| 데이터베이스 설계서 | Supabase 테이블, 컬럼, 관계, 제약조건, ERD |
| 대시보드 구현 결과물 | 실행 가능한 Streamlit 대시보드와 핵심 기능 시연 |

## 권장 구조

```text
team-project
|-- backend
|-- frontend
|-- docs
| |-- api-spec.md
| |-- ui-design.md
| |-- supabase-schema.md
| |-- dashboard-result.md
| |-- streaming-response-design.md
| `-- test-checklist.md
|-- presentation
| `-- final-presentation.md
|--.env.example
`-- README.md
```

## 제출 전 확인할 것

- 백엔드가 `uvicorn`으로 실행되는가?
- 프론트엔드가 `streamlit run`으로 실행되는가?
- Supabase 테이블 설계 문서가 있는가?
- API 명세와 테스트 체크리스트가 있는가?
- 화면 설계서에 주요 화면과 사용자 액션 흐름이 정리되어 있는가?
- 구현된 대시보드가 로그 수집, 조회, 시각화 기능을 보여주는가?
- README만 보고 실행할 수 있는가?
