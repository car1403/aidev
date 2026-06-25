# Supabase Schema Template

Supabase 데이터베이스 설계서 템플릿입니다.

## 1. 테이블 목록

| 테이블 | 목적 |
| --- | --- |
| profiles | 사용자 기본 정보 |
| conversations | 대화 묶음 |
| messages | 사용자 메시지와 AI 응답 |
| service_logs | API 호출과 오류 로그 |
| feedbacks | 사용자 피드백 |

## 2. 테이블 상세

### profiles

| 컬럼 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| id | uuid | Y | 사용자 식별자 |
| email | text | Y | 이메일 |
| display_name | text | N | 표시 이름 |
| created_at | timestamptz | Y | 생성 시간 |

### service_logs

| 컬럼 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| id | uuid | Y | 로그 식별자 |
| user_id | uuid | N | 사용자 식별자 |
| action | text | Y | 실행 작업 이름 |
| status | text | Y | success, fail, warning |
| metadata | jsonb | Y | 추가 정보 |
| created_at | timestamptz | Y | 생성 시간 |

## 3. 관계

```text
profiles 1:N conversations
conversations 1:N messages
messages 1:N feedbacks
profiles 1:N service_logs
```

## 4. RLS 기준

```text
RLS를 켠 경우:
- 사용자는 자신의 데이터만 조회합니다.
- insert/update/delete 정책을 별도로 테스트합니다.

service role key:
- FastAPI 백엔드에서만 사용합니다.
- Streamlit에 직접 넣지 않습니다.
```

## 5. 테스트 데이터

테스트 데이터는 `sql/seed-sample-data.sql`을 참고합니다.
