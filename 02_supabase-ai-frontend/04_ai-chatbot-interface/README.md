# 04_ai-chatbot-interface

Streamlit으로 AI 챗봇 화면을 구성하는 단원입니다.

이 단원에서는 실제 LLM API를 호출하지 않습니다. 대신 사용자가 질문을 입력하고, 임시 응답 또는 샘플 백엔드 응답을 확인하며, 대화 흐름을 이어가는 프론트엔드 구조를 학습합니다.

## 학습 목표

- Streamlit의 chat UI 컴포넌트를 사용할 수 있다.
- 사용자 메시지와 assistant 응답을 구분해 출력할 수 있다.
- 프롬프트 입력값을 검증하고 응답 화면을 만들 수 있다.
- `st.session_state`로 대화 이력을 유지할 수 있다.
- mock chat service 호출 함수를 화면 코드와 분리할 수 있다.
- 백엔드 mock chat API를 호출하는 인터페이스 구조를 이해한다.
- AI 응답 생성 중 `st.spinner`, `st.status`, `st.empty` 같은 표시 도구로 사용자에게 진행 상태를 안내할 수 있다.

## 학습 순서

```text
01_ch1_chat-ui-basic
-> 02_ch2_prompt-input-and-response
-> 03_ch3_conversation-history
-> 04_ch4_mock-chat-service-interface
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
04_ai-chatbot-interface
├─ README.md
├─ 00_references
├─ 01_ch1_chat-ui-basic
├─ 02_ch2_prompt-input-and-response
├─ 03_ch3_conversation-history
├─ 04_ch4_mock-chat-service-interface
├─ 10_labs
└─ 20_assignments
```

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
streamlit run.\04_ai-chatbot-interface\01_ch1_chat-ui-basic\01_chat-message-basic.py
```

## 실행 확인 기준

- 사용자와 assistant 메시지가 서로 다른 역할로 표시된다.
- 입력창에 질문을 넣으면 응답이 화면에 표시된다.
- 새 메시지를 입력해도 이전 대화가 유지된다.
- mock 응답 함수가 화면 코드와 분리되어 있다.
- 백엔드 호출 실패 시 사용자에게 안내 메시지가 표시된다.

## 다음 단원 연결

`05_state-session-and-data`에서는 로그인 상태, 토큰, 사용자별 대화 이력, 캐시를 다룹니다. 인증이 필요한 API 연동은 그 단원에서 더 깊게 연결합니다.

SSE 기반 실시간 응답 스트리밍은 백엔드 SSE 엔드포인트, Streamlit 표시, Supabase 최종 메시지 저장이 함께 필요하므로 `03_supabase-ai-mini-project`에서 통합 실습으로 다룹니다.



