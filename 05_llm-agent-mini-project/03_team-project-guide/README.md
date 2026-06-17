# 03 Team Project Guide

이 폴더는 `05_llm-agent-mini-project`의 팀 프로젝트 진행 문서입니다.

이번 미니 프로젝트의 기준 주제는 **복합 API 연계 일정 조정 에이전트**입니다. 학생들은 `04_llm-agent-orchestration`에서 배운 Prompt, Tool Use, Function Calling, Memory, LangGraph를 연결해 사용자의 일정 조정 요청을 분석하고, 필요한 도구를 선택하고, 결과를 검증한 뒤 최종 제안을 생성하는 단일 에이전트를 구현합니다.

## 프로젝트 큰 방향

```text
1. LangGraph를 이용한 다중 도구(Multi-tool) 선택 및 순환형 워크플로우 설계
2. 에이전트의 판단 오류를 스스로 수정하는 자기 성찰 및 피드백 루프 구현
3. 실시간 API 데이터 기반의 의사결정 시나리오 테스트 및 서비스 배포 실습
```

05 과정에서는 기본적으로 Mock data와 Python Tool을 사용해 에이전트 흐름을 완성합니다. OpenAI API, 로컬 Llama, pgvector, 외부 API는 팀 상황에 따라 선택 확장합니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 `06_multi-agent-service-ops`에서 학습합니다.

## 최종 프로젝트 주제

```text
분야:
단일 에이전트 추론 및 AI 오케스트레이션

프로젝트:
복합 API 연계 일정 조정 에이전트
```

## 필수 산출물

| 산출물 | 설명 |
| --- | --- |
| 에이전트 아키텍처 설계서 | StateGraph Node, `인지 -> 판단 -> 행동 -> 검증` 사고 흐름, Decision, Tool, Memory, State 구조를 설명하는 문서 |
| 에이전트 시험 결과 보고서 | 판단 오류, 재시도, Fallback, 자기 성찰, 피드백 루프, 개선 전후 수치 결과를 정리하는 문서 |

## 문서 목록

```text
01_topic-selection.md
02_role-and-schedule.md
03_project-requirements.md
04_test-checklist.md
05_final-presentation.md
06_submission-checklist.md
```

## 제출 전 확인할 것

- StateGraph의 각 Node가 `인지 -> 판단 -> 행동 -> 검증` 흐름에 맞게 배치되었는가?
- 분기 조건과 fallback 흐름이 edge 또는 node로 문서화되었는가?
- Session Memory와 Long-term Memory 적용 여부, 컨텍스트 요약 전략이 설명되었는가?
- Function Calling 또는 Tool Use 흐름이 `선택 -> 호출 -> 결과 처리 -> 다음 노드 결정` 순서로 명확한가?
- Agent State 필드가 타입 힌트와 함께 정리되었고 중복이 없는가?
- 판단 오류 감지 기준과 재시도 전략이 오류 유형별로 있는가?
- 자기 성찰 적용 전후 결과를 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수로 비교했는가?
