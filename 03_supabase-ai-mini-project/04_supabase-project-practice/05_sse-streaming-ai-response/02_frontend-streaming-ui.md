# 02. Frontend Streaming UI

이 문서는 Streamlit에서 SSE 응답을 받아 화면에 실시간으로 표시하는 방법을 설명합니다.

## 핵심 개념

Streamlit은 React의 `EventSource`처럼 브라우저에서 직접 SSE를 받는 구조보다, Python 코드에서 `httpx.stream()`으로 응답을 읽고 화면을 갱신하는 방식이 초보자에게 이해하기 쉽습니다.

```text
httpx.stream():
응답 본문을 한 번에 받지 않고 줄 단위 또는 조각 단위로 읽는 방식

st.empty():
화면에서 나중에 내용을 계속 바꿔 넣을 수 있는 빈 자리
```

## 화면 흐름

```text
사용자 질문 입력
-> "스트리밍 응답 받기" 버튼 클릭
-> FastAPI /api/chat/stream 호출
-> chunk를 받을 때마다 answer_text에 누적
-> st.empty() 영역을 계속 갱신
-> [DONE] 수신 후 최종 응답 표시
```

## Streamlit 예시

팀 템플릿에는 아래 예제 파일이 포함되어 있습니다.

```text
99_team-projects/supabase-team-template/frontend/streaming_app.py
```

실행 예시:

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run streaming_app.py --server.port 8502
```

## 확인 요약

```text
[ ] 응답이 한 번에 표시되지 않고 조금씩 누적되는가?
[ ] [DONE] 이벤트를 받으면 스트리밍이 끝나는가?
[ ] 서버 오류가 나면 화면에 오류 메시지가 표시되는가?
[ ] 최종 응답을 Supabase에 저장할 위치를 문서화했는가?
```
