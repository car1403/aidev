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

## Node 역할

| Node | 역할 |
| --- | --- |
| `analyze_request` | 사용자 요청에서 참석자와 회의 시간을 파악합니다. |
| `check_schedules` | Mock 일정 데이터에서 참석자별 가능 시간을 조회합니다. |
| `choose_slot` | 공통 가능 시간대 중 하나를 선택합니다. |
| `draft_message` | 선택된 시간대를 바탕으로 응답 초안을 만듭니다. |
| `finalize_answer` | 최종 답변을 정리합니다. |

## 프로젝트로 확장할 때

팀 프로젝트에서는 이 흐름을 그대로 복사하기보다 다음 질문에 맞게 수정합니다.

- 우리 프로젝트의 사용자 요청은 무엇인가?
- 어떤 Tool을 호출해야 하는가?
- 실패했을 때 fallback Node가 필요한가?
- RAG 또는 Memory Node를 어느 위치에 추가할 것인가?
