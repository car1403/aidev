# Lab 07 - Upstash Redis 환경변수 확인

이 실습은 Upstash Redis를 사용하기 위한 REST URL과 token이 준비되어 있는지 확인합니다.

## 학습 목표

- Redis를 “빠르게 꺼내 쓰는 임시 저장소”로 이해합니다.
- Upstash Redis REST URL과 token의 역할을 구분합니다.
- Redis token이 외부에 노출되면 안 되는 이유를 설명합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\01_check_upstash_env.py
```

## 확인 기준

- `UPSTASH_REDIS_REST_URL`이 설정되어 있습니다.
- `UPSTASH_REDIS_REST_TOKEN`이 설정되어 있습니다.
- placeholder 값이 아니라 실제 Upstash Console에서 발급받은 값입니다.

## 정리 질문

- Supabase와 Redis는 각각 어떤 데이터를 저장하는 데 적합한가요?
- Redis token을 GitHub에 올리면 어떤 문제가 생길 수 있나요?
