# Handoff Context Design

Agent 간 업무 인계와 Context 공유 구조를 작성합니다.

## 1. Agent 흐름

```text
Supervisor Agent
-> Diagnosis Agent
-> Recovery Agent
-> Validation Agent
-> Reporter Agent
```

## 2. Handoff Context

```text
request_id:
current_agent:
next_agent:
handoff_reason:
handoff_context:
previous_result:
required_action:
allowed_tools:
```

## 3. Agent별 Context

| Agent | 받는 Context | 다음 Agent에게 전달할 Context |
| --- | --- | --- |
| Supervisor Agent |  |  |
| Diagnosis Agent |  |  |
| Recovery Agent |  |  |
| Validation Agent |  |  |
| Reporter Agent |  |  |

## 4. MCP/Tool 연결

| Agent | 사용할 Tool | 필요한 권한 | 제한 사항 |
| --- | --- | --- | --- |
| Diagnosis Agent |  |  |  |
| Recovery Agent |  |  |  |
| Validation Agent |  |  |  |

## 5. 민감 정보 처리

```text
Context에 포함해도 되는 정보:
Context에서 제외할 정보:
마스킹할 정보:
로그에 남기지 않을 정보:
```
