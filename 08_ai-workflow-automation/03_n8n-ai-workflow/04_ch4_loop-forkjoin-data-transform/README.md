# 04_ch4_loop-forkjoin-data-transform

n8n과 같은 워크플로우 도구에서 반복 처리, 병렬 처리, 데이터 변환 노드가 어떻게 동작하는지 학습하는 챕터입니다.

## 학습 목표

- Loop 노드가 반복 작업을 처리하는 방식을 이해합니다.
- Fork-Join 구조로 여러 작업을 병렬 처리하고 결과를 합치는 방식을 이해합니다.
- 데이터 파싱, 변환, 집계 노드의 역할을 설명할 수 있습니다.
- 반복과 병렬 처리에서 오류가 발생했을 때 fallback을 설계할 수 있습니다.

## 기본 구조

```text
Webhook Trigger
-> Parse Data
-> Loop Items
-> Fork
 -> RAG Search
 -> AI Summary
 -> Ticket Classify
-> Join
-> Aggregate Result
-> Respond
```

## 노코드 도구에서의 대응

| 개념 | n8n/AIPP/Dify 관점 |
| --- | --- |
| Loop | 여러 항목을 하나씩 반복 처리 |
| Fork | 여러 경로를 동시에 실행 |
| Join | 여러 결과를 하나로 합침 |
| Parse | 입력 JSON이나 텍스트를 필드로 분리 |
| Transform | 필드명, 값, 형식을 바꿈 |
| Aggregate | 여러 결과를 요약하거나 집계 |

## 실행 예제

```powershell
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python.\04_ch4_loop-forkjoin-data-transform\01_loop_forkjoin_transform.py
```
