# 05_ch5_handoff-context-mcp

Agent 간 업무 인계(Handoff), 컨텍스트 공유, MCP(Model Context Protocol) 관점의 외부 도구 연결 구조를 학습합니다.

## 학습 목표

- Agent 간 Handoff가 왜 필요한지 이해합니다.
- 다음 Agent에게 전달해야 할 Context를 구조화할 수 있습니다.
- Context를 모두 공유하는 방식과 필요한 정보만 전달하는 방식의 차이를 설명할 수 있습니다.
- Agent 간 Context 동기화와 협업 일관성 유지 기준을 설계할 수 있습니다.
- MCP를 외부 도구와 컨텍스트를 연결하는 표준화된 인터페이스 관점으로 이해합니다.
- Multi-Agent 서비스에서 Agent 간 정보 전달 규칙을 설계할 수 있습니다.

## 핵심 개념

### Handoff

Handoff는 한 Agent가 처리하던 업무를 다른 Agent에게 넘기는 구조입니다.

예시:

```text
Supervisor Agent
-> Diagnosis Agent
-> Recovery Agent
-> Validation Agent
-> Reporter Agent
```

각 Agent는 이전 Agent의 전체 대화가 아니라, 다음 작업에 필요한 요약된 Context를 받아야 합니다.

### Context

Context는 Agent가 다음 판단을 하기 위해 필요한 실행 정보입니다.

```text
request_id
user_request
current_agent
previous_result
handoff_reason
required_action
constraints
```

운영 환경에서는 Context가 너무 크면 비용과 지연이 늘고, 너무 작으면 Agent가 잘못 판단할 수 있습니다.

### Context 동기화

Context 동기화는 여러 Agent가 같은 요청을 같은 기준으로 이해하도록 만드는 과정입니다.

```text
Supervisor Agent가 request_id와 공통 조건을 만든다.
-> Diagnosis Agent가 장애 원인을 추가한다.
-> Recovery Agent가 복구 전략을 추가한다.
-> Validation Agent가 복구 결과를 검증한다.
-> Reporter Agent가 전체 결과를 요약한다.
```

동기화할 핵심 필드 예시:

```text
request_id
service_name
incident_type
current_status
previous_result
next_action
confidence
policy_notes
```

모든 Agent가 전체 대화를 그대로 공유할 필요는 없습니다. 대신 공통으로 필요한 값은 유지하고, 각 Agent가 추가한 판단 근거는 `previous_result` 또는 `handoff_summary`로 넘깁니다.

### MCP 관점

MCP는 모델 또는 Agent가 외부 도구, 데이터, 파일, 서비스와 연결될 때 사용할 수 있는 표준화된 연결 방식으로 이해할 수 있습니다.

이 단원에서는 실제 MCP 서버를 구축하기보다, 다음 질문을 중심으로 구조를 설계합니다.

```text
Agent가 어떤 외부 도구를 사용할 수 있는가?
도구 호출에 필요한 입력 Context는 무엇인가?
도구 결과를 다음 Agent에게 어떻게 전달하는가?
권한이 없는 Agent는 어떤 도구를 호출하지 못하게 할 것인가?
```

## 실행 예제

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
python.\05_ch5_handoff-context-mcp\01_handoff_context_mcp.py
```

## 수업에서 확인할 질문

```text
Handoff할 때 전체 대화를 넘겨야 하는가?
다음 Agent에게 꼭 필요한 Context는 무엇인가?
Agent 간 Context가 서로 다를 때 어떻게 동기화할 것인가?
협업 일관성을 확인하는 기준은 무엇인가?
Context에 민감 정보가 포함되면 어떻게 처리해야 하는가?
MCP 같은 도구 연결 구조에서 권한 확인은 어디서 해야 하는가?
```
