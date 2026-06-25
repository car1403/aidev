# 03. Supabase Final Message Save

이 문서는 SSE 스트리밍이 끝난 뒤 최종 assistant 응답을 Supabase에 저장하는 흐름을 설명합니다.

## 저장 기준

처음 구현할 때는 아래 기준을 권장합니다.

```text
사용자 질문
-> messages 테이블에 저장

스트리밍 chunk
-> 화면에만 표시

assistant 최종 응답
-> messages 테이블에 저장

오류와 실행 정보
-> service_logs 테이블에 저장
```

## chunk를 모두 저장하지 않는 이유

AI 응답 하나가 50개의 chunk로 나뉘어 전송될 수 있습니다. 모든 chunk를 저장하면 하나의 답변을 위해 너무 많은 데이터가 생성됩니다.

초보자 과정에서는 아래 방식이 단순하고 관리하기 쉽습니다.

```text
화면 표시
-> chunk 누적

DB 저장
-> 완성된 최종 응답 1개
```

## 권장 테이블

```text
conversations
- id
- user_id
- title
- created_at

messages
- id
- conversation_id
- role
- content
- created_at

service_logs
- id
- user_id
- action
- status
- metadata
- created_at
```

## 저장 흐름

```text
1. 사용자가 질문을 입력합니다.
2. FastAPI가 사용자 메시지를 messages 테이블에 저장합니다.
3. FastAPI가 AI 응답을 SSE로 전송합니다.
4. Streamlit이 chunk를 화면에 누적 표시합니다.
5. 스트리밍이 완료됩니다.
6. FastAPI가 최종 assistant 메시지를 messages 테이블에 저장합니다.
7. FastAPI가 실행 시간, 성공 여부, 오류 정보를 service_logs 테이블에 저장합니다.
```

## 프로젝트 문서에 작성할 내용

팀 프로젝트의 `docs/streaming-response-design.md`에는 아래 내용을 정리합니다.

```text
스트리밍 API 경로:
일반 응답 API와의 차이:
화면에 표시할 chunk 형식:
최종 응답 저장 테이블:
오류 발생 시 fallback:
테스트 방법:
```
