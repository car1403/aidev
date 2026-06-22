# 06_multi-agent-service-ops

이 과정은 **Multi-Agent 기반 AI 서비스를 실제 운영 가능한 형태로 구성하는 방법**을 학습하는 과정입니다.

앞선 `04_llm-agent-orchestration`, `05_llm-agent-mini-project`에서 Agent, Tool, RAG, LangGraph 같은 실행 흐름을 배웠다면, 이 과정에서는 그 결과물을 서비스처럼 실행하고 운영하는 방법을 다룹니다.

핵심은 아래 흐름입니다.

```text
Multi-Agent 설계
-> Docker로 서비스 패키징
-> Docker Compose로 여러 서비스 실행
-> Git/GitHub로 변경 관리
-> GitHub Actions로 자동 검증
-> AWS 배포 흐름 이해
-> 보안/가드레일 적용
-> Auto Healing 장애 대응
-> 로그/모니터링/운영 대시보드 구성
```

## 과정 목표

- 단일 Agent와 Multi-Agent 구조의 차이를 이해합니다.
- 역할 기반 Agent 협업 구조를 설계합니다.
- FastAPI, Streamlit, worker, monitor 서비스를 Docker로 실행합니다.
- Docker Compose로 여러 서비스를 한 번에 실행하고 로그를 확인합니다.
- Git과 GitHub로 코드 변경 이력을 관리합니다.
- GitHub Actions로 Docker build와 기본 검증을 자동화합니다.
- AWS 배포의 기본 흐름과 주요 용어를 이해합니다.
- Prompt Injection, Guardrail, Tool 권한 제어를 적용합니다.
- Health Check, Retry, Restart, Fallback 기반 Auto Healing 흐름을 구성합니다.
- 운영 로그, 이벤트 이력, 모니터링 대시보드를 확인합니다.

## 전체 구조

```text
06_multi-agent-service-ops
├─.venv
├─.gitignore
├─.env.example
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

## 초보자 진행 원칙

이 과정은 Docker와 운영 도구가 많이 등장합니다. 처음부터 AWS 배포까지 한 번에 하려고 하지 말고, 아래 순서대로 작은 단위로 확인하는 것이 좋습니다.

1. 로컬 Python `.venv`가 작동하는지 확인합니다.
2. Docker Desktop이 실행되는지 확인합니다.
3. 단일 Docker 서비스 하나를 build/run 해봅니다.
4. Docker Compose로 backend, frontend, worker, monitor를 함께 실행합니다.
5. Health Check와 로그를 확인합니다.
6. Multi-Agent 협업 구조를 코드로 이해합니다.
7. 보안/가드레일과 Auto Healing 흐름을 붙입니다.
8. Git/GitHub Actions와 AWS 배포 흐름은 후반에 다룹니다.

이 과정에서는 `06_multi-agent-service-ops` 최상위의 `.venv` 하나를 사용합니다. 다만 실제 서비스 실행은 Docker Compose가 중심입니다.

## 강의 진행용 핵심 흐름

수업 중 바로 사용할 수 있는 진행 흐름입니다.

| 단계 | 수업 목표 | 확인 결과 |
| --- | --- | --- |
| 1 | Docker Desktop과 `docker compose` 확인 | `docker compose version` 출력 |
| 2 | 단일 FastAPI 서비스를 Docker image로 build/run | `http://127.0.0.1:8000/health` 정상 응답 |
| 3 | Docker Compose로 여러 서비스 실행 | backend, frontend, worker, monitor 컨테이너 확인 |
| 4 | Health Check와 logs 확인 | `docker compose ps`, `docker compose logs backend` 실행 |
| 5 | Multi-Agent 역할 분리 이해 | supervisor, diagnosis, recovery, validation 역할 설명 |
| 6 | GitHub Actions CI 흐름 이해 | workflow 위치와 실행 조건 설명 |
| 7 | AWS 배포 흐름 이해 | Docker image, ECR, App Runner/ECS, CloudWatch 관계 설명 |
| 8 | Auto Healing과 Observability 연결 | 장애 감지, 재시도, 복구 로그, 대시보드 확인 |

초보자 수업에서는 “컨테이너가 왜 필요한가?”보다 먼저 “컨테이너가 실제로 실행되고 health check가 되는가?”를 확인하는 것이 좋습니다. 실행 결과를 본 뒤 Dockerfile, Compose, CI/CD, AWS 개념을 연결하면 이해가 훨씬 쉽습니다.

## 04, 05와의 차이

```text
04_llm-agent-orchestration:
- Docker run으로 Ollama, pgvector 같은 단일 도구 실행
- Agent, Tool, RAG, LangGraph 원리 학습

05_llm-agent-mini-project:
- Agent 미니 프로젝트 완성
- Docker는 선택 확장

06_multi-agent-service-ops:
- Docker Compose가 핵심
- 여러 서비스를 함께 실행
- GitHub Actions, AWS, Health Check, 로그, Auto Healing까지 운영 관점으로 확장
```

## 권장 학습 순서

```text
00_references
-> 02_service-deployment-and-automation
-> 01_multi-agent-collaboration
-> 03_ai-security-and-guardrails
-> 04_auto-healing-workflow
-> 05_observability-and-ops-dashboard
-> 99_mini-project
```

Docker가 처음이라면 `02_service-deployment-and-automation`을 먼저 실행해 보는 것이 좋습니다. 서비스가 어떻게 실행되는지 감이 잡힌 뒤 Multi-Agent, 보안, Auto Healing을 붙이면 이해가 훨씬 쉽습니다.

## 단원별 핵심 내용

| 단원 | 핵심 내용 |
| --- | --- |
| `00_references` | 전체 과정 큰 그림, 환경 체크, Docker/AWS/Git/운영 개념 |
| `01_multi-agent-collaboration` | 단일 Agent와 Multi-Agent 비교, 역할 분리, Supervisor/Router, Handoff/Context/MCP, 결과 검증과 Feedback Loop |
| `02_service-deployment-and-automation` | Docker, Docker Compose, Health Check, GitHub Actions, AWS 배포 기본 |
| `03_ai-security-and-guardrails` | Prompt Injection 방어, 정책 기반 응답 검증, Tool 권한 제어, 보안 Runbook, 감사 로그, Guardrails 통합 설계 |
| `04_auto-healing-workflow` | 장애 유형 분류, Retry, Restart, Fallback, 복구 결과 검증 |
| `05_observability-and-ops-dashboard` | 로그, 이벤트 이력, Trace, LangSmith식 실행 추적, 실행 상태, Streamlit 운영 대시보드 |
| `99_mini-project` | Auto Healing Multi-Agent Service 통합 미니 프로젝트 |

## 이미지 기준 과정 점검

이 과정은 이미지의 세 가지 큰 축을 아래처럼 반영합니다.

| 이미지 기준 | 06 과정 반영 위치 | 수업에서 확인할 것 |
| --- | --- | --- |
| 멀티 에이전트 협업 설계 | `01_multi-agent-collaboration` | 단일 Agent와 Multi-Agent 차이, 역할 분리, Supervisor/Router, Handoff, Context 동기화, Feedback Loop |
| 서비스 배포 및 자동화 운영 | `02_service-deployment-and-automation`, `04_auto-healing-workflow`, `05_observability-and-ops-dashboard` | Docker, Docker Compose, Health Check, GitHub Actions, AWS 배포 흐름, Auto Healing, 로그와 대시보드 |
| AI 보안 및 가드레일 설계 | `03_ai-security-and-guardrails` | Prompt Injection 방어, 정책 기반 응답 검증, Tool 권한 제어, 감사 로그, Guardrails 통합 검증 |

세부적으로는 다음 항목을 설명할 수 있어야 합니다.

- Agent 간 업무 인계(Handoff) 시 어떤 Context를 넘기는가?
- Agent 간 Context 동기화와 협업 일관성을 어떻게 유지하는가?
- Docker Compose에서 backend, frontend, worker, monitor가 어떤 역할을 나누는가?
- GitHub Actions가 Docker build 실패를 어떻게 자동으로 잡아 주는가?
- AWS App Runner 또는 ECS로 옮길 때 image, port, env, health check, log가 어떻게 연결되는가?
- Prompt Injection, Tool 권한, 정책 위반 로그를 어떻게 관리하는가?

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
-> 운영자 확인
```

이 과정의 실습은 위 흐름을 작은 서비스 단위로 나누어 배웁니다.

```text
실행되는 코드
-> 컨테이너로 실행 가능한 서비스
-> 여러 서비스를 함께 실행하는 Docker Compose 구성
-> 변경 사항을 Git으로 관리
-> GitHub Actions로 자동 검증
-> AWS 같은 환경에 배포
-> 장애가 나면 감지하고 복구
-> 운영자가 상태를 볼 수 있게 기록
```

## 주요 기술 설명

### Multi-Agent

Multi-Agent는 하나의 Agent가 모든 일을 처리하지 않고, 여러 Agent가 역할을 나누어 협업하는 구조입니다.

예시:

```text
Supervisor Agent : 전체 요청을 보고 담당 Agent 선택
Diagnosis Agent : 장애 원인 분석
Recovery Agent : 복구 전략 선택
Validation Agent : 복구 결과 검증
Reporter Agent : 운영자에게 결과 요약
```

장점:

- 복잡한 업무를 역할별로 나눌 수 있습니다.
- 각 Agent의 책임이 명확해집니다.
- 실패한 단계만 다시 실행하기 쉽습니다.
- 로그와 디버깅이 쉬워집니다.

주의:

- Agent가 많아질수록 입력/출력 형식을 맞추는 것이 중요합니다.
- Agent 간 결과 검증과 재시도 전략이 필요합니다.

### Docker

Docker는 애플리케이션 실행 환경을 컨테이너로 묶어 실행하는 도구입니다.

```text
내 PC 직접 실행 : PC에 설치된 Python, pip, 환경변수의 영향을 많이 받음
Docker 실행 : 정해진 이미지와 컨테이너 환경에서 실행
```

이 과정에서는 FastAPI backend, Streamlit frontend, worker, monitor를 Docker 서비스로 실행합니다.

### Dockerfile

Dockerfile은 Docker image를 만드는 설계도입니다.

일반적인 Python 서비스 Dockerfile 흐름:

```text
1. Python 기본 이미지 선택
2. 작업 폴더 생성
3. requirements.txt 복사
4. pip install 실행
5. 애플리케이션 코드 복사
6. 실행 명령 지정
```

### Docker Compose

Docker Compose는 여러 컨테이너를 하나의 `docker-compose.yml` 파일로 함께 실행하는 도구입니다.

이 과정의 Compose 서비스 구성:

```text
backend : API 요청 처리
frontend : 사용자 화면
worker : 백그라운드 Agent 작업
monitor : 상태와 이벤트 대시보드
```

Docker Compose를 쓰는 이유:

- 여러 서비스를 명령 한 번으로 실행할 수 있습니다.
- 서비스별 포트, 환경변수, 의존 관계를 파일로 관리할 수 있습니다.
- 운영 구조를 문서가 아니라 실행 가능한 설정으로 남길 수 있습니다.

### Health Check

Health Check는 서비스가 정상인지 확인하는 검사입니다.

대표 예시:

```text
GET /health
```

정상 응답 예시:

```json
{
 "status": "ok"
}
```

운영에서는 Health Check가 장애 감지, 재시작, 트래픽 전환의 기준이 됩니다.

### Auto Healing

Auto Healing은 장애를 감지하고 자동으로 복구를 시도하는 구조입니다.

```text
Health Check 실패
-> 장애 유형 분류
-> Retry
-> Restart
-> Fallback
-> 복구 결과 검증
-> 운영 로그 기록
```

처음에는 실제 서버를 강제로 재시작하기보다, 복구 전략을 시뮬레이션하고 로그로 확인하는 방식부터 시작합니다.

### Guardrail

Guardrail은 AI가 위험하거나 정책에 맞지 않는 응답이나 Tool 실행을 하지 않도록 제한하는 규칙입니다.

예시:

```text
Prompt Injection 탐지
Tool 실행 권한 확인
응답에 민감정보 포함 여부 검사
운영 정책 위반 응답 차단
```

### Observability

Observability는 서비스 내부 상태를 외부에서 이해할 수 있게 만드는 운영 역량입니다.

주요 구성:

```text
Log : 어떤 일이 발생했는지 기록
Metric : 숫자로 보는 상태
Trace : 요청이 어떤 단계를 거쳤는지 추적
Dashboard : 운영자가 한눈에 보는 화면
```

### Git과 GitHub Actions

Git은 코드 변경 이력을 관리하는 도구입니다.

기본 흐름:

```text
git status
-> git add
-> git commit
-> git push
```

GitHub Actions는 GitHub에서 코드가 push되거나 pull request가 열릴 때 자동으로 검증 명령을 실행하는 도구입니다.

이 과정에서는 처음부터 완전 자동 배포를 목표로 하지 않고, 먼저 Docker image가 정상적으로 build되는지 확인하는 CI 흐름을 다룹니다.

### AWS

AWS는 클라우드에서 서버, 컨테이너, 로그, 네트워크, 권한을 관리하는 플랫폼입니다.

초보자 관점의 기본 배포 흐름:

```text
Docker image 생성
-> 이미지 저장소에 업로드
-> AWS 서비스에서 이미지 실행
-> 환경변수 설정
-> Health Check 확인
-> 로그와 비용 확인
```

대표 용어:

```text
ECR : Docker image 저장소
ECS : 컨테이너 실행/관리 서비스
App Runner : 컨테이너 기반 앱을 비교적 간단히 배포하는 서비스
CloudWatch : 로그와 지표 확인 서비스
IAM : 사용자, 역할, 권한 관리 서비스
Region : AWS 리소스를 생성하는 지역
```

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

PowerShell 기준 기본 흐름:

```powershell
cd C:\aidev\06_multi-agent-service-ops
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
Copy-Item.env.example.env
```

이미 `.venv`가 만들어져 있다면 다시 만들 필요는 없습니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
```

`.env`에는 실제 API Key를 넣고, `.env.example`에는 예시 값만 둡니다.

## Docker Desktop 확인

Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

`docker ps`가 실패하면 Docker Desktop이 아직 실행 중이 아닐 가능성이 큽니다.

## 단일 Docker 서비스 실행

먼저 FastAPI backend 하나를 Docker image로 만들고 실행합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_ch1_docker-service-packaging
docker build -t aidev-agent-backend:local.
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 Health Check를 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

확인이 끝나면 컨테이너가 실행 중인 PowerShell에서 `Ctrl + C`로 종료합니다.

## Docker Compose 멀티 서비스 실행

backend, frontend, worker, monitor를 함께 실행합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item.env.example.env
docker compose up --build
```

실행 전에 Compose 파일 문법을 확인하려면 아래 명령을 사용할 수 있습니다.

```powershell
docker compose config
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
```

다른 PowerShell에서 상태와 로그를 확인합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

종료:

```powershell
docker compose down
```

백그라운드 실행:

```powershell
docker compose up --build -d
```

## Llama/Ollama 로컬 LLM 실행 선택 실습

이 과정의 핵심은 서비스 운영이지만, 로컬 LLM을 운영 서비스처럼 다루는 감각을 위해 Ollama/Llama를 선택 실습으로 사용할 수 있습니다.

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
docker exec -it ollama-llm ollama list
```

간단한 호출 확인:

```powershell
Invoke-RestMethod http://127.0.0.1:11434/api/generate `
 -Method Post `
 -ContentType "application/json" `
 -Body '{"model":"llama3.2","prompt":"서비스 운영에서 health check가 중요한 이유를 한 문장으로 설명해줘.","stream":false}'
```

중지와 재시작:

```powershell
docker stop ollama-llm
docker start ollama-llm
```

## Git 기본 흐름

Git 설치 확인:

```powershell
git --version
```

처음 한 번 사용자 정보를 설정합니다.

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

변경 상태 확인:

```powershell
cd C:\aidev
git status
git status --short
git diff
```

커밋 예시:

```powershell
git add 06_multi-agent-service-ops
git commit -m "docs: expand multi-agent service ops guide"
```

주의:

- `.env`는 커밋하지 않습니다.
- `.venv`는 커밋하지 않습니다.
- API Key, AWS Access Key, 비밀번호는 코드와 README에 적지 않습니다.

## GitHub Actions 위치

실습용 workflow 예시는 아래 위치에 있습니다.

```text
02_service-deployment-and-automation/04_ch4_github-actions-cicd/.github/workflows/docker-build-check.yml
```

실제 GitHub 저장소에서 동작하게 하려면 workflow 파일이 저장소 최상위의 `.github/workflows` 아래에 있어야 합니다.

예시:

```text
C:\aidev\.github\workflows\docker-build-check.yml
```

06 과정만 별도 저장소로 운영한다면 아래 위치도 가능합니다.

```text
C:\aidev\06_multi-agent-service-ops\.github\workflows\docker-build-check.yml
```

GitHub Actions의 기본 흐름:

```text
push 또는 pull request
-> GitHub Actions runner 실행
-> Python 문법 검사
-> Docker image build
-> 성공/실패 확인
```

초보자 수업에서는 처음부터 AWS 배포까지 자동화하지 않습니다. 먼저 GitHub Actions가 Docker image build 실패를 자동으로 잡아 주는지 확인합니다.

```text
1단계: Docker build 자동 검증
2단계: 테스트 자동 실행
3단계: ECR push
4단계: AWS App Runner 또는 ECS 배포
```

3, 4단계는 AWS 비용과 권한 설정이 필요하므로 수업 안내에 따라 확장합니다.

## AWS 배포 기본 흐름

처음에는 복잡한 아키텍처보다 아래 흐름을 이해하는 데 집중합니다.

```text
1. 로컬에서 Docker image build
2. 로컬에서 container 실행 확인
3. Health Check endpoint 확인
4. Docker image를 이미지 저장소에 push
5. AWS 서비스에서 image 실행
6. 환경변수 설정
7. 외부 URL로 Health Check 확인
8. CloudWatch Logs와 비용 확인
```

AWS CLI 확인:

```powershell
aws --version
aws configure
aws sts get-caller-identity
```

주의:

- AWS 계정은 비용이 발생할 수 있습니다.
- 실습 후 사용하지 않는 리소스는 삭제합니다.
- Access Key는 GitHub나 코드에 직접 올리지 않습니다.
- 가능하면 장기 Access Key보다 OIDC 기반 인증을 이후 학습 목표로 둡니다.

초보자에게는 App Runner가 가장 단순한 첫 배포 후보가 될 수 있습니다. 다만 여러 컨테이너를 운영하거나 세밀한 네트워크, Auto Scaling, Load Balancer 구성이 필요하면 ECS로 확장합니다.

```text
App Runner:
- 컨테이너 기반 웹 서비스를 비교적 간단히 배포
- 초보자 첫 배포 흐름 설명에 적합

ECS:
- 컨테이너를 더 세밀하게 운영
- Task Definition, Service, Cluster, Load Balancer 개념 필요

EC2:
- 서버를 직접 관리
- 자유도는 높지만 운영 책임도 큼
```

## 99 미니 프로젝트 실행

통합 미니 프로젝트 위치:

```text
99_mini-project/sample-auto-healing-agent
```

실행:

```powershell
cd C:\aidev\06_multi-agent-service-ops\99_mini-project\sample-auto-healing-agent
Copy-Item.env.example.env
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
```

팀 프로젝트 템플릿:

```text
99_mini-project/team-template
```

팀 프로젝트에서는 다음 항목을 확장합니다.

- Agent 역할 분리
- 장애 유형 추가
- 복구 전략 추가
- Guardrail 정책 추가
- 운영 이벤트 로그 확장
- Monitor 대시보드 지표 추가
- Docker Compose 구성 검증

## 자주 만나는 오류

### docker 명령을 찾을 수 없음

Docker Desktop 설치 여부를 확인하고 PowerShell을 새로 엽니다.

```powershell
docker --version
```

### docker ps가 실패함

Docker Desktop이 실행 중인지 확인합니다.

```powershell
docker ps
```

### 포트 충돌

8000, 8801, 8802, 11434 포트를 다른 프로그램이나 컨테이너가 사용 중일 수 있습니다.

```powershell
docker ps
docker compose down
```

필요하면 `docker-compose.yml`의 포트 번호를 바꿉니다.

### 컨테이너 이름 충돌

```powershell
docker ps -a
docker stop 컨테이너이름
docker rm 컨테이너이름
```

### GitHub Actions가 실행되지 않음

확인할 것:

- workflow 파일이 `.github/workflows` 아래에 있는가?
- 파일 확장자가 `.yml` 또는 `.yaml`인가?
- 저장소의 Actions 기능이 켜져 있는가?
- push한 branch가 workflow 조건에 포함되는가?

### AWS 배포 후 접속이 안 됨

확인할 것:

- 컨테이너가 올바른 포트로 실행되는가?
- Health Check 경로가 맞는가?
- 환경변수가 설정되어 있는가?
- IAM 권한이 충분한가?
- CloudWatch Logs에 오류가 있는가?

## 비용과 보안 주의

- OpenAI API 호출은 비용이 발생할 수 있습니다.
- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- Docker volume에는 모델 파일이나 데이터가 남을 수 있습니다.
- `.env`는 GitHub에 올리지 않습니다.
- AWS Access Key는 코드, README, 발표 자료에 적지 않습니다.
- GitHub Actions 로그에 비밀 값이 출력되지 않게 합니다.
- 실습 후 불필요한 컨테이너와 클라우드 리소스를 정리합니다.

## 첫 실행 추천 순서

완전 초보자는 아래 순서로 진행하는 것이 좋습니다.

```text
1. 00_references 읽기
2. Python과.venv 확인
3. requirements.txt 설치
4. Docker Desktop 설치와 실행 확인
5. 02-01에서 단일 Docker 서비스 build/run
6. 02-02에서 Docker Compose 멀티 서비스 실행
7. Health Check와 logs 확인
8. 01에서 Multi-Agent 협업 구조 이해
9. 03에서 보안/Guardrail 구조 실습
10. 04에서 Auto Healing 흐름 실습
11. 05에서 로그/모니터링/대시보드 실습
12. Git으로 변경 사항 관리
13. GitHub Actions로 Docker build 검증
14. AWS 배포 기본 흐름 학습
15. 99 미니 프로젝트 실행
```

## 참고 문서

- Docker Desktop: https://docs.docker.com/desktop/
- Docker Compose: https://docs.docker.com/compose/
- Ollama Llama 3.2: https://ollama.com/library/llama3.2
- GitHub Actions: https://docs.github.com/actions
- GitHub Actions Secrets: https://docs.github.com/actions/security-guides/using-secrets-in-github-actions
- AWS App Runner: https://docs.aws.amazon.com/apprunner/
- AWS ECR: https://docs.aws.amazon.com/ecr/
- AWS CloudWatch Logs: https://docs.aws.amazon.com/cloudwatch/
