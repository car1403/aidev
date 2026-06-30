# 99_final-frontend-project

이 단원은 `03_supabase-ai-frontend`의 최종 프로젝트입니다.

목표는 **개인화 AI 챗봇 서비스 통합 구현, 서비스 로그 수집, 최종 배포 실습 흐름 이해**입니다. 수강생은 Streamlit 화면에서 회원가입, 로그인, token 저장, 챗봇 대화, 이전 대화 조회, 서비스 로그 조회, 응답 생성 상태 표시를 하나의 UX로 연결합니다.

## 프로젝트 목표

```text
회원가입
-> 로그인
-> access_token 저장
-> Authorization header로 보호 API 호출
-> 챗봇 질문/응답
-> 이전 대화 기록 조회
-> 서비스 로그 조회
-> 배포 전 점검
```

## backend 사용 기준

이 프로젝트에는 backend가 두 종류 있습니다.

| 폴더 | 역할 | 수업 기준 |
| --- | --- | --- |
| `backend_mock` | 프론트 개발용 제공 backend입니다. Supabase, Gemini, Redis 없이 메모리로 동작합니다. | 필수 |
| `backend_service` | 실제 서비스 연결용 backend입니다. Supabase Auth/DB, Gemini, 선택형 Upstash Redis를 사용합니다. | 선택/심화 |

초보자 수업에서는 먼저 `backend_mock`으로 화면과 API 연결 흐름을 완성합니다. 이후 시간이 있거나 배포 실습까지 진행할 때 `backend_service`로 바꿔 연결합니다.

## 제공 API

`backend_mock`과 `backend_service`는 같은 API 계약을 사용합니다.

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | backend 상태 확인 |
| POST | `/auth/signup` | 회원가입 |
| POST | `/auth/signin` | 로그인과 token 발급 |
| POST | `/auth/signout` | 로그아웃 |
| GET | `/me` | 현재 사용자 조회 |
| POST | `/chat` | AI 답변 생성 |
| GET | `/conversations` | 사용자 대화 기록 조회 |
| GET | `/service-logs` | 서비스 로그 조회 |

## 폴더 구조

```text
99_final-frontend-project
├─ README.md
├─ backend_mock
├─ backend_service
├─ starter
├─ solution
├─ templates
└─ checklist
```

## 필수 구현 범위

| 항목 | 기준 |
| --- | --- |
| Streamlit 챗봇 UI | 사용자 메시지와 assistant 응답을 구분해 표시합니다. |
| 회원가입/로그인 UI | backend의 `/auth/signup`, `/auth/signin`을 호출합니다. |
| 로그인 상태 유지 | `st.session_state`에 `access_token`과 사용자 정보를 저장합니다. |
| Authorization header | 보호 API 호출 시 `Bearer token`을 보냅니다. |
| 대화 기록 조회 | `/conversations` 응답을 화면에 표시합니다. |
| 응답 생성 상태 | `st.spinner`, `st.status`, `st.empty` 등으로 생성 중 상태를 보여 줍니다. |
| 서비스 로그 조회 | `/service-logs` 응답을 표로 표시합니다. |
| 보안 | 프론트엔드에 service role key, LLM API key, Redis token을 두지 않습니다. |

## 선택 구현 범위

| 항목 | 설명 |
| --- | --- |
| 실제 Supabase Auth | `backend_service`에서 Supabase Auth 회원가입/로그인을 연결합니다. |
| 실제 Gemini 호출 | `backend_service`에서 Gemini API를 호출합니다. |
| Upstash Redis | 배포 시 Redis 캐시/세션 저장소로 선택 확장합니다. |
| 실제 배포 | FastAPI -> Render, Redis -> Upstash, Streamlit -> Streamlit Community Cloud 흐름을 선택 적용합니다. |
| React 구조 비교 | React 실습 확대는 훈련생 수준과 진도에 따라 선택 적용합니다. |
| SSE 스트리밍 | 04 미니 프로젝트에서 본격적으로 다룹니다. |

## 실행 순서

PowerShell 1: 프론트 개발용 mock backend 실행

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_mock
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

PowerShell 2: frontend solution 실행

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\solution
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

선택: 실제 서비스 backend 실행

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_service
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 배포 실습 기준

무료 배포 서비스 활용은 과정 산출물에 포함하되, 실제 배포 수행은 수업 시간과 훈련생 수준에 따라 선택 적용합니다.

```text
FastAPI -> Render
Redis -> Upstash
Streamlit -> Streamlit Community Cloud
```

자세한 배포 절차는 [06_deployment-checklist.md](templates/06_deployment-checklist.md)를 확인합니다.

완성 후 점검은 [final-checklist.md](checklist/final-checklist.md)를 확인합니다.

Docker, AWS, GitHub Actions 기반 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 다음 과정 연결

이 프로젝트는 `04_supabase-ai-mini-project`로 넘어가기 전 프론트엔드 통합 감각을 정리하는 단계입니다. SSE 스트리밍, Supabase 최종 저장, 피드백 데이터, 팀 프로젝트 산출물은 `04_supabase-ai-mini-project`에서 본격적으로 다룹니다.
