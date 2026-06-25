# Audit Policy Log

감사 로그와 정책 위반 추적 기준을 정리합니다.

## 1. 감사 로그 필드

| 필드 | 의미 |
| --- | --- |
| `timestamp` | 이벤트 발생 시간 |
| `incident_id` | 장애 이벤트 식별자 |
| `agent_name` | 판단 또는 실행한 Agent |
| `action` | 실행하려는 작업 |
| `policy_result` | allow 또는 block |
| `reason` | 허용/차단 이유 |
| `risk_level` | low, medium, high |

## 2. 정책 위반 예시

| 위반 유형 | 예시 | 처리 |
| --- | --- | --- |
| 민감 정보 요청 | API Key 출력 요청 | block |
| 위험 Tool 요청 | 삭제 명령 실행 | block |
| Prompt Injection | 이전 지시 무시 요청 | block |
| 권한 초과 | Agent 권한 밖 Tool 호출 | block |

## 3. 로그 예시

```json
{
  "timestamp": "2026-06-25T10:00:00",
  "incident_id": "inc-001",
  "agent_name": "guardrail",
  "action": "delete_resource",
  "policy_result": "block",
  "reason": "dangerous action is not allowed",
  "risk_level": "high"
}
```

## 4. 확인 기준

- 정책 위반이 기록되는가?
- 누가 어떤 작업을 요청했는지 알 수 있는가?
- 차단 이유가 남는가?
- monitor에서 감사 이벤트를 확인할 수 있는가?
