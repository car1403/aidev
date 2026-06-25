# Assignment 06 - Upstash Redis 캐시와 요청 제한 설계

Upstash Redis를 사용해 캐시, 임시 세션, 요청 횟수 제한을 설계하는 과제입니다.

## 목표

- Supabase와 Redis의 역할을 구분할 수 있습니다.
- TTL이 필요한 데이터를 예로 들 수 있습니다.
- AI API 비용 관점에서 rate limit이 필요한 이유를 설명할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. Upstash Redis를 사용하는 이유
2. Supabase에 저장할 데이터 목록
3. Redis에 저장할 데이터 목록
4. TTL이 필요한 데이터 예시 3개
5. 사용자별 요청 횟수 제한이 필요한 이유
6. UPSTASH_REDIS_REST_TOKEN을 프론트엔드에 넣으면 안 되는 이유
7. Redis key naming 규칙
8. cache hit/cache miss 흐름 설명
9. FastAPI에서 rate limit을 적용할 endpoint 후보
```

## 작성 예시

```text
Supabase 저장:
- 대화 이력
- 서비스 로그
- 사용자 피드백

Upstash Redis 저장:
- 최근 API 요청 횟수
- 30초짜리 임시 캐시
- 중복 요청 방지 key
```

## 확인 기준

- Redis를 영구 데이터베이스처럼 사용하지 않았습니다.
- TTL 설정 이유가 구체적입니다.
- rate limit이 서비스 안정성과 비용 관리에 어떻게 연결되는지 설명했습니다.
