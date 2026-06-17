# Lab 05. Handoff, Context Sync, MCP

## 목표

Agent 간 업무 인계(Handoff), Context 공유, Agent 간 Context 동기화, MCP식 외부 도구 연결 구조를 설계합니다.

## 실습

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
python .\05_ch5_handoff-context-mcp\01_handoff_context_mcp.py
```

## 작성할 내용

```text
1. Agent 역할 목록
2. 각 Agent가 받는 Context
3. 각 Agent가 다음 Agent에게 넘기는 Context
4. Agent별 허용 Tool 목록
5. 민감 정보가 Context에 들어갈 때 처리 기준
6. Agent 간 Context 동기화 기준
7. 협업 일관성이 깨졌을 때 fallback 기준
```

## 확인 질문

- 전체 대화를 모두 넘기는 것과 필요한 Context만 넘기는 것의 차이는 무엇인가?
- Agent 간 Context가 서로 다르게 해석되었는지 어떻게 확인할 것인가?
- Context 동기화에 반드시 필요한 필드는 무엇인가?
- Handoff 실패 시 어떤 fallback이 필요한가?
- MCP 같은 도구 연결 구조에서 권한 검사는 어디서 해야 하는가?
