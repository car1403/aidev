# 05_ch5_node-interaction-architecture

워크플로우 노드 간 데이터 흐름과 상호작용 구조를 학습하는 챕터입니다.

노코드 워크플로우에서는 각 노드가 독립적으로 보이지만, 실제로는 이전 노드의 출력이 다음 노드의 입력으로 연결됩니다. 이 연결 구조를 이해해야 복잡한 워크플로우를 안정적으로 설계할 수 있습니다.

## 학습 목표

- 노드 간 입력과 출력 계약을 정의할 수 있습니다.
- 노드 실행 순서와 의존 관계를 설명할 수 있습니다.
- 실패한 노드가 뒤쪽 노드에 어떤 영향을 주는지 이해합니다.
- 병렬 실행과 결과 통합 구조의 기본 개념을 이해합니다.

## 기본 구조

```text
Trigger Node
-> Data Prepare Node
-> Branch Node
-> AI Node
-> Tool Node
-> Merge Node
-> Output Node
```

## 노드 상호작용에서 확인할 것

```text
각 노드의 입력 필드
각 노드의 출력 필드
다음 노드가 필요로 하는 데이터
실패 시 fallback 경로
병렬 실행 후 결과 병합 방식
```

## 실행 예제

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python.\05_ch5_node-interaction-architecture\01_node_interaction_map.py
```
