# Lab 03. n8n과 AI API 연동 설계

## 목표

n8n에서 AI API를 호출하는 구조를 설계합니다.

## 준비

아래 예제를 실행해 데이터 흐름을 먼저 확인합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python .\03_ch3_ai-api-workflow-integration\01_ai_api_workflow_simulation.py
```

## 할 일

1. n8n이 AI API에 보낼 요청 Body를 설계합니다.
2. AI API가 반환할 응답 JSON을 설계합니다.
3. 응답의 `urgency` 값에 따른 후속 Action을 정합니다.
4. 오류가 발생했을 때 대체 흐름을 정합니다.

## 결과물

```text
AI API URL:
Request Body:
Response Body:
성공 Action:
실패 Action:
로그 항목:
```
