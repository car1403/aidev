# Database Design Document

이 문서는 Supabase PostgreSQL 데이터베이스 설계서입니다.

## 1. 설계 원칙

- 테이블은 3정규화(3NF)를 기준으로 설계합니다.
- 데이터 중복을 최소화합니다.
- 삽입, 갱신, 삭제 이상현상이 생기지 않도록 테이블을 나눕니다.
- 논리 ERD와 물리 ERD를 모두 작성합니다.
- 모든 컬럼의 타입, 길이, 제약조건, 기본값, 설명을 작성합니다.

## 2. Logical ERD

아래 형식으로 엔티티, 속성, 관계, 카디널리티를 정리합니다.

```text
profiles 1 --- N log_events
log_events 1 --- 0..1 ai_responses
log_events 1 --- 0..N feedback
```

논리 ERD에는 다음을 반드시 포함합니다.

- 엔티티 이름
- 주요 속성
- 엔티티 간 관계
- 1:1, 1:N, N:M 같은 카디널리티
- 사용자별 접근 제어가 필요한 테이블 표시

## 3. Physical Tables

### profiles

| Column | Type | Constraint | Default | Description |
| --- | --- | --- | --- | --- |
| id | uuid | PK | gen_random_uuid() | 사용자 ID |
| display_name | varchar(50) | NOT NULL | - | 표시 이름 |
| created_at | timestamptz | NOT NULL | now() | 생성 시각 |

### log_events

| Column | Type | Constraint | Default | Description |
| --- | --- | --- | --- | --- |
| id | bigint | PK | identity | 로그 ID |
| user_id | uuid | FK, nullable | - | 사용자 ID |
| event_type | varchar(50) | NOT NULL | - | 로그 유형 |
| message | text | NOT NULL | - | 로그 메시지 |
| status | varchar(20) | NOT NULL | `success` | 처리 상태 |
| metadata | jsonb | nullable | `{}` | 추가 정보 |
| created_at | timestamptz | NOT NULL | now() | 생성 시각 |

### ai_responses

| Column | Type | Constraint | Default | Description |
| --- | --- | --- | --- | --- |
| id | bigint | PK | identity | AI 응답 ID |
| log_event_id | bigint | FK, NOT NULL | - | 연결된 로그 ID |
| prompt | text | NOT NULL | - | 사용자 입력 또는 프롬프트 |
| answer | text | NOT NULL | - | AI 응답 |
| latency_ms | integer | nullable | - | 처리 시간 |
| created_at | timestamptz | NOT NULL | now() | 생성 시각 |

### feedback

| Column | Type | Constraint | Default | Description |
| --- | --- | --- | --- | --- |
| id | bigint | PK | identity | 피드백 ID |
| log_event_id | bigint | FK, NOT NULL | - | 연결된 로그 ID |
| score | integer | CHECK 1~5 | - | 만족도 점수 |
| comment | text | nullable | - | 사용자 의견 |
| created_at | timestamptz | NOT NULL | now() | 생성 시각 |

## 3-1. Column Definition Checklist

- [ ] 모든 컬럼의 데이터 타입이 명확합니다.
- [ ] 문자열 컬럼은 길이 제한이 필요한지 검토했습니다.
- [ ] 필수 컬럼에는 `NOT NULL`을 적용했습니다.
- [ ] 중복되면 안 되는 값에는 `UNIQUE`를 검토했습니다.
- [ ] 값의 범위가 있는 컬럼에는 `CHECK`를 검토했습니다.
- [ ] 기본값이 필요한 컬럼에는 `DEFAULT`를 작성했습니다.
- [ ] 각 컬럼의 설명 또는 코멘트를 작성했습니다.

## 4. Indexes

| Table | Index | Columns | Reason |
| --- | --- | --- | --- |
| log_events | idx_log_events_created_at | created_at | 최근 로그 정렬 |
| log_events | idx_log_events_event_type | event_type | 유형별 필터 |
| log_events | idx_log_events_status | status | 상태별 필터 |

## 4-1. Normalization Review

3정규화(3NF) 기준으로 아래 질문에 답합니다.

- [ ] 한 컬럼에 여러 값이 들어가지 않습니다.
- [ ] 기본키 일부에만 의존하는 컬럼이 없습니다.
- [ ] 기본키가 아닌 컬럼이 다른 일반 컬럼에 의존하지 않습니다.
- [ ] 사용자 정보, 로그, AI 응답, 피드백이 역할에 맞게 분리되어 있습니다.
- [ ] 삽입, 갱신, 삭제 이상현상이 발생하지 않도록 설계했습니다.

## 5. RLS Policy

RLS를 사용한다면 아래 내용을 작성합니다.

```text
테이블:
정책 이름:
허용 대상:
허용 조건:
테스트 결과:
```

## 6. Schema Review Checklist

- [ ] 3정규화 기준으로 테이블이 나뉘어 있습니다.
- [ ] PK/FK 관계가 명확합니다.
- [ ] 컬럼 타입과 제약조건이 정의되어 있습니다.
- [ ] JSONB 컬럼은 필요한 경우에만 사용합니다.
- [ ] 대시보드 조회에 필요한 인덱스를 고려했습니다.
- [ ] 논리 ERD와 물리 ERD가 서로 일치합니다.
- [ ] Supabase RLS 적용 여부와 정책 테스트 결과를 작성했습니다.
