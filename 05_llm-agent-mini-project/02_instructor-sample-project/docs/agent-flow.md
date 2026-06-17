# Agent Flow

샘플 일정 조정 에이전트의 LangGraph 흐름입니다.

```text
START
-> analyze_request
-> check_schedules
-> choose_slot
-> draft_message
-> finalize_answer
-> END
```

## State 필드

| 필드 | 의미 |
| --- | --- |
| user_request | 사용자 요청 원문 |
| participants | 참석자 목록 |
| duration_minutes | 회의 시간 |
| available_slots | 공통 가능 시간대 목록 |
| selected_slot | 선택된 시간대 |
| draft_message | 초안 메시지 |
| final_answer | 최종 답변 |
