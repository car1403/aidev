# 05_sse-streaming-ai-response

이 단계에서는 Server-Sent Events(SSE)를 사용해 AI 응답 생성 과정을 Streamlit 화면에 실시간으로 표시하는 흐름을 정리합니다.

SSE는 필수 구현 항목은 아닙니다. 먼저 일반 API 응답으로 프로젝트를 완성한 뒤, 시간이 남거나 팀 프로젝트의 완성도를 높이고 싶을 때 선택 확장으로 적용합니다.

## SSE가 필요한 이유

일반 API는 서버가 응답 전체를 만든 뒤 한 번에 반환합니다.

```text
사용자 질문
-> 서버가 AI 응답 전체 생성
-> 전체 응답을 한 번에 화면에 표시
```

SSE는 응답이 만들어지는 중간 과정을 작은 조각으로 계속 전달합니다.

```text
사용자 질문
-> 서버가 응답 조각(chunk)을 생성
-> 화면에 chunk를 누적 표시
-> 생성 완료 후 최종 메시지 저장
```

AI 챗봇에서는 사용자가 기다리는 시간을 줄이고, 응답이 생성되고 있다는 느낌을 주기 위해 SSE를 자주 사용합니다.

## 전체 구조

```text
Streamlit
-> FastAPI /api/chat/stream 호출
-> FastAPI StreamingResponse 반환
-> text/event-stream 형식으로 chunk 전송
-> Streamlit 화면에 chunk 누적 표시
-> 완료 후 최종 assistant 메시지를 Supabase에 저장
```

## Supabase와 SSE 역할 구분

```text
SSE
-> AI 응답을 실시간으로 화면에 보내는 통신 방식

Supabase
-> 사용자 질문, 최종 AI 응답, 서비스 로그, 피드백을 저장하는 데이터 저장소
```

처음 배우는 단계에서는 모든 chunk를 Supabase에 저장하지 않습니다. chunk를 모두 저장하면 데이터가 너무 많아지고, 테이블 구조와 로그 관리가 복잡해집니다.

권장 방식:

```text
사용자 질문
-> messages 테이블에 저장

AI 응답 chunk
-> Streamlit 화면에만 표시

최종 assistant 응답
-> messages 테이블에 저장

오류와 실행 정보
-> service_logs 테이블에 저장
```

## 실습 문서 순서

- [01_backend-sse-api.md](./01_backend-sse-api.md)
- [02_frontend-streaming-ui.md](./02_frontend-streaming-ui.md)
- [03_supabase-final-message-save.md](./03_supabase-final-message-save.md)

## 체크리스트

- [ ] 일반 응답 API와 스트리밍 응답 API의 차이를 설명할 수 있다.
- [ ] FastAPI에서 `StreamingResponse`를 사용하는 이유를 설명할 수 있다.
- [ ] Streamlit 화면에서 chunk가 누적 표시되는 흐름을 설명할 수 있다.
- [ ] Supabase에는 최종 assistant 메시지만 저장하는 이유를 설명할 수 있다.
- [ ] 오류 발생 시 fallback 메시지와 로그 저장 흐름을 정리했다.
