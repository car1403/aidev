# Lab 03. Supabase Schema Review

## 목표

API 설계가 Supabase 테이블 구조와 어떻게 연결되는지 확인합니다.

## 확인 파일

```text
../03_supabase-schema/table-design.md
../03_supabase-schema/mini-service-schema.sql
```

## 확인할 테이블

```text
mini_questions
mini_service_logs
```

## 확인할 내용

- `mini_questions`에 `user_id`, `question`, `answer`, `provider`, `model`, `actual_api_called`, `llm_call_mode`, `created_at` 컬럼이 있나요?
- `mini_service_logs`에 `event_type`, `message`, `metadata`, `created_at` 컬럼이 있나요?
- 사용자별 조회를 위한 인덱스가 있나요?
- 최신순 조회를 위한 인덱스가 있나요?
- 로그에 민감 정보를 저장하지 않는 기준이 있나요?

## 정리할 내용

API 요청 필드와 LLM 호출 상태 정보가 어떤 테이블 컬럼에 저장되는지 연결해서 적어 봅니다.
