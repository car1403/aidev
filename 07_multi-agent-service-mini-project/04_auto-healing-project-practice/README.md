# 04_auto-healing-project-practice

이 폴더는 Auto Healing 프로젝트의 핵심 흐름을 설계하는 실습입니다.

실제 코드를 많이 작성하기 전에, 장애가 발생했을 때 어떤 Agent가 어떤 판단을 하고 어떤 복구 전략을 선택할지 먼저 정리합니다.

## 실습 순서

1. [01_agent-collaboration-design.md](./01_agent-collaboration-design.md)
2. [02_failure-recovery-design.md](./02_failure-recovery-design.md)
3. [03_health-check-retry-fallback.md](./03_health-check-retry-fallback.md)
4. [04_deployment-result-validation.md](./04_deployment-result-validation.md)

## 핵심 흐름

```text
장애 이벤트
-> Supervisor가 담당 Agent 선택
-> Diagnosis가 장애 유형 분석
-> Recovery가 복구 전략 선택
-> Validation이 Health Check로 결과 확인
-> Reporter가 결과 요약
-> Guardrail이 위험 작업과 정책 위반 여부 확인
```

## 최종 문서 연결

이 폴더에서 정리한 내용은 팀 프로젝트의 `docs` 문서로 옮겨집니다.

| 실습 문서 | 최종 산출물 |
| --- | --- |
| Agent 협업 설계 | `docs/multi-agent-architecture.md` |
| 장애 복구 설계 | `docs/deployment-recovery-report.md` |
| Health Check/Retry/Fallback | `docs/test-checklist.md` |
| 배포 결과 검증 | `docs/pipeline-result-report.md` |
