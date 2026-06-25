# Lab 10 - Redis 세션과 Cache-aside

이 실습은 Redis에 임시 세션 상태를 저장하고, cache-aside 패턴으로 데이터 조회 흐름을 이해합니다.

## 학습 목표

- Redis에 JSON 형태의 임시 상태를 저장할 수 있습니다.
- cache hit와 cache miss를 구분할 수 있습니다.
- Supabase와 Redis를 함께 사용할 때 역할을 나눌 수 있습니다.

## 실행 방법

세션 상태 저장:

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\04_session_state_example.py
```

Cache-aside 흐름:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\05_cache_aside_mock.py
```

## 확인 기준

- Redis에 사용자별 임시 상태가 저장됩니다.
- 캐시가 있으면 Redis에서 먼저 값을 가져옵니다.
- 캐시가 없으면 Supabase를 조회한다고 가정한 뒤 Redis에 다시 저장합니다.

## 정리 질문

- 로그인 세션 같은 임시 상태는 왜 TTL이 필요할까요?
- cache-aside 패턴은 데이터베이스 부하를 어떻게 줄이나요?
