# Multi-Agent Architecture

## 1. 프로젝트 개요

```text
프로젝트 이름:
해결하려는 장애:
주요 사용자:
주요 서비스:
```

## 2. 아키텍처 선택 이유

아래 기준으로 왜 Multi-Agent 구조를 선택했는지 작성합니다.

- 응답 속도
- 결정 일관성
- 장애 격리
- 역할 분리
- 확장 가능성

## 3. Agent 역할

| Agent | 역할 | 입력 | 출력 | 사용 가능한 Tool |
| --- | --- | --- | --- | --- |
| Supervisor | 전체 흐름 조율 | 장애 이벤트 | 다음 Agent 선택 | router |
| Diagnosis | 장애 유형 분석 | 장애 이벤트, 로그 | failure_type | log_reader |
| Recovery | 복구 전략 선택 | failure_type | recovery_plan | retry, fallback |
| Validation | 복구 결과 검증 | recovery_result | validation_result | health_check |
| Reporter | 결과 요약 | 전체 실행 결과 | report | summary |
| Guardrail | 위험 작업 제한 | 요청, Tool 실행 계획 | allow/block | policy_check |

## 4. Handoff 흐름

```text
Supervisor
-> Diagnosis
-> Recovery
-> Validation
-> Reporter
```

## 5. Context 동기화 기준

```text
incident_id:
service_name:
failure_type:
current_agent:
next_agent:
previous_result:
allowed_tools:
blocked_tools:
required_action:
```

## 6. 검증 기준

- Agent 책임이 중복되지 않는가?
- Handoff Context가 누락되지 않는가?
- 실패 시 Feedback Loop가 있는가?
- 위험한 Tool 실행이 제한되는가?
- monitor에서 실행 결과를 확인할 수 있는가?
