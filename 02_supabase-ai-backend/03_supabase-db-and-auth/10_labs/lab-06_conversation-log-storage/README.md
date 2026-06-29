# Lab 06 - 대화 이력과 서비스 로그 저장

이 실습은 AI 챗봇 서비스에서 필요한 대화 이력과 서비스 로그를 Supabase에 저장하는 흐름을 확인합니다.

앞 단원에서는 LLM 호출을 `mock-first -> Gemini SDK 최소 예제 -> Gemini SDK 안내형 예제 -> OpenAI 선택 비교` 흐름으로 정리했습니다. 이 실습의 예제는 비용 없이 실행할 수 있도록 mock 응답을 저장하지만, 같은 저장 구조는 Gemini SDK 응답 저장에도 그대로 사용할 수 있습니다.

## 학습 목표

- 대화 묶음과 개별 메시지를 분리해서 저장하는 이유를 이해합니다.
- 서비스 로그가 디버깅과 운영에 필요한 이유를 설명할 수 있습니다.
- Supabase 테이블이 없을 때 발생하는 오류와 해결 방법을 확인합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\05_conversation-history-and-service-logs\01_insert_conversation_and_log.py
```

## 테이블 오류가 발생할 때

`PGRST205` 또는 `Could not find the table` 오류가 나오면 Supabase SQL Editor에서 아래 파일을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

## 확인 기준

- `conversations` 테이블에 대화 묶음이 저장됩니다.
- `messages` 테이블에 사용자 메시지와 AI 메시지가 저장됩니다.
- `service_logs` 테이블에 실행 로그가 저장됩니다.
- `service_logs.metadata`에 `provider`, `model`, `actual_api_called`, `llm_call_mode` 같은 호출 정보가 남습니다.

## 정리 질문

- 대화 이력은 왜 Redis가 아니라 Supabase에 저장하는 것이 적절한가요?
- 서비스 로그는 사용자 화면에 직접 보이지 않는데 왜 필요한가요?
- mock 응답 저장 구조를 Gemini SDK 응답 저장 구조로 확장하려면 어떤 값이 추가로 필요할까요?
