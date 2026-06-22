# 03_ch3_trigger-condition-action

Trigger, Condition, Action 기반의 자동화 흐름을 학습하는 챕터입니다.

## 핵심 개념

```text
Trigger: 워크플로우를 시작하는 사건
Condition: 어떤 경로로 갈지 결정하는 조건
Action: 실제로 수행되는 작업
```

## 예시

```text
Trigger: 새 고객 문의 접수
Condition: 긴급도가 high인가?
Action:
 - high이면 운영팀 알림
 - 아니면 일반 응답 생성
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python.\03_ch3_trigger-condition-action\01_trigger_condition_action.py
```

## 학습 포인트

- Trigger는 자동화의 시작점이다.
- Condition은 분기 기준이다.
- Action은 워크플로우가 실제로 수행하는 일이다.
- n8n, AIPP, Dify의 노드 기반 흐름도 결국 이 구조를 확장한 것이다.
