# 05_sse-streaming-ai-response

이 단원은 Server-Sent Events(SSE)를 사용해 AI 응답을 실시간으로 화면에 표시하는 통합 실습입니다.

01 과정에서 배운 FastAPI, 02 과정에서 배운 Streamlit, 03 과정에서 사용하는 Supabase 저장 흐름을 하나로 연결합니다.

## 학습 목표

- SSE가 무엇인지 설명할 수 있다.
- FastAPI에서 `StreamingResponse`로 `text/event-stream` 응답을 만들 수 있다.
- Streamlit에서 스트리밍 응답을 받아 화면에 누적 표시할 수 있다.
- 스트리밍 완료 후 최종 assistant 응답만 Supabase `messages` 테이블에 저장하는 흐름을 설계할 수 있다.
- 스트리밍 실패 시 fallback 메시지와 로그 저장 흐름을 설계할 수 있다.

## SSE가 필요한 이유

일반 API 응답은 서버가 모든 결과를 만든 뒤 한 번에 반환합니다.

```text
사용자 질문
-> 서버가 전체 AI 응답 생성
-> 응답 전체를 한 번에 화면에 표시
```

SSE는 응답이 만들어지는 중간 과정도 조금씩 화면에 보낼 수 있습니다.

```text
사용자 질문
-> 서버가 응답 조각(chunk)을 하나씩 생성
-> 화면이 chunk를 받을 때마다 문장을 누적 표시
-> 완료 후 최종 응답 저장
```

AI 챗봇에서는 사용자가 기다리는 느낌을 줄일 수 있기 때문에 SSE가 자주 사용됩니다.

## 전체 구조

```text
Streamlit
-> POST /api/chat/stream
-> FastAPI StreamingResponse
-> text/event-stream
-> Streamlit 화면에 chunk 누적 표시
-> 스트리밍 완료
-> POST /api/messages 또는 backend 내부 로직으로 Supabase 저장
```

## Supabase와 SSE 역할 구분

```text
SSE:
AI 응답을 실시간으로 화면에 보내는 통신 방식

Supabase:
사용자, 대화방, 최종 메시지, 사용 로그를 저장하는 데이터 저장소
```

초보자 과정에서는 모든 chunk를 Supabase에 저장하지 않습니다. chunk를 모두 저장하면 테이블 설계와 로그 관리가 복잡해집니다.

권장 방식:

```text
사용자 질문: messages 테이블에 저장
assistant 최종 응답: messages 테이블에 저장
스트리밍 chunk: 화면에만 표시
오류/실패 기록: usage_logs 테이블에 저장
```

## 실습 문서 순서

```text
01_backend-sse-api.md
-> 02_frontend-streaming-ui.md
-> 03_supabase-final-message-save.md
```

## 권장 API 구조

```text
POST /api/chat
일반 AI 응답을 한 번에 반환하는 API

POST /api/chat/stream
SSE 기반 스트리밍 응답 API

POST /api/conversations/{conversation_id}/messages
최종 메시지 저장 API
```

## 팀 프로젝트 적용 기준

팀 프로젝트에서 SSE를 적용한다면 아래 항목을 문서화합니다.

```text
[ ] 일반 응답 API와 스트리밍 응답 API의 차이를 설명한다.
[ ] 스트리밍 중 화면에 표시할 내용을 정의한다.
[ ] 스트리밍 완료 후 Supabase에 저장할 최종 메시지 구조를 정의한다.
[ ] 스트리밍 실패 시 fallback 메시지를 정의한다.
[ ] 테스트 체크리스트에 정상/오류/중단 상황을 포함한다.
```
