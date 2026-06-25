# Agent Design

이 문서는 에이전트 설계를 빠르게 확인하기 위한 요약 문서입니다. 최종 제출 기준은 `agent-architecture.md`와 `agent-test-report.md`를 우선합니다.

## State

| Field | Type | Description |
| --- | --- | --- |
| user_request | str | 사용자가 입력한 원본 요청 |
| intent | str | 요청 의도 분석 결과 |
| required_tools | list[str] | 필요하다고 판단한 Tool 목록 |
| tools_called | list[str] | 실제 호출한 Tool 목록 |
| tool_results | dict | Tool 실행 결과 |
| error_count | int | 오류 또는 재시도 횟수 |
| iteration | int | 현재 반복 실행 횟수 |
| memory_summary | str | 이전 대화 또는 기억 요약 |
| decision_reason | str | Tool 선택 이유 |
| reflection_notes | list[str] | 자기 성찰 또는 개선 메모 |
| final_answer | str | 최종 응답 |

## Nodes

| Node | Role |
| --- | --- |
| collect_request | 사용자 요청을 State에 저장합니다. |
| analyze_intent | 요청 의도와 필요한 정보를 분석합니다. |
| decide_tool | 어떤 Tool을 실행할지 결정합니다. |
| call_tool | 선택된 Tool을 실행합니다. |
| validate_result | Tool 결과가 충분하고 일관적인지 검증합니다. |
| reflect_or_retry | 오류가 있으면 수정 전략을 선택합니다. |
| generate_final_answer | 최종 일정 제안을 생성합니다. |

## Tools

| Tool | Input | Output |
| --- | --- | --- |
| check_calendar_tool | participants, date_range | 참여자별 일정 |
| find_available_slot_tool | schedules, duration | 가능한 시간 후보 |
| draft_schedule_message_tool | selected_slot, participants | 일정 제안 메시지 |

## 핵심 설계 기준

- State 필드는 너무 많지 않게 유지하되, 판단과 검증에 필요한 값은 빠뜨리지 않습니다.
- Tool은 한 가지 일을 분명하게 수행하도록 나눕니다.
- Decision Node는 Tool을 선택한 이유를 `decision_reason`에 남깁니다.
- Tool 결과와 최종 응답이 다르면 `validate_result`에서 감지합니다.
- 실패 상황은 숨기지 않고 추가 질문, 대체 제안, fallback 응답으로 처리합니다.
