# 04_ai-workflow-project-practice

AI 워크플로우 미니 프로젝트를 단계별로 설계하는 실습 문서입니다.

이 폴더의 문서는 팀 프로젝트를 바로 구현하기 전에, 직접 먼저 생각을 정리하도록 돕는 설계 연습 자료입니다. 강의에서는 이 문서를 하나씩 작성한 뒤 `99_team-projects`의 팀 템플릿으로 옮겨가면 좋습니다.

## 실습 순서

```text
01_workflow-scenario-design.md
-> 02_tool-and-platform-design.md
-> 03_api-and-automation-flow.md
-> 04_ops-quality-validation.md
-> 05_rag-data-node-design.md
-> 06_security-resource-multi-agent-ops.md
```

## 문서별 역할

| 문서 | 작성 목표 |
| --- | --- |
| 01_workflow-scenario-design.md | 어떤 업무를 자동화할지 정리 |
| 02_tool-and-platform-design.md | AIPP, n8n, Dify, FastAPI, Streamlit 중 사용할 도구 선택 |
| 03_api-and-automation-flow.md | API, Webhook, 자동화 흐름 설계 |
| 04_ops-quality-validation.md | 오류 처리, 로그, 품질 검증 기준 설계 |
| 05_rag-data-node-design.md | RAG, 데이터 처리 노드, 노드 간 데이터 흐름 설계 |
| 06_security-resource-multi-agent-ops.md | 보안 필터, 리소스 관리, Multi-Agent Workflow 운영 설계 |

## 강의 진행 팁

처음부터 완벽한 구현을 요구하지 않아도 됩니다. 먼저 아래 질문에 답하게 하면 프로젝트 방향이 빠르게 정리됩니다.

```text
1. 어떤 업무를 자동화할 것인가?
2. 사용자는 누구인가?
3. 입력 데이터는 무엇인가?
4. AI는 무엇을 판단하거나 생성하는가?
5. 어떤 도구가 필요한가?
6. RAG 또는 Knowledge가 필요한가?
7. 잘못된 입력이나 공격성 입력은 어떻게 막을 것인가?
8. 실패하면 어떤 fallback 흐름으로 처리할 것인가?
9. 로그, 비용, 품질은 어떻게 확인할 것인가?
10. 여러 Agent가 필요하다면 역할을 어떻게 나눌 것인가?
```
