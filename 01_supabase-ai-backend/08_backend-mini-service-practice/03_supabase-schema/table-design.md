# Table Design

이 문서는 `AI 질문 응답 백엔드 미니 서비스`의 Supabase 테이블 설계서입니다.

## 1. mini_questions

`mini_questions` 테이블은 사용자의 질문과 AI 답변을 저장합니다.

### 사용하는 API

| API | 역할 |
| --- | --- |
| `POST /questions` | 질문과 답변 생성 후 저장 |
| `GET /questions` | 질문/답변 목록 조회 |
| `GET /questions/{question_id}` | 질문/답변 상세 조회 |

### 컬럼 설계

| 컬럼 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `uuid` | 필수 | 질문/답변 기록의 고유 id |
| `user_id` | `text` | 필수 | 질문을 보낸 사용자 id |
| `question` | `text` | 필수 | 사용자가 보낸 질문 |
| `answer` | `text` | 필수 | mock LLM 또는 실제 LLM이 생성한 답변 |
| `model` | `text` | 필수 | 답변 생성에 사용한 모델 이름 |
| `created_at` | `timestamptz` | 필수 | 저장 시간 |

### 예시 데이터

| user_id | question | answer | model |
| --- | --- | --- | --- |
| student01 | FastAPI에서 Pydantic은 왜 사용하나요? | 요청 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다. | mock-teacher |

### 설계 이유

- 질문과 답변은 나중에 다시 조회해야 하므로 Supabase에 저장합니다.
- `user_id`가 있어야 사용자별 기록 조회가 가능합니다.
- `model`을 저장하면 mock 답변과 실제 LLM 답변을 구분할 수 있습니다.
- `created_at`이 있어야 최신순 정렬이 가능합니다.

## 2. mini_service_logs

`mini_service_logs` 테이블은 서비스 실행 결과를 저장합니다.

### 사용하는 API

| API | 역할 |
| --- | --- |
| `POST /service-logs` | 서비스 로그 저장 |
| `GET /service-logs` | 서비스 로그 목록 조회 |
| `POST /questions` 내부 처리 | 질문 처리 성공/실패 로그 자동 저장 |

### 컬럼 설계

| 컬럼 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `uuid` | 필수 | 로그 고유 id |
| `event_type` | `text` | 필수 | 로그 종류 |
| `message` | `text` | 필수 | 사람이 읽을 수 있는 로그 메시지 |
| `metadata` | `jsonb` | 필수 | endpoint, question_id, 처리 시간 등 추가 정보 |
| `created_at` | `timestamptz` | 필수 | 저장 시간 |

### event_type 예시

| event_type | 설명 |
| --- | --- |
| `question_created` | 질문/답변 생성 성공 |
| `question_not_found` | 질문 기록 조회 실패 |
| `validation_error` | 요청 데이터 검증 실패 |
| `supabase_error` | Supabase 저장 또는 조회 실패 |
| `api_error` | 일반 API 처리 실패 |

### metadata 예시

```json
{
  "user_id": "student01",
  "question_id": "question-001",
  "endpoint": "POST /questions",
  "duration_ms": 120
}
```

### 설계 이유

- 로그는 운영 중 문제를 찾기 위한 데이터입니다.
- `event_type`이 있으면 오류 종류별로 검색하기 쉽습니다.
- `metadata`는 상황마다 필요한 추가 정보가 다르므로 `jsonb`로 저장합니다.
- API Key, 비밀번호, 토큰 같은 민감 정보는 `metadata`에 저장하지 않습니다.

## 3. 인덱스 설계

| 인덱스 | 대상 | 이유 |
| --- | --- | --- |
| `idx_mini_questions_user_id` | `mini_questions(user_id)` | 사용자별 질문 목록 조회 속도 개선 |
| `idx_mini_questions_created_at` | `mini_questions(created_at)` | 최신순 정렬 속도 개선 |
| `idx_mini_service_logs_event_type` | `mini_service_logs(event_type)` | 로그 종류별 조회 속도 개선 |
| `idx_mini_service_logs_created_at` | `mini_service_logs(created_at)` | 최신 로그 조회 속도 개선 |

## 4. Supabase와 Upstash Redis 역할 구분

| 데이터 | 저장 위치 |
| --- | --- |
| 질문/답변 기록 | Supabase |
| 서비스 로그 | Supabase |
| 반복 질문 응답 캐시 | Upstash Redis 선택 |
| 요청 제한 카운터 | Upstash Redis 선택 |

이번 스키마 파일은 Supabase 테이블만 다룹니다. Redis는 테이블을 만드는 방식이 아니라 Key-Value 형태로 사용합니다.

## 5. 완료 체크리스트

- [ ] API 설계의 필드와 테이블 컬럼이 일치한다.
- [ ] 질문/답변 저장 테이블이 있다.
- [ ] 서비스 로그 저장 테이블이 있다.
- [ ] 사용자별 조회를 위한 `user_id`가 있다.
- [ ] 최신순 조회를 위한 `created_at`이 있다.
- [ ] 검색에 필요한 인덱스가 있다.
- [ ] 민감 정보를 로그에 저장하지 않는 기준이 있다.
