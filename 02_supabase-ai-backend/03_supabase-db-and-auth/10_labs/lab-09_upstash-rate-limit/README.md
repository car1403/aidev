# Lab 09 - Upstash Redis 요청 횟수 제한

이 실습은 Redis를 사용해 사용자별 요청 횟수를 제한하는 구조를 확인합니다.

## 학습 목표

- rate limit이 AI API 비용 관리와 서비스 안정성에 필요한 이유를 이해합니다.
- Redis `INCR`와 TTL을 사용한 제한 흐름을 설명할 수 있습니다.
- 제한 초과 시 요청을 거절하는 흐름을 이해합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\03_rate_limit_example.py
```

## 확인 기준

- 같은 사용자 ID로 요청 횟수가 증가합니다.
- 정해진 횟수를 넘으면 제한 상태가 됩니다.
- 일정 시간이 지나면 다시 요청할 수 있습니다.

## 정리 질문

- 무료 AI API를 사용할 때 rate limit이 왜 중요한가요?
- 사용자별 제한과 전체 서비스 제한은 어떻게 다를까요?
