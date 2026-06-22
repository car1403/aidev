# Audit Policy Log

감사 로그와 정책 위반 이력 추적 설계를 작성합니다.

## 1. 감사 로그 항목

```text
event_id:
timestamp:
request_id:
user_id:
agent_name:
tool_name:
policy_name:
decision:
reason:
risk_level:
action_taken:
```

## 2. 정책 위반 유형

| 정책 | 위반 예시 | 처리 방식 |
| --- | --- | --- |
| Prompt Injection | | block |
| 민감 정보 보호 | | redact |
| Tool 권한 제한 | | review |
| 복구 명령 제한 | | escalate |

## 3. decision 기준

```text
allow:
block:
redact:
review:
escalate:
```

## 4. 운영 대시보드 표시 기준

```text
전체 이벤트 수:
정책 위반 이벤트 수:
위험도 높은 이벤트:
반복 위반 사용자:
사람 검토 대기 이벤트:
```
