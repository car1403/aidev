# Multi-Agent Service Team Template

이 폴더는 07 최종 미니 프로젝트를 시작하기 위한 팀 템플릿입니다.

주제는 **에러 자가 치유(Auto Healing) 워크플로우**입니다. Docker Compose로 backend, frontend, worker, monitor를 함께 실행하고, 장애 이벤트가 들어왔을 때 여러 Agent가 역할을 나누어 복구 흐름을 처리하는 구조를 구현합니다.

## 실행 목표

```text
1. 장애 이벤트 입력
2. Agent 기반 장애 유형 분석
3. 복구 전략 선택
4. Health Check와 결과 검증
5. 운영 로그와 대시보드 표시
6. 보안/감사/Guardrails 기준 문서화
```

## 서비스 구성

| 서비스 | 역할 |
| --- | --- |
| backend | FastAPI API 서버, Health Check, 장애 이벤트 처리 |
| frontend | 장애 이벤트 입력과 결과 확인 화면 |
| worker | 장애 감지, 복구 전략 선택, Feedback Loop 처리 |
| monitor | 운영 이벤트, 서비스 상태, 복구 결과 대시보드 |

## 실행 준비

Docker Desktop이 실행 중인지 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인 주소

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

## 로그 확인

다른 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간 worker 로그:

```powershell
docker compose logs -f worker
```

## 종료

```powershell
docker compose down
```

## 주로 수정할 파일

```text
backend/main.py
-> Health Check, 장애 이벤트 API, 복구 결과 API

worker/main.py
-> 장애 감지, Retry, Restart, Fallback, Feedback Loop 로직

frontend/app.py
-> 장애 이벤트 입력과 실행 결과 확인 화면

monitor/app.py
-> 운영 이벤트, 서비스 상태, 감사 로그 대시보드

docker-compose.yml
-> 서비스 구성, 포트, 환경변수, healthcheck

docs/*.md
-> 설계서, 보고서, 테스트 체크리스트
```

## 필수 구현 기준

- Docker Compose로 3개 이상의 서비스가 실행되어야 합니다.
- backend `/health`가 정상 응답해야 합니다.
- 장애 유형을 2개 이상 정의해야 합니다.
- 복구 전략을 2개 이상 정의해야 합니다.
- Agent 역할을 3개 이상 정의해야 합니다.
- Agent 간 Handoff/Context 구조를 문서화해야 합니다.
- Feedback Loop 기반 결과 검증 흐름이 있어야 합니다.
- worker 또는 monitor에서 운영 로그를 확인할 수 있어야 합니다.
- 보안 Runbook, 감사 로그, Guardrails 검증 기준을 작성해야 합니다.

## 필수 산출물

| 산출물 | 파일 |
| --- | --- |
| 멀티 에이전트 아키텍처 설계서 | `docs/multi-agent-architecture.md` |
| 배포 및 장애 복구 보고서 | `docs/deployment-recovery-report.md` |
| 파이프라인 구현 결과 보고서 | `docs/pipeline-result-report.md` |
| 테스트 체크리스트 | `docs/test-checklist.md` |
| Handoff/Context 설계 | `docs/handoff-context-design.md` |
| Feedback Loop 검토 | `docs/feedback-loop-review.md` |
| 보안 Runbook | `docs/security-runbook.md` |
| 감사 로그/정책 위반 추적 | `docs/audit-policy-log.md` |
| Guardrails 검증 | `docs/guardrails-validation.md` |
| LangSmith식 실행 추적 계획 | `docs/langsmith-tracing-plan.md` |

## 선택 확장 기준

- GitHub Actions Docker build check
- AWS App Runner 또는 ECS 배포 체크리스트
- CloudWatch Logs 확인 계획
- LangSmith trace/run/span 추적 계획
- 위험 Tool 실행 제한
- Prompt Injection 방어
- 비용과 보안 주의 사항 정리

## 발표 전 확인

- [ ] `docker compose config`가 통과한다.
- [ ] `docker compose up --build`가 동작한다.
- [ ] backend `/health`가 정상 응답한다.
- [ ] frontend에서 장애 이벤트를 입력할 수 있다.
- [ ] worker 로그에서 장애 처리 흐름을 확인할 수 있다.
- [ ] monitor에서 운영 상태와 복구 결과를 확인할 수 있다.
- [ ] 필수 문서가 작성되어 있다.
- [ ] `.env`와 API Key가 Git에 올라가지 않았다.
