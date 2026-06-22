# 02_ch2_aipp-workflow-design

업무 시나리오를 AIPP식 노드 기반 워크플로우로 설계하는 챕터입니다.

## 핵심 개념

워크플로우 설계는 화면에서 노드를 먼저 그리는 일이 아닙니다.

먼저 업무를 단계로 나누고, 각 단계의 입력과 출력을 정의해야 합니다.

```text
업무 목표
-> 필요한 입력
-> 처리 단계
-> 조건 분기
-> 최종 결과
-> 운영 로그
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\02_aipp-workflow
python.\02_ch2_aipp-workflow-design\01_design_workflow_nodes.py
```

## 학습 포인트

- 노드는 역할이 하나만 명확해야 한다.
- LLM 노드에는 판단/요약/생성을 맡긴다.
- Tool 노드에는 실제 조회/전송/저장을 맡긴다.
- Condition 노드는 다음 실행 경로를 결정한다.
