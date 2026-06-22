# 03_ch3_ai-api-workflow-integration

n8n에서 AI API 또는 자체 백엔드 API를 호출하는 구조를 학습하는 챕터입니다.

## 핵심 개념

n8n이 직접 모든 AI 로직을 처리하지 않아도 됩니다.

운영 관점에서는 n8n이 워크플로우를 담당하고, AI 처리는 별도 API가 담당하는 구조가 깔끔합니다.

```text
n8n Webhook
-> HTTP Request
-> FastAPI AI Backend
-> AI 분류/생성 결과
-> n8n 후속 Action
```

## HTTP Request 노드 설계

```text
Method: POST
URL: http://host.docker.internal:8000/analyze
Body:
 ticket_id
 title
 message
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python.\03_ch3_ai-api-workflow-integration\01_ai_api_workflow_simulation.py
```
