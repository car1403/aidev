# Streaming Response Design

이 문서는 팀 프로젝트에서 SSE 기반 실시간 AI 응답 스트리밍을 적용할 때 작성하는 설계 문서입니다.

SSE는 필수 구현 항목이 아니라 선택 확장 기능입니다. 다만 AI 챗봇이나 피드백 서비스처럼 응답 생성 시간이 길어질 수 있는 프로젝트라면 적용을 권장합니다.

## 1. 적용 여부

```text
[ ] SSE 스트리밍을 적용한다.
[ ] 이번 프로젝트에서는 일반 응답 API만 사용한다.
```

적용하거나 적용하지 않는 이유:

```text

```

## 2. API 설계

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/api/chat` | 일반 AI 응답을 한 번에 반환 |
| POST | `/api/chat/stream` | SSE 기반 스트리밍 응답 반환 |
| POST | `/api/conversations/{conversation_id}/messages` | 최종 메시지 저장 |

프로젝트에서 사용할 실제 경로:

```text
일반 응답 API:
스트리밍 응답 API:
최종 메시지 저장 API:
```

## 3. SSE 이벤트 형식

권장 이벤트 형식:

```json
{"type": "chunk", "content": "응답 일부"}
{"type": "done", "content": "최종 응답 전체"}
{"type": "error", "content": "오류 메시지"}
```

## 4. 화면 표시 방식

```text
사용자 질문 입력
-> 스트리밍 API 호출
-> chunk가 올 때마다 화면에 누적 표시
-> done 이벤트 수신
-> 최종 응답 표시
-> 최종 응답 저장
```

## 5. Supabase 저장 기준

```text
사용자 질문 저장 테이블:
assistant 최종 응답 저장 테이블:
사용 로그 저장 테이블:
chunk 저장 여부:
```

초보자 프로젝트에서는 아래 방식을 권장합니다.

```text
chunk는 화면에만 표시한다.
최종 assistant 응답만 messages 테이블에 저장한다.
오류는 usage_logs 테이블에 저장한다.
```

## 6. 오류와 fallback

```text
스트리밍 API 호출 실패:
중간에 연결이 끊긴 경우:
AI 응답 생성 실패:
Supabase 저장 실패:
사용자에게 보여줄 fallback 메시지:
```

## 7. 테스트 항목

```text
[ ] 정상 질문에서 chunk가 순서대로 표시된다.
[ ] done 이벤트를 받으면 최종 응답이 완성된다.
[ ] 빈 질문은 요청하지 않는다.
[ ] 서버가 꺼져 있으면 오류 메시지를 표시한다.
[ ] 최종 응답 저장 흐름을 문서화했다.
```
