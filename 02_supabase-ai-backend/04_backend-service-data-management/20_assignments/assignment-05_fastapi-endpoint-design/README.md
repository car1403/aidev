# Assignment 05 - FastAPI Endpoint 설계

서비스 데이터 관리를 위한 FastAPI endpoint의 요청/응답 구조를 설계하는 과제입니다.

이 과제의 endpoint는 LLM을 직접 호출하는 단계가 아니라, 앞 단원의 Gemini SDK endpoint에서 생성한 응답을 저장하고 조회하기 위한 서비스 데이터 API입니다.

## 목표

- endpoint별 HTTP Method와 URL을 설계할 수 있습니다.
- Request Body와 Response Body를 JSON 형태로 작성할 수 있습니다.
- endpoint가 어떤 Supabase 테이블과 연결되는지 설명할 수 있습니다.

## 설계할 endpoint

```text
GET /profiles/{user_id}
POST /conversations
POST /conversations/{conversation_id}/messages
GET /conversations/{conversation_id}/messages
POST /service-logs
```

## 제출물

각 endpoint마다 아래 내용을 작성합니다.

```text
1. HTTP Method
2. URL
3. 목적
4. Request Body
5. Response Body
6. 오류 상황
7. 연결되는 Supabase 테이블
8. LLM 응답 저장과 연결될 경우 필요한 metadata
```

## 작성 예시

```text
Endpoint: POST /conversations
목적: 새 대화 묶음을 생성한다.
Request Body:
{
  "user_id": "student01",
  "title": "FastAPI 질문"
}
Response Body:
{
  "item": {
    "id": "...",
    "user_id": "student01",
    "title": "FastAPI 질문"
  }
}
연결 테이블: conversations
오류 상황: title이 비어 있으면 422, Supabase 저장 실패 시 500
```

## 확인 기준

- Method와 URL이 기능에 맞게 작성되었습니다.
- Request/Response JSON이 실제 구현 가능한 형태입니다.
- 오류 상황을 최소 1개 이상 포함했습니다.
- Supabase 테이블 연결이 명확합니다.
- 서비스 로그 endpoint에 `provider`, `model`, `actual_api_called`, `llm_call_mode` 같은 metadata가 포함됩니다.
