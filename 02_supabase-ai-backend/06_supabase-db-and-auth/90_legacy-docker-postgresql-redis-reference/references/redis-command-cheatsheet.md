# Redis 명령 요약

## 문자열

```text
SET key value
GET key
DEL key
```

## 만료 시간

```text
SETEX session:abc 3600 user-1
TTL session:abc
```

## 리스트

```text
LPUSH conversation:1 "user message"
LRANGE conversation:1 0 -1
LTRIM conversation:1 0 19
```

