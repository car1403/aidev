# Project Plan

## 프로젝트 주제

복합 API 연계 일정 조정 에이전트

## 해결하려는 문제

여러 사람의 일정, 회의 길이, 선호 시간대를 고려해서 가능한 회의 시간을 제안합니다. 사용자의 요청에 정보가 부족하거나 일정 충돌이 있는 경우에는 에이전트가 추가 질문 또는 대체 제안을 해야 합니다.

## 사용자

일정 조정이 필요한 팀, 스터디 그룹, 프로젝트 모임을 기본 사용자로 가정합니다.

## 사용자 요청 예시

```text
예시 1: 다음 주 월요일 오후에 3명이 가능한 1시간 회의 시간을 찾아줘.
예시 2: 이번 주 안에 민수, 지연, 수빈이 모두 가능한 시간으로 회의 잡아줘.
예시 3: 내일 오전 회의가 가능한지 확인하고 초대 메시지도 만들어줘.
```

## 주요 기능

1. 사용자 요청에서 날짜, 참여자, 회의 길이 같은 조건을 추출합니다.
2. Mock 일정 데이터를 조회해서 가능한 시간을 찾습니다.
3. 가능한 시간이 없으면 대체 시간이나 추가 질문을 생성합니다.
4. 최종 일정 제안과 초대 메시지를 Streamlit 화면에 표시합니다.

## 필요한 Tool

| Tool | Input | Output | Failure Case |
| --- | --- | --- | --- |
| check_calendar_tool | participants, date_range | 참여자별 일정 목록 | 참여자 이름 누락, 날짜 범위 누락 |
| find_available_slot_tool | schedules, duration | 가능한 시간 후보 | 가능한 시간이 없음, 회의 길이 누락 |
| draft_schedule_message_tool | selected_slot, participants | 일정 초대 메시지 | 선택된 시간이 없음 |

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
- 현재 대화에서 사용자가 말한 날짜, 참여자, 회의 길이를 저장합니다.

Long-term Memory:
- 선택 기능입니다. 반복되는 선호 시간대나 자주 만나는 참여자 정보를 저장할 수 있습니다.

요약 전략:
- 긴 대화가 이어지면 최근 요청과 확정된 조건만 짧게 요약합니다.
```

## 테스트할 오류 유형

- [ ] Tool 선택 오류
- [ ] 파라미터 누락
- [ ] 응답 불일치
- [ ] 일정 충돌
- [ ] 정보 부족

## 팀 구성

| 이름 | 역할 |
| --- | --- |
| | Agent Architecture |
| | Backend/Graph |
| | Tools/Data |
| | Frontend |
| | Test Report/Presentation |
