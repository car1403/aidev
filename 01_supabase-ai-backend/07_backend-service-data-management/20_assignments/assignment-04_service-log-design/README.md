# Assignment 04 - 서비스 로그 설계

서비스 운영과 오류 분석을 위한 `service_logs` 구조를 설계하는 과제입니다.

## 목표

- 서비스 로그가 필요한 이유를 설명할 수 있습니다.
- `event_type`, `message`, `metadata`의 역할을 구분할 수 있습니다.
- 로그에 저장하면 안 되는 민감 정보를 설명할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. service_logs 테이블 목적
2. event_type 예시 5개
3. metadata에 넣을 수 있는 값 5개
4. 오류 발생 시 저장할 정보
5. 로그에 저장하면 안 되는 민감 정보
6. 운영 대시보드에서 조회할 필터 조건 3개
7. 예시 로그 데이터 1개
```

## event_type 예시

```text
ai.answer.created
ai.answer.failed
message.created
profile.updated
rate_limit.exceeded
```

## metadata 예시

```json
{
  "endpoint": "/ai/chat",
  "status_code": 200,
  "duration_ms": 320,
  "model": "gemini-2.5-flash-lite"
}
```

## 확인 기준

- 성공 로그와 오류 로그를 구분했습니다.
- `metadata`를 JSON으로 사용하는 이유를 설명했습니다.
- access token, API key, service role key 같은 민감 정보를 로그에 넣지 않는다고 명시했습니다.
