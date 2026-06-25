# 03. Supabase Schema

이 폴더에서는 `02_api-design`에서 설계한 API가 사용할 Supabase 테이블을 설계합니다.

API는 데이터를 주고받는 입구이고, Supabase 스키마는 그 데이터를 저장하는 구조입니다. 따라서 API 요청/응답에 등장한 필드가 어떤 테이블과 컬럼으로 저장되는지 연결해서 생각해야 합니다.

## 이번 단계의 목표

- 질문/답변 기록을 저장할 테이블을 설계합니다.
- 서비스 로그를 저장할 테이블을 설계합니다.
- Supabase SQL Editor에서 실행할 SQL 파일을 준비합니다.
- 인덱스가 왜 필요한지 간단히 이해합니다.
- RLS는 이번 단계에서 깊게 적용하지 않고, 이후 확장 기준만 확인합니다.

## 사용 테이블

이번 미니 서비스에서는 최소 두 개의 테이블을 사용합니다.

```text
mini_questions
-> 사용자 질문과 AI 답변 저장

mini_service_logs
-> API 처리 성공/실패와 오류 로그 저장
```

## API와 테이블 연결

| API | 사용하는 테이블 | 설명 |
| --- | --- | --- |
| `POST /questions` | `mini_questions`, `mini_service_logs` | 질문/답변을 저장하고 성공 로그를 남깁니다. |
| `GET /questions` | `mini_questions` | 질문/답변 목록을 조회합니다. |
| `GET /questions/{question_id}` | `mini_questions` | 질문/답변 1개를 조회합니다. |
| `POST /service-logs` | `mini_service_logs` | 서비스 로그를 저장합니다. |
| `GET /service-logs` | `mini_service_logs` | 서비스 로그 목록을 조회합니다. |

## SQL 파일

Supabase Dashboard의 SQL Editor에서 아래 파일을 실행합니다.

```text
mini-service-schema.sql
```

실행 전에 Supabase 프로젝트가 준비되어 있어야 합니다. Supabase 프로젝트 생성과 키 확인 방법은 상위 과정의 `SETUP.md`와 `03_supabase-db-and-auth`를 참고합니다.

## 설계 기준

| 기준 | 설명 |
| --- | --- |
| 질문과 답변은 Supabase에 저장 | 나중에 다시 조회해야 하는 영구 데이터입니다. |
| 서비스 로그도 Supabase에 저장 | 오류 분석과 실행 흐름 확인에 필요합니다. |
| `user_id`를 둠 | 사용자별 조회와 향후 Auth/RLS 확장을 위해 필요합니다. |
| LLM 호출 상태 컬럼을 둠 | `provider`, `model`, `actual_api_called`, `llm_call_mode`로 mock-first와 Gemini SDK 응답을 구분합니다. |
| `metadata`는 `jsonb` 사용 | 로그마다 추가 정보가 다를 수 있기 때문입니다. |
| `created_at`을 둠 | 최신순 조회와 실행 시점 확인에 필요합니다. |

## RLS 적용 기준

이번 단원에서는 먼저 백엔드 서버에서 Supabase에 저장하는 흐름을 이해합니다.

RLS는 다음 단계에서 점진적으로 확장할 수 있습니다.

```text
1. mock 서버로 API 구조 확인
2. Supabase 테이블 생성
3. 서버에서 Supabase 저장 흐름 확인
4. Auth 사용자와 user_id 연결
5. RLS 정책 적용
```

RLS를 바로 적용하면 초보 단계에서 오류 원인을 찾기 어려울 수 있습니다. 따라서 이 단원에서는 “어떤 컬럼이 RLS에 필요할지”를 먼저 생각하는 수준으로 진행합니다.

## 다음 단계 연결

이 폴더에서 만든 테이블 구조는 `04_implementation-guide`의 코드에서 사용됩니다.

```text
mini_questions
-> main_mock.py의 메모리 저장 구조
-> main_supabase.py의 Supabase 저장 구조

mini_service_logs
-> service_logger.py
-> main_supabase.py의 로그 저장 구조
```

테이블 이름과 컬럼 이름이 코드와 다르면 Supabase 저장 과정에서 오류가 발생합니다. SQL 파일, 설계 문서, Python 코드의 이름을 반드시 일치시킵니다.
