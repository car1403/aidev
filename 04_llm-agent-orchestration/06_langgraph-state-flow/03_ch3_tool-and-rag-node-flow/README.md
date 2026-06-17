# 03_ch3_tool-and-rag-node-flow

이 챕터에서는 Tool 호출과 RAG 검색을 LangGraph Node로 연결하는 방법을 학습합니다.

## 핵심 개념

- Tool Node는 외부 기능을 실행하는 단계입니다.
- RAG Node는 질문과 관련 있는 context를 검색합니다.
- Hybrid Memory는 Session Memory와 Vector Memory를 함께 활용합니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\06_langgraph-state-flow
.\.venv\Scripts\Activate.ps1
python .\03_ch3_tool-and-rag-node-flow\01_tool-node-style-flow.py
python .\03_ch3_tool-and-rag-node-flow\02_mock-rag-node-flow.py
python .\03_ch3_tool-and-rag-node-flow\03_llm-answer-node.py
python .\03_ch3_tool-and-rag-node-flow\04_hybrid-memory-flow.py
```

## 확인 질문

- Tool 결과는 State의 어느 필드에 저장해야 할까요?
- RAG 결과와 Memory 결과가 충돌하면 어떻게 처리할까요?

