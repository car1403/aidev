# 01 Agent State Design

아래 형식으로 팀 프로젝트의 State를 설계합니다.

```python
class AgentState(TypedDict):
    user_request: str
    intent: str
    tool_results: list[dict]
    context: str
    final_answer: str
```

## 작성할 것

- 각 필드의 의미
- 어느 노드에서 값이 채워지는지
- Streamlit 화면에 보여줄 필드
