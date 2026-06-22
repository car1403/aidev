# 02_aipp-workflow

이 단원은 AIPP를 사용해 AI 워크플로우를 설계하고 실행하는 흐름을 학습합니다.

수업에서는 AIPP를 특정 버튼을 외우는 도구로 보지 않고, 업무 자동화 흐름을 `입력`, `AI 판단`, `도구 실행`, `조건 분기`, `출력`, `로그`로 나누어 설계하는 도구로 다룹니다.

## 학습 목표

- AIPP 기반 AI 워크플로우의 전체 구조를 이해합니다.
- 업무 시나리오를 노드 기반 워크플로우로 분해할 수 있습니다.
- LLM, Agent, Tool, Knowledge, Condition, Output의 역할을 구분할 수 있습니다.
- 실행 결과와 로그를 보고 워크플로우를 개선할 수 있습니다.
- 이후 n8n, Dify 실습과 비교할 수 있는 설계 기준을 만듭니다.

## 전체 구조

```text
02_aipp-workflow
├─ README.md
├─ 01_ch1_aipp-overview
├─ 02_ch2_aipp-workflow-design
├─ 03_ch3_aipp-agent-tool-data-flow
├─ 10_labs
└─ 20_assignments
```

## 권장 학습 순서

```text
01_ch1_aipp-overview
-> 02_ch2_aipp-workflow-design
-> 03_ch3_aipp-agent-tool-data-flow
-> 10_labs
-> 20_assignments
```

## AIPP에서 바라볼 핵심 구조

```text
업무 시나리오
-> Trigger
-> Input Data
-> LLM / Agent Node
-> Tool / Knowledge Node
-> Condition Node
-> Output
-> Log / Review
```

AIPP 화면에서 다음 질문을 계속 확인합니다.

```text
이 워크플로우는 어떤 이벤트로 시작하는가?
입력값은 무엇인가?
AI가 판단해야 하는 부분은 어디인가?
외부 도구나 문서 검색이 필요한가?
조건에 따라 경로가 나뉘는가?
결과는 어떤 형태로 출력되는가?
실행 로그에서 무엇을 확인할 수 있는가?
```

## 강의용 화면 실습 순서

수업 진행에서는 아래 순서로 AIPP 화면을 보여주며 진행합니다.

```text
1. AIPP 접속
2. 로그인
3. 새 프로젝트 생성
4. 새 워크플로우 생성
5. 워크플로우 이름 입력
6. 입력값 필드 생성
7. LLM 또는 Agent 노드 추가
8. 문의 유형 분류 프롬프트 작성
9. 조건 분기 노드 추가
10. 긴급 문의와 일반 문의 경로 분리
11. Tool 또는 Knowledge 연결
12. 응답 생성 노드 추가
13. 결과 출력 노드 추가
14. 테스트 입력 실행
15. 실행 결과와 로그 확인
```

도구 화면의 실제 메뉴명은 버전이나 계정 권한에 따라 다를 수 있습니다. 수업에서는 메뉴명을 외우기보다 위 구조가 화면 어디에 해당하는지 찾는 연습을 합니다.

## 실습 시나리오

수업에서 사용할 기본 시나리오:

```text
사내 기술 지원 문의 자동화
```

입력 예시:

```text
사내 ERP 로그인이 되지 않습니다. 오전 업무 시작 전까지 해결이 필요합니다.
```

기대 처리:

```text
유형: 계정/로그인
긴급도: 높음
처리 경로: 운영팀 알림 + 답변 초안 생성
```

## 실행 준비

상위 폴더에서 가상환경을 활성화합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

02 단원의 Python 예제는 실제 AIPP API 없이 실행됩니다. 도구 화면 실습 전에 워크플로우 구조를 코드와 문서로 먼저 이해하기 위한 예제입니다.

## Python 예제 실행 순서

```powershell
cd C:\aidev\08_ai-workflow-automation\02_aipp-workflow
python.\01_ch1_aipp-overview\01_aipp_workflow_concept.py
python.\02_ch2_aipp-workflow-design\01_design_workflow_nodes.py
python.\03_ch3_aipp-agent-tool-data-flow\01_agent_tool_data_flow.py
```

## 실습 체크리스트

```text
[ ] 업무 시나리오를 한 문장으로 정의했다.
[ ] 입력값을 정했다.
[ ] AI가 판단할 항목을 정했다.
[ ] Tool 또는 Knowledge가 필요한지 판단했다.
[ ] 조건 분기 기준을 정했다.
[ ] 결과 출력 형태를 정했다.
[ ] 실패했을 때의 대체 흐름을 정했다.
[ ] 실행 로그에서 확인할 항목을 정했다.
```

## 과제 방향

과제에서는 직접 직접 하나의 업무 시나리오를 선택하고 AIPP 워크플로우 설계 문서를 작성합니다.

예시 주제:

```text
기술 지원 문의 분류
회의록 요약과 후속 작업 생성
고객 문의 긴급도 판단
사내 문서 검색 기반 답변 초안 작성
```

결과물에는 다음이 포함되어야 합니다.

- 업무 시나리오
- 입력 데이터 예시
- 노드 구성도
- AI 판단 기준
- 조건 분기 기준
- 출력 결과 예시
- 오류 처리와 로그 확인 계획

## 이후 단원과의 연결

```text
02 AIPP Workflow
-> 03 n8n AI Workflow
-> 04 Dify AI Workflow
-> 05 Workflow Ops and Quality
-> 99 Mini Project
```
