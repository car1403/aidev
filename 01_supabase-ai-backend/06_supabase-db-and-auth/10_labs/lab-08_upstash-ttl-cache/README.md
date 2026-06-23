# Lab 08 - Upstash Redis TTL 캐시

이 실습은 Redis에 값을 저장하고 TTL이 지나면 자동으로 사라지는 흐름을 확인합니다.

## 학습 목표

- key/value 저장 구조를 이해합니다.
- TTL이 “임시 데이터 자동 만료 시간”이라는 것을 설명할 수 있습니다.
- 캐시가 데이터베이스 조회 횟수를 줄이는 방식을 이해합니다.

## 실행 방법

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\02_cache_set_get_ttl.py
```

## 확인 기준

- 값이 Redis에 저장됩니다.
- TTL이 지나기 전에는 값을 조회할 수 있습니다.
- TTL이 지나면 값이 사라집니다.

## 정리 질문

- AI 답변 캐시는 어떤 상황에서 유용할까요?
- 오래 보관해야 하는 데이터는 왜 Redis보다 Supabase가 적절할까요?
