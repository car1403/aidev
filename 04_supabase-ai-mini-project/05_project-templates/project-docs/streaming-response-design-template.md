# Streaming Response Design Template

SSE 기반 실시간 응답 설계 문서 템플릿입니다.

SSE는 선택 확장입니다. 구현하지 않는 경우에도 설계 방향만 문서로 정리할 수 있습니다.

## 1. 적용 여부

```text
SSE 구현 여부:
구현 / 설계만 작성 / 미적용
```

## 2. 일반 응답과 스트리밍 응답 차이

```text
일반 응답:
서버가 전체 응답을 만든 뒤 한 번에 반환합니다.

스트리밍 응답:
서버가 응답 조각(chunk)을 생성할 때마다 화면에 전달합니다.
```

## 3. API 경로

```text
일반 응답 API:
POST /api/chat

스트리밍 응답 API:
POST /api/chat/stream
```

## 4. 화면 표시 방식

```text
Streamlit에서 httpx.stream()으로 응답을 읽습니다.
chunk를 받을 때마다 st.empty() 영역을 갱신합니다.
[DONE] 이벤트를 받으면 스트리밍을 종료합니다.
```

## 5. Supabase 저장 기준

```text
사용자 질문:
messages 테이블에 저장

AI 응답 chunk:
화면에만 표시

최종 assistant 응답:
messages 테이블에 저장

오류와 실행 정보:
service_logs 테이블에 저장
```

## 6. 오류 처리

| 상황 | 처리 |
| --- | --- |
| AI API 오류 | fallback 메시지 표시 |
| 네트워크 끊김 | 재시도 안내 |
| 빈 응답 | 사용자 안내 메시지 표시 |
| 저장 실패 | service_logs에 오류 기록 |
