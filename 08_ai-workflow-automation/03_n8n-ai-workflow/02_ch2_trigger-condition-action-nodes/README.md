# 02_ch2_trigger-condition-action-nodes

n8n에서 Trigger, Condition, Action 노드 기반 흐름을 설계하는 챕터입니다.

## 핵심 개념

```text
Trigger: 워크플로우 시작
Set: 필요한 데이터 정리
IF/Switch: 조건 분기
HTTP Request: 외부 API 호출
Action: 알림, 저장, 응답
```

## 예시 흐름

```text
Webhook Trigger
-> Set
-> IF urgent?
-> urgent이면 운영팀 알림
-> 아니면 일반 응답 생성
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python.\02_ch2_trigger-condition-action-nodes\01_n8n_branching_workflow.py
```
