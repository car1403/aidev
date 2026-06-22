# 00_admin

`00_admin`은 `C:\aidev` 전체 수업을 진행하기 위한 공용 안내 폴더입니다.

이 폴더는 별도 관리용 폴더가 아니라, **수업을 시작하고 운영할 때 함께 열어 보는 공용 운영 안내서**입니다.

여기에서는 개발 환경 준비 방법, VS Code 사용법, Markdown 문서 보는 법, `.venv` 사용법, Codex 설치와 로그인 방법, OpenAI 계정과 결제의 차이, 과정별 학습 순서, 프로젝트 제출 기준, 수업 진행 체크리스트, 평가표, 프로젝트 운영 자료를 한곳에서 확인합니다.

## 먼저 읽는 순서

처음 수업을 시작할 때는 아래 순서대로 읽습니다.

```text
00_admin/README.md
-> 03_student-guides/01_getting-started/README.md
-> 03_student-guides/01_getting-started/01_python-install-guide.md
-> 03_student-guides/01_getting-started/02_vscode-install-guide.md
-> 03_student-guides/01_getting-started/03_vscode-extensions-guide.md
-> 03_student-guides/01_getting-started/06_markdown-preview-guide.md
-> 03_student-guides/01_getting-started/08_codex-install-and-login-guide.md
-> 03_student-guides/01_getting-started/09_openai-account-billing-guide.md
-> 03_student-guides/01_getting-started/07_first-run-checklist.md
```

수업 전체 흐름을 보고 싶을 때는 아래 문서를 봅니다.

```text
01_curriculum-overview/01_course-roadmap.md
01_curriculum-overview/02_course-sequence.md
01_curriculum-overview/04_folder-map.md
```

## 전체 과정

현재 `C:\aidev`는 아래 과정으로 구성되어 있습니다.

| 번호 | 폴더 | 수업 핵심 |
| --- | --- | --- |
| 01 | `01_supabase-ai-backend` | Python, FastAPI, Supabase 기반 백엔드 |
| 02 | `02_supabase-ai-frontend` | Streamlit, API 호출, AI 서비스 UI |
| 03 | `03_supabase-ai-mini-project` | Supabase 기반 AI 미니 프로젝트, SSE 스트리밍 통합 실습 |
| 04 | `04_llm-agent-orchestration` | Docker 기반 LLM Agent, Tool, Memory, RAG |
| 05 | `05_llm-agent-mini-project` | LLM Agent 미니 프로젝트 |
| 06 | `06_multi-agent-service-ops` | Docker Compose, AWS, GitHub Actions, 운영/보안 |
| 07 | `07_multi-agent-service-mini-project` | Multi-Agent 서비스 운영 미니 프로젝트 |
| 08 | `08_ai-workflow-automation` | AIPP, n8n, Dify 기반 AI Workflow 자동화 |
| 09 | `09_ai-workflow-mini-project` | AI Workflow 미니 프로젝트 |

## 00_admin 구조

수업에서는 아래의 번호가 붙은 구조를 기준으로 안내합니다.

```text
00_admin
|-- README.md
|-- 01_curriculum-overview
|-- 02_class-operation
|-- 03_student-guides
|   |-- 01_getting-started
|   |-- 02_how-to-study
|   `-- 03_submission-guide
|-- 04_lesson-plans
|-- 05_checklists
|-- 06_rubrics-and-evaluation
|-- 07_project-management
|-- 08_environment-and-troubleshooting
`-- 09_templates
```

함께 볼 때는 번호가 붙은 새 폴더를 기준으로 안내하면 됩니다.

## 폴더별 역할

| 폴더 | 역할 |
| --- | --- |
| `01_curriculum-overview` | 01~09 전체 과정의 큰 그림, 순서, 목표, 도구 지도 |
| `02_class-operation` | 강의 진행 방식, 실시간 코딩, Q&A, 시간 관리 |
| `03_student-guides` | 설치, VS Code, PowerShell, `.venv`, Markdown, Codex, OpenAI 계정 안내 |
| `04_lesson-plans` | 01~09 과정별 수업 계획 |
| `05_checklists` | 수업 전/중/후, 프로젝트, 발표 체크리스트 |
| `06_rubrics-and-evaluation` | 평가 기준과 루브릭 |
| `07_project-management` | 팀 구성, 주제 선정, 일정 관리, 제출 현황 |
| `08_environment-and-troubleshooting` | 설치/실행 중 자주 만나는 오류 해결 |
| `09_templates` | README, 과제, 프로젝트, 발표 자료 템플릿 |

## 처음 시작할 때 가장 중요한 원칙

처음에는 모든 것을 한 번에 이해하려고 하지 않아도 됩니다.

아래 순서만 지키면 됩니다.

```text
1. README.md를 Preview로 읽는다.
2. Python과 VS Code 설치 상태를 확인한다.
3. 필요한 VS Code 확장을 설치한다.
4. Codex를 사용할 경우 설치와 로그인을 확인한다.
5. OpenAI 계정과 결제 방식의 차이를 이해한다.
6. PowerShell에서 현재 폴더 위치를 확인한다.
7. 과정 폴더 최상위에 .venv를 만든다.
8. .venv를 활성화한다.
9. requirements.txt를 설치한다.
10. 예제 파일 하나를 실행한다.
11. 오류가 나오면 오류 메시지를 복사해 원인을 확인한다.
```

## Codex와 OpenAI 계정 안내

Codex는 이 수업에서 코드 작성, 코드 설명, 오류 분석, README 보강, 실습 구조 점검에 활용할 수 있는 OpenAI의 코딩 보조 도구입니다.

Codex와 OpenAI 계정 설정은 아래 문서를 먼저 확인합니다.

```text
03_student-guides/01_getting-started/08_codex-install-and-login-guide.md
03_student-guides/01_getting-started/09_openai-account-billing-guide.md
```

중요한 점은 **ChatGPT 구독 결제**와 **OpenAI API Platform 결제**가 서로 다르다는 것입니다.

ChatGPT에서 Codex를 사용하는 것과, Python 코드에서 OpenAI API를 호출해 비용이 발생하는 것은 별개의 흐름입니다. 수업에서 API 키를 사용하는 실습은 필요한 시점에 별도로 안내합니다.

## 가상환경 기준

각 과정은 과정 폴더 최상위의 `.venv` 하나를 사용합니다.

예:

```text
01_supabase-ai-backend/.venv
02_supabase-ai-frontend/.venv
03_supabase-ai-mini-project/.venv
```

하위 실습 폴더마다 `.venv`를 새로 만들지 않습니다.

## Docker 기준

01~03 과정은 Supabase 중심으로 진행합니다. Docker는 본격적으로 `06_multi-agent-service-ops`에서 다룹니다.

04~05 과정에서는 Docker Desktop에서 컨테이너를 직접 실행해 LLM, PostgreSQL, pgvector 같은 환경을 경험합니다. 06 과정에서는 Docker Compose, AWS, GitHub Actions까지 확장합니다.

## AI 모델 기준

01~03 과정에서는 초보자가 비용 부담을 줄이고 쉽게 시작할 수 있도록 `Gemini 2.5 Flash-Lite`를 기본 AI 모델 예제로 사용합니다.

OpenAI 예제 파일은 필요할 때 선택적으로 사용할 수 있도록 유지합니다. 수업에서는 먼저 Gemini API Key 발급, `.env` 설정, 기본 호출 흐름을 익힌 뒤, 추가 비교나 심화 실습에서 OpenAI API를 다룰 수 있습니다.

04~09 과정에서는 학습 목적에 따라 OpenAI, Gemini, Llama 계열 모델을 비교하거나 선택적으로 사용합니다. OpenAI 모델 예제는 과정 문서 기준에 맞춰 `gpt-4.1-mini`를 기본 예시로 사용합니다.

## Redis와 무료 배포 기준

01~03 과정에서 Redis가 필요한 경우 로컬 Redis나 Docker Redis 대신 `Upstash Redis`를 우선 사용합니다.

초보자 배포 실습은 아래 무료 또는 무료 체험 기반 흐름을 기준으로 설명합니다.

```text
FastAPI -> Render
Redis -> Upstash
Streamlit -> Streamlit Community Cloud
Supabase -> 관리형 데이터베이스와 Auth
```

03 미니 프로젝트에서는 배포를 필수로 보지 않고, 수업 시간과 진도와 난이도에 따라 선택 실습으로 진행합니다.

## SSE 기준

Server-Sent Events(SSE) 기반 실시간 AI 응답 스트리밍은 `03_supabase-ai-mini-project`에서 통합 실습으로 다룹니다.

```text
FastAPI SSE 엔드포인트
-> Streamlit 실시간 응답 표시
-> Supabase 최종 메시지 저장
```

01과 02에서는 기본 백엔드/프론트엔드 구조를 먼저 배우고, 03에서 실제 프로젝트 기능으로 연결합니다.
