# Supabase Team Project Template

Supabase 기반 팀 프로젝트 시작 템플릿입니다.

이번 팀 프로젝트의 기준 주제는 **실시간 로그 대시보드 인터페이스**입니다. 팀은 이 템플릿을 복사한 뒤, 프로젝트 목적에 맞게 Supabase 테이블, FastAPI API, Streamlit 화면, 대시보드 지표를 수정해서 사용합니다.

## 프로젝트 진행 방향

```text
1. 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습
2. 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작
3. 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화
```

## 구조

```text
team-template
|-- README.md
|--.env.example
|-- backend
|-- frontend
|-- docs
| |-- project-plan.md
| |-- api-spec.md
| |-- ui-design.md
| |-- supabase-schema.md
| |-- dashboard-result.md
| |-- streaming-response-design.md
| |-- deployment-guide.md
| `-- test-checklist.md
`-- presentation
 `-- final-presentation.md
```

## 필수 산출물

| 산출물 | 파일 |
| --- | --- |
| API 설계 문서 | `docs/api-spec.md` |
| 화면 설계서 | `docs/ui-design.md` |
| 데이터베이스 설계서 | `docs/supabase-schema.md` |
| 대시보드 구현 결과물 | `docs/dashboard-result.md` |
| 선택 배포 설명서 | `docs/deployment-guide.md` |

각 산출물은 실제 코드와 일치해야 합니다. 예를 들어 `docs/api-spec.md`에 `GET /api/logs`가 있다면 FastAPI 코드에도 같은 endpoint가 있어야 하고, Streamlit 화면에서도 해당 API를 호출해야 합니다.

## 기본 실행 흐름

```text
Supabase 테이블 준비
-> backend 실행
-> frontend 실행
-> Streamlit에서 FastAPI 호출
-> FastAPI에서 Supabase 호출
-> 로그 저장/조회/시각화
-> SSE 또는 자동 새로고침으로 AI 응답 또는 로그 상태를 실시간 표시
```

## 실시간 표시 기준

이번 미니 프로젝트는 실시간 로그 대시보드 인터페이스가 주제입니다. 따라서 팀은 아래 둘 중 하나의 방식을 선택해 실시간성을 설명하고 구현합니다.

```text
기본 구현:
Streamlit 새로고침 버튼 또는 주기적 재조회로 최신 로그 표시

권장 확장:
SSE로 AI 응답 또는 로그 상태를 실시간 표시
```

AI 응답 생성 시간이 길거나 로그 상태를 실시간으로 보여주고 싶다면 Server-Sent Events(SSE)를 적용합니다.

```text
FastAPI /api/chat/stream
-> text/event-stream 응답
-> Streamlit 화면에 chunk 실시간 표시
-> 완료 후 최종 assistant 응답과 로그를 Supabase에 저장
```

예제 파일:

```text
backend/streaming_example.py
frontend/streaming_app.py
docs/streaming-response-design.md
```

## 팀에서 수정할 것

- 프로젝트명
- 수집할 로그 종류
- Supabase 테이블명
- API 경로와 HTTP Method
- Pydantic 모델
- Streamlit 대시보드 화면
- 차트/테이블/필터 구성
- 사용자 피드백 데이터 활용 방식
- SSE 적용 여부와 최종 데이터 저장 방식
- Render, Upstash, Streamlit Community Cloud 배포 여부
- 배포 URL과 배포 중 발생한 오류 해결 과정
- 문서와 발표 자료

## 선택 배포 구조

배포는 필수가 아닙니다. 팀 프로젝트의 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase 연동을 시연하는 것입니다. 시간이 충분하거나 외부 URL로 결과물을 보여주고 싶은 팀은 무료 배포 서비스를 선택적으로 사용합니다.

팀 프로젝트를 무료 배포 서비스에 올릴 경우 아래 구조를 기준으로 합니다.

```text
Streamlit Community Cloud
-> Render FastAPI Backend
-> Supabase Database/Auth
-> Upstash Redis 선택 사용
```

배포할 때는 `backend`와 `frontend`가 각각 독립적으로 실행될 수 있어야 합니다.

```text
backend/requirements.txt -> Render에서 설치
frontend/requirements.txt -> Streamlit Community Cloud에서 설치
```

배포 절차와 환경변수 등록 기준은 `docs/deployment-guide.md`에 정리합니다.
