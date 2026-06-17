# Lab 03. Trigger, Condition, Action 설계

## 목표

업무 자동화를 Trigger, Condition, Action 구조로 설계합니다.

## 준비

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\03_ch3_trigger-condition-action\01_trigger_condition_action.py
```

## 실습 시나리오

```text
새로운 고객 문의가 접수되면,
프리미엄 고객이거나 장애 키워드가 포함된 경우 운영팀에 즉시 알림을 보낸다.
그 외 문의는 일반 응답을 생성한다.
```

## 할 일

1. Trigger 이벤트에 필요한 데이터를 정리합니다.
2. Condition 조건을 2개 이상 작성합니다.
3. 긴급 Action과 일반 Action을 나눕니다.
4. 로그에 남길 정보를 정합니다.

## 결과물

```text
Trigger:
Condition 1:
Condition 2:
Action - 긴급:
Action - 일반:
Log:
```

## 추가 실습

`customer_tier`를 `basic`으로 바꾸고, `message`에서 긴급 키워드를 제거한 뒤 실행 결과를 비교합니다.
