# 99 Team Projects

이 폴더는 05 과정의 최종 LLM Agent 미니 프로젝트를 진행하는 위치입니다.

04 과정에서 배운 Prompt, Tool Use, Memory, LangGraph, Self-Reflection을 바탕으로 하나의 작은 에이전트 서비스를 설계하고 실행합니다. 핵심은 복잡한 기능을 많이 넣는 것이 아니라, 에이전트가 어떤 기준으로 판단하고 어떤 도구를 호출하며 실패 상황을 어떻게 복구하는지 명확하게 보여주는 것입니다.

## 기본 템플릿

기본 템플릿은 아래 폴더입니다.

```text
llm-agent-team-template
```

프로젝트를 시작할 때는 템플릿을 복사해서 새 폴더를 만든 뒤 수정합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\99_team-projects
Copy-Item .\llm-agent-team-template .\team-01-schedule-agent -Recurse
cd .\team-01-schedule-agent
```

폴더 이름은 프로젝트 주제가 드러나도록 정합니다.

```text
team-01-schedule-agent
team-02-study-coach-agent
team-03-document-helper-agent
```

## 권장 프로젝트 주제

| 주제 | 설명 |
| --- | --- |
| 일정 조정 에이전트 | 사용자 요청을 분석하고 일정 확인 Tool을 호출해 가능한 시간을 제안합니다. |
| 학습 코치 에이전트 | 학습 목표와 현재 수준을 바탕으로 학습 계획을 추천합니다. |
| 문서 요약 에이전트 | 입력 문서의 핵심 내용을 요약하고 질문에 답변합니다. |
| 고객 문의 분류 에이전트 | 문의 내용을 분류하고 필요한 처리 부서나 다음 행동을 추천합니다. |

## 진행 기준

- 먼저 템플릿을 그대로 실행합니다.
- 그다음 주제에 맞게 State, Tool, Graph, UI를 조금씩 수정합니다.
- OpenAI API Key가 없어도 Mock data와 Mock 응답으로 기본 흐름을 완성할 수 있어야 합니다.
- API Key는 코드에 직접 쓰지 않고 `.env`에만 작성합니다.
- README, 설계 문서, 테스트 보고서를 코드와 함께 계속 업데이트합니다.
- Docker Compose, AWS 배포, GitHub Actions는 06 과정에서 다루므로 05에서는 필수로 넣지 않습니다.

## 최종 확인 기준

- Agent State 구조가 문서와 코드에 일치합니다.
- LangGraph 노드 흐름이 `인지 -> 판단 -> 행동 -> 검증` 순서로 설명됩니다.
- Tool이 2개 이상 있고, Tool 입력값과 출력값이 문서화되어 있습니다.
- 실패 상황에 대한 fallback 또는 retry 흐름이 있습니다.
- Streamlit 화면에서 에이전트 실행 결과를 확인할 수 있습니다.
- `docs/agent-architecture.md`와 `docs/agent-test-report.md`가 작성되어 있습니다.
