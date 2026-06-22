# Project Plan

## 프로젝트 주제

복합 API 연계 일정 조정 에이전트

## 해결하려는 문제


## 사용자


## 사용자 요청 예시

```text
예시 1:
예시 2:
예시 3:
```

## 주요 기능

1.
2.
3.

## 필요한 Tool

| Tool | Input | Output | Failure Case |
| --- | --- | --- | --- |
| check_calendar_tool | | | |
| find_available_slot_tool | | | |
| draft_schedule_message_tool | | | |

## 에이전트 흐름

```text
START
-> collect_request
-> analyze_intent
-> decide_tool
-> call_tool
-> validate_result
-> reflect_or_retry
-> generate_final_answer
-> END
```

## Memory 사용 계획

```text
Session Memory:
Long-term Memory:
요약 전략:
```

## 시험할 오류 유형

- [ ] 도구 선택 오류
- [ ] 파라미터 누락
- [ ] 응답 불일치
- [ ] 일정 충돌
- [ ] 정보 부족

## 팀원 역할

| 이름 | 역할 |
| --- | --- |
| | Agent Architecture |
| | Backend/Graph |
| | Tools/Data |
| | Frontend |
| | Test Report/Presentation |
