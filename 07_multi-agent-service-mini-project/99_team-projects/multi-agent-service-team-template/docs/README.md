# Docs

이 폴더는 07 최종 미니 프로젝트의 산출물을 정리하는 위치입니다.

코드가 동작하더라도 문서가 없으면 프로젝트의 설계 의도와 운영 기준을 설명하기 어렵습니다. 아래 문서를 기준으로 Agent 구조, 장애 대응, 배포 검증, 보안 기준을 정리합니다.

## 필수 산출물

| 파일 | 역할 |
| --- | --- |
| `multi-agent-architecture.md` | Agent 역할, Handoff, Context 동기화 설계 |
| `deployment-recovery-report.md` | 장애 감지, 복구 전략, 배포/운영 검증 보고 |
| `pipeline-result-report.md` | 커밋, 빌드, 테스트, 배포, 알림 흐름 정리 |
| `test-checklist.md` | 실행, 기능, 문서, 보안 테스트 체크리스트 |

## 보조 산출물

| 파일 | 역할 |
| --- | --- |
| `handoff-context-design.md` | Agent 간 Context 전달 구조 |
| `feedback-loop-review.md` | 복구 실패 후 재시도와 개선 흐름 |
| `security-runbook.md` | 보안 운영 기준과 위험 작업 제한 |
| `audit-policy-log.md` | 감사 로그와 정책 위반 추적 기준 |
| `guardrails-validation.md` | 입력/출력 검증과 Guardrail 기준 |
| `langsmith-tracing-plan.md` | trace/run/span 관점의 실행 추적 계획 |

## 작성 순서

1. `multi-agent-architecture.md`에서 Agent 역할과 협업 구조를 정리합니다.
2. `handoff-context-design.md`에서 Agent 간 전달 데이터를 정리합니다.
3. `deployment-recovery-report.md`에서 장애 유형과 복구 전략을 정리합니다.
4. `feedback-loop-review.md`에서 실패 후 재시도 기준을 정리합니다.
5. `security-runbook.md`, `audit-policy-log.md`, `guardrails-validation.md`에서 보안 기준을 정리합니다.
6. `pipeline-result-report.md`에서 GitHub Actions와 배포 확장 기준을 정리합니다.
7. `test-checklist.md`로 실행과 제출 전 검증을 완료합니다.

## 작성 기준

- 문서에 적은 Agent 이름은 코드와 일치해야 합니다.
- 문서에 적은 장애 유형은 시연할 수 있어야 합니다.
- 복구 전략은 로그나 화면에서 확인 가능해야 합니다.
- 실제 구현하지 않은 AWS 배포는 “선택 확장 설계”로 명확히 표시합니다.
- API Key, AWS Key, 비밀번호는 문서에 적지 않습니다.
