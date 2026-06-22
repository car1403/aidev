# 03 Graph Flow Design

LangGraph 흐름을 설계합니다.

## 기본 예시

```text
START
-> analyze_request
-> run_tools
-> generate_answer
-> END
```

## 선택 확장

```text
START
-> analyze_request
-> route
 -> rag_search
 -> tool_call
 -> ask_clarifying_question
-> evaluate_answer
-> END
```
