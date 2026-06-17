# 01 Agent Collaboration Design

## 작성할 것

- Supervisor Agent
- Ops Agent
- Recovery Agent
- Reviewer Agent
- Monitor Agent

각 Agent의 입력, 출력, 책임을 정리합니다.

## Handoff와 Context 설계

Agent 간 업무를 넘길 때 어떤 정보를 전달할지 작성합니다.

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

## MCP/Tool 연결 설계

각 Agent가 사용할 수 있는 Tool을 정리합니다.

| Agent | 허용 Tool | 금지 Tool | 권한 이유 |
| --- | --- | --- | --- |
| Supervisor Agent |  |  |  |
| Diagnosis Agent |  |  |  |
| Recovery Agent |  |  |  |
| Validation Agent |  |  |  |
| Monitor Agent |  |  |  |

## 확인 질문

- 다음 Agent에게 전체 대화를 넘겨야 하는가, 요약 Context만 넘겨야 하는가?
- 복구 Tool을 실행할 수 있는 Agent는 누구인가?
- Context에 민감 정보가 포함될 경우 어떻게 마스킹할 것인가?
