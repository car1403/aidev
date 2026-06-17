# Chatbot Interface Notes

## 챗봇 UI의 기본 요소

- 사용자 입력 영역
- 사용자 메시지 출력 영역
- assistant 응답 출력 영역
- 대화 이력 저장 공간
- 응답 생성 또는 API 호출 함수
- 오류 메시지 표시 영역

## Streamlit 주요 기능

- `st.chat_message("user")`: 사용자 메시지 영역을 표시합니다.
- `st.chat_message("assistant")`: assistant 메시지 영역을 표시합니다.
- `st.chat_input()`: 채팅 입력창을 표시합니다.
- `st.session_state`: 화면이 다시 실행되어도 값을 유지합니다.
- `st.spinner()`: 응답을 기다리는 동안 로딩 상태를 보여줍니다.

## 수업 기준

이 단원에서는 AI 모델의 세부 동작보다 화면 흐름과 데이터 흐름에 집중합니다.

```text
질문 입력
-> 메시지 목록에 사용자 질문 저장
-> mock 응답 함수 호출
-> 메시지 목록에 assistant 응답 저장
-> 전체 메시지 목록 다시 출력
```



