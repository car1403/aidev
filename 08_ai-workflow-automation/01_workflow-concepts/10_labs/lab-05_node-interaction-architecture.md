# Lab 05. Node Interaction Architecture

## 목표

워크플로우 노드 간 입력/출력 계약과 상호작용 구조를 설계합니다.

## 실습

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\05_ch5_node-interaction-architecture\01_node_interaction_map.py
```

## 작성할 내용

```text
노드 이름:
필수 입력:
출력:
다음 노드:
실패 시 fallback:
```

## 확인 질문

- 다음 노드가 필요한 입력을 이전 노드가 제공하는가?
- 병렬 실행 후 결과를 어디에서 합칠 것인가?
- 실패한 노드의 오류를 어디에 기록할 것인가?
