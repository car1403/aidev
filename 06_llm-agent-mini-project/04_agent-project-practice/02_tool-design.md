# 02 Tool Design

Tool은 Agent가 외부 기능을 사용하기 위한 Python 함수입니다.

05 프로젝트에서는 실제 외부 API를 바로 붙이기보다 Mock data 기반 Tool을 먼저 작성합니다. Tool이 안정적으로 동작한 뒤 필요할 때 외부 API로 바꿉니다.

## 작성할 것

| Tool 이름 | 입력 | 출력 | 실패 시 처리 | State 저장 위치 |
| --- | --- | --- | --- | --- |
| `extract_participants` | 사용자 요청 | 참석자 목록 | 기본 참석자 사용 | `participants` |
| `find_common_available_slots` | 참석자 목록, 회의 시간 | 가능 시간 목록 | 빈 목록 반환 | `tool_results` |
| `select_best_slot` | 가능 시간 목록 | 선택된 시간 | fallback 이동 | `tool_results` |

## 기준

- 함수 이름은 동작을 설명해야 합니다.
- 입력과 출력 구조가 단순해야 합니다.
- 실패해도 프로그램이 멈추지 않아야 합니다.
- Tool 결과는 State에 저장되어야 합니다.
- 외부 API로 바꾸기 전 Mock data로 같은 입력/출력 구조를 검증해야 합니다.

## Tool 설계 질문

- 이 Tool이 없으면 Agent가 문제를 해결할 수 없는가?
- Tool 입력값은 State에서 가져올 수 있는가?
- Tool 출력값은 다음 Node가 바로 사용할 수 있는가?
- 실패했을 때 재시도할 것인가, fallback할 것인가?
