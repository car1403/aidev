# Lab 05 - 서비스 로그 구조와 저장

이 실습은 서비스 로그 구조를 이해하고 Supabase에 성공 로그와 오류 로그를 저장합니다.

## 목표

- `event_type`, `message`, `metadata`의 역할을 설명할 수 있습니다.
- 성공 로그와 오류 로그의 차이를 구분할 수 있습니다.
- 민감한 정보를 로그에 저장하면 안 되는 이유를 이해합니다.

## 구조 예제 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\03_service-logs\01_service_log_schema_example.py
```

## Supabase 저장 예제 실행

성공 로그 저장:

```powershell
python .\07_backend-service-data-management\03_service-logs\02_insert_service_log.py
```

오류 로그 저장:

```powershell
python .\07_backend-service-data-management\03_service-logs\03_error_log_example.py
```

## 확인 기준

- `service_logs` 테이블에 `practice.success` 로그가 저장됩니다.
- `service_logs` 테이블에 `practice.error` 로그가 저장됩니다.
- `metadata`에 `status_code`, `duration_ms`, `error_type` 같은 정보가 들어갑니다.

## 정리 질문

- 로그에 access token이나 service role key를 저장하면 왜 위험한가요?
- 운영 대시보드에서 가장 먼저 보고 싶은 `event_type`은 무엇인가요?
