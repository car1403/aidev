# 06 LangGraph State Flow

이 단원은 Agent 실행 흐름을 LangGraph의 State, Node, Edge 구조로 설계하는 방법을 학습합니다.

앞 단원에서 프롬프트, Tool, RAG, Memory를 따로 배웠다면, 이 단원에서는 이 요소들을 하나의 상태 흐름으로 묶습니다.

## 학습 목표

- StateGraph의 State, Node, Edge 개념을 이해합니다.
- 여러 단계의 상태 업데이트 흐름을 구현합니다.
- 조건 분기, Retry, Self-Reflection 구조를 설계합니다.
- Tool Node와 RAG Node를 Agent 흐름에 연결합니다.
- Session Memory와 Vector Memory를 함께 사용하는 Hybrid Memory 흐름을 봅니다.
- Planning, Tracing, Evaluation 관점에서 Agent 실행 결과를 점검합니다.

## 폴더 구성

```text
06_langgraph-state-flow
├─.env.example
├─ 01_ch1_langgraph-basic-state-node-edge
│ ├─ 01_basic-state-graph.py
│ └─ 02_multi-step-state-update.py
├─ 02_ch2_conditional-routing
│ ├─ 01_conditional-route-basic.py
│ └─ 02_retry-and-reflection-flow.py
├─ 03_ch3_tool-and-rag-node-flow
│ ├─ 01_tool-node-style-flow.py
│ ├─ 02_mock-rag-node-flow.py
│ ├─ 03_llm-answer-node.py
│ └─ 04_hybrid-memory-flow.py
└─ 04_ch4_debugging-with-langsmith
 ├─ 01_tracing-env-check.py
 └─ 02_planning-tracing-evaluation.py
```

## 실습 시작 순서

```powershell
cd C:\aidev\04_llm-agent-orchestration\06_langgraph-state-flow
python -m venv.venv
.\.venv\Scripts\Activate.ps1
pip install langgraph langchain langchain-openai langchain-core openai python-dotenv
Copy-Item.env.example.env
```

## 실행 순서

```powershell
python.\01_ch1_langgraph-basic-state-node-edge\01_basic-state-graph.py
python.\01_ch1_langgraph-basic-state-node-edge\02_multi-step-state-update.py
python.\02_ch2_conditional-routing\01_conditional-route-basic.py
python.\02_ch2_conditional-routing\02_retry-and-reflection-flow.py
python.\03_ch3_tool-and-rag-node-flow\01_tool-node-style-flow.py
python.\03_ch3_tool-and-rag-node-flow\02_mock-rag-node-flow.py
python.\03_ch3_tool-and-rag-node-flow\03_llm-answer-node.py
python.\03_ch3_tool-and-rag-node-flow\04_hybrid-memory-flow.py
python.\04_ch4_debugging-with-langsmith\01_tracing-env-check.py
python.\04_ch4_debugging-with-langsmith\02_planning-tracing-evaluation.py
```

## 수업 중 확인 질문

- State에는 어떤 정보를 넣어야 하나요?
- Node는 함수와 어떤 점이 비슷하고 어떤 점이 다른가요?
- 조건 분기는 Agent 품질에 어떤 영향을 주나요?
- Reflection과 Retry는 언제 필요할까요?
- Tracing은 Agent 디버깅에서 어떤 도움을 주나요?

