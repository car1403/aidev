# 03 Team Project Guide

이 폴더는 `06_llm-agent-mini-project`의 팀 프로젝트 진행 문서입니다.

이번 미니 프로젝트의 기준 주제는 **복합 API 연계 일정 조정 Agent**입니다. 실제 API를 처음부터 붙이지 않고, 먼저 Mock data와 Python Tool로 Agent 흐름을 완성한 뒤 필요할 때 선택 확장합니다.

## 프로젝트 진행 방향

```text
1. LangGraph를 이용한 Multi-tool 선택 및 순환형 workflow 설계
2. Agent 판단 오류를 감지하고 수정하는 Self-Reflection 및 Feedback Loop 구현
3. Mock data 기반 의사결정 시나리오 테스트
4. 필요할 때 OpenAI API, 로컬 Llama, RAG, Memory, 외부 API 선택 확장
```

Docker Compose, AWS 배포, GitHub Actions, 서비스 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 최종 프로젝트 기준 주제

```text
분야:
단일 Agent 추론 및 AI 오케스트레이션

프로젝트:
복합 API 연계 일정 조정 Agent
```

## 필수 산출물

| 산출물 | 설명 |
| --- | --- |
| Agent Architecture 설계서 | StateGraph Node, 분기 조건, Memory, Tool 호출 흐름, 공유 State 필드를 설명하는 문서 |
| Agent Test Report | 판단 오류, 재시도, Fallback, Self-Reflection, 개선 전후 결과를 정리하는 문서 |

06 과정의 필수 산출물은 위 2가지입니다. 실행 가능한 Agent 코드는 산출물 검증을 위한 기본 조건이며, 프로젝트 계획서, 테스트 체크리스트, 발표 자료는 선택 보조 산출물입니다.

## 문서 목록

```text
01_topic-selection.md
02_role-and-schedule.md
03_project-requirements.md
04_test-checklist.md
05_final-presentation.md
06_submission-checklist.md
```

## 진행 순서

1. `01_topic-selection.md`에서 프로젝트 주제와 사용자 요청 예시를 정합니다.
2. `02_role-and-schedule.md`에서 팀 구성과 일정 계획을 정합니다.
3. `03_project-requirements.md`에서 필수 구현 범위를 확인합니다.
4. `04_test-checklist.md` 기준으로 정상/실패 요청을 선택적으로 점검합니다.
5. 필요하면 `05_final-presentation.md` 기준으로 발표 자료를 정리합니다.
6. `06_submission-checklist.md`로 최종 제출 전 빠진 항목을 확인합니다.

## 제출 전 핵심 확인

- StateGraph의 각 Node가 `인지 -> 판단 -> 행동 -> 검증 -> 최종 응답` 흐름에 맞게 배치되었는가?
- 분기 조건과 fallback 흐름이 edge 또는 node로 문서화되었는가?
- Tool Use 흐름이 `선택 -> 호출 -> 결과 처리 -> 다음 노드 결정` 순서로 표현되었는가?
- Agent State 필드가 타입 힌트와 함께 정리되었는가?
- 판단 오류 감지 기준과 재시도 전략이 시험 결과 보고서에 포함되었는가?
- API Key 없이도 Mock data 기반 최소 흐름을 실행할 수 있는가?
