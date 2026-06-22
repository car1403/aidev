# Labs

Supabase 테이블과 FastAPI endpoint를 연결하는 실습을 진행합니다.

## Lab 01 - 사용자 프로필 데이터 구조

목표:

- Auth 사용자 id와 서비스 프로필 데이터의 차이를 이해합니다.
- `profiles` 테이블에 어떤 컬럼이 필요한지 설명합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\01_user-profile-data\01_profile_schema_example.py
```

## Lab 02 - 대화 이력 구조

목표:

- `conversations`와 `messages`를 분리하는 이유를 이해합니다.
- `role` 값으로 user/assistant 메시지를 구분합니다.

실행:

```powershell
python .\07_backend-service-data-management\02_conversation-history\01_conversation_schema_example.py
```

## Lab 03 - 서비스 로그 구조

목표:

- `event_type`, `message`, `metadata`의 역할을 이해합니다.
- 로그가 운영과 오류 분석에 필요한 이유를 설명합니다.

실행:

```powershell
python .\07_backend-service-data-management\03_service-logs\01_service_log_schema_example.py
```

## Lab 04 - Mock FastAPI 서비스 데이터 API

목표:

- 외부 서비스 없이 API 구조를 먼저 확인합니다.
- 사용자 프로필, 대화방, 메시지, 서비스 로그 endpoint를 Swagger UI에서 테스트합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

Swagger UI:

```text
http://127.0.0.1:8003/docs
```

## Lab 05 - Supabase 저장 예제

목표:

- 실제 Supabase 테이블에 사용자 프로필, 대화 이력, 서비스 로그를 저장합니다.
- 실행 전 `.env`와 `supabase-schema.sql` 적용 여부를 확인합니다.

실행 예:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\01_user-profile-data\02_profile_crud_supabase.py
python .\07_backend-service-data-management\02_conversation-history\02_save_conversation_message.py
python .\07_backend-service-data-management\03_service-logs\02_insert_service_log.py
```

실제 데이터가 Supabase에 저장되므로 수업 중 수업 중 함께 실행합니다.
