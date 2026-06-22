# AI Development Course

이 저장소는 Python 기초부터 Supabase 기반 AI 서비스, LLM Agent, Docker 기반 운영, AI Workflow 자동화까지 단계적으로 학습하기 위한 실습형 강의 저장소입니다.

각 과정 폴더의 README를 기준으로 실습을 진행하고, `00_admin`의 운영 안내 자료를 함께 확인하면서 설치, 실습, 프로젝트, 평가 흐름을 단계적으로 따라갑니다.

## 학습 대상

이 저장소는 아래 목표를 가진 입문자와 실습 중심 학습 과정을 기준으로 구성되어 있습니다.

```text
Python을 처음 배우는 경우
FastAPI와 Streamlit으로 AI 서비스를 만들어 보고 싶은 경우
Supabase로 데이터 저장, 인증, 대화 이력을 다루고 싶은 경우
LLM API, Agent, RAG, Tool Calling을 단계적으로 배우고 싶은 경우
Docker, Docker Compose, AWS, GitHub Actions 운영 흐름을 익히고 싶은 경우
AIPP, n8n, Dify 같은 AI Workflow 도구를 실습하고 싶은 경우
```

## 전체 과정

| 번호 | 폴더 | 핵심 내용 |
| --- | --- | --- |
| 00 | `00_admin` | 수업 시작 안내, 설치, VS Code, `.venv`, Codex, 결제, 평가 자료 |
| 01 | `01_supabase-ai-backend` | Python, FastAPI, Gemini, Supabase, Upstash Redis 기반 백엔드 |
| 02 | `02_supabase-ai-frontend` | Streamlit UI, API 호출, 챗봇 화면, 사용자 상태 관리 |
| 03 | `03_supabase-ai-mini-project` | Supabase + FastAPI + Streamlit 통합 미니 프로젝트, SSE 스트리밍 |
| 04 | `04_llm-agent-orchestration` | Docker 기반 LLM Agent, Tool, Memory, RAG, LangGraph |
| 05 | `05_llm-agent-mini-project` | LangGraph 기반 단일 Agent 미니 프로젝트 |
| 06 | `06_multi-agent-service-ops` | Multi-Agent 협업, Docker Compose, AWS, GitHub Actions, 운영/보안 |
| 07 | `07_multi-agent-service-mini-project` | Auto Healing Workflow 기반 Multi-Agent 서비스 운영 미니 프로젝트 |
| 08 | `08_ai-workflow-automation` | AIPP, n8n, Dify 기반 AI Workflow 설계와 운영 |
| 09 | `09_ai-workflow-mini-project` | 노코드/로코드 기반 AI Workflow 미니 프로젝트 |

## 처음 시작하는 순서

처음 수업을 시작할 때는 아래 순서대로 진행합니다.

```text
1. 00_admin/README.md 읽기
2. Python 설치 확인
3. VS Code 설치 확인
4. VS Code 확장 설치
5. Markdown Preview 사용법 확인
6. PowerShell 기본 명령 확인
7. 과정 폴더 최상위에.venv 만들기
8. requirements.txt 설치
9. 예제 Python 파일 실행
10. 오류가 나오면 README와 troubleshooting 문서 확인
```

가장 먼저 볼 문서:

```text
00_admin/README.md
00_admin/03_student-guides/01_getting-started/README.md
```

## 과정별 환경 기준

### 01~03 Supabase 기반 AI 서비스

01~03 과정은 Supabase 중심으로 진행합니다.

```text
FastAPI
Streamlit
Supabase
Gemini 2.5 Flash-Lite
Upstash Redis
SSE streaming
```

Docker는 01~03에서 필수로 사용하지 않습니다.

03 미니 프로젝트에서는 선택 실습으로 아래 무료 배포 흐름을 다룰 수 있습니다.

```text
FastAPI -> Render
Redis -> Upstash
Streamlit -> Streamlit Community Cloud
```

### 04~05 LLM Agent

04부터 Docker Desktop을 사용합니다.

```text
Docker Desktop
Llama 계열 로컬 LLM
PostgreSQL
pgvector
LangGraph
LangSmith
RAG
Tool Calling
```

04~05에서는 Docker Compose보다 Docker Desktop에서 필요한 컨테이너를 직접 실행하는 흐름을 먼저 익힙니다.

### 06~07 Multi-Agent Service Ops

06부터 운영 관점을 본격적으로 다룹니다.

```text
Docker Compose
AWS
GitHub Actions
CI/CD
CloudWatch
Auto Healing
Guardrails
Multi-Agent 협업
```

### 08~09 AI Workflow Automation

08~09는 노코드/로코드 AI Workflow 설계와 미니 프로젝트를 다룹니다.

```text
AIPP
n8n
Dify
Trigger / Condition / Action
RAG Node
Data Processing Node
Workflow Ops Assistant
```

## 가상환경 기준

각 과정은 과정 폴더 최상위에 `.venv` 하나를 사용합니다.

예시:

```text
01_supabase-ai-backend/.venv
02_supabase-ai-frontend/.venv
03_supabase-ai-mini-project/.venv
04_llm-agent-orchestration/.venv
```

하위 실습 폴더마다 `.venv`를 새로 만들지 않습니다.

기본 실행 흐름:

```powershell
cd C:\aidev\01_supabase-ai-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Git과 보안 주의

GitHub에 올리면 안 되는 파일과 정보가 있습니다.

```text
.env
.venv
__pycache__
실제 API key
Supabase service role key
Gemini API key
OpenAI API key
Upstash Redis token
개인정보가 들어간 테스트 데이터
```

GitHub에는 보통 아래 파일을 올립니다.

```text
README.md
SETUP.md
requirements.txt
.env.example
Python 코드
실습 문서
과제 문서
```

## AI 모델 사용 기준

01~03 과정에서는 `Gemini 2.5 Flash-Lite`를 기본 AI 모델 예제로 사용합니다.

OpenAI 예제 파일은 선택 또는 심화 실습용으로 유지합니다.

04~09 과정에서는 학습 목적에 따라 OpenAI, Gemini, Llama 계열 모델을 비교하거나 선택적으로 사용할 수 있습니다.

OpenAI 모델 예제는 과정 문서 기준에 맞춰 `gpt-4.1-mini`를 기본 예시로 사용합니다.

## 수업 진행 방식

각 과정은 보통 아래 흐름으로 진행합니다.

```text
README 읽기
-> SETUP 확인
-> 예제 실행
-> Lab 실습
-> Assignment 작성
-> Mini Project 또는 Final Project
-> 발표와 코드 리뷰
```

각 폴더의 README를 먼저 읽고, `00_admin`의 체크리스트와 수업 계획서를 함께 사용합니다.

## 추천 시작 위치

처음 시작한다면 아래 문서부터 여십시오.

```text
00_admin/README.md
01_supabase-ai-backend/README.md
01_supabase-ai-backend/SETUP.md
```

이후 과정은 01부터 09까지 순서대로 진행하는 것을 권장합니다.
