# 03 Graph Flow Design

이 문서는 LangGraph 실행 흐름을 설계하기 위한 실습 문서입니다.

Graph는 Agent의 사고 흐름을 코드로 표현한 것입니다. 단순히 함수를 순서대로 호출하는 것이 아니라, State를 기준으로 다음 Node를 선택합니다.

## 기본 흐름 예시

```text
START
-> collect_request
-> analyze_intent
-> decide_tool
-> call_tool
-> validate_result
-> generate_final_answer
-> END
```

## Reflection과 Fallback이 있는 흐름

```text
START
-> collect_request
-> analyze_intent
-> decide_tool
-> call_tool
-> validate_result
   -> success: generate_final_answer
   -> retry: reflect_or_retry
   -> fallback: generate_fallback_answer
-> END
```

## 작성할 것

| Node | 입력 State | 출력 State | 다음 Node 조건 |
| --- | --- | --- | --- |
| `collect_request` | 사용자 입력 | `user_request` | 항상 `analyze_intent` |
| `analyze_intent` | `user_request` | `intent` | 항상 `decide_tool` |
| `decide_tool` | `intent` | `required_tools` | Tool 필요 여부 |
| `call_tool` | `required_tools` | `tool_results` | 결과 충분성 |
| `validate_result` | `tool_results` | `decision_reason` | 성공/재시도/fallback |

## 점검 질문

- 조건 분기 기준이 State 값으로 판단 가능한가?
- 재시도 횟수 제한이 있는가?
- fallback Node가 최종 사용자에게 이해 가능한 메시지를 만드는가?
- RAG 또는 Memory Node를 추가한다면 어느 위치가 적절한가?
