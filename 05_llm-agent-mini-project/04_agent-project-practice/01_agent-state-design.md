# 01 Agent State Design

이 문서는 팀 프로젝트의 Agent State를 설계하기 위한 실습 문서입니다.

State는 Agent 실행 중 공유되는 데이터입니다. Node가 바뀌어도 계속 전달되는 값이므로, 너무 적어도 문제이고 너무 많아도 디버깅이 어려워집니다.

## 권장 State 예시

```python
class AgentState(TypedDict):
    user_request: str
    intent: str
    participants: list[str]
    required_tools: list[str]
    tools_called: list[str]
    tool_results: dict
    error_count: int
    iteration: int
    memory_summary: str
    decision_reason: str
    reflection_notes: list[str]
    final_answer: str
```

## 작성할 것

| 필드 | 타입 | 어느 Node에서 채우는가 | UI에 보여줄 것인가 | 필요한 이유 |
| --- | --- | --- | --- | --- |
| `user_request` | `str` | 입력 단계 | 예 | 원본 요청 보관 |
| `intent` | `str` | 요청 분석 Node | 예 | 어떤 작업인지 판단 |
| `tools_called` | `list[str]` | Tool 실행 Node | 예 | 실행 이력 확인 |
| `final_answer` | `str` | 최종 응답 Node | 예 | 사용자에게 보여줄 답변 |

## 점검 질문

- 같은 의미의 값이 여러 필드에 중복 저장되어 있지 않은가?
- 오류 횟수와 반복 횟수를 구분했는가?
- Tool 결과를 원본 그대로 저장할지 요약해서 저장할지 정했는가?
- UI에 보여줄 State와 내부 디버깅용 State를 구분했는가?
