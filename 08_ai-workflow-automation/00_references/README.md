# 00_references

`08_ai-workflow-automation` 과정을 시작하기 전에 읽는 사전 참고 자료입니다.

이 폴더는 AIPP, n8n, Dify를 바로 사용하기 전에 수업 참여자가 먼저 알아야 할 개념, 실습 환경, 도구 선택 기준, 오류 해결 방법, 미니 프로젝트 방향을 정리합니다.

## 강의에서 읽는 순서

```text
01_course-big-picture.md
-> 02_ai-workflow-key-concepts.md
-> 03_aipp-n8n-dify-comparison.md
-> 04_environment-checklist.md
-> 05_docker-and-local-tools.md
-> 06_api-and-webhook-basic.md
-> 07_workflow-ops-quality-map.md
-> 08_security-and-cost-safety.md
-> 09_common-errors-for-beginners.md
-> 10_mini-project-roadmap.md
-> 11_aipp-n8n-dify-class-manual.md
-> 12_curriculum-image-alignment.md
```

## 문서별 목적

| 파일 | 목적 |
| --- | --- |
| 01_course-big-picture.md | 08 과정 전체 흐름 이해 |
| 02_ai-workflow-key-concepts.md | Trigger, Condition, Action, LLM, Tool, Memory 개념 정리 |
| 03_aipp-n8n-dify-comparison.md | AIPP, n8n, Dify 역할 차이 비교 |
| 04_environment-checklist.md | Python, .venv, Docker, API Key 준비 확인 |
| 05_docker-and-local-tools.md | n8n, Dify 같은 로컬 도구 실행 관점 이해 |
| 06_api-and-webhook-basic.md | Webhook, HTTP API, JSON 기본 개념 |
| 07_workflow-ops-quality-map.md | 운영, 로그, 비용, 오류 처리, 품질 관리 큰 그림 |
| 08_security-and-cost-safety.md | API Key, 비용, 민감정보, 응답 검증 주의사항 |
| 09_common-errors-for-beginners.md | 초보자가 자주 만나는 오류와 해결 방향 |
| 10_mini-project-roadmap.md | 99 미니 프로젝트 진행 로드맵 |
| 11_aipp-n8n-dify-class-manual.md | AIPP, n8n, Dify를 수업에서 따라 하는 단계별 매뉴얼 |
| 12_curriculum-image-alignment.md | 이미지 커리큘럼과 실제 08 폴더 구조 대응표 |

## 핵심 요약

08 과정에서 중요한 것은 도구의 모든 버튼을 외우는 것이 아닙니다. 업무를 자동화 가능한 흐름으로 나누고, 그 흐름을 AIPP, n8n, Dify 중 적절한 도구에 옮기는 능력이 핵심입니다.

```text
업무 시나리오
-> 입력 데이터
-> Trigger
-> Condition
-> AI / Tool 처리
-> Output
-> Log
-> Error Handling
```

## 08 과정 전체 흐름

```text
00_references
-> 01_workflow-concepts
-> 02_aipp-workflow
-> 03_n8n-ai-workflow
-> 04_dify-ai-workflow
-> 05_workflow-ops-and-quality
-> 99_mini-project
```

## 진행 팁

수업 초반에는 AIPP, n8n, Dify를 모두 깊게 다루기보다 같은 업무 시나리오를 세 도구 관점에서 비교하는 방식이 좋습니다.

예시 시나리오:

```text
기술 지원 문의가 들어왔다.
문의 유형을 분류한다.
긴급도에 따라 분기한다.
문서 검색 또는 AI 답변 생성을 수행한다.
답변 후보를 만들고 로그를 남긴다.
```

이 시나리오를 세 도구로 나누어 보면 다음과 같습니다.

| 도구 | 수업에서 보여줄 관점 |
| --- | --- |
| AIPP | AI 업무 흐름을 노드와 단계로 설계하는 방법 |
| n8n | Webhook, IF, HTTP Request로 자동화 흐름을 연결하는 방법 |
| Dify | Knowledge/RAG와 Chatflow로 AI 답변 앱을 만드는 방법 |

수업을 진행할 때는 `11_aipp-n8n-dify-class-manual.md`를 옆에 열어 두고, 각 도구 화면에서 같은 순서로 실습을 진행하면 됩니다.
