# 07_supabase-redis-debugging-with-codex

Supabase와 Upstash Redis 실습에서 자주 발생하는 오류를 Codex와 함께 분석하는 단원입니다.

## 학습 목표

- `.env` 설정 오류를 찾을 수 있습니다.
- Supabase 테이블명/컬럼명 불일치 오류를 분석할 수 있습니다.
- update/delete 조건 누락 위험을 리뷰할 수 있습니다.
- Upstash Redis URL/token 누락, TTL 누락 문제를 점검할 수 있습니다.

## 자주 만나는 오류

| 상황 | 확인할 것 |
| --- | --- |
| `SUPABASE_URL` missing | `.env` 위치와 변수명 |
| relation does not exist | SQL Editor에서 테이블 생성 여부 |
| column does not exist | Python dict key와 테이블 컬럼명 |
| Upstash 401 | REST token 오타 또는 누락 |
| rate limit이 초기화되지 않음 | `expire` 또는 TTL 설정 여부 |

## Codex 요청 예시

```text
Supabase 실습에서 아래 오류가 발생했습니다.

실행 명령:

오류 메시지:

관련 코드:

.env에는 어떤 변수명이 필요한지 알려주고,
테이블 생성 여부와 컬럼명 확인 순서를 초보자 기준으로 설명해줘.
```

