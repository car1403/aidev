# 07. Backend Service Data Management

이 단원에서는 FastAPI 백엔드에서 실제 서비스에 필요한 데이터를 어떻게 나누고 저장하는지 학습합니다.

앞 단원인 `03_supabase-db-and-auth`에서는 Supabase 프로젝트 생성, 테이블 CRUD, Auth, RLS, Upstash Redis의 기본 사용 흐름을 익혔습니다. 이번 단원에서는 그 내용을 바탕으로 사용자 프로필, 대화 이력, 서비스 로그, API 엔드포인트를 하나의 백엔드 서비스 데이터 구조로 연결합니다.

## 핵심 요약

- Supabase에는 오래 보관해야 하는 데이터를 저장합니다.
- Upstash Redis에는 짧게 유지되는 임시 데이터와 캐시 데이터를 저장합니다.
- FastAPI는 화면이나 외부 클라이언트가 사용할 API 입구 역할을 합니다.
- 사용자 정보, 대화 이력, 서비스 로그는 서로 다른 목적을 가지므로 테이블을 분리해서 설계합니다.
- 먼저 mock 데이터로 API 구조를 확인한 뒤, Supabase 연동 코드로 확장합니다.
- 앞 단원의 LLM 호출 흐름은 `mock-first -> Gemini SDK 최소 예제 -> Gemini SDK 안내형 예제 -> OpenAI 선택 비교` 기준으로 이어집니다.

## 이 단원에서 다루는 데이터

| 데이터 | 저장 위치 | 설명 |
| --- | --- | --- |
| 사용자 프로필 | Supabase | 사용자 id, 이메일, 이름, 학습 수준, 선호 언어 같은 사용자 기본 정보 |
| 대화방 정보 | Supabase | 하나의 대화 흐름을 묶는 단위 |
| 대화 메시지 | Supabase | 사용자 질문, AI 응답, 역할, 작성 시간 |
| 서비스 로그 | Supabase | API 호출, 성공/실패, 오류 내용, 처리 시간, 운영 기록 |
| 임시 상태/캐시 | Upstash Redis | TTL이 필요한 캐시, 요청 제한 카운터, 중복 요청 방지, 짧은 세션 상태 |

## Supabase와 Redis를 나누는 기준

```text
오래 보관하고 다시 조회해야 한다 -> Supabase
사용자별 접근 제어가 필요하다 -> Supabase + Auth/RLS
운영 분석과 오류 추적에 사용한다 -> Supabase service_logs
짧은 시간만 유지하면 된다 -> Upstash Redis
빠르게 읽고 사라져도 된다 -> Upstash Redis
```

이 과정에서는 Redis 서버를 노트북에 직접 설치하지 않고 Upstash Redis를 사용합니다. Docker 기반 Redis 실행, Docker Compose, 로컬 PostgreSQL 운영은 `C:\aidev\07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 폴더 구성

```text
04_backend-service-data-management
├─ README.md
├─ 00_references
├─ 01_user-profile-data
├─ 02_conversation-history
├─ 03_service-logs
├─ 04_fastapi-service-endpoints
├─ 10_labs
└─ 20_assignments
```

## 학습 순서

1. `00_references`에서 서비스 데이터 설계 기준을 먼저 확인합니다.
2. `01_user-profile-data`에서 사용자 프로필 테이블과 CRUD 흐름을 학습합니다.
3. `02_conversation-history`에서 대화방과 메시지를 분리해서 저장하는 이유를 학습합니다.
4. `03_service-logs`에서 서비스 로그가 운영과 오류 분석에 왜 필요한지 확인합니다.
5. `04_fastapi-service-endpoints`에서 mock API와 Supabase 연동 API를 비교합니다.
6. `10_labs`에서 테이블 설계, CRUD, mock API, Supabase API를 직접 점검합니다.
7. `20_assignments`에서 서비스 데이터 관리 설계를 과제로 정리합니다.

## 실행 준비

이 단원은 `02_supabase-ai-backend` 루트의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

이미 앞 단원에서 패키지를 설치했다면 `pip install -r requirements.txt`는 다시 실행하지 않아도 됩니다. 다만 새 터미널을 열었다면 가상환경 활성화는 다시 해야 합니다.

## 구조 확인 예제 실행

아래 예제는 Supabase에 접속하지 않고 데이터 구조를 먼저 확인하는 예제입니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\04_backend-service-data-management\01_user-profile-data\01_profile_schema_example.py
python .\04_backend-service-data-management\02_conversation-history\01_conversation_schema_example.py
python .\04_backend-service-data-management\03_service-logs\01_service_log_schema_example.py
```

## mock FastAPI 서버 실행

mock 서버는 Supabase 키가 없어도 API 구조를 먼저 확인할 수 있는 연습용 서버입니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\04_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8003/docs
```

Swagger UI에서 프로필 조회, 대화 생성, 메시지 저장, 서비스 로그 저장 API를 직접 실행해 볼 수 있습니다.

## Supabase 연동 예제 실행 기준

Supabase 연동 예제는 실제 프로젝트 URL과 API Key가 필요합니다.

```text
SUPABASE_URL=본인의 Supabase Project URL
SUPABASE_ANON_KEY=본인의 Supabase anon public key
```

실습 전에 Supabase Dashboard에서 필요한 테이블이 만들어져 있어야 합니다. 테이블 설계 기준은 각 하위 폴더의 README와 `00_references`를 함께 확인합니다.

## 이 단원에서 꼭 구분해야 하는 것

| 구분 | 설명 |
| --- | --- |
| Auth 사용자 | Supabase Auth가 관리하는 로그인 계정 |
| Profile | 서비스에서 추가로 관리하는 사용자 표시 정보 |
| Conversation | 하나의 대화 묶음 |
| Message | 대화 안에 들어가는 사용자 질문 또는 AI 응답 |
| Service Log | 서비스 실행 결과와 오류를 추적하기 위한 운영 데이터 |
| Cache | 같은 요청을 빠르게 처리하기 위한 임시 데이터 |

## 다음 단원과의 연결

이 단원에서 만든 사용자 프로필, 대화 이력, 서비스 로그 구조는 `05_backend-mini-service-practice`와 `99_final-backend-project`에서 더 큰 서비스 흐름으로 이어집니다.

특히 개인화 AI 챗봇을 만들 때는 다음 흐름을 계속 사용합니다.

```text
사용자 요청
-> FastAPI 엔드포인트
-> 사용자 프로필 조회
-> 이전 대화 이력 조회
-> mock 응답 생성 또는 Gemini SDK 응답 생성
-> 메시지 저장
-> 서비스 로그 저장
-> 응답 반환
```

서비스 로그에는 LLM 호출 결과를 나중에 추적할 수 있도록 다음 값을 함께 남기는 것이 좋습니다.

```json
{
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite",
  "actual_api_called": false,
  "llm_call_mode": "mock-first"
}
```

실제 Gemini SDK endpoint와 연결하면 `actual_api_called`를 `true`로 바꾸고, 처리 시간과 오류 정보를 함께 저장합니다.
