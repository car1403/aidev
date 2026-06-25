# 01. Backend SSE API

이 문서는 FastAPI에서 SSE 스트리밍 엔드포인트를 설계하는 방법을 설명합니다.

## 핵심 개념

FastAPI에서 SSE 응답을 만들 때는 `StreamingResponse`를 사용합니다.

```text
StreamingResponse
-> 응답 데이터를 한 번에 모두 만들지 않고 여러 조각으로 나누어 계속 보내는 응답 방식

media_type="text/event-stream"
-> 브라우저나 클라이언트에게 이 응답이 SSE 형식이라는 것을 알려주는 값
```

## SSE 기본 형식

SSE는 보통 아래와 같은 형식으로 데이터를 보냅니다.

```text
data: 첫 번째 응답 조각

data: 두 번째 응답 조각

data: [DONE]
```

각 이벤트 사이에는 빈 줄이 들어갑니다.

## 권장 API

```text
POST /api/chat
-> 일반 AI 응답을 한 번에 반환하는 API

POST /api/chat/stream
-> AI 응답을 chunk 단위로 반환하는 SSE API
```

## 설계 흐름

```text
1. 사용자 질문을 받습니다.
2. 사용자 질문을 messages 테이블에 저장합니다.
3. AI 응답을 chunk 단위로 생성합니다.
4. 각 chunk를 SSE 형식으로 전송합니다.
5. 전체 응답이 끝나면 [DONE] 이벤트를 보냅니다.
6. 최종 assistant 응답을 messages 테이블에 저장합니다.
7. 실행 성공/실패를 service_logs 테이블에 저장합니다.
```

## 주의할 점

- Swagger UI에서는 SSE 흐름을 보기 어렵습니다.
- PowerShell, curl, Streamlit 같은 클라이언트로 테스트하는 것이 좋습니다.
- chunk마다 Supabase에 저장하지 않고, 최종 응답만 저장하는 방식을 먼저 사용합니다.
- 오류가 발생하면 화면에 표시할 fallback 메시지를 준비합니다.

## 체크리스트

- [ ] `/api/chat`과 `/api/chat/stream`의 역할을 구분했다.
- [ ] `StreamingResponse`와 `text/event-stream`을 사용한다.
- [ ] `[DONE]` 이벤트를 보내는 기준을 정했다.
- [ ] 최종 assistant 응답 저장 위치를 정했다.
- [ ] 오류 발생 시 service log에 남길 값을 정했다.
