# Lab 01. AI 워크플로우 단계 분해

## 목표

업무 자동화 시나리오를 AI 워크플로우 단계로 나누어 봅니다.

## 준비

아래 예제를 먼저 실행합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\01_ch1_ai-workflow-big-picture\01_ai_workflow_map.py
```

## 실습 시나리오

```text
고객이 기술 지원 문의를 남기면,
문의 유형과 긴급도를 분류하고,
관련 도움말 문서를 찾아서,
답변 초안을 생성하고,
담당자에게 전달한다.
```

## 할 일

1. Trigger를 정의합니다.
2. 입력 데이터에 필요한 항목을 적습니다.
3. LLM이 필요한 단계를 표시합니다.
4. Tool이 필요한 단계를 표시합니다.
5. 최종 Output을 정의합니다.
6. 실행 로그에 남겨야 할 정보를 적습니다.

## 결과물

아래 형식으로 정리합니다.

```text
Trigger:
Input:
Condition:
LLM:
Tool:
Action:
Output:
Log:
```
