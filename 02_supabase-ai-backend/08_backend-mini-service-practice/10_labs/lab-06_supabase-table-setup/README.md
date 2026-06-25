# Lab 06. Supabase Table Setup

## 목표

Supabase SQL Editor에서 미니 서비스 테이블을 생성합니다.

## 실행 파일

```text
../03_supabase-schema/mini-service-schema.sql
```

## 실행 순서

1. Supabase Dashboard에 접속합니다.
2. 실습 프로젝트를 선택합니다.
3. 왼쪽 메뉴에서 SQL Editor를 엽니다.
4. `mini-service-schema.sql` 내용을 붙여 넣습니다.
5. Run 버튼을 눌러 실행합니다.
6. Table Editor에서 `mini_questions`, `mini_service_logs`가 생성되었는지 확인합니다.

## 확인할 내용

- `mini_questions` 테이블이 생성되었나요?
- `mini_service_logs` 테이블이 생성되었나요?
- 각 테이블에 `created_at` 컬럼이 있나요?
- 인덱스 생성 SQL이 포함되어 있나요?

## 주의할 점

`SUPABASE_SERVICE_ROLE_KEY`는 서버에서만 사용해야 합니다. 공개 저장소나 화면에 노출하지 않습니다.
