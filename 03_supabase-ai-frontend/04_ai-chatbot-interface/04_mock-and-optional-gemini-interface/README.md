# 04_mock-and-optional-gemini-interface

챗봇 화면과 응답 생성 로직을 분리하는 방법을 학습합니다.

기본 실습은 비용이 들지 않는 mock 응답으로 진행합니다. 이후 선택 실습으로 Gemini SDK 응답을 Streamlit 화면에 표시합니다. Gemini 선택 실습은 `GEMINI_API_KEY`가 있을 때만 실제 호출하고, key가 없으면 mock 응답으로 안전하게 대체합니다.

## 학습 목표

- 화면 코드와 응답 생성 코드를 분리할 수 있습니다.
- 로컬 mock 응답 함수를 만들 수 있습니다.
- `03_api-integration/00_sample_backend`의 `/api/chat/mock` 응답을 화면에 표시할 수 있습니다.
- 선택 실습으로 Gemini SDK 응답을 화면에 표시할 수 있습니다.
- API key가 없을 때 실제 호출을 하지 않는 안전 장치를 이해합니다.

## 예제 파일

```text
01_local-ai-function.py
02_backend-chat-api-client.py
03_chat-api-error-handling.py
04_chat-service-config.py
05_optional-gemini-sdk-response.py
```

## 샘플 백엔드 실행

백엔드 chat API 구조만 빠르게 확인할 때는 `03_api-integration`의 샘플 백엔드를 사용합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
cd .\03_api-integration\00_sample_backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\04_ai-chatbot-interface\04_mock-and-optional-gemini-interface\02_backend-chat-api-client.py
```

## Gemini 선택 실습 실행 예시

`.env`에 실제 key가 있을 때만 Gemini API를 호출합니다.

```text
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\04_ai-chatbot-interface\04_mock-and-optional-gemini-interface\05_optional-gemini-sdk-response.py
```

## 확인할 내용

- 화면 코드와 응답 생성 코드가 분리되어 있는가?
- mock 응답을 챗봇 메시지로 표시할 수 있는가?
- 백엔드 mock chat API 응답을 챗봇 메시지로 표시할 수 있는가?
- API 호출 실패 시 오류 메시지를 보여줄 수 있는가?
- Gemini API key가 없을 때 실제 호출 없이 mock 응답으로 진행되는가?

## 수업 메모

Docker와 배포는 이 챕터에서 다루지 않습니다. 서비스 실행 환경과 운영은 `07_multi-agent-service-ops`에서 학습합니다.
