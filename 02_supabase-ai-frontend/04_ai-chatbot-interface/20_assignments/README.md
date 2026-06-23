# 20_assignments

`04_ai-chatbot-interface` 과제 안내입니다.

과제의 핵심은 챗봇 UI의 기본 흐름을 직접 구성하는 것입니다. 실제 로그인, Supabase 저장, 사용자별 대화 관리까지 한 번에 만들지 않습니다.

## 제출 과제

```text
assignment-01-basic-chatbot-ui.md
assignment-02-chat-history-app.md
assignment-03-ai-service-client.md
```

## 제출 기준

- `st.chat_message`와 `st.chat_input`을 사용합니다.
- 사용자 메시지와 assistant 메시지를 구분합니다.
- mock 응답 함수를 별도로 분리합니다.
- 대화 이력은 화면에서 확인 가능한 간단한 목록으로 구성합니다.
- 백엔드 API를 사용하는 경우 `/api/chat/mock` 호출과 연결 실패 처리를 포함합니다.
- Gemini SDK를 사용하는 경우 선택 기능으로 분리하고, API key가 없을 때 mock 응답으로 대체합니다.
- 주요 코드 줄에 본인이 이해한 한글 주석을 작성합니다.
