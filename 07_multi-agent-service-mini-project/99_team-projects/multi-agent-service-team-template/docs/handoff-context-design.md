# Handoff Context Design

Agent 간 업무 인계 구조를 정리합니다.

## 1. Context 필드

| 필드 | 의미 | 예시 |
| --- | --- | --- |
| `incident_id` | 장애 이벤트 식별자 | `inc-001` |
| `service_name` | 장애가 발생한 서비스 | `backend` |
| `failure_type` | 장애 유형 | `timeout` |
| `current_agent` | 현재 Agent | `diagnosis` |
| `next_agent` | 다음 Agent | `recovery` |
| `handoff_reason` | 인계 이유 | `timeout detected` |
| `previous_result` | 이전 판단 결과 | `request exceeded threshold` |
| `allowed_tools` | 허용 Tool | `health_check` |
| `blocked_tools` | 차단 Tool | `delete_resource` |
| `required_action` | 다음 작업 | `retry and validate` |

## 2. Handoff 예시

```json
{
  "incident_id": "inc-001",
  "service_name": "backend",
  "failure_type": "timeout",
  "current_agent": "diagnosis",
  "next_agent": "recovery",
  "handoff_reason": "timeout detected",
  "previous_result": "backend response exceeded threshold",
  "allowed_tools": ["retry_request", "health_check"],
  "blocked_tools": ["delete_resource"],
  "required_action": "retry and validate"
}
```

## 3. 동기화 기준

- 모든 Agent는 같은 `incident_id`를 사용합니다.
- `service_name`이 중간에 바뀌면 이유를 기록합니다.
- `failure_type`이 바뀌면 재분류 근거를 기록합니다.
- `previous_result`가 비어 있으면 다음 Agent가 판단을 중단합니다.
- 권한이 없는 Tool 요청은 Guardrail에서 차단합니다.
