# 03_team-project-guide

이 폴더는 07 최종 미니 프로젝트를 기획하고 운영하기 위한 가이드입니다.

07의 프로젝트는 단순히 코드를 제출하는 것이 아니라, Multi-Agent 서비스 운영 구조를 설계하고 실행 결과를 문서로 설명하는 과정입니다.

## 진행 순서

1. [01_topic-selection.md](./01_topic-selection.md)
2. [02_role-and-schedule.md](./02_role-and-schedule.md)
3. [03_project-requirements.md](./03_project-requirements.md)
4. [04_test-checklist.md](./04_test-checklist.md)
5. [05_final-presentation.md](./05_final-presentation.md)
6. [06_submission-checklist.md](./06_submission-checklist.md)

## 팀 구성

권장 팀 구성은 4~5명입니다.

| 역할 | 담당 내용 |
| --- | --- |
| API 담당 | backend API, Health Check, 장애 이벤트 처리 |
| Worker 담당 | 장애 유형 분류, 복구 전략, Feedback Loop |
| UI/Monitor 담당 | frontend 화면, monitor 대시보드 |
| Docker/CI 담당 | Docker Compose, GitHub Actions, 실행 검증 |
| 문서/QA 담당 | 설계서, 보고서, 테스트 체크리스트, 발표 자료 |

## 프로젝트 핵심 산출물

```text
docs/multi-agent-architecture.md
docs/deployment-recovery-report.md
docs/pipeline-result-report.md
docs/test-checklist.md
```

추가 산출물:

```text
docs/handoff-context-design.md
docs/feedback-loop-review.md
docs/security-runbook.md
docs/audit-policy-log.md
docs/guardrails-validation.md
docs/langsmith-tracing-plan.md
```

## 권장 일정

| 단계 | 할 일 |
| --- | --- |
| 1 | 샘플 프로젝트 실행, 팀 구성, 주제 선택 |
| 2 | Agent 역할, 장애 유형, 복구 전략 설계 |
| 3 | backend, worker, frontend, monitor 기본 구현 |
| 4 | Docker Compose 실행, Health Check, 로그 확인 |
| 5 | 보안/감사/Guardrails 문서 작성 |
| 6 | GitHub Actions/AWS 선택 확장 기준 작성 |
| 7 | 테스트 체크리스트 작성과 최종 시연 준비 |

## 최종 기준

프로젝트는 아래 질문에 답할 수 있어야 합니다.

- 어떤 장애를 해결하려고 하는가?
- 어떤 Agent가 어떤 역할을 맡는가?
- Agent 간 Context는 어떻게 전달되는가?
- 복구 전략은 무엇인가?
- 복구 결과는 어떻게 검증하는가?
- 운영 로그와 감사 로그는 어디에 남는가?
- Docker Compose로 전체 서비스를 실행할 수 있는가?
- GitHub Actions와 AWS로 확장할 수 있는 구조인가?
