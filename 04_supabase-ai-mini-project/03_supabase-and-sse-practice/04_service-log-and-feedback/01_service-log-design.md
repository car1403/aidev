# 01. 서비스 로그 설계

서비스 로그는 실행 중에 발생한 중요한 이벤트를 기록하는 데이터입니다.

## 로그에 남기면 좋은 정보

```text
action
-> 어떤 작업이 실행되었는지

status
-> success, fail, warning 같은 실행 결과

metadata
-> 실행 시간, 오류 코드, 요청 정보 같은 추가 정보

created_at
-> 언제 발생했는지
```

## 로그 예시

```json
{
  "action": "chat_message_create",
  "status": "success",
  "metadata": {
    "conversation_id": "sample-id",
    "model": "gemini-2.5-flash-lite"
  }
}
```

## 로그를 남기는 위치

```text
FastAPI API 호출 시작
-> 필요한 경우 요청 정보 기록

Supabase 저장 성공
-> success 로그 기록

외부 API 오류
-> fail 로그 기록
```

## 설계 기준

- 모든 작은 동작을 다 기록하지 않습니다.
- 발표와 디버깅에 도움이 되는 이벤트를 기록합니다.
- 민감한 정보, API key, 비밀번호는 로그에 남기지 않습니다.
