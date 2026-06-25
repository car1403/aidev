# 01. Agent Collaboration Design

Auto Healing 프로젝트의 첫 단계는 Agent 역할을 나누는 것입니다.

## 권장 Agent 구조

| Agent | 책임 |
| --- | --- |
| Supervisor Agent | 장애 요청을 보고 다음 Agent를 선택합니다. |
| Diagnosis Agent | 장애 원인과 유형을 분석합니다. |
| Recovery Agent | 복구 전략을 선택하고 실행합니다. |
| Validation Agent | 복구 이후 서비스 상태를 검증합니다. |
| Reporter Agent | 실행 결과와 다음 조치를 요약합니다. |
| Guardrail Agent | 위험 작업, 권한, 정책 위반 가능성을 확인합니다. |

## Handoff Context 설계

Agent 간 업무를 넘길 때는 아래 정보가 누락되지 않아야 합니다.

```json
{
  "incident_id": "inc-001",
  "service_name": "backend",
  "failure_type": "timeout",
  "current_agent": "diagnosis",
  "next_agent": "recovery",
  "handoff_reason": "timeout detected",
  "previous_result": "request exceeded 5 seconds",
  "allowed_tools": ["retry_request", "health_check"],
  "blocked_tools": ["delete_resource"],
  "required_action": "retry and validate"
}
```

## Agent 간 Context 동기화 기준

- 모든 Agent가 같은 `incident_id`를 사용합니다.
- 장애 대상 서비스인 `service_name`이 바뀌지 않아야 합니다.
- 장애 유형인 `failure_type`은 변경 시 이유를 기록합니다.
- 이전 Agent의 판단 결과가 `previous_result`에 남아야 합니다.
- Tool 권한은 Agent 역할에 맞게 제한합니다.
- 판단이 충돌하면 Feedback Loop로 다시 검증합니다.

## 설계 체크리스트

- [ ] Agent 역할이 3개 이상 정의되어 있다.
- [ ] Agent 간 책임 중복이 없다.
- [ ] Handoff Context 필드가 정의되어 있다.
- [ ] Context 동기화 기준이 있다.
- [ ] 위험한 Tool 실행 제한 기준이 있다.
- [ ] 복구 실패 시 Feedback Loop가 있다.
