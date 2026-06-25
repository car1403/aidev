# 07_multi-agent-service-mini-project

`07_multi-agent-service-mini-project`는 `06_multi-agent-service-ops`에서 학습한 Multi-Agent 협업, Docker Compose, 서비스 운영, Auto Healing, 보안 가드레일, 관측성(Observability)을 하나의 미니 프로젝트로 묶어 구현하는 과정입니다.

이 과정의 주제는 **에러 자가 치유(Auto Healing) 워크플로우**입니다. 장애가 발생했을 때 여러 Agent가 역할을 나누어 원인을 분석하고, 복구 전략을 선택하고, 실행 결과를 검증하고, 운영 로그와 대시보드에 남기는 구조를 만듭니다.

07은 새로운 이론을 많이 추가하는 과정이 아닙니다. 06에서 배운 내용을 실제 프로젝트 산출물로 정리하고, Docker Compose 기반 서비스로 실행하며, 최종 발표와 제출이 가능한 형태로 다듬는 단계입니다.

## 핵심 요약

```text
06_multi-agent-service-ops
-> Multi-Agent 협업, Docker Compose, GitHub Actions, AWS, 보안, Auto Healing, Observability 학습

07_multi-agent-service-mini-project
-> 위 내용을 팀 미니 프로젝트로 구현하고 산출물로 제출
```

최종 프로젝트는 아래 흐름이 끝까지 보여야 합니다.

```text
장애 이벤트 발생
-> 장애 유형 분류
-> 담당 Agent 선택
-> Context 전달
-> 복구 전략 선택
-> 복구 실행 또는 시뮬레이션
-> Health Check 재확인
-> 결과 검증과 Feedback Loop
-> 운영 로그와 감사 로그 기록
-> Monitor 대시보드에서 결과 확인
```

## 프로젝트 주제

```text
멀티 에이전트 협업 및 서비스 운영
-> 에러 자가 치유(Auto Healing) 워크플로우
```

## 프로젝트 진행 방향

1. 에이전트 협업 시나리오와 전체 구조를 설계합니다.
2. 장애 유형별 감지 기준과 복구 전략을 정리합니다.
3. Docker Compose로 backend, frontend, worker, monitor 서비스를 실행합니다.
4. Agent 간 Handoff, Context 공유, Feedback Loop를 문서와 코드에 반영합니다.
5. 보안 가드레일, 감사 로그, 정책 위반 추적 기준을 정리합니다.
6. GitHub Actions와 AWS 배포는 선택 확장 항목으로 체크리스트를 작성합니다.
7. 최종 산출물을 기준에 맞게 제출하고 시연합니다.

## 06 과정과의 연결

| 06 과정 내용 | 07 프로젝트 적용 |
| --- | --- |
| Multi-Agent 협업 설계 | Supervisor, Diagnosis, Recovery, Validation, Reporter 역할 설계 |
| Handoff/Context/MCP | Agent 간 업무 인계 Context, Tool 권한, 실행 결과 전달 구조 설계 |
| Agent 간 동기화 | request_id, incident_id, service_name, failure_type 기준으로 협업 일관성 유지 |
| Feedback Loop | 복구 실패 시 재시도, fallback, 검증 Agent 재판단 흐름 설계 |
| Docker Compose | backend, frontend, worker, monitor를 하나의 프로젝트로 실행 |
| GitHub Actions | Docker Compose 설정과 Docker image build 자동 검증 |
| AWS 배포 | App Runner 또는 ECS 확장 체크리스트 작성 |
| AI 보안/가드레일 | 위험한 복구 명령 제한, 정책 기반 응답 검증, Prompt Injection 방어 |
| Auto Healing | Health Check, Retry, Restart, Reconnect, Fallback 흐름 구현 |
| Observability | 서비스 로그, 실행 상태, LangSmith식 trace/run/span 관점 정리 |

## 필수 산출물

| 산출물 | 파일 예시 | 핵심 확인 기준 |
| --- | --- | --- |
| 멀티 에이전트 아키텍처 설계서 | `docs/multi-agent-architecture.md` | Agent 역할, 책임, Handoff, Context 동기화가 명확한가 |
| 배포 및 장애 복구 보고서 | `docs/deployment-recovery-report.md` | Compose 구조, 장애 감지 기준, 복구 전략, 복구 결과가 정리되었는가 |
| 파이프라인 구현 결과 보고서 | `docs/pipeline-result-report.md` | 커밋, 빌드, 테스트, 배포, 알림, 실패 처리 흐름이 설명되었는가 |

## 필수 구현 범위

```text
backend  : Health Check, 장애 이벤트 접수 API, 복구 결과 조회 API
frontend : 장애 이벤트 입력과 결과 확인 화면
worker   : 장애 유형 분류, 복구 전략 선택, 재시도/대체 경로 처리
monitor  : 운영 이벤트, 실행 상태, 복구 결과, 감사 로그 표시
```

처음부터 완벽한 운영 시스템을 만들 필요는 없습니다. 중요한 것은 작은 장애 시나리오라도 아래 기준을 만족하는 것입니다.

- 장애 이벤트가 들어오는가?
- Agent가 역할에 따라 판단하는가?
- Context가 다음 Agent로 전달되는가?
- 복구 전략이 선택되는가?
- 복구 결과가 검증되는가?
- 운영 로그와 대시보드에 결과가 남는가?
- 보안상 위험한 작업은 제한되는가?

## 권장 Agent 역할

| Agent | 역할 |
| --- | --- |
| Supervisor Agent | 전체 장애 요청을 보고 담당 Agent와 실행 순서를 결정합니다. |
| Diagnosis Agent | 장애 원인과 유형을 분석합니다. |
| Recovery Agent | Retry, Restart, Reconnect, Fallback 등 복구 전략을 선택합니다. |
| Validation Agent | 복구 이후 Health Check와 결과를 검증합니다. |
| Reporter Agent | 실행 결과, 실패 원인, 다음 조치를 요약합니다. |
| Guardrail Agent | 위험한 명령, 민감 정보, 정책 위반 가능성을 확인합니다. |

## Agent 간 Context 예시

```json
{
  "incident_id": "inc-2026-001",
  "service_name": "backend",
  "failure_type": "timeout",
  "current_agent": "diagnosis",
  "next_agent": "recovery",
  "handoff_reason": "timeout failure classified",
  "previous_result": "backend response exceeded threshold",
  "allowed_tools": ["health_check", "retry_request"],
  "blocked_tools": ["delete_resource", "rotate_secret"],
  "required_action": "retry and verify"
}
```

## 과정 구조

```text
07_multi-agent-service-mini-project
├─ README.md
├─ SETUP.md
├─ .env.example
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

## 폴더별 역할

| 폴더 | 역할 |
| --- | --- |
| `00_references` | 프로젝트를 시작하기 전 확인할 개념, 체크리스트, 제출 기준 |
| `01_local-dev-basic` | Docker Desktop, Docker Compose, Health Check 확인 |
| `02_instructor-sample-project` | backend, frontend, worker, monitor가 함께 동작하는 샘플 서비스 |
| `03_team-project-guide` | 팀 구성, 주제 선택, 역할 분담, 일정, 발표 기준 |
| `04_auto-healing-project-practice` | 장애 감지, 복구 전략, Feedback Loop 설계 실습 |
| `05_multi-agent-service-sample-assets` | 프로젝트에 재사용할 수 있는 샘플 문서와 구조 안내 |
| `99_team-projects` | 최종 팀 프로젝트 템플릿과 작업 공간 |

## 권장 진행 순서

1. [SETUP.md](./SETUP.md)를 보고 Python `.venv`, Docker Desktop, Docker Compose를 확인합니다.
2. [00_references](./00_references/README.md)를 읽고 프로젝트 기준을 확인합니다.
3. [01_local-dev-basic](./01_local-dev-basic/README.md)에서 Docker와 Health Check 흐름을 확인합니다.
4. [02_instructor-sample-project](./02_instructor-sample-project/README.md)를 실행해서 샘플 서비스 흐름을 확인합니다.
5. [03_team-project-guide](./03_team-project-guide/README.md)에서 팀 구성과 산출물 기준을 정리합니다.
6. [04_auto-healing-project-practice](./04_auto-healing-project-practice/README.md)에서 장애 대응 흐름을 설계합니다.
7. [99_team-projects](./99_team-projects/multi-agent-service-team-template/README.md)의 템플릿을 기반으로 최종 프로젝트를 진행합니다.

## 빠른 실행

공통 환경 준비:

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

샘플 프로젝트 실행:

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

종료:

```powershell
docker compose down
```

## 팀 프로젝트 시작

팀 템플릿을 복사해서 새 폴더를 만듭니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
Copy-Item .\99_team-projects\multi-agent-service-team-template .\99_team-projects\team-01-auto-healing-service -Recurse
```

복사 후 새 프로젝트 폴더에서 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\team-01-auto-healing-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 최종 시연 체크리스트

1. `docker compose config`가 통과하는가?
2. `docker compose up --build`로 전체 서비스가 실행되는가?
3. backend `/health`가 정상 응답하는가?
4. frontend에서 장애 이벤트를 입력할 수 있는가?
5. worker 로그에서 장애 분석과 복구 전략 선택이 보이는가?
6. monitor에서 운영 이벤트와 복구 결과를 확인할 수 있는가?
7. Agent 역할과 Handoff Context가 문서화되어 있는가?
8. 장애 유형 2개 이상과 복구 전략 2개 이상이 정리되어 있는가?
9. 보안 Runbook, 감사 로그, Guardrails 검증 기준이 있는가?
10. GitHub Actions와 AWS 배포는 필수 여부와 선택 확장 기준이 명확한가?

## GitHub Actions와 AWS 기준

07에서 GitHub Actions와 AWS 실제 배포는 필수가 아닙니다. 다만 운영형 프로젝트로 확장할 수 있도록 아래 항목을 문서에 정리하는 것을 권장합니다.

```text
GitHub Actions:
- Python 문법 검사
- docker compose config 검증
- Docker image build 검증

AWS:
- ECR image 저장 전략
- App Runner 또는 ECS 선택 기준
- 환경변수와 secret 관리 방식
- /health 기반 Health Check
- CloudWatch Logs 확인 방식
- 실습 후 리소스 삭제 계획
```

## 주의 사항

- `.env`는 GitHub에 올리지 않습니다.
- API Key, AWS Access Key, 비밀번호는 문서나 발표 자료에 적지 않습니다.
- Docker Desktop이 켜져 있어야 Compose 명령이 동작합니다.
- AWS 실습은 비용이 발생할 수 있으므로 실제 배포 전에 범위와 삭제 계획을 확인합니다.
- `aidev_student`에는 지금 반영하지 않습니다. 최종 정리 후 한꺼번에 반영합니다.
