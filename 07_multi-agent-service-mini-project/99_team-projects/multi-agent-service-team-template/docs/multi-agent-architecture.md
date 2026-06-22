# Multi-Agent Architecture Design Document

이 문서는 멀티 에이전트 아키텍처 설계서입니다.

## 1. Business Requirements

이번 프로젝트는 **에러 자가 치유(Auto Healing) 워크플로우**를 구현합니다.

아키텍처를 선택할 때 아래 기준을 고려합니다.

| Requirement | Architecture Decision | Reason |
| --- | --- | --- |
| 응답 속도 | | |
| 결정 일관성 | | |
| 장애 격리 | | |
| 운영 가시성 | | |

아키텍처 선택 근거에는 아래 질문에 대한 답을 포함합니다.

- 장애 대응 속도가 중요한가, 판단 정확도가 더 중요한가?
- 장애가 발생한 Agent 또는 서비스만 격리할 수 있는 구조인가?
- Agent의 결정이 서로 충돌할 때 누가 최종 결정을 내리는가?
- 운영자가 실행 이력과 장애 복구 결과를 추적할 수 있는가?

## 2. Agent Roles

| Agent | Role | Responsibility | Depends On | Not Responsible For |
| --- | --- | --- | --- | --- |
| Planner Agent | 복구 계획 수립 | 장애 시나리오 분석과 작업 순서 결정 | Diagnosis | 실제 복구 명령 실행 |
| Executor Agent | 복구 실행 | Retry, Restart, Fallback 실행 또는 시뮬레이션 | Planner | 최종 검증 |
| Critic Agent | 결과 검증 | 복구 성공 여부 판단과 재시도 기준 제시 | Executor | 복구 실행 |
| Memory Keeper Agent | 상태와 이력 관리 | 장애 이력, 복구 결과, 반복 패턴 저장 | All Agents | 정책 결정 |
| Reporter Agent | 운영자 보고 | 결과 요약과 알림 메시지 작성 | Critic | 복구 판단 |

## 3. Handoff Flow

```text
Supervisor
-> Planner
-> Executor
-> Critic
-> Reporter
```

Handoff 흐름에는 각 Agent가 어떤 결과를 다음 Agent에게 넘기는지 함께 작성합니다.

| From | To | Handoff Reason | Required Context |
| --- | --- | --- | --- |
| Supervisor | Planner | 장애 요청을 복구 계획으로 변환 | incident_id, service_name, failure_type |
| Planner | Executor | 복구 전략 실행 요청 | recovery_plan, allowed_tools |
| Executor | Critic | 복구 결과 검증 요청 | execution_result, health_check_result |
| Critic | Reporter | 운영자 보고 요청 | validation_result, final_status |

## 4. Handoff Context

Agent 간 작업을 넘길 때 아래 Context를 전달합니다.

| Field | Type | Description |
| --- | --- | --- |
| incident_id | string | 장애 이벤트 ID |
| service_name | string | 장애가 발생한 서비스 |
| failure_type | string | 장애 유형 |
| severity | string | 심각도 |
| previous_result | object | 이전 Agent의 결과 |
| memory_summary | string | 이전 장애 이력 요약 |
| allowed_tools | list[string] | 다음 Agent가 사용할 수 있는 Tool |
| next_action | string | 다음 작업 |
| handoff_summary | string | 다음 Agent에게 전달할 핵심 요약 |
| policy_notes | string | 보안 정책 또는 운영 제한 사항 |

## 5. Context Synchronization

Agent 간 Context 동기화는 여러 Agent가 같은 장애 요청을 같은 기준으로 이해하도록 만드는 과정입니다.

| Sync Rule | Description |
| --- | --- |
| incident_id 유지 | 모든 Agent가 같은 장애 이벤트를 처리하는지 확인합니다. |
| service_name/failure_type 일관성 | 장애 대상과 장애 유형이 중간에 바뀌지 않게 합니다. |
| previous_result 갱신 | 이전 Agent의 최신 판단 결과를 다음 Agent가 사용합니다. |
| memory_summary 업데이트 | 반복 장애나 이전 복구 결과를 요약해 공유합니다. |
| allowed_tools 제한 | Agent 역할에 맞는 Tool만 사용할 수 있게 합니다. |
| consistency_check | Agent 간 판단 충돌이 있으면 Critic 또는 Feedback Loop로 보냅니다. |

## 6. Communication Structure

선택한 Context 공유 방식을 표시합니다.

```text
[ ] 메시지 큐
[ ] 공유 상태 저장소
[ ] API 기반 Handoff
[ ] 파일 또는 로그 기반 Context 공유
```

선택 이유:


## 7. Responsibility Review

- [ ] Agent 역할 간 중복이 없습니다.
- [ ] Agent 역할 간 공백이 없습니다.
- [ ] Handoff 시 필요한 Context가 누락되지 않습니다.
- [ ] Agent 간 Context 동기화 기준이 있습니다.
- [ ] Context 불일치 시 Critic 또는 Feedback Loop가 검증합니다.
- [ ] 복구 Tool 실행 권한이 제한되어 있습니다.
- [ ] 운영자 승인 필요 작업이 구분되어 있습니다.
