# 세션과 상태 저장 패턴

AI 서비스에서는 모든 데이터를 한 곳에 저장하지 않습니다. 오래 보관해야 하는 데이터는 Supabase에 저장하고, 짧게 유지할 임시 상태는 Upstash Redis에 저장합니다.

## 저장 위치 기준

| 데이터 | 권장 저장 위치 | 이유 |
|---|---|---|
| 사용자 프로필 | Supabase | 나중에 다시 조회해야 하는 영구 데이터 |
| 대화 이력 | Supabase | 사용자가 과거 대화를 다시 볼 수 있어야 함 |
| 서비스 로그 | Supabase | 오류 분석과 운영 기록에 필요 |
| 로그인 중 임시 상태 | Upstash Redis | 빠르게 조회하고 만료되어도 됨 |
| 최근 API 요청 횟수 | Upstash Redis | 일정 시간이 지나면 초기화되어도 됨 |
| 짧은 검색 결과 캐시 | Upstash Redis | 잠깐 재사용하면 충분함 |

## Redis Key 예시

```text
session:{user_id}
rate-limit:{user_id}:{minute}
cache:answer:{hash}
cache:profile:{user_id}
```

## Redis에 저장할 JSON 예시

```json
{
  "user_id": "user-001",
  "last_question": "오늘 학습 내용 요약해줘",
  "step": "waiting_for_answer"
}
```

## 원칙

- Redis에는 민감한 정보를 최소한으로 저장합니다.
- Redis key에는 TTL을 설정해 자동 만료되게 합니다.
- 사용자별 대화 이력은 길이를 제한하거나 Supabase에 저장합니다.
- 장기 보관, 검색, 분석이 필요한 데이터는 Supabase에 저장합니다.

## 현재 과정에서 확인할 예제

```text
06_upstash-redis-cache-and-session\04_session_state_example.py
06_upstash-redis-cache-and-session\05_cache_aside_mock.py
```
