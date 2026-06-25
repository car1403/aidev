# 05_multi-agent-service-sample-assets

이 폴더는 07 최종 프로젝트에서 참고할 수 있는 샘플 자산의 안내 공간입니다.

프로젝트의 실제 작업은 `99_team-projects/multi-agent-service-team-template`을 복사해서 진행합니다. 이 폴더는 중복 코드를 계속 늘리는 곳이 아니라, 팀 프로젝트에서 어떤 자료를 가져다 쓰면 좋은지 정리하는 참고 공간으로 사용합니다.

## 참고할 샘플 위치

| 자료 | 위치 | 용도 |
| --- | --- | --- |
| 실행 가능한 샘플 서비스 | `02_instructor-sample-project` | backend, frontend, worker, monitor 흐름 확인 |
| 팀 프로젝트 템플릿 | `99_team-projects/multi-agent-service-team-template` | 최종 프로젝트 시작점 |
| Auto Healing 설계 문서 | `04_auto-healing-project-practice` | 장애 유형과 복구 전략 설계 |
| 프로젝트 기준 문서 | `00_references` | 제출 기준과 체크리스트 확인 |

## 재사용할 수 있는 설계 요소

아래 항목은 팀 프로젝트 문서에 그대로 가져가서 수정할 수 있습니다.

```text
Agent 역할 표
Handoff Context 예시
장애 유형 표
복구 전략 표
Health Check 기준
Retry/Fallback 기준
Guardrail 기준
감사 로그 기준
LangSmith식 trace/run/span 계획
GitHub Actions 검증 흐름
AWS 배포 체크리스트
```

## 권장 사용 방법

1. `02_instructor-sample-project`를 먼저 실행합니다.
2. `99_team-projects/multi-agent-service-team-template`을 복사합니다.
3. 이 폴더의 안내를 보며 필요한 설계 요소를 선택합니다.
4. 팀 프로젝트의 `docs` 문서에 맞게 수정합니다.
5. 코드와 문서가 같은 구조를 설명하는지 확인합니다.

## 주의 사항

- 샘플 문장을 그대로 제출하기보다 팀 프로젝트 주제에 맞게 수정합니다.
- Agent 이름과 장애 유형은 실제 구현한 코드와 일치해야 합니다.
- 문서에 적은 복구 전략은 시연이나 로그로 확인 가능해야 합니다.
- AWS/GitHub Actions는 선택 확장이므로 실제 적용 여부를 문서에 명확히 적습니다.
