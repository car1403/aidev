# Agent Design

이 문서는 기존 호환용 설계 문서입니다. 최종 제출 기준은 `agent-architecture.md`를 우선으로 합니다.

## State

| Field | Type | Description |
| --- | --- | --- |
| user_request | str | 사용자 일정 요청 |
| intent | str | 분석된 의도 |
| required_tools | list[str] | 필요하다고 판단한 Tool 목록 |
| tools_called | list[str] | 실제 호출한 Tool 목록 |
| tool_results | dict | Tool 실행 결과 |
| error_count | int | 오류 또는 재시도 횟수 |
| iteration | int | 현재 반복 실행 횟수 |
| memory_summary | str | 이전 대화 또는 기억 요약 |
| decision_reason | str | Tool 선택 이유 |
| reflection_notes | list[str] | 자기 성찰 메모 |
| final_answer | str | 최종 답변 |

## Nodes

| Node | Role |
| --- | --- |
| collect_request | 사용자 요청을 State에 저장 |
| analyze_intent | 요청 의도와 필요한 정보 분석 |
| decide_tool | 어떤 Tool을 실행할지 결정 |
| call_tool | Tool 실행 |
| validate_result | Tool 결과 검증 |
| reflect_or_retry | 오류가 있으면 수정 전략 선택 |
| generate_final_answer | 최종 일정 제안 생성 |

## Tools

| Tool | Input | Output |
| --- | --- | --- |
| check_calendar_tool | participants, date_range | 참석자 일정 |
| find_available_slot_tool | schedules, duration | 가능한 시간 후보 |
| draft_schedule_message_tool | selected_slot, participants | 일정 제안 메시지 |
