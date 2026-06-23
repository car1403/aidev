# 04_ai-chatbot-interface

Streamlit으로 AI 챗봇 화면을 구성하는 단원입니다.

이 단원에서는 챗봇 화면의 기본 구조를 먼저 만듭니다. 기본 실습은 비용이 들지 않는 mock 응답으로 진행하고, 선택 실습으로 `01_supabase-ai-backend`에서 배운 Gemini SDK 응답을 Streamlit 화면에 한 번 표시해 봅니다.

중요한 기준은 다음과 같습니다.

```text
04_ai-chatbot-interface
-> mock 챗봇 UI 중심
-> Gemini SDK 단발 응답 표시 선택 실습
-> 대화 이력은 맛보기 수준

05_state-session-and-data
-> session_state 본격 학습
-> 로그인 상태
-> 사용자별 대화 이력
-> 서비스 로그와 데이터 관리
```

즉, 이 단원은 “챗봇 화면을 어떻게 만들고 응답을 어떻게 보여 줄 것인가”에 집중합니다. 대화 저장, 사용자별 이력 조회, Supabase 저장, SSE 스트리밍은 뒤 과정에서 더 깊게 다룹니다.

## 학습 목표

- Streamlit의 chat UI 컴포넌트를 사용할 수 있습니다.
- 사용자 메시지와 assistant 응답을 구분해 출력할 수 있습니다.
- 프롬프트 입력값을 검증하고 mock 응답 화면을 만들 수 있습니다.
- 응답 생성 함수를 화면 코드와 분리할 수 있습니다.
- 백엔드 mock chat API 응답을 챗봇 메시지로 표시할 수 있습니다.
- 선택 실습으로 Gemini SDK 응답을 Streamlit 화면에 표시할 수 있습니다.
- API key가 없을 때 mock 응답으로 안전하게 대체하는 흐름을 이해합니다.

## 학습 순서

```text
01_chat-ui-basic
-> 02_prompt-input-and-response
-> 03_conversation-history-preview
-> 04_mock-and-optional-gemini-interface
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
04_ai-chatbot-interface
├─ README.md
├─ 00_references
├─ 01_chat-ui-basic
├─ 02_prompt-input-and-response
├─ 03_conversation-history-preview
├─ 04_mock-and-optional-gemini-interface
├─ 10_labs
└─ 20_assignments
```

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\04_ai-chatbot-interface\01_chat-ui-basic\01_chat-message-basic.py
```

## 선택 실습: Gemini SDK 응답 표시

Gemini SDK 선택 실습은 API key가 있을 때만 실제 호출합니다. key가 없거나 placeholder 값이면 실제 API를 호출하지 않고 mock 응답으로 진행합니다.

`.env` 예시:

```text
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행 예시:

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\04_ai-chatbot-interface\04_mock-and-optional-gemini-interface\05_optional-gemini-sdk-response.py
```

## 실행 확인 기준

- 사용자와 assistant 메시지가 서로 다른 역할로 표시됩니다.
- 입력창에 질문을 넣으면 mock 응답이 화면에 표시됩니다.
- 응답 생성 함수가 화면 코드와 분리되어 있습니다.
- Gemini API key가 없으면 mock 응답으로 안전하게 진행됩니다.
- Gemini API key가 있으면 `gemini-2.5-flash-lite` 응답을 화면에 표시할 수 있습니다.

## 다음 단원 연결

`05_state-session-and-data`에서는 로그인 상태, 토큰, 사용자별 대화 이력, 캐시, 서비스 로그를 본격적으로 다룹니다. 인증이 필요한 API 연동과 사용자별 데이터 관리는 그 단원에서 더 깊게 연결합니다.

SSE 기반 실시간 응답 스트리밍은 백엔드 SSE 엔드포인트, Streamlit 표시, Supabase 최종 메시지 저장이 함께 필요하므로 `03_supabase-ai-mini-project`에서 통합 실습으로 다룹니다.
