# 03. Supabase Final Message Save

이 문서는 SSE 스트리밍이 끝난 뒤 최종 assistant 응답을 Supabase에 저장하는 흐름을 설명합니다.

## 저장 기준

초보자 과정에서는 아래 기준을 권장합니다.

```text
사용자 질문: Supabase messages 테이블에 저장
스트리밍 chunk: 화면에만 표시
assistant 최종 응답: Supabase messages 테이블에 저장
오류와 실행 정보: usage_logs 테이블에 저장
```

## 왜 chunk를 모두 저장하지 않나요?

AI 응답이 50개의 chunk로 나뉘어 오면, 모든 chunk를 저장할 경우 메시지 하나에 대해 데이터가 너무 많이 생깁니다.

처음 배우는 단계에서는 다음 방식이 더 단순합니다.

```text
화면 표시: chunk 누적
DB 저장: 완성된 최종 응답 1개
```

## 권장 테이블

```text
conversations
- id uuid primary key
- user_id uuid
- title text
- created_at timestamptz

messages
- id uuid primary key
- conversation_id uuid
- role text
- content text
- created_at timestamptz

usage_logs
- id uuid primary key
- user_id uuid
- action text
- metadata jsonb
- created_at timestamptz
```

## 저장 흐름

```text
1. 사용자가 질문을 입력한다.
2. backend가 사용자 메시지를 messages 테이블에 저장한다.
3. backend가 AI 응답을 SSE로 전송한다.
4. frontend가 chunk를 화면에 누적 표시한다.
5. 스트리밍이 완료된다.
6. backend 또는 frontend가 최종 assistant 메시지를 messages 테이블에 저장한다.
7. usage_logs에 실행 시간, 성공 여부, 오류 정보를 저장한다.
```

## 프로젝트 문서에 작성할 내용

팀 프로젝트의 `docs/streaming-response-design.md`에 아래 내용을 작성합니다.

```text
스트리밍 API 경로:
일반 응답 API와의 차이:
화면에 표시할 chunk 형식:
최종 응답 저장 테이블:
오류 발생 시 fallback:
테스트 방법:
```
