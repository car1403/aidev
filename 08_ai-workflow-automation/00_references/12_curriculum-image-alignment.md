# 12_curriculum-image-alignment

이 문서는 제공된 이미지의 `노코드 멀티 에이전트 워크플로우 설계 및 운영` 내용을 `08_ai-workflow-automation` 폴더 구조와 대조하기 위한 강의 점검표입니다.

처음 진행할 때는 "오늘 배우는 내용이 어느 폴더에 들어 있는지" 확인할 수 있고, 운영 관점에서는 수업 전 누락된 항목이 없는지 빠르게 점검할 수 있습니다.

## 이미지 기준 전체 흐름

이미지의 내용은 크게 다음 4개 영역으로 정리할 수 있습니다.

| 이미지 영역 | 수업에서 다루는 핵심 질문 |
| --- | --- |
| AI 워크플로우 개념 및 구성 요소 이해 | AI Workflow는 무엇이고 LLM, RAG, 데이터 처리 노드는 어떻게 연결되는가? |
| AI 워크플로우 설계 및 구현 | AIPP, n8n, Dify 같은 도구로 업무 자동화 흐름을 어떻게 설계하는가? |
| 운영/확장 관점의 AI 워크플로우 설계 고도화 | 복잡한 업무, RAG, Multi-Agent, 보안 흐름을 어떻게 확장하는가? |
| AI 워크플로우 운영 및 관리 역량 강화 | 버전, 비용, 오류, 품질, 로그, 리소스를 어떻게 운영 기준으로 관리하는가? |

## 실제 폴더 대응표

| 이미지 항목 | 현재 반영 위치 |
| --- | --- |
| AI 워크플로우 개념 이해 | `01_workflow-concepts/01_ch1_ai-workflow-big-picture` |
| 전체 아키텍처 구조 | `01_workflow-concepts/02_ch2_llm-tool-memory-workflow` |
| LLM 노드 역할과 동작 | `01_workflow-concepts/02_ch2_llm-tool-memory-workflow` |
| Trigger, Condition, Action 분석 | `01_workflow-concepts/03_ch3_trigger-condition-action` |
| RAG 노드 기능 이해 | `01_workflow-concepts/04_ch4_rag-data-processing-nodes` |
| 데이터 처리 노드 이해 | `01_workflow-concepts/04_ch4_rag-data-processing-nodes` |
| 노드 상호작용 구조 | `01_workflow-concepts/05_ch5_node-interaction-architecture` |
| AIPP 기반 워크플로우 설계 | `02_aipp-workflow` |
| n8n Webhook, IF, HTTP Request | `03_n8n-ai-workflow/01~03` |
| Loop, Fork-Join, 데이터 변환/집계 | `03_n8n-ai-workflow/04_ch4_loop-forkjoin-data-transform` |
| Dify Chatflow, Workflow, Knowledge/RAG | `04_dify-ai-workflow` |
| 버전, 비용, API 사용량 관리 | `05_workflow-ops-and-quality/01_ch1_version-and-cost-management` |
| 오류 처리, 예외 흐름, 안정화 전략 | `05_workflow-ops-and-quality/02_ch2_error-handling-and-exception-flow` |
| 실행 로그 분석과 개선 | `05_workflow-ops-and-quality/03_ch3_log-analysis-and-improvement` |
| 데이터 품질 검증 | `05_workflow-ops-and-quality/04_ch4_data-quality-validation` |
| Workflow Ops Assistant | `05_workflow-ops-and-quality/05_ch5_workflow-ops-assistant` |
| Prompt Injection 방어, 입력/출력 필터링 | `05_workflow-ops-and-quality/06_ch6_prompt-injection-and-security-filters` |
| 리소스 관리, 확장성, 템플릿 운영 | `05_workflow-ops-and-quality/07_ch7_resource-scaling-template-ops` |
| Multi-Agent Workflow 운영 | `05_workflow-ops-and-quality/08_ch8_multi-agent-workflow-ops` |
| 교과목 단위 프로젝트 | `99_mini-project` |

## 강의 운영 관점에서 보강된 항목

이번 점검에서 다음 항목을 보강했습니다.

```text
RAG 노드와 데이터 처리 노드
노드 간 데이터 흐름과 상호작용 구조
n8n Loop, Fork-Join, 데이터 변환/집계 흐름
Prompt Injection 방어와 입력/출력 보안 필터
리소스 관리와 확장성 운영 기준
Workflow Template 운영 기준
Multi-Agent Workflow 운영 구조
```

## 핵심 메시지

다음 순서로 설명하면 이해가 쉽습니다.

```text
1. AI Workflow는 "업무 흐름을 노드로 나눈 자동화 구조"입니다.
2. LLM은 판단과 생성 역할을 담당하지만, 모든 일을 혼자 처리하지 않습니다.
3. Tool은 외부 API, 검색, 데이터베이스, 알림 같은 실제 행동을 수행합니다.
4. RAG는 필요한 지식을 찾아 LLM에게 전달하는 구조입니다.
5. 데이터 처리 노드는 입력을 정리하고, 변환하고, 결과를 검증합니다.
6. n8n, AIPP, Dify는 이 흐름을 화면에서 설계하도록 도와주는 도구입니다.
7. 운영 단계에서는 로그, 비용, 오류, 보안, 품질, 리소스 관리가 중요합니다.
8. Mini Project에서는 하나의 실제 업무 시나리오를 끝까지 설계하고 검증합니다.
```

## 수업 전 점검 체크리스트

수업 전에 아래 항목을 확인합니다.

```text
[ ] 08_ai-workflow-automation 최상위.venv가 준비되어 있다.
[ ] requirements.txt 설치가 완료되어 있다.
[ ] 01_workflow-concepts의 Python 예제를 실행해 보았다.
[ ] n8n Docker 컨테이너 실행 방법을 확인했다.
[ ] AIPP, n8n, Dify 중 수업에서 실제로 사용할 도구를 정했다.
[ ] API Key가 필요한 실습과 필요 없는 실습을 구분했다.
[ ] 수업용 실습은 실제 개인정보나 회사 데이터를 사용하지 않도록 안내한다.
[ ] 99_mini-project의 결과물 기준을 수업 초반에 안내한다.
```

## 현재 판단

현재 `08_ai-workflow-automation`은 이미지의 주요 커리큘럼 흐름과 잘 맞습니다.

특히 초반에는 개념과 도구 사용법을 배우고, 중반에는 n8n/Dify/AIPP를 활용해 실제 Workflow를 설계하며, 후반에는 운영, 보안, 품질, 리소스 관리와 Multi-Agent Workflow 운영까지 확장하는 구조입니다.
