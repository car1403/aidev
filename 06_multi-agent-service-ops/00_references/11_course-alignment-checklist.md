# Course Alignment Checklist

이 문서는 `06_multi-agent-service-ops`가 수업 이미지의 요구 내용을 어떻게 반영하는지 확인하는 학생용 체크리스트입니다.

## 1. 멀티 에이전트 협업 설계

| 확인 항목 | 학습 위치 | 체크 |
| --- | --- | --- |
| 단일 Agent와 Multi-Agent 구조 비교 | `01_multi-agent-collaboration/01_ch1_single-vs-multi-agent` | [ ] |
| 역할(Role) 기반 Agent 분리 | `01_multi-agent-collaboration/02_ch2_role-based-agent-design` | [ ] |
| Supervisor/Router 기반 작업 분배 | `01_multi-agent-collaboration/03_ch3_supervisor-router-workflow` | [ ] |
| 분산 협업 구조와 Agent 결과 통합 | `01_multi-agent-collaboration/04_ch4_distributed-agent-collaboration` | [ ] |
| Agent 간 Handoff와 Context 공유 | `01_multi-agent-collaboration/05_ch5_handoff-context-mcp` | [ ] |
| Agent 간 Context 동기화 및 협업 일관성 유지 | `01_multi-agent-collaboration/05_ch5_handoff-context-mcp`, `06_ch6_feedback-loop-result-review` | [ ] |
| 결과 검증과 Feedback Loop | `01_multi-agent-collaboration/06_ch6_feedback-loop-result-review` | [ ] |

## 2. 서비스 배포 및 자동화 운영

| 확인 항목 | 학습 위치 | 체크 |
| --- | --- | --- |
| Docker 기반 서비스 패키징 | `02_service-deployment-and-automation/01_ch1_docker-service-packaging` | [ ] |
| Docker Compose 기반 멀티 서비스 실행 | `02_service-deployment-and-automation/02_ch2_docker-compose-multi-service` | [ ] |
| Health Check와 Runtime 로그 확인 | `02_service-deployment-and-automation/03_ch3_service-health-and-runtime` | [ ] |
| GitHub Actions 기반 CI/CD 기본 흐름 | `02_service-deployment-and-automation/04_ch4_github-actions-cicd` | [ ] |
| AWS App Runner 또는 ECS 배포 체크리스트 | `02_service-deployment-and-automation/05_ch5_aws-deployment-basic`, `10_labs/lab-06_aws-apprunner-ecs-optional-deployment.md` | [ ] |
| 장애 감지, Retry, Restart, Fallback | `04_auto-healing-workflow` | [ ] |
| 서비스 로그, Trace, 운영 대시보드 | `05_observability-and-ops-dashboard` | [ ] |

## 3. AI 보안 및 가드레일 설계

| 확인 항목 | 학습 위치 | 체크 |
| --- | --- | --- |
| Prompt Injection 방어 | `03_ai-security-and-guardrails/01_ch1_prompt-injection-defense` | [ ] |
| 입력 검증과 응답 필터링 | `03_ai-security-and-guardrails/02_ch2_policy-based-response-validation` | [ ] |
| Tool 실행 권한 제어 | `03_ai-security-and-guardrails/03_ch3_tool-permission-control` | [ ] |
| Multi-Agent 접근 제어 | `03_ai-security-and-guardrails/04_ch4_multi-agent-access-control` | [ ] |
| 보안 운영 가이드라인 | `03_ai-security-and-guardrails/10_labs/lab-05_security-policy-runbook.md` | [ ] |
| 감사 로그와 정책 위반 추적 | `03_ai-security-and-guardrails/10_labs/lab-06_audit-policy-violation-tracking.md` | [ ] |
| Guardrails AI 통합 검증 | `03_ai-security-and-guardrails/10_labs/lab-07_guardrails-ai-integrated-validation.md` | [ ] |

## 4. 최종 확인 질문

- Multi-Agent 협업 구조에서 각 Agent의 책임이 명확한가?
- Agent 간 Context가 누락되거나 서로 다르게 해석되는 문제가 없는가?
- Docker Compose로 실행한 서비스가 health check와 log를 제공하는가?
- AWS 배포 전 image, port, env, health check, log, 비용, 삭제 계획이 정리되었는가?
- 보안 정책 위반과 Tool 권한 오류가 로그로 추적되는가?
