# 06_multi-agent-service-ops

이 과정은 **Multi-Agent 기반 AI 서비스를 실제 운영 가능한 형태로 구성하는 방법**을 학습하는 과정입니다.

04 과정에서는 단일 Agent, Tool, RAG, Memory, LangGraph 같은 실행 원리를 배웠고, 05 과정에서는 그 내용을 바탕으로 LLM Agent 미니 프로젝트를 만들었습니다. 06 과정에서는 그 결과물을 서비스처럼 실행하고 운영하는 방법을 다룹니다.

핵심 흐름은 다음과 같습니다.

```text
Multi-Agent 협업 설계
-> Docker로 서비스 패키징
-> Docker Compose로 여러 서비스 실행
-> Git/GitHub로 변경 관리
-> GitHub Actions로 자동 검증
-> AWS 배포 흐름 이해
-> AI 보안/가드레일 적용
-> Auto Healing 장애 대응
-> 로그/추적/운영 대시보드 구성
```

## 04, 05, 06의 역할

| 과정 | 핵심 역할 | Docker/AWS 범위 |
| --- | --- | --- |
| `04_llm-agent-orchestration` | Prompt, Tool Use, RAG, Memory, LangGraph 원리 학습 | Docker Desktop에서 `docker run`으로 Ollama, pgvector 같은 단일 도구 실행 |
| `05_llm-agent-mini-project` | 단일 Agent 미니 프로젝트 구현 | Docker는 선택 확장 |
| `06_multi-agent-service-ops` | Multi-Agent 서비스를 운영 관점으로 확장 | Docker Compose, GitHub Actions, AWS 배포 흐름, 로그, 모니터링, Auto Healing |

06에서는 Supabase 중심 실습이 아니라 **Docker 기반 서비스 운영 흐름**을 사용합니다. 데이터베이스, 캐시, 백엔드, 프론트엔드, 작업자, 모니터링 화면처럼 여러 구성 요소를 함께 실행하는 감각을 익히는 것이 중요합니다.

## 과정 목표

- 단일 Agent와 Multi-Agent 구조의 차이를 이해합니다.
- 역할 기반 Agent 협업 구조를 설계합니다.
- Agent 간 Handoff, Context 공유, Context 동기화 기준을 정리합니다.
- FastAPI, Streamlit, worker, monitor 서비스를 Docker로 실행합니다.
- Docker Compose로 여러 서비스를 한 번에 실행하고 로그를 확인합니다.
- Git과 GitHub로 코드 변경 이력을 관리합니다.
- GitHub Actions로 Docker build와 기본 검증을 자동화합니다.
- AWS 배포의 기본 흐름과 주요 용어를 이해합니다.
- Prompt Injection, Guardrail, Tool 권한 제어를 적용합니다.
- Health Check, Retry, Restart, Fallback 기반 Auto Healing 흐름을 구성합니다.
- 운영 로그, 이벤트 이력, tracing, 운영 대시보드를 확인합니다.

## 전체 구조

```text
06_multi-agent-service-ops
├─ .venv
├─ .gitignore
├─ .env.example
├─ requirements.txt
├─ README.md
├─ SETUP.md
├─ 00_references
├─ 01_multi-agent-collaboration
├─ 02_service-deployment-and-automation
├─ 03_ai-security-and-guardrails
├─ 04_auto-healing-workflow
├─ 05_observability-and-ops-dashboard
└─ 99_mini-project
```

## 권장 학습 순서

Docker가 처음이라면 Multi-Agent 코드보다 서비스 실행 흐름을 먼저 보는 것이 좋습니다.

```text
00_references
-> 02_service-deployment-and-automation
-> 01_multi-agent-collaboration
-> 03_ai-security-and-guardrails
-> 04_auto-healing-workflow
-> 05_observability-and-ops-dashboard
-> 99_mini-project
```

이 순서로 진행하면 먼저 컨테이너와 Compose 실행 감각을 잡고, 그 위에 Multi-Agent 협업, 보안, 장애 대응, 관측성을 붙일 수 있습니다.

## 단원별 핵심 내용

| 단원 | 핵심 내용 |
| --- | --- |
| `00_references` | 전체 과정 큰 그림, 환경 체크, Docker/AWS/Git/운영 개념 |
| `01_multi-agent-collaboration` | 단일 Agent와 Multi-Agent 비교, 역할 분리, Supervisor/Router, Handoff/Context/MCP, Context 동기화, 결과 검증과 Feedback Loop |
| `02_service-deployment-and-automation` | Docker, Docker Compose, Health Check, GitHub Actions, AWS 배포 기본 |
| `03_ai-security-and-guardrails` | Prompt Injection 방어, 정책 기반 응답 검증, Tool 권한 제어, 보안 Runbook, 감사 로그, Guardrails 통합 설계 |
| `04_auto-healing-workflow` | 장애 유형 분류, Retry, Restart, Fallback, 복구 결과 검증 |
| `05_observability-and-ops-dashboard` | 로그, 이벤트 이력, Trace, LangSmith식 실행 추적, 실행 상태, Streamlit 운영 대시보드 |
| `99_mini-project` | Auto Healing Multi-Agent Service 통합 미니 프로젝트 |

## 이미지 기준 과정 반영

| 기준 | 06 과정 반영 위치 | 확인할 것 |
| --- | --- | --- |
| 멀티 에이전트 협업 설계 | `01_multi-agent-collaboration` | 역할 기반 Agent 분리, Supervisor/Router, Handoff, Agent 간 Context 동기화, Feedback Loop |
| 서비스 배포 및 자동화 운영 | `02_service-deployment-and-automation`, `04_auto-healing-workflow`, `05_observability-and-ops-dashboard` | Docker Compose, Health Check, GitHub Actions, AWS 배포 흐름, Auto Healing, 로그와 대시보드 |
| AI 보안 및 가드레일 설계 | `03_ai-security-and-guardrails` | Prompt Injection 방어, 정책 기반 응답 검증, Tool 권한 제어, 감사 로그, Guardrails 통합 검증 |

## 먼저 이해해야 할 큰 그림

실제 AI 서비스는 모델 호출 코드 하나만으로 운영되지 않습니다.

```text
사용자 요청
-> Frontend
-> Backend API
-> Agent / Multi-Agent Workflow
-> Tool / 외부 API / 데이터
-> Worker
-> Logs / Events / Monitor
-> 운영 상태 확인
```

06 과정의 실습은 위 흐름을 작은 서비스 단위로 나누어 배웁니다.

```text
실행되는 코드
-> 컨테이너로 실행 가능한 서비스
-> 여러 서비스를 함께 실행하는 Docker Compose 구성
-> 변경 사항을 Git으로 관리
-> GitHub Actions로 자동 검증
-> AWS 같은 환경에 배포
-> 장애가 나면 감지하고 복구
-> 상태를 볼 수 있게 기록
```

## 핵심 기술 요약

### Multi-Agent

Multi-Agent는 하나의 Agent가 모든 일을 처리하지 않고, 여러 Agent가 역할을 나누어 협업하는 구조입니다.

```text
Supervisor Agent : 전체 요청을 보고 담당 Agent 선택
Diagnosis Agent : 장애 원인 분석
Recovery Agent : 복구 전략 선택
Validation Agent : 복구 결과 검증
Reporter Agent : 결과 요약
```

중요한 기준은 Agent 수를 늘리는 것이 아니라, 역할과 책임을 명확하게 나누는 것입니다.

### Docker

Docker는 애플리케이션 실행 환경을 컨테이너로 묶어 실행하는 도구입니다.

```text
내 PC 직접 실행 : PC에 설치된 Python, pip, 환경변수의 영향을 많이 받음
Docker 실행 : 정해진 image와 container 환경에서 실행
```

### Docker Compose

Docker Compose는 여러 컨테이너를 하나의 `docker-compose.yml` 파일로 함께 실행하는 도구입니다.

06 과정의 기본 서비스 구성은 다음과 같습니다.

```text
backend : FastAPI API 서버
frontend : Streamlit 사용자 화면
worker : 백그라운드 Agent 작업
monitor : 상태와 이벤트 대시보드
```

### Health Check

Health Check는 서비스가 정상인지 확인하는 검사입니다.

대표 예시:

```text
GET /health
```

이 endpoint가 정상 응답을 반환하면 서비스가 살아 있다고 판단할 수 있습니다.

### GitHub Actions

GitHub Actions는 GitHub에 코드를 push하거나 pull request를 만들었을 때 자동으로 검증 작업을 실행하는 도구입니다.

06에서는 처음부터 복잡한 배포 자동화를 목표로 하지 않습니다. 먼저 아래 흐름을 이해합니다.

```text
push 또는 pull request
-> GitHub Actions 실행
-> Python 문법 검사
-> Docker image build
-> 성공/실패 확인
```

### AWS

AWS는 로컬에서 만든 Docker 기반 서비스를 클라우드 환경에서 실행할 수 있게 해주는 인프라 서비스입니다.

초보자 기준으로는 먼저 아래 관계만 이해하면 충분합니다.

```text
Docker image -> ECR에 저장
ECR image -> App Runner 또는 ECS에서 실행
실행 로그 -> CloudWatch에서 확인
비밀 값 -> Secrets Manager 또는 Parameter Store에서 관리
권한 -> IAM으로 관리
```

AWS 실습은 비용이 발생할 수 있으므로 선택 실습으로 다루며, 리소스 정리 방법을 반드시 함께 확인합니다.

### Auto Healing

Auto Healing은 장애를 감지하고 가능한 경우 자동으로 복구하는 흐름입니다.

```text
장애 감지
-> 원인 분류
-> 복구 전략 선택
-> 재시도 또는 대체 경로 실행
-> 복구 결과 검증
-> 로그 기록
```

## 빠른 시작

### 1. 폴더 이동

```powershell
cd C:\aidev\06_multi-agent-service-ops
```

### 2. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

### 3. 환경변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

`.env`에는 실제 API Key를 작성합니다. `.env`는 GitHub에 올리지 않습니다.

### 4. Docker 확인

```powershell
docker --version
docker compose version
docker run hello-world
```

### 5. 단일 서비스 build/run

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

### 6. Docker Compose 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

확인 URL:

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

종료:

```powershell
docker compose down
```

## 06에서 다루지 않는 것

- LangGraph 자체 기초 문법은 04에서 이미 다룹니다.
- 단일 Agent 미니 프로젝트 설계는 05에서 이미 다룹니다.
- Supabase 중심 DB 실습은 01~03에서 다룹니다.
- 06에서는 Docker Compose, 서비스 운영, 보안, 장애 대응, 관측성에 집중합니다.

## 최종 산출물 기준

99 미니 프로젝트에서는 다음 산출물을 정리합니다.

- Multi-Agent 아키텍처 설계서
- Docker Compose 실행 결과
- 장애 유형별 복구 보고서
- GitHub Actions 실행 결과 또는 검증 계획
- 보안/가드레일 점검표
- 로그/모니터링 대시보드 결과
- 최종 발표 문서
