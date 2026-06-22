# 04_ch4_mock-chat-service-interface

챗봇 화면과 chat service 호출 코드를 분리하는 방법을 학습합니다.

이 챕터의 기본 방향은 Streamlit 화면이 `01_supabase-ai-backend`의 chat API를 호출하는 구조를 이해하는 것입니다. 폴더 안의 mock service는 백엔드가 아직 준비되지 않았을 때 화면 흐름을 먼저 연습하기 위한 보조 자료입니다.

## 예제 파일

```text
01_local-ai-function.py
02_backend-chat-api-client.py
03_chat-api-error-handling.py
04_chat-service-config.py
```

## 기본 백엔드 연결

수업에서는 먼저 `01_supabase-ai-backend`의 API 서버를 실행한 뒤 프론트엔드에서 `/api/chat` 형태의 엔드포인트를 호출하는 흐름으로 진행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 보조 샘플 백엔드

chat API 구조만 빠르게 확인할 때는 아래 샘플을 사용할 수 있습니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend\04_ai-chatbot-interface\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-ai-service-sample:app --reload --host 127.0.0.1 --port 8000
```

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run.\04_ai-chatbot-interface\04_ch4_mock-chat-service-interface\02_backend-chat-api-client.py
```

## 확인할 내용

- 화면 코드와 API 호출 코드가 분리되어 있는가?
- 백엔드 API 응답을 챗봇 메시지로 표시할 수 있는가?
- API 호출 실패 시 오류 메시지를 보여줄 수 있는가?
- 대화 기록 저장은 이후 Supabase 백엔드 API와 연결할 수 있는가?

## 수업 메모

Docker와 배포는 이 챕터에서 다루지 않습니다. 서비스 실행 환경과 운영은 `06_multi-agent-service-ops`에서 학습합니다.
