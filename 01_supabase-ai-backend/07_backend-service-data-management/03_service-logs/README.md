# 03. Service Logs

API 호출 성공/실패, 오류 메시지, 실행 시간 같은 서비스 로그를 설계합니다.

## 서비스 로그가 필요한 이유

서비스 로그는 운영자가 나중에 문제를 추적하기 위한 기록입니다. AI 서비스에서는 단순히 답변만 저장하는 것이 아니라, 어떤 요청이 성공했고 실패했는지 함께 남겨야 합니다.

서비스 로그에 자주 들어가는 정보:

```text
event_type
message
metadata
created_at
```

`metadata`에는 JSON 형태로 추가 정보를 저장합니다.

예:

```json
{
  "endpoint": "/ai/chat",
  "status_code": 200,
  "duration_ms": 320,
  "model": "mock-teacher"
}
```

## 실습 파일

```text
01_service_log_schema_example.py
-> 서비스 로그 구조를 Python dict로 확인합니다.

02_insert_service_log.py
-> Supabase service_logs 테이블에 성공 로그를 저장합니다.

03_error_log_example.py
-> 예외가 발생했을 때 오류 로그를 남기는 흐름을 실습합니다.
```
