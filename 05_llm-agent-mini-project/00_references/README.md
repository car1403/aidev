# 00 References

이 폴더는 `05_llm-agent-mini-project`를 시작하기 전에 읽는 참고 자료입니다.

## 읽는 순서

1. `01_project-big-picture.md`
2. `02_agent-project-idea-list.md`
3. `03_agent-design-checklist.md`
4. `04_previous-course-link.md`
5. `05_docker-local-extension-guide.md`
6. `06_practice-material-checklist.md`

## 문서별 역할

| 문서 | 역할 |
| --- | --- |
| `01_project-big-picture.md` | 05 미니 프로젝트의 전체 흐름을 이해합니다. |
| `02_agent-project-idea-list.md` | 팀별 프로젝트 아이디어를 고를 때 참고합니다. |
| `03_agent-design-checklist.md` | State, Tool, Graph, UI 설계 전 점검 질문을 확인합니다. |
| `04_previous-course-link.md` | 04 과정에서 배운 내용을 05 프로젝트에 어떻게 연결하는지 확인합니다. |
| `05_docker-local-extension-guide.md` | 로컬 Llama 또는 pgvector를 선택 확장할 때 Docker 실행 방법을 확인합니다. |
| `06_practice-material-checklist.md` | 실습 파일과 과제 자료가 어떤 역할을 하는지 확인합니다. |

## 핵심 질문

- 이 프로젝트의 사용자는 누구인가?
- 사용자는 어떤 요청을 입력하는가?
- Agent는 어떤 상태를 저장해야 하는가?
- 어떤 Tool이 필요한가?
- RAG 또는 Memory가 꼭 필요한가?
- Docker 확장이 필요한가, 아니면 Mock data로 충분한가?
- 최종 결과는 Streamlit 화면에서 어떻게 보여줄 것인가?
- 테스트 결과를 어떤 기준으로 성공 또는 실패로 판단할 것인가?
- 발표 자료에서 Agent 구조를 한 장으로 설명할 수 있는가?

## 정리 기준

05 과정의 기준 설명과 제출 기준은 최상위 `README.md`에 통합되어 있습니다. `00_references`는 수업 전에 참고하거나 프로젝트 진행 중 다시 확인하는 보조 자료만 둡니다.

## 05에서 가장 중요한 기준

05는 04의 개념을 다시 길게 설명하는 과정이 아닙니다. 04에서 배운 Prompt, Tool, RAG, Memory, LangGraph를 실제 프로젝트 안에서 어떻게 조합하는지 확인하는 과정입니다.

따라서 참고 문서를 읽을 때는 항상 아래 흐름을 기준으로 봅니다.

```text
문제 정의
-> 사용자 요청 예시
-> State 설계
-> Tool 설계
-> Graph 흐름 설계
-> Mock data 기반 실행
-> LLM/RAG/Memory 선택 확장
-> 테스트와 발표
```
