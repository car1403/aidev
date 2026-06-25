# 04 Agent Project Practice

이 폴더는 팀 프로젝트를 구현하기 전에 Agent 설계를 연습하는 곳입니다.

코드를 바로 작성하기 전에 State, Tool, Graph, UI 테스트 계획을 먼저 정리합니다. 이 문서들이 정리되어 있으면 `99_team-projects`의 최종 설계서와 시험 결과 보고서를 훨씬 쉽게 작성할 수 있습니다.

## 실습 순서

1. `01_agent-state-design.md` 작성
2. `02_tool-design.md` 작성
3. `03_graph-flow-design.md` 작성
4. `04_ui-test-plan.md` 작성

## 실습에서 확인할 기준

- State에는 사용자 요청, Tool 호출 결과, 오류 횟수, 반복 횟수, 최종 답변이 구분되어 있는가?
- Tool은 입력값, 출력값, 실패 상황이 명확한가?
- Graph는 `인지 -> 판단 -> 행동 -> 검증 -> 최종 응답` 흐름으로 설명되는가?
- Decision Node는 도구 필요 여부, 사용자 의도, 데이터 충분성에 따라 분기하는가?
- Fallback은 말로만 설명하지 않고 별도 흐름으로 표현되는가?
- UI 테스트 계획에는 정상 요청, 정보 부족 요청, Tool 오류, 응답 불일치 상황이 포함되는가?

## 완료 후 이동

이 폴더의 문서를 작성한 뒤 아래 템플릿에 반영합니다.

```text
99_team-projects/llm-agent-team-template/docs/project-plan.md
99_team-projects/llm-agent-team-template/docs/agent-architecture.md
99_team-projects/llm-agent-team-template/docs/agent-test-report.md
```
