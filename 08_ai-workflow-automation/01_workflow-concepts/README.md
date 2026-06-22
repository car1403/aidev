# 01_workflow-concepts

AI 워크플로우 자동화의 기본 개념을 학습하는 단원입니다.

이 단원에서는 AIPP, n8n, Dify 같은 도구를 바로 사용하기 전에, 모든 워크플로우 도구에 공통으로 들어가는 구조를 먼저 이해합니다.

## 학습 목표

- AI 워크플로우가 일반 자동화와 어떻게 다른지 설명할 수 있다.
- LLM, Tool, Memory가 워크플로우 안에서 어떤 역할을 하는지 이해한다.
- RAG 노드와 데이터 처리 노드의 역할을 이해한다.
- 노드 간 입력/출력 계약과 상호작용 구조를 설계할 수 있다.
- Trigger, Condition, Action 기반의 자동화 흐름을 설계할 수 있다.
- 업무 자동화 시나리오를 단계별 실행 흐름으로 분해할 수 있다.
- 이후 AIPP, n8n, Dify 실습에서 공통으로 쓰이는 개념을 미리 익힌다.

## 전체 구조

```text
01_workflow-concepts
├─ README.md
├─ 01_ch1_ai-workflow-big-picture
├─ 02_ch2_llm-tool-memory-workflow
├─ 03_ch3_trigger-condition-action
├─ 04_ch4_rag-data-processing-nodes
├─ 05_ch5_node-interaction-architecture
├─ 10_labs
└─ 20_assignments
```

## 권장 학습 순서

```text
01_ch1_ai-workflow-big-picture
-> 02_ch2_llm-tool-memory-workflow
-> 03_ch3_trigger-condition-action
-> 04_ch4_rag-data-processing-nodes
-> 05_ch5_node-interaction-architecture
-> 10_labs
-> 20_assignments
```

## 단원별 핵심 내용

| 챕터 | 내용 |
| --- | --- |
| 01_ch1_ai-workflow-big-picture | AI 워크플로우의 전체 구조, 일반 자동화와 AI 자동화의 차이 |
| 02_ch2_llm-tool-memory-workflow | LLM, Tool, Memory 역할과 데이터 흐름 |
| 03_ch3_trigger-condition-action | Trigger, Condition, Action 기반 실행 흐름 설계 |
| 04_ch4_rag-data-processing-nodes | RAG, 전처리, 변환, 후처리 데이터 노드 역할 |
| 05_ch5_node-interaction-architecture | 노드 간 데이터 흐름, 입력/출력 계약, 상호작용 구조 |
| 10_labs | 개념을 손으로 분해하고 Python으로 실행해보는 실습 |
| 20_assignments | 업무 자동화 시나리오 설계 과제 |

## AI 워크플로우란?

AI 워크플로우는 단순히 AI에게 질문하고 답을 받는 구조가 아닙니다.

업무 이벤트가 발생했을 때, 필요한 데이터를 모으고, AI가 판단하거나 문장을 생성하고, 외부 도구를 실행하고, 결과를 검증하는 전체 흐름입니다.

```text
업무 이벤트 발생
-> 입력 데이터 수집
-> 조건 판단
-> LLM 분석 또는 생성
-> Tool 실행
-> 결과 저장
-> 사용자 또는 운영자에게 알림
```

예시:

```text
고객 문의 접수
-> 문의 유형 분류
-> 지식베이스 검색
-> 답변 초안 생성
-> 위험 표현 검증
-> 담당자에게 전달
```

## 일반 자동화와 AI 워크플로우의 차이

일반 자동화는 규칙이 명확한 작업에 강합니다.

```text
새 메일 도착
-> 첨부 파일 저장
-> 슬랙 알림 전송
```

AI 워크플로우는 판단, 요약, 분류, 생성, 검색 보강이 필요한 작업에 적합합니다.

```text
새 고객 문의 도착
-> 문의 의도 분석
-> 긴급도 판단
-> 관련 문서 검색
-> 답변 초안 생성
-> 담당 부서 분류
```

## 핵심 구성 요소

```text
Trigger: 워크플로우를 시작하는 사건
Input: 워크플로우에 들어오는 데이터
Condition: 다음 단계를 결정하는 조건
LLM: 판단, 요약, 생성, 분류를 담당하는 AI 모델
Tool: 외부 API, DB, 파일, 알림 등 실제 작업을 수행하는 기능
Memory: 이전 실행 이력, 사용자 정보, 대화 맥락
Action: 실제로 수행되는 작업
Output: 사용자나 시스템에 전달되는 결과
Log: 실행 기록과 오류 기록
```

## 이번 단원에서 다루는 예제

이번 단원은 외부 서비스 없이 Python만으로 개념을 연습합니다.

```text
1. 업무 요청을 워크플로우 단계로 분해
2. LLM, Tool, Memory 역할을 코드 구조로 표현
3. Trigger, Condition, Action 흐름을 Python 함수로 실행
```

## 실행 준비

상위 폴더에서 가상 환경을 활성화합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

01 단원 예제는 기본적으로 외부 API Key 없이 실행됩니다.

## 실습 파일 실행 순서

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python.\01_ch1_ai-workflow-big-picture\01_ai_workflow_map.py
python.\02_ch2_llm-tool-memory-workflow\01_llm_tool_memory_flow.py
python.\03_ch3_trigger-condition-action\01_trigger_condition_action.py
python.\04_ch4_rag-data-processing-nodes\01_rag_data_processing_nodes.py
python.\05_ch5_node-interaction-architecture\01_node_interaction_map.py
```

## 이후 단원과의 연결

01 단원의 개념은 이후 도구 실습에서 그대로 이어집니다.

```text
01 개념 학습
-> 02 AIPP에서 노드 기반 워크플로우 설계
-> 03 n8n에서 Trigger와 Action 자동화 구성
-> 04 Dify에서 LLM 앱과 Workflow 구성
-> 05 운영/품질/오류 처리 체계화
-> 99 미니 프로젝트
```
