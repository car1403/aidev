# Security Runbook

AI 서비스 운영 보안 가이드라인과 대응 절차를 작성합니다.

## 1. 보호해야 할 정보

```text
API Key:
AWS Secret:
사용자 개인정보:
운영 로그:
시스템 프롬프트:
```

## 2. 위험 입력 유형

```text
Prompt Injection:
권한 없는 복구 명령 요청:
민감 정보 요청:
위험 Tool 실행 요청:
```

## 3. 대응 절차

```text
위험 입력 탐지
-> 요청 차단 또는 마스킹
-> 감사 로그 저장
-> 반복 발생 시 운영자 알림
-> 필요 시 사람 검토
```

## 4. Agent별 권한 기준

| Agent | 허용 작업 | 금지 작업 | 승인 필요 작업 |
| --- | --- | --- | --- |
| Supervisor Agent |  |  |  |
| Diagnosis Agent |  |  |  |
| Recovery Agent |  |  |  |
| Validation Agent |  |  |  |

## 5. 운영자 알림 기준

```text
정책 위반 반복:
위험 Tool 실행 요청:
복구 실패 반복:
민감 정보 노출 위험:
```
