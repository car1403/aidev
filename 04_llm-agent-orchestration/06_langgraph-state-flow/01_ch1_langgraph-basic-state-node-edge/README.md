# 01_ch1_langgraph-basic-state-node-edge

이 챕터에서는 LangGraph의 가장 기본 구조인 State, Node, Edge를 학습합니다.

## 핵심 개념

- State는 Agent 흐름 전체에서 공유되는 데이터입니다.
- Node는 State를 입력받아 처리하고 다시 State를 반환합니다.
- Edge는 다음에 실행할 Node를 연결합니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\06_langgraph-state-flow
.\.venv\Scripts\Activate.ps1
python.\01_ch1_langgraph-basic-state-node-edge\01_basic-state-graph.py
python.\01_ch1_langgraph-basic-state-node-edge\02_multi-step-state-update.py
```

## 확인 질문

- State에는 어떤 정보를 넣어야 할까요?
- Node는 일반 함수와 무엇이 비슷한가요?

