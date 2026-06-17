# Agent Architecture Design Document

이 문서는 에이전트 아키텍처 설계서입니다. 팀 프로젝트에서는 코드만 제출하는 것이 아니라, 에이전트가 어떤 순서로 생각하고, 어떤 기준으로 도구를 선택하고, 오류가 났을 때 어떻게 복구하는지 문서로 설명해야 합니다.

## 1. Architecture Goal

이번 프로젝트는 **복합 API 연계 일정 조정 에이전트**를 구현합니다.

에이전트는 사용자 요청을 분석하고, 필요한 Tool을 선택하고, Tool 결과를 검증한 뒤, 오류가 있으면 재시도하거나 fallback을 적용해 최종 일정 제안을 생성합니다.

## 2. StateGraph Flow

아래 흐름은 에이전트의 사고 과정을 `인지 -> 판단 -> 행동 -> 검증` 단계로 나누어 표현한 예시입니다.

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

| Thinking Step | Graph Node | Description |
| --- | --- | --- |
| 인지 | collect_request, analyze_intent | 사용자 요청과 필요한 정보를 파악합니다. |
| 판단 | decide_tool | 어떤 Tool을 사용할지 결정합니다. |
| 행동 | call_tool | 일정 조회, 후보 시간 계산 같은 Tool을 실행합니다. |
| 검증 | validate_result, reflect_or_retry | Tool 결과가 충분한지 확인하고 오류 시 재시도 또는 fallback을 선택합니다. |
| 응답 | generate_final_answer | 검증된 결과를 사용자 답변으로 정리합니다. |

## 3. Node Design

| Node | Purpose | Input State | Output State |
| --- | --- | --- | --- |
| collect_request | 사용자 요청 저장 | user_request | user_request, messages |
| analyze_intent | 의도와 필요 정보 분석 | user_request, messages | intent, required_tools |
| decide_tool | 실행할 Tool 선택 | intent, required_tools | decision_reason |
| call_tool | Tool 실행 | required_tools, decision_reason | tools_called, tool_results |
| validate_result | 결과 검증 | tool_results | error_count, validation_result |
| reflect_or_retry | 재시도 또는 fallback 결정 | error_count, tool_results | reflection_notes, iteration |
| generate_final_answer | 최종 답변 생성 | tool_results, reflection_notes | final_answer |

## 4. Branch Conditions

분기 조건은 "그럴 것 같다"가 아니라 명확한 기준값 또는 정책으로 작성합니다.

| Condition | Criteria | Next Node | Fallback |
| --- | --- | --- | --- |
| 도구 필요 | 일정 조회 또는 후보 시간 계산이 필요함 | call_tool | 도구 선택 기준을 다시 계산 |
| 정보 부족 | 날짜, 참석자, 회의 길이 중 필수 정보 누락 | generate_final_answer | 사용자에게 누락 정보 질문 |
| 데이터 충분 | 참석자 일정과 후보 시간이 모두 있음 | validate_result | 없음 |
| 결과 검증 성공 | 일정 후보가 1개 이상 있고 충돌이 없음 | generate_final_answer | 없음 |
| 결과 검증 실패 | 일정 후보 없음, Tool 오류, 응답 불일치 | reflect_or_retry | 대체 날짜 또는 시간 축소 제안 |
| 재시도 초과 | error_count >= 2 또는 iteration >= 3 | generate_final_answer | 실패 이유와 다음 행동 제안 |

## 5. Memory Strategy

| Memory Type | Use | Strategy |
| --- | --- | --- |
| Session Memory | 현재 대화의 요청, 선택 도구, 결과 보관 | Agent State에 저장 |
| Long-term Memory | 사용자 선호 시간, 반복 회의 패턴 저장 | 선택 확장 |
| Summary | 긴 대화에서 핵심 조건만 유지 | 참가자, 날짜, 선호 조건 중심 요약 |

컨텍스트 윈도우가 길어질 때는 모든 대화 원문을 계속 넣지 않습니다. 학생 프로젝트에서는 아래 기준으로 요약합니다.

| Data | Keep Raw? | Summary Strategy |
| --- | --- | --- |
| 최근 사용자 요청 | yes | 최신 요청은 원문 유지 |
| 참석자, 날짜, 회의 길이 | yes | 필수 조건이므로 State 필드로 유지 |
| 오래된 대화 | no | 결정에 필요한 선호 조건만 `memory_summary`로 요약 |
| Tool 실행 로그 | partial | 마지막 성공 결과와 오류 원인만 보관 |

## 6. Tool Use Flow

Function Calling 또는 Tool Use 호출 흐름은 아래처럼 표현합니다.

```text
사용자 요청
-> decide_tool: 필요한 도구 선택
-> call_tool: Python 함수 또는 외부 API 호출
-> validate_result: 결과의 누락, 충돌, 불일치 확인
-> reflect_or_retry: 오류 원인 기록 후 재시도 또는 fallback
-> generate_final_answer: 최종 응답 생성
```

| Step | Description | Output |
| --- | --- | --- |
| select tool | 사용자 의도와 필요한 데이터에 맞는 도구 선택 | required_tools |
| call tool | Python 함수 또는 외부 API 실행 | tool_results |
| handle result | 결과 누락, 오류, 충돌 여부 확인 | validation_result |
| decide next node | 성공이면 답변 생성, 실패면 재시도 또는 fallback | next_node |

## 7. Shared State Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| messages | list[dict] | optional | 대화 메시지 목록 |
| user_request | str | yes | 사용자 원문 요청 |
| intent | str | yes | 요청 의도 |
| required_tools | list[str] | yes | 필요한 Tool 목록 |
| tools_called | list[str] | yes | 실제 호출한 Tool 목록 |
| tool_results | dict | yes | Tool 결과 |
| error_count | int | yes | 오류 또는 재시도 횟수 |
| iteration | int | yes | 반복 실행 횟수 |
| memory_summary | str | optional | 기억 요약 |
| decision_reason | str | yes | 도구 선택 이유 |
| validation_result | dict | optional | 결과 검증 정보 |
| reflection_notes | list[str] | optional | 자기 성찰 메모 |
| final_answer | str | yes | 최종 답변 |

State 설계 시 주의할 점:

- 같은 값을 `intent`, `decision_reason`, `final_answer`에 반복해서 저장하지 않습니다.
- Tool 결과 원본은 `tool_results`에 두고, 화면에 보여줄 문장은 `final_answer`에서만 관리합니다.
- 재시도 횟수는 `error_count`와 `iteration`처럼 목적을 나누어 관리합니다.
- 타입 힌트를 사용해 학생과 강사가 State 구조를 빠르게 확인할 수 있게 합니다.

## 8. Fallback Strategy

```text
도구 호출 실패:
사용자에게 일부 정보를 다시 요청한다.

가능한 시간이 없음:
대체 날짜 또는 회의 시간을 줄이는 옵션을 제안한다.

필수 정보 부족:
누락된 정보를 짧게 질문한다.

응답 불일치:
reflection node에서 원인을 기록하고 한 번 재시도한다.
```

## 9. Review Checklist

- [ ] Node가 `인지 -> 판단 -> 행동 -> 검증` 단계로 설명되었습니다.
- [ ] Start, Decision, Tools, Reflection 또는 Review, End 흐름이 있습니다.
- [ ] 분기 조건이 기준값 또는 정책으로 정의되었습니다.
- [ ] fallback 흐름이 edge 또는 node로 표현되었습니다.
- [ ] Session Memory와 Long-term Memory 전략이 설명되었습니다.
- [ ] 컨텍스트 윈도우와 요약 전략이 설명되었습니다.
- [ ] Tool 호출 흐름이 `선택 -> 호출 -> 결과 처리 -> 다음 노드 결정` 순서로 명확합니다.
- [ ] State 필드 타입이 명확합니다.
- [ ] 불필요한 State 중복이 없습니다.
