# 10_labs

이 폴더는 `04_backend-service-data-management`에서 배운 사용자 프로필, 대화 이력, 서비스 로그, FastAPI endpoint를 작은 실습 단위로 다시 확인하는 공간입니다.

앞쪽 챕터에서는 각각의 데이터 구조를 따로 확인했습니다. 이 폴더에서는 그 내용을 순서대로 실행하면서 “서비스에서 어떤 데이터를 어떤 테이블에 저장하는지”를 정리합니다.

LLM 응답은 앞 단원의 `02_llm-api-integration` 기준에 맞춰 `mock-first -> Gemini SDK 최소 예제 -> Gemini SDK 안내형 예제 -> OpenAI 선택 비교` 흐름으로 바라봅니다. 여기서는 LLM을 새로 호출하기보다, mock 응답과 Gemini SDK 응답이 같은 저장 구조와 로그 구조로 관리될 수 있는지를 확인합니다.

## 실습 전 준비

백엔드 과정 루트에서 가상환경을 활성화합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

Supabase를 사용하는 실습은 `.env`와 테이블이 준비되어 있어야 합니다.

```text
C:\aidev\02_supabase-ai-backend\.env
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

`supabase-schema.sql`은 Supabase Dashboard의 SQL Editor에서 실행합니다.

## 실습 순서

| 순서 | 폴더 | 연결 챕터 | 핵심 결과 |
|---|---|---|---|
| 1 | `lab-01_user-profile-schema` | `01_user-profile-data` | 프로필 데이터 구조 이해 |
| 2 | `lab-02_user-profile-supabase-crud` | `01_user-profile-data` | Supabase `profiles` 저장/조회 |
| 3 | `lab-03_conversation-message-schema` | `02_conversation-history` | `conversations`와 `messages` 관계 이해 |
| 4 | `lab-04_conversation-message-supabase` | `02_conversation-history` | 대화 묶음과 메시지 저장/조회 |
| 5 | `lab-05_service-log-design` | `03_service-logs` | 서비스 로그 구조와 metadata 이해 |
| 6 | `lab-06_mock-fastapi-service-api` | `04_fastapi-service-endpoints` | Supabase 없이 API 구조 확인 |
| 7 | `lab-07_supabase-fastapi-service-api` | `04_fastapi-service-endpoints` | Supabase에 실제 저장되는 API 확인 |
| 99 | `lab-99_service-data-review-checklist` | 전체 | 데이터 저장 위치와 제출 전 점검 |

## Supabase와 Redis 기준

이 단원은 서비스 데이터 관리가 중심입니다.

```text
사용자 프로필 -> Supabase
대화 이력 -> Supabase
서비스 로그 -> Supabase
짧은 캐시/TTL/요청 제한 -> Upstash Redis
```

Redis 실습은 이전 단원의 `06_upstash-redis-cache-and-session`에서 다루었고, 이 단원에서는 “영구 저장이 필요한 서비스 데이터는 Supabase에 둔다”는 기준을 확인합니다.

## 실습 결과 정리 방법

각 lab을 진행한 뒤 아래 내용을 짧게 기록하면 좋습니다.

- 실행한 파일 또는 접속한 URL
- 정상 실행 결과
- Supabase Table Editor에서 확인한 테이블
- 오류가 발생한 경우 오류 메시지와 해결 방법
- 이 데이터가 Supabase에 저장되어야 하는 이유
- LLM 응답과 관련된 경우 `provider`, `model`, `actual_api_called`, `llm_call_mode` 값
