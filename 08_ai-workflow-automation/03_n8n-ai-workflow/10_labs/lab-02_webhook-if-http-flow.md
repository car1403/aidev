# Lab 02. Webhook, IF, HTTP Request 흐름 설계

## 목표

n8n에서 고객 문의 자동화 흐름을 설계합니다.

## 목표 흐름

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
```

## 할 일

1. Webhook으로 받을 JSON 데이터를 정의합니다.
2. Set 노드에서 사용할 필드를 정리합니다.
3. IF 노드의 긴급 조건을 작성합니다.
4. HTTP Request 노드가 호출할 API URL을 정합니다.
5. Webhook 응답 JSON을 설계합니다.

## 예시 입력

```json
{
  "ticket_id": "N8N-3001",
  "title": "AI 서비스 응답 지연",
  "message": "프리미엄 고객인데 AI 응답이 너무 느립니다.",
  "customer_tier": "premium"
}
```

## 결과물

```text
Webhook URL:
Input JSON:
IF 조건:
HTTP Request URL:
Response JSON:
```
