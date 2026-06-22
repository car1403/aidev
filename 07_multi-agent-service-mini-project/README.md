# 07_multi-agent-service-mini-project

`06_multi-agent-service-ops` 과정에서 학습한 Multi-Agent 협업, Docker Compose, AI 보안/가드레일, Auto Healing, Observability를 하나의 미니 프로젝트로 구현하는 과정입니다.

이 과정은 `06_multi-agent-service-ops`의 운영 구조를 팀 프로젝트로 연결합니다. 프로젝트 주제는 Docker Compose 기반 **에러 자가 치유(Auto Healing) 워크플로우**입니다.

07은 새 이론을 많이 추가하는 과정이 아니라, 06에서 배운 Docker Compose, Health Check, GitHub Actions, AWS 배포 체크리스트, Auto Healing, Observability를 하나의 결과물로 묶어 보는 단계입니다.

## 프로젝트 주제

```text
멀티 에이전트 협업 및 서비스 운영
-> 에러 자가 치유(Auto Healing) 워크플로우
```

## 프로젝트 진행 방향

```text
1. 에이전트 협업 시나리오 및 구조 설계
2. 장애 유형별 복구 로직 및 자동화 파이프라인 구현
3. 협업 기반 실행 흐름 통합 구현
4. 서비스 배포 및 결과 검증
```

## 필수 산출물

팀 프로젝트는 아래 3가지 산출물을 기준으로 평가합니다.

| 산출물 | 핵심 확인 기준 |
| --- | --- |
| 멀티 에이전트 아키텍처 설계서 | 비즈니스 요구사항, Agent 역할, Handoff, Context 공유 구조가 명확한가 |
| 배포 및 장애 복구 보고서 | Compose/배포 매니페스트, 장애 감지 매트릭, 자동 복구 스크립트와 복구율이 정리되었는가 |
| 파이프라인 구현 결과 보고서 | 커밋, 빌드, 테스트, 배포, 알림, 실패 처리 흐름이 파이프라인 다이어그램으로 표현되었는가 |

### 멀티 에이전트 아키텍처 설계서에 꼭 들어갈 내용

`docs/multi-agent-architecture.md`에는 아래 기준을 직접 설명해야 합니다.

- 아키텍처 구조가 비즈니스 요구사항인 응답 속도, 결정 일관성, 장애 격리 기준에 맞게 선택되었는가?
- Planner, Executor, Critic, Memory Keeper, Reporter 같은 각 Agent의 역할, 책임 범위, 의존 관계가 명확한가?
- Agent 간 책임 중복이나 책임 공백이 없는가?
- Handoff 시 Context에 상태, 메모리, 중간 결과, 권한 정보가 누락 없이 전달되는가?
- Agent 간 Context 동기화와 협업 일관성 유지 기준이 정리되었는가?
- 메시지 큐, 공유 상태, API, 로그 파일 등 Context 전달 구조가 문서화되었는가?

### 배포 및 장애 복구 보고서에 꼭 들어갈 내용

`docs/deployment-recovery-report.md`에는 아래 기준을 직접 시험하고 기록해야 합니다.

- Docker Compose 또는 선택 확장 배포 매니페스트가 작성되었는가?
- 멀티 컨테이너 서비스 구성에 backend, frontend, worker, monitor의 역할과 port가 정리되었는가?
- 서비스 디스커버리, 로드밸런싱, 시크릿 관리, 환경변수 관리 방식이 설명되었는가?
- 네트워크 타임아웃, 연결 끊김, DB 연결 풀 고갈, API 5xx, Rate Limit, LLM 할루시네이션, 토큰 한도, Prompt Injection 등 장애 유형별 감지 메트릭이 있는가?
- 장애 유형별 자동 복구 흐름이 Retry, Restart, Reconnect, Fallback, 대체 모델 호출, 캐시 fallback 중 어떤 전략으로 구성되었는가?
- 수동 개입 없이 복구되는 시나리오 비율이 제시되었는가?

### 파이프라인 구현 결과 보고서에 꼭 들어갈 내용

`docs/pipeline-result-report.md`에는 아래 기준을 직접 설명해야 합니다.

- `코드 커밋 -> 빌드 -> 테스트 -> 배포` 전체 단계가 다이어그램으로 표현되었는가?
- 각 단계의 입력, 출력, 실패 시 처리 규칙이 정의되었는가?
- 단위 테스트와 통합 테스트의 커버리지 기준, 테스트 데이터 관리 방식이 정리되었는가?
- 실패 시 파이프라인을 차단하는 기준이 명시되었는가?
- 성공, 실패, 지연 결과를 Slack, Teams, PagerDuty 같은 알림 채널로 전달하는 구조가 설명되었는가?
- 장애 발생 시 담당자 할당과 에스컬레이션 기준이 정리되었는가?

## 프로젝트 목표

- 에이전트 협업 시나리오와 구조를 설계한다.
- Agent 간 Handoff, Context 공유, MCP/Tool 연결 구조를 설계한다.
- 장애 유형별 복구 로직과 자동화 파이프라인을 구현한다.
- Health Check, Retry, Restart, Fallback 기반 장애 대응 흐름을 구성한다.
- Feedback Loop 기반 복구 결과 검증과 재시도 흐름을 정리한다.
- Docker Compose로 backend, frontend, worker, monitor 서비스를 실행한다.
- 복구 결과와 운영 이벤트를 검증하고 대시보드에서 확인한다.
- LangSmith식 trace/run/span 관점으로 실행 추적 계획을 작성한다.
- 보안 Runbook, 감사 로그, 정책 위반 추적, Guardrails 검증 기준을 작성한다.
- GitHub Actions로 Docker Compose 설정과 Docker build를 자동 검증하는 흐름을 이해한다.
- AWS 배포 체크리스트를 작성하고 App Runner/ECS/ECR/CloudWatch 연결 관계를 설명한다.

## 06 과정과의 연결

`06_multi-agent-service-ops`에서 배운 내용은 이 미니 프로젝트에서 다음처럼 사용합니다.

| 06 과정 내용 | 07 프로젝트 적용 |
| --- | --- |
| Multi-Agent 협업 설계 | Supervisor, Diagnosis, Recovery, Validation 역할 설계 |
| Handoff/Context/MCP | Agent 간 업무 인계 Context, Tool 연결, 권한 전달 구조 설계 |
| Context 동기화 | Agent 간 상태, 메모리, 중간 결과를 일관되게 전달하고 불일치 시 feedback loop 적용 |
| Feedback Loop | 복구 결과 검증, 재시도, 사람 검토 또는 fallback 흐름 설계 |
| Docker Compose | backend, frontend, worker, monitor 통합 실행 |
| AI 보안/가드레일 | 위험한 복구 명령 제한, 정책 기반 실행 여부 판단, Guardrails 검증 |
| Auto Healing | 장애 감지, 재시도, 재시작, 대체 경로 흐름 구현 |
| Observability | 이벤트 로그, 상태 추적, LangSmith식 trace, 운영 대시보드 표시 |
| 보안 운영 | 보안 Runbook, 감사 로그, 정책 위반 추적 |
| GitHub Actions | Compose 설정과 Docker build 자동 검증 |
| AWS 배포 설계 | ECR, App Runner/ECS, CloudWatch 기반 배포 체크리스트 작성 |

07은 새 이론을 많이 추가하는 과정이라기보다, 06에서 배운 운영 구조를 하나의 팀 프로젝트로 묶어 보는 단계입니다.

## 강의 진행용 핵심 흐름

| 단계 | 수업 목표 | 확인 결과 |
| --- | --- | --- |
| 1 | Docker Desktop과 Compose 확인 | `docker compose version` 출력 |
| 2 | 수업용 샘플 Compose 설정 검증 | `docker compose config` 통과 |
| 3 | 수업용 샘플 서비스 실행 | backend, frontend, worker, monitor 실행 |
| 4 | Health Check 확인 | `http://127.0.0.1:8000/health` 정상 응답 |
| 5 | Auto Healing 요청 실행 | frontend에서 장애 메시지 입력 후 결과 확인 |
| 6 | 운영 로그 확인 | `docker compose logs worker` 확인 |
| 7 | 팀 템플릿 복사 | 팀별 프로젝트 폴더 생성 |
| 8 | GitHub Actions/AWS 제출 기준 정리 | CI 체크와 배포 체크리스트 작성 |

초보자 수업에서는 “완벽한 자동 복구 시스템”을 처음부터 만들기보다, 장애 이벤트가 들어오고 Agent가 복구 전략을 선택하고 운영 화면에서 결과를 확인하는 흐름이 끝까지 보이는 것을 우선 목표로 합니다.

## 이번 프로젝트에서 만드는 것

최종 목표는 여러 서비스가 함께 동작하는 작은 운영형 AI 서비스를 만들고, 장애가 발생했을 때 Multi-Agent가 원인을 분류하고 복구 흐름을 제안하거나 실행하는 구조를 구현하는 것입니다.

기본 서비스 구성은 다음과 같습니다.

```text
backend : Health Check와 장애 대응 API 제공
frontend : 사용자가 상태와 결과를 확인하는 화면
worker : 백그라운드에서 장애 감지와 복구 작업 수행
monitor : 로그, 이벤트, 서비스 상태를 보여주는 운영 대시보드
```

Agent 역할 예시는 다음과 같습니다.

```text
Supervisor Agent : 전체 장애 요청을 보고 담당 Agent 선택
Diagnosis Agent : 장애 원인과 유형 분석
Recovery Agent : Retry, Restart, Fallback 등 복구 전략 선택
Validation Agent : 복구 결과 검증
Reporter Agent : 운영자에게 결과 요약
```

Agent 간에는 다음 정보를 명확히 전달해야 합니다.

```text
request_id
current_agent
next_agent
handoff_reason
handoff_context
previous_result
allowed_tools
required_action
```

MCP/Tool 연결을 설계할 때는 어떤 Agent가 어떤 Tool을 호출할 수 있는지 함께 정리합니다.

Agent 간 Context 동기화 기준도 함께 작성합니다.

```text
공통 incident_id 또는 request_id를 유지하는가?
각 Agent가 같은 service_name과 failure_type을 보고 있는가?
previous_result와 handoff_summary가 최신 상태인가?
allowed_tools가 Agent 역할에 맞게 제한되어 있는가?
Agent 간 판단이 충돌하면 Critic 또는 Feedback Loop가 다시 검증하는가?
```

처음에는 모든 기능을 완벽히 자동화하기보다, 아래 흐름이 끝까지 보이는 것을 목표로 합니다.

```text
장애 이벤트 발생
-> 장애 유형 분류
-> 복구 전략 선택
-> 복구 실행 또는 시뮬레이션
-> Health Check 재확인
-> 결과 검증과 Feedback Loop
-> 운영 이벤트 기록
-> 감사 로그와 정책 위반 여부 기록
-> 대시보드에서 결과 확인
```

## 과정 구조

```text
07_multi-agent-service-mini-project
├─.venv
├─.gitignore
├─ README.md
├─ SETUP.md
├─.env.example
├─ requirements.txt
├─ 00_references
├─ 01_local-dev-basic
├─ 02_instructor-sample-project
├─ 03_team-project-guide
├─ 04_auto-healing-project-practice
├─ 05_multi-agent-service-sample-assets
└─ 99_team-projects
 └─ multi-agent-service-team-template
```

## 폴더를 읽는 방법

각 폴더의 역할은 다음과 같습니다.

```text
00_references 프로젝트 참고 자료
01_local-dev-basic Docker/Docker Compose 로컬 실행 기초
02_instructor-sample-project 수업용 샘플 Auto Healing 서비스
03_team-project-guide 팀 프로젝트 주제, 역할, 일정 가이드
04_auto-healing-project-practice 장애 대응 흐름 설계 실습
05_multi-agent-service-sample-assets 샘플 코드와 운영 참고 자료
99_team-projects 팀별 최종 프로젝트 작업 공간
```

초보자는 `02_instructor-sample-project`를 먼저 실행해서 서비스 4개가 함께 뜨는 감각을 잡고, 그 다음 `99_team-projects\multi-agent-service-team-template`을 복사해서 자기 팀 프로젝트를 시작하면 됩니다.

## 권장 학습 흐름

```text
00_references 읽기
-> 01_local-dev-basic에서 Docker/Docker Compose 환경 확인
-> 02_instructor-sample-project에서 수업용 샘플 실행
-> 03_team-project-guide에서 팀 주제/역할/일정 확정
-> 04_auto-healing-project-practice에서 장애 대응 흐름 설계
-> 99_team-projects/multi-agent-service-team-template 기반 팀 프로젝트 진행
```

초보자에게는 아래처럼 더 작게 나누어 진행하는 것을 권장합니다.

1. `SETUP.md`를 보고 Python `.venv`와 Docker Desktop을 준비합니다.
2. `docker --version`, `docker compose version`, `docker ps`로 Docker 실행 상태를 확인합니다.
3. `docker compose config`로 Compose 설정을 먼저 확인합니다.
4. `02_instructor-sample-project`에서 수업용 샘플을 먼저 실행합니다.
5. `http://127.0.0.1:8000/health`로 backend health check를 확인합니다.
6. `http://127.0.0.1:8801`에서 frontend 화면을 확인합니다.
7. `http://127.0.0.1:8802`에서 monitor 화면을 확인합니다.
8. `docs/test-checklist.md`를 읽고 어떤 결과를 검증해야 하는지 확인합니다.
9. 팀 템플릿을 복사해 팀 프로젝트 폴더를 만듭니다.
10. 장애 유형, Agent 역할, 복구 전략을 문서로 먼저 정리합니다.
11. backend, worker, monitor를 작은 단위로 수정하며 Docker Compose로 반복 검증합니다.
12. 선택 사항으로 GitHub Actions build check와 AWS 배포 체크리스트를 작성합니다.

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

PowerShell 기준 기본 흐름은 다음과 같습니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
Copy-Item.env.example.env
```

이미 `.venv`가 만들어져 있다면 다시 만들 필요는 없습니다. 그때는 아래처럼 활성화부터 시작하면 됩니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
.\.venv\Scripts\Activate.ps1
```

이 과정에서는 Python 실행과 보조 스크립트 확인에는 최상위 `.venv`를 사용하고, 실제 서비스 실행은 Docker Compose를 중심으로 진행합니다.

## Docker Desktop 확인

Docker Compose 프로젝트를 실행하기 전에는 Docker Desktop이 켜져 있어야 합니다.

```powershell
docker --version
docker compose version
docker ps
```

`docker ps`가 실패하면 Docker Desktop을 먼저 실행한 뒤 다시 확인합니다.

## 수업용 샘플 실행 방법

수업용 샘플은 backend, frontend, worker, monitor를 Docker Compose로 함께 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item.env.example.env
docker compose config
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
```

로그를 확인할 때는 다른 PowerShell을 열어 아래 명령을 사용합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\02_instructor-sample-project
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간 로그를 보려면 아래 명령을 사용합니다.

```powershell
docker compose logs -f worker
```

종료:

```powershell
docker compose down
```

## 팀 프로젝트 시작 방법

팀 프로젝트는 `99_team-projects\multi-agent-service-team-template`을 복사해서 시작합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
Copy-Item.\99_team-projects\multi-agent-service-team-template.\99_team-projects\team-01-auto-healing-service -Recurse
```

팀 이름에 맞게 `team-01-auto-healing-service` 부분만 바꾸면 됩니다.

복사한 뒤에는 아래 문서를 먼저 정리합니다.

```text
docs/README.md 프로젝트 설명, 실행 방법, 팀 역할
docs/multi-agent-architecture.md 멀티 에이전트 아키텍처 설계서
docs/deployment-recovery-report.md 배포 및 장애 복구 보고서
docs/pipeline-result-report.md 파이프라인 구현 결과 보고서
docs/test-checklist.md Health Check, 복구, 대시보드 검증 항목
docs/handoff-context-design.md Agent 간 업무 인계와 Context 설계
docs/feedback-loop-review.md 복구 결과 검증과 재시도 설계
docs/security-runbook.md 보안 운영 Runbook
docs/audit-policy-log.md 감사 로그와 정책 위반 추적 설계
docs/guardrails-validation.md Guardrails 검증 기준
docs/langsmith-tracing-plan.md LangSmith식 실행 추적 계획
backend/README.md API와 장애 이벤트 처리 설명
worker/README.md 장애 감지와 복구 작업 설명
monitor/README.md 운영 대시보드 설명
docker/README.md Docker Compose 구성 설명
```

코드는 아래 파일부터 작은 단위로 수정합니다.

```text
backend/main.py Health Check, 장애 이벤트 API
worker/main.py 장애 감지, Retry, Restart, Fallback 로직
monitor/app.py 운영 이벤트와 상태 표시
frontend/app.py 사용자 확인 화면
docker-compose.yml 서비스 구성과 포트
```

## 팀 템플릿 실행 방법

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
Copy-Item.env.example.env
docker compose config
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
```

## 최종 산출물

팀 프로젝트가 끝나면 아래 결과물이 있어야 합니다.

- 멀티 에이전트 아키텍처 설계서
- 배포 및 장애 복구 보고서
- 파이프라인 구현 결과 보고서
- Docker Compose로 실행되는 backend, frontend, worker, monitor
- 장애 유형 2개 이상
- 복구 전략 2개 이상
- Health Check 검증 흐름
- 운영 이벤트 로그 또는 상태 기록
- Monitor 대시보드 화면
- 팀 README와 테스트 체크리스트
- 발표 자료 또는 시연 시나리오
- 선택 사항: GitHub Actions Docker build check
- 선택 사항: AWS 배포 체크리스트

## 최종 시연 체크리스트

발표나 제출 전에는 아래 순서로 확인합니다.

1. `docker compose up --build`로 전체 서비스가 실행되는가?
2. backend `/health`가 정상 응답하는가?
3. frontend 화면이 열리는가?
4. monitor 화면이 열리는가?
5. worker 로그에서 장애 감지 또는 복구 이벤트가 보이는가?
6. 장애 유형 2개 이상을 설명할 수 있는가?
7. 복구 전략 2개 이상을 설명할 수 있는가?
8. Guardrail 또는 안전 제한 규칙이 있는가?
9. `docs/test-checklist.md`에 테스트 결과가 정리되어 있는가?
10. 팀 README만 보고 다른 사람이 실행할 수 있는가?
11. `docker compose config`가 통과하는가?
12. AWS 배포 시 어떤 서비스로 확장할지 설명할 수 있는가?

## GitHub Actions와 AWS 제출 기준

07에서 GitHub Actions와 AWS 실제 배포는 필수는 아니지만, 06에서 배운 내용을 프로젝트 산출물에 반영하는 것을 권장합니다.

```text
GitHub Actions:
- Python 문법 검사
- docker compose config 검증
- Docker image build 검증

AWS 배포 체크리스트:
- ECR image 저장 전략
- App Runner 또는 ECS 중 배포 후보 선택
- 환경변수와 secret 관리 방식
- /health 기반 Health Check
- CloudWatch Logs 확인 방식
- 실습 후 삭제할 리소스 목록
```

팀 프로젝트가 실제 AWS 배포까지 진행하지 않더라도, 위 항목을 문서로 설명할 수 있으면 운영 관점의 설계가 반영된 것입니다.

App Runner와 ECS 선택 기준은 다음처럼 정리합니다.

| 기준 | App Runner | ECS |
| --- | --- | --- |
| 난이도 | 낮음 | 중간 이상 |
| 첫 배포 적합성 | 초보자 첫 클라우드 배포 설명에 적합 | 운영 구조 확장 설명에 적합 |
| 운영 제어 | 제한적 | 세밀함 |
| 여러 서비스 구성 | 단일 웹 서비스에 적합 | backend, worker, monitor 등 확장에 적합 |
| 체크 포인트 | image, port, env, health check, log | cluster, task definition, service, security group, ALB, log |

## 실습 후 정리

Docker Compose 실습이 끝나면 컨테이너를 종료합니다.

```powershell
docker compose down
```

이미지까지 다시 빌드하고 싶거나 디스크 공간을 정리해야 할 때는 먼저 현재 상태를 확인합니다.

```powershell
docker ps -a
docker images
```

사용하지 않는 Docker 리소스를 정리할 때는 아래 명령을 사용할 수 있습니다.

```powershell
docker system prune
```

주의: 이 명령은 사용하지 않는 컨테이너, 네트워크, 이미지 캐시를 정리합니다. 실행 중인 프로젝트가 있다면 먼저 어떤 컨테이너가 켜져 있는지 확인합니다.

## 자주 만나는 오류

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 확인합니다.

포트 충돌이 나면 이미 다른 컨테이너가 실행 중일 수 있습니다.

```powershell
docker ps
docker compose down
```

`Copy-Item.env.example.env`에서 이미 파일이 있다고 나오면 기존 `.env`를 그대로 사용하거나, 필요한 경우 내용을 확인한 뒤 다시 만듭니다.

컨테이너가 정상적으로 뜨지 않으면 로그를 먼저 확인합니다.

```powershell
docker compose logs backend
docker compose logs worker
```

화면은 열리는데 데이터가 이상하면 아래 순서로 확인합니다.

1. backend의 `/health`가 정상 응답하는가?
2. worker 로그에 장애 감지 이벤트가 기록되는가?
3. 복구 전략이 선택되는가?
4. monitor가 이벤트를 표시하는가?
5. frontend가 올바른 API 주소를 보고 있는가?
