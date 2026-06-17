# 20_assignments

이 폴더는 Supabase 중심 과제를 진행하는 공간입니다.

## Assignment 01 - Supabase 프로젝트 준비 보고서

제출 내용:

- Supabase 프로젝트 생성 여부
- `.env`에 필요한 값 목록
- anon key와 service role key 차이 설명
- 실제 key 값은 제출하지 않음

## Assignment 02 - Supabase 테이블 설계

제출 내용:

- `learning_notes`
- `conversations`
- `messages`
- `service_logs`

각 테이블에 대해 다음을 작성합니다.

```text
테이블 목적
컬럼 목록
primary key
외래키 관계
사용 예시
```

## Assignment 03 - FastAPI + Supabase API

제출 내용:

- `/health`
- `/notes` GET
- `/notes` POST

확인 기준:

- Swagger에서 endpoint가 보입니다.
- Supabase 테이블에 데이터가 저장됩니다.
- 오류가 나면 적절한 메시지를 반환합니다.

## Assignment 04 - Supabase Auth/RLS 설계

제출 내용:

- 어떤 데이터를 사용자별로 제한할지 설명
- RLS가 필요한 이유
- anon key와 service role key 사용 위치
- Streamlit 또는 브라우저에 service role key를 넣으면 안 되는 이유

## Assignment 05 - Upstash Redis 캐시/요청 제한 설계

제출 내용:

- Upstash Redis를 사용하는 이유
- Supabase에 저장할 데이터와 Redis에 저장할 데이터 구분
- TTL이 필요한 데이터 예시 3개
- 사용자별 요청 횟수 제한이 필요한 이유
- `UPSTASH_REDIS_REST_TOKEN`을 프론트엔드에 두면 안 되는 이유
- Redis key naming 규칙
- cache hit/cache miss 흐름 설명
- FastAPI에서 rate limit을 적용할 endpoint 후보

작성 예시:

```text
Supabase 저장:
- 대화 이력
- 서비스 로그
- 사용자 피드백

Upstash Redis 저장:
- 최근 API 요청 횟수
- 30초짜리 임시 캐시
- 중복 요청 방지 key
```

## Assignment 06 - 대화 이력과 서비스 로그 저장 설계

제출 내용:

- `conversations`, `messages`, `service_logs` 테이블 역할 구분
- 사용자 질문과 AI 답변이 어떤 순서로 저장되는지 설명
- 오류가 발생했을 때 `service_logs.metadata`에 넣을 정보
- Redis에 저장하지 않고 Supabase에 저장해야 하는 이유
- 나중에 관리자 화면에서 조회할 수 있는 로그 필터 조건 3개

## Assignment 99 - Supabase DB/Auth Mini Design

제출 내용:

- 프로젝트 주제
- Supabase 테이블 구조
- FastAPI endpoint 목록
- Auth/RLS 적용 계획
- 대화 이력 또는 서비스 로그 저장 흐름
- Upstash Redis를 사용할 캐시/TTL/요청 제한 설계

## Legacy Docker assignments

이전 Docker/PostgreSQL/Redis 직접 실행 과제는 아래 참고 폴더로 이동했습니다.

```text
../90_legacy-docker-postgresql-redis-reference/assignments
```

Docker 기반 과제와 운영 실습은 `C:\aidev\06_multi-agent-service-ops`에서 진행합니다.
