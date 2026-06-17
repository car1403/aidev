# n8n Workflow Plan

## 목표

n8n으로 문의 접수부터 API 호출, 알림까지 연결합니다.

## 권장 노드

```text
Webhook Trigger
-> Set
-> HTTP Request: FastAPI /analyze 호출
-> IF: next_action이 send_ops_alert인가?
-> Slack/Email Action
-> Respond to Webhook
```

## HTTP Request

```text
Method: POST
URL: http://host.docker.internal:8900/analyze
Body: customer_name, customer_tier, title, message
```

## 응답 활용

```text
category
urgency
draft_answer
validation_status
next_action
```
