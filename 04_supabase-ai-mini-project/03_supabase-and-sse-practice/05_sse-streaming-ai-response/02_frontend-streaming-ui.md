# 02. Frontend Streaming UI

이 문서는 Streamlit에서 SSE 응답을 받아 화면에 실시간으로 표시하는 방법을 설명합니다.

## 핵심 개념

Streamlit은 일반 웹 프론트엔드의 `EventSource` 방식보다 Python 코드에서 `httpx.stream()`으로 응답을 읽고 화면을 갱신하는 방식이 초보자에게 이해하기 쉽습니다.

```text
httpx.stream()
-> 응답 본문을 한 번에 받지 않고 줄 단위 또는 조각 단위로 읽는 방식

st.empty()
-> 화면에서 나중에 내용이 계속 바뀔 수 있는 빈 영역
```

## 화면 흐름

```text
사용자 질문 입력
-> "스트리밍 응답 받기" 버튼 클릭
-> Streamlit이 FastAPI /api/chat/stream 호출
-> chunk를 받을 때마다 answer_text에 누적
-> st.empty() 영역을 계속 갱신
-> [DONE]을 받으면 스트리밍 종료
```

## 화면에 보여줄 상태

```text
응답 생성 중
-> 사용자가 기다리는 동안 표시

응답 일부 표시
-> chunk가 도착할 때마다 누적 표시

완료
-> 최종 응답 표시

오류
-> 서버 연결 실패 또는 AI API 오류 안내
```

## Supabase 저장 위치

Streamlit 화면은 chunk를 표시하는 역할에 집중합니다.

최종 응답 저장은 가능하면 FastAPI에서 처리합니다. 그래야 service role key를 Streamlit 화면 코드에 넣지 않아도 됩니다.

## 체크리스트

- [ ] chunk가 도착할 때마다 화면이 갱신된다.
- [ ] `[DONE]` 이벤트를 받으면 스트리밍이 종료된다.
- [ ] 서버가 꺼져 있을 때 오류 메시지를 표시한다.
- [ ] 최종 응답 저장 위치가 문서화되어 있다.
