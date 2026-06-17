# 06. API And Webhook Basic

## API란?

API는 프로그램끼리 데이터를 주고받는 약속입니다.

예시:

```text
n8n -> FastAPI backend
frontend -> Dify API
workflow tool -> external service
```

## HTTP Method

```text
GET: 데이터 조회
POST: 데이터 생성 또는 실행 요청
PUT/PATCH: 데이터 수정
DELETE: 데이터 삭제
```

## JSON

워크플로우 도구들은 보통 JSON으로 데이터를 주고받습니다.

```json
{
  "ticket_id": "TS-1001",
  "title": "AI 서비스 응답 지연",
  "message": "응답이 느립니다.",
  "customer_tier": "premium"
}
```

## Webhook

Webhook은 외부에서 특정 URL을 호출하면 워크플로우가 시작되는 구조입니다.

```text
외부 서비스
-> Webhook URL 호출
-> n8n Workflow 시작
-> AI API 호출
-> 결과 반환
```

## n8n에서 자주 쓰는 구조

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
```

## FastAPI와 연결 예시

```text
POST http://127.0.0.1:8900/analyze
```

요청 Body:

```json
{
  "customer_name": "Jean",
  "customer_tier": "premium",
  "title": "AI 서비스 응답 지연",
  "message": "응답이 느리고 장애가 의심됩니다."
}
```

응답:

```json
{
  "category": "technical_issue",
  "urgency": "high",
  "next_action": "send_ops_alert"
}
```
