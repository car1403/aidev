# Assignment 03. Supabase Schema Document

## 목표

미니 서비스에서 사용할 Supabase 테이블 설계를 문서로 정리합니다.

## 참고 파일

```text
../03_supabase-schema/README.md
../03_supabase-schema/table-design.md
../03_supabase-schema/mini-service-schema.sql
```

## 제출 내용

아래 테이블을 기준으로 작성합니다.

```text
mini_questions
mini_service_logs
```

## mini_questions 작성 항목

- 테이블 목적
- 컬럼 목록
- 각 컬럼의 타입과 의미
- `user_id`가 필요한 이유
- `created_at`이 필요한 이유
- 사용자별 조회와 최신순 조회에 필요한 인덱스

## mini_service_logs 작성 항목

- 테이블 목적
- `event_type` 예시
- `message`에 들어갈 내용
- `metadata`에 넣을 수 있는 값
- 로그에 저장하면 안 되는 민감 정보
- 로그 조회에 필요한 인덱스

## 완료 기준

- API 설계의 필드와 테이블 컬럼이 서로 맞습니다.
- 질문/답변 저장 테이블과 서비스 로그 테이블이 분리되어 있습니다.
- 인덱스가 필요한 이유가 설명되어 있습니다.
- RLS는 이후 확장 기준으로 설명되어 있습니다.
