# 07. Backend Service Data Management

이 단원은 Supabase DB와 Auth를 이해한 뒤, 실제 백엔드 서비스에서 관리해야 하는 사용자 정보, 대화 이력, 서비스 로그를 설계하는 단계입니다.

`06_supabase-db-and-auth`에서 Supabase 프로젝트, 테이블, CRUD, Auth, RLS를 배웠다면, 이 단원에서는 그 지식을 서비스 데이터 구조로 연결합니다.

## 학습 목표

- 사용자 정보 테이블과 서비스 데이터 테이블을 구분할 수 있습니다.
- 대화 이력 저장 구조를 설계할 수 있습니다.
- 서비스 로그를 왜 저장해야 하는지 설명할 수 있습니다.
- FastAPI endpoint와 Supabase 테이블을 연결하는 흐름을 이해합니다.
- Upstash Redis는 임시 상태, 캐시, 요청 제한에 사용하고, Supabase는 영구 저장에 사용한다는 기준을 이해합니다.
- 실제 서비스에서 필요한 데이터 저장 흐름을 작은 코드 예제로 구현할 수 있습니다.

## 권장 구성

```text
07_backend-service-data-management
├─ README.md
├─ 00_references
├─ 01_user-profile-data
├─ 02_conversation-history
├─ 03_service-logs
├─ 04_fastapi-service-endpoints
├─ 10_labs
└─ 20_assignments
```

## 수업에서 다루는 데이터 예시

| 데이터 | 설명 |
| --- | --- |
| 사용자 정보 | 사용자 id, 이메일, 이름, 가입일 같은 기본 정보 |
| 대화 이력 | 사용자의 질문, AI 응답, 생성 시간 |
| 서비스 로그 | API 호출 시간, 성공/실패 여부, 오류 메시지 |
| 피드백 데이터 | 응답이 도움이 되었는지에 대한 사용자 평가 |
| Redis 임시 데이터 | 캐시, 요청 제한 카운터, 짧게 유지되는 사용자 상태 |

## Supabase 기반 저장 흐름

```text
FastAPI 요청 수신
-> 사용자 식별
-> Supabase 테이블 조회
-> 서비스 로직 실행
-> 결과 저장
-> 응답 반환
```

## Upstash Redis 학습 기준

이미지에는 Redis 세션 관리와 사용자 상태 유지가 포함되어 있습니다. `01_supabase-ai-backend`에서는 Redis 서버를 직접 실행하지 않고, Upstash Redis를 사용합니다.

이 과정에서는 대화 이력과 서비스 로그를 Supabase 테이블에 저장하고, 짧게 유지해도 되는 값은 Upstash Redis에 저장하는 기준을 배웁니다.

```text
Supabase
-> 오래 보관할 데이터
-> 사용자 정보, 대화 이력, 서비스 로그, 피드백

Upstash Redis
-> 짧게 보관할 임시 데이터
-> TTL 캐시, 요청 횟수 제한, 중복 요청 방지, 임시 세션 상태
```

Upstash Redis 실습은 `06_supabase-db-and-auth/06_ch6_upstash-redis-cache-and-session`에서 진행합니다.

Docker 기반 Redis 운영, Redis 컨테이너 실행, Docker Compose 연동은 `C:\aidev\06_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 실습 예제 구성

이 단원은 `06_supabase-db-and-auth`에서 배운 CRUD, Auth/RLS, 로그 저장 개념을 실제 서비스 구조로 묶어보는 단계입니다.

```text
01_user-profile-data
├─ 01_profile_schema_example.py
└─ 02_profile_crud_supabase.py

02_conversation-history
├─ 01_conversation_schema_example.py
├─ 02_save_conversation_message.py
└─ 03_list_conversation_messages.py

03_service-logs
├─ 01_service_log_schema_example.py
├─ 02_insert_service_log.py
└─ 03_error_log_example.py

04_fastapi-service-endpoints
├─ main_mock.py
└─ main_supabase.py
```

## 수업 진행 순서

1. 사용자 프로필 데이터가 왜 필요한지 설명합니다.
2. 대화 세션과 메시지를 분리해서 저장하는 이유를 확인합니다.
3. 서비스 로그가 오류 분석과 운영 개선에 왜 필요한지 확인합니다.
4. mock FastAPI 서버로 전체 API 구조를 먼저 실행합니다.
5. Supabase 환경변수가 준비된 수업 참여자는 Supabase 연동 예제로 확장합니다.

## 실행 예시

비용과 외부 서비스 영향 없이 구조만 확인:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\01_user-profile-data\01_profile_schema_example.py
python .\07_backend-service-data-management\02_conversation-history\01_conversation_schema_example.py
python .\07_backend-service-data-management\03_service-logs\01_service_log_schema_example.py
```

mock FastAPI 서버 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

Swagger UI:

```text
http://127.0.0.1:8003/docs
```

Supabase 연동 예제는 실제 데이터가 저장될 수 있으므로, 수업 중 함께 `.env`와 테이블을 확인한 뒤 실행합니다.
