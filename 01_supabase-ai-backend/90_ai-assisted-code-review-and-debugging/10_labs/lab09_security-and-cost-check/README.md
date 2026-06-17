# Lab 09 - 보안과 비용 체크

## 목표

AI 백엔드 코드에서 민감 정보 노출과 비용 위험을 점검합니다.

## 사용할 체크리스트

```text
../../00_references/security-cost-checklist.md
../../00_references/backend-review-checklist.md
```

## 점검 대상 예시

```text
05_llm-api-integration
06_supabase-db-and-auth
08_backend-mini-service-practice
```

## 실습 절차

1. 실제 API 호출 파일과 mock 파일을 구분합니다.
2. key/token을 출력하는 코드가 있는지 찾습니다.
3. `max_tokens` 제한이 있는지 확인합니다.
4. Redis TTL이 설정되어 있는지 확인합니다.
5. 서비스 로그에 민감 정보가 들어갈 가능성이 있는지 확인합니다.

## 제출 내용

```text
점검한 파일:
발견한 위험:
수정 제안:
직접 확인한 실행 결과:
```
