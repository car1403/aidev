# 00. References

이 문서는 `04_backend-service-data-management` 단원에서 계속 참고하는 서비스 데이터 설계 기준입니다.

이번 단원에서는 단순히 데이터를 저장하는 방법만 보지 않습니다. 어떤 데이터가 오래 보관되어야 하는지, 어떤 데이터가 임시로만 필요 한지, 어떤 데이터가 운영 분석에 필요한지를 구분합니다.

## 데이터 저장 위치 판단 기준

| 질문 | 권장 위치 | 이유 |
| --- | --- | --- |
| 나중에 다시 조회해야 하나요? | Supabase | 영구 저장이 필요합니다. |
| 사용자별 권한 제어가 필요한가요? | Supabase + Auth/RLS | 로그인 사용자 기준으로 접근 제어를 해야 합니다. |
| 운영 분석이나 오류 추적에 필요한가요? | Supabase | 로그를 누적해서 분석해야 합니다. |
| 일정 시간이 지나면 사라져도 되나요? | Upstash Redis | TTL을 설정해서 자동 만료시킬 수 있습니다. |
| 같은 응답을 빠르게 재사용하면 되나요? | Upstash Redis | 캐시로 응답 속도를 개선할 수 있습니다. |
| 요청 횟수 제한이나 중복 요청 방지가 필요한가요? | Upstash Redis | 카운터와 짧은 상태 저장에 적합합니다. |

## 주요 테이블 설계 기준

### profiles

`profiles` 테이블은 Supabase Auth 사용자와 서비스 사용자 정보를 연결합니다.

| 컬럼 | 예시 | 설명 |
| --- | --- | --- |
| id | auth user id | Supabase Auth의 사용자 id와 연결되는 기본키 |
| email | user@example.com | 로그인 이메일 |
| display_name | 홍길동 | 화면에 보여줄 이름 |
| preferred_language | ko | 선호 언어 |
| course_level | beginner | 학습 수준 |
| created_at | 자동 생성 시간 | 프로필 생성 시간 |

핵심 기준:

- 로그인 계정 자체는 Supabase Auth가 관리합니다.
- 서비스에서 추가로 필요한 표시 이름, 학습 수준, 설정값은 `profiles`에 저장합니다.
- `profiles.id`는 보통 Supabase Auth의 `auth.users.id`와 같은 값을 사용합니다.

### conversations

`conversations` 테이블은 여러 메시지를 하나로 묶는 대화방 역할을 합니다.

| 컬럼 | 예시 | 설명 |
| --- | --- | --- |
| id | uuid | 대화방 id |
| user_id | auth user id | 대화를 소유한 사용자 |
| title | FastAPI 질문 | 대화 제목 |
| created_at | 자동 생성 시간 | 대화 생성 시간 |

핵심 기준:

- 하나의 사용자는 여러 대화를 가질 수 있습니다.
- 대화 제목은 처음 질문을 바탕으로 만들거나 사용자가 수정할 수 있습니다.
- 대화방을 기준으로 메시지를 묶으면 이전 대화 조회가 쉬워집니다.

### messages

`messages` 테이블은 사용자 질문과 AI 응답을 저장합니다.

| 컬럼 | 예시 | 설명 |
| --- | --- | --- |
| id | uuid | 메시지 id |
| conversation_id | uuid | 어떤 대화방에 속하는지 |
| role | user 또는 assistant | 메시지 작성 주체 |
| content | 질문 또는 응답 내용 | 실제 메시지 본문 |
| created_at | 자동 생성 시간 | 메시지 생성 시간 |

핵심 기준:

- `role`은 최소한 `user`, `assistant`를 구분합니다.
- 메시지는 반드시 특정 `conversation_id`에 연결되어야 합니다.
- 나중에 대화 이어하기를 구현하려면 메시지 순서와 작성 시간이 중요합니다.

### service_logs

`service_logs` 테이블은 서비스 실행 기록과 오류를 저장합니다.

| 컬럼 | 예시 | 설명 |
| --- | --- | --- |
| id | uuid | 로그 id |
| event_type | api_success | 로그 종류 |
| message | 메시지 저장 성공 | 사람이 읽을 수 있는 설명 |
| metadata | JSON | 요청 경로, 처리 시간, 오류 코드 같은 추가 정보 |
| created_at | 자동 생성 시간 | 로그 생성 시간 |

핵심 기준:

- 로그에는 비밀번호, API Key, 토큰 같은 민감 정보를 저장하지 않습니다.
- `event_type`은 검색하기 쉬운 짧은 이름으로 정합니다.
- `metadata`에는 분석에 필요한 추가 정보를 JSON 형태로 저장합니다.

## event_type 예시

| event_type | 사용 상황 |
| --- | --- |
| profile_created | 사용자 프로필 생성 |
| conversation_created | 새 대화방 생성 |
| message_saved | 사용자 질문 또는 AI 응답 저장 |
| api_success | API 요청 성공 |
| api_error | API 요청 실패 |
| supabase_error | Supabase 연동 오류 |
| validation_error | 요청 데이터 검증 실패 |
| cache_hit | Redis 캐시 사용 |
| cache_miss | Redis 캐시 미사용 |

## Supabase와 Upstash Redis 역할 비교

| 항목 | Supabase | Upstash Redis |
| --- | --- | --- |
| 저장 기간 | 오래 보관 | 짧게 보관 |
| 대표 용도 | 사용자 정보, 대화 이력, 서비스 로그 | 캐시, 요청 제한, 임시 상태 |
| 데이터 형태 | 관계형 테이블 | Key-Value |
| 권한 제어 | Auth/RLS 사용 가능 | 애플리케이션 코드에서 제어 |
| 조회 방식 | SQL/REST API 기반 | Key 조회 |
| 예시 | `profiles`, `messages`, `service_logs` | `rate_limit:user01`, `cache:answer:123` |

## FastAPI 엔드포인트 설계 기준

| 기능 | HTTP Method | URL 예시 | 설명 |
| --- | --- | --- | --- |
| 사용자 프로필 조회 | GET | `/profiles/{user_id}` | 특정 사용자 프로필 조회 |
| 사용자 프로필 저장 | POST | `/profiles` | 사용자 프로필 생성 또는 저장 |
| 대화방 생성 | POST | `/conversations` | 새 대화 시작 |
| 메시지 저장 | POST | `/messages` | 사용자 질문 또는 AI 응답 저장 |
| 대화 메시지 조회 | GET | `/conversations/{conversation_id}/messages` | 특정 대화의 메시지 목록 조회 |
| 서비스 로그 저장 | POST | `/service-logs` | 운영 로그 저장 |
| 상태 확인 | GET | `/health` | 서버 정상 동작 확인 |

## 요청/응답 설계 기준

좋은 API는 요청과 응답 구조가 예측 가능해야 합니다.

요청 데이터 예시:

```json
{
  "user_id": "student01",
  "display_name": "홍길동",
  "preferred_language": "ko",
  "course_level": "beginner"
}
```

응답 데이터 예시:

```json
{
  "ok": true,
  "data": {
    "user_id": "student01",
    "display_name": "홍길동"
  }
}
```

오류 응답 예시:

```json
{
  "ok": false,
  "error": {
    "code": "profile_not_found",
    "message": "사용자 프로필을 찾을 수 없습니다."
  }
}
```

## 서비스 데이터 체크리스트

| 점검 항목 | 확인 질문 |
| --- | --- |
| 사용자 프로필 | 로그인 사용자와 서비스 프로필이 어떻게 연결되어 있나요? |
| 대화방 | 여러 메시지를 하나의 대화 흐름으로 묶을 수 있나요? |
| 메시지 | `user`와 `assistant` 역할이 명확히 구분되나요? |
| 서비스 로그 | 성공, 실패, 오류, 처리 시간을 추적할 수 있나요? |
| 민감 정보 | API Key, 토큰, 비밀번호가 로그에 저장되지 않나요? |
| Redis 사용 | 영구 저장 데이터와 임시 데이터가 구분되어 있나요? |
| API 구조 | URL과 HTTP Method가 기능에 맞게 사용되나요? |
| 오류 처리 | Supabase 오류와 입력값 오류가 구분되어 응답되나요? |

## 관련 단원 연결

- `03_supabase-db-and-auth`: Supabase 프로젝트, Auth, RLS, Upstash Redis 기본 사용
- `04_backend-service-data-management`: 사용자 프로필, 대화 이력, 서비스 로그, API 엔드포인트 설계
- `05_backend-mini-service-practice`: 위 데이터를 활용한 작은 백엔드 서비스 구현
- `99_final-backend-project`: 개인화 AI 챗봇 백엔드 프로젝트로 확장
