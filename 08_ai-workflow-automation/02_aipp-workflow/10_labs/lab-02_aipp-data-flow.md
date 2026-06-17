# Lab 02. AIPP 데이터 흐름 설계

## 목표

노드 사이에서 어떤 데이터가 전달되는지 설계합니다.

## 준비

```powershell
cd C:\aidev\08_ai-workflow-automation\02_aipp-workflow
python .\02_ch2_aipp-workflow-design\01_design_workflow_nodes.py
```

## 할 일

각 노드에 대해 입력 데이터와 출력 데이터를 정리합니다.

## 결과물

```text
Node Name:
Node Type:
Input:
Output:
다음 노드:
로그에 남길 값:
```

## 체크 포인트

- LLM 노드가 실제 DB 조회를 직접 담당하지 않도록 설계했는가?
- Tool 노드의 결과가 다음 LLM 노드에 전달되는가?
- 검증 결과가 Action 분기에 사용되는가?
