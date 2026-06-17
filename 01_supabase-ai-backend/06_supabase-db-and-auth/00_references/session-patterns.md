# 세션 패턴

## 세션 키 예시

```text
session:{session_id}
conversation:{user_id}
```

## 저장 데이터 예시

```json
{
  "user_id": 1,
  "email": "alice@example.com"
}
```

## 원칙

- 세션에는 민감 정보를 최소화한다.
- TTL을 설정해 만료되게 한다.
- 사용자별 대화 이력은 길이를 제한한다.

