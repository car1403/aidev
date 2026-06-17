# 03. Supabase Schema

미니 서비스에 필요한 Supabase 테이블, 컬럼, 관계, RLS 적용 기준을 설계합니다.

## 사용 테이블

이번 미니 서비스에서는 최소 두 개의 테이블을 사용합니다.

```text
mini_qa_items
-> 사용자 질문과 AI 답변 저장

mini_service_logs
-> API 처리 로그 저장
```

## SQL 파일

```text
mini-service-schema.sql
```

Supabase Dashboard의 SQL Editor에서 실행합니다.

## 설계 기준

- 질문과 답변은 나중에 다시 조회해야 하므로 Supabase에 저장합니다.
- 서비스 로그는 오류 분석과 수업 중 검증에 사용합니다.
- 사용자별 접근 제어는 이후 Auth/RLS 단계에서 확장할 수 있도록 `user_id` 컬럼을 둡니다.
