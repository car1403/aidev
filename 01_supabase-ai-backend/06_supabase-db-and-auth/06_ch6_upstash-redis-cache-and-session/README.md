# 06_ch6_upstash-redis-cache-and-session

이 챕터에서는 Redis를 직접 설치하지 않고, 관리형 Redis 서비스인 Upstash Redis를 사용합니다.

`01_supabase-ai-backend`의 기본 방향은 Supabase 중심입니다. Supabase는 오래 보관해야 하는 사용자 정보, 대화 이력, 서비스 로그를 저장합니다. Upstash Redis는 빠르게 읽고 쓰지만 오래 보관할 필요가 없는 임시 데이터에 사용합니다.

## 왜 Upstash Redis를 사용하나요?

초보자가 Docker로 Redis를 직접 실행하면 Redis 자체보다 Docker 설치, 포트, 컨테이너 상태, 네트워크 문제에 시간을 많이 쓰게 됩니다.

그래서 이 과정에서는 먼저 Upstash Redis를 사용해 Redis의 핵심 개념을 배웁니다.

```text
Supabase
-> 오래 보관할 데이터
-> 사용자 정보, 대화 이력, 서비스 로그, 피드백

Upstash Redis
-> 짧게 보관할 임시 데이터
-> 캐시, TTL, 중복 요청 방지, 요청 횟수 제한, 임시 세션 상태
```

Docker로 Redis를 직접 실행하고 운영하는 방법은 `C:\aidev\06_multi-agent-service-ops`에서 다룹니다.

## 학습 목표

- Redis가 어떤 상황에서 필요한지 설명할 수 있습니다.
- Supabase와 Redis의 역할 차이를 구분할 수 있습니다.
- Upstash Redis REST URL과 Token을 `.env`에 설정할 수 있습니다.
- FastAPI/Python 코드에서 Redis에 값을 저장하고 조회할 수 있습니다.
- TTL을 사용해 일정 시간이 지나면 데이터가 자동으로 사라지게 만들 수 있습니다.
- 간단한 API 요청 횟수 제한 흐름을 이해할 수 있습니다.

## 먼저 준비할 것

Upstash Redis를 사용하려면 Upstash에서 Redis database를 만든 뒤 REST API 정보를 복사해야 합니다.

1. Upstash에 접속합니다.
2. Redis database를 생성합니다.
3. database 상세 화면에서 REST API 정보를 확인합니다.
4. `UPSTASH_REDIS_REST_URL` 값을 복사합니다.
5. `UPSTASH_REDIS_REST_TOKEN` 값을 복사합니다.
6. `C:\aidev\01_supabase-ai-backend\.env` 파일에 붙여 넣습니다.

`.env` 예시는 다음과 같습니다.

```env
UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
```

주의할 점:

- Upstash token은 비밀번호처럼 다룹니다.
- `.env` 파일은 GitHub에 올리지 않습니다.
- Streamlit이나 브라우저 코드에 Upstash token을 넣지 않습니다.
- Upstash Redis 호출은 FastAPI 같은 백엔드 코드에서 처리합니다.

## 실습 파일

```text
01_check_upstash_env.py
->.env에 Upstash Redis 값이 들어 있는지 확인합니다.

02_cache_set_get_ttl.py
-> Redis에 값을 저장하고, TTL이 지나면 사라지는지 확인합니다.

03_rate_limit_example.py
-> 사용자별 요청 횟수를 Redis에 저장해 간단한 rate limit을 실습합니다.

04_session_state_example.py
-> 사용자별 임시 세션 상태를 Redis에 저장하고 TTL로 자동 만료되게 합니다.

05_cache_aside_mock.py
-> Redis cache-aside 패턴을 mock 데이터로 연습합니다.

06_fastapi_rate_limit_dependency.py
-> FastAPI endpoint 앞에서 Redis 기반 요청 제한을 적용하는 구조를 실습합니다.
```

## 실행 방법

최상위 과정 폴더에서 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python.\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\01_check_upstash_env.py
python.\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\02_cache_set_get_ttl.py
python.\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\03_rate_limit_example.py
python.\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\04_session_state_example.py
python.\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\05_cache_aside_mock.py
```

## 수업에서 설명할 핵심 개념

### Redis

Redis는 데이터를 메모리 중심으로 빠르게 저장하고 조회하는 저장소입니다. 일반적인 데이터베이스처럼 오래 보관하는 용도보다는 빠른 캐시, 임시 상태, 요청 제한 같은 곳에 많이 사용합니다.

Redis를 처음 배울 때는 다음 네 가지를 먼저 기억하면 됩니다.

| 개념 | 의미 | 예시 |
| --- | --- | --- |
| key | 값을 찾기 위한 이름 | `session:student01` |
| value | key에 저장되는 실제 데이터 | 사용자 상태 JSON |
| TTL | 값이 살아 있는 시간 | 300초 후 자동 삭제 |
| INCR | 숫자를 1 증가시키는 명령 | 요청 횟수 카운트 |

## Redis key 이름 짓기

Redis는 key/value 저장소이므로 key 이름을 잘 정하는 것이 중요합니다. 수업에서는 다음 규칙을 사용합니다.

```text
course:01:cache:profile:student01
course:01:session:student01
course:01:rate-limit:student01
```

앞부분에 과정명이나 기능명을 붙이면 서로 다른 실습 데이터가 섞이는 것을 줄일 수 있습니다.

### Cache

캐시는 자주 사용하는 데이터를 잠시 저장해 두는 방식입니다. 매번 Supabase를 조회하지 않고 Redis에 값이 있으면 Redis 값을 먼저 사용할 수 있습니다.

```text
요청 수신
-> Redis에 캐시가 있는지 확인
-> 있으면 Redis 값 반환
-> 없으면 Supabase 조회
-> 조회 결과를 Redis에 잠시 저장
-> 응답 반환
```

### TTL

TTL은 Time To Live의 줄임말입니다. 데이터를 몇 초 동안만 유지할지 정하는 값입니다. 예를 들어 TTL을 60초로 설정하면 60초 뒤에 Redis 값이 자동으로 사라집니다.

TTL이 유용한 예:

- 로그인 후 임시 인증 상태
- AI 응답 생성 중 중복 요청 방지 key
- 30초 동안만 재사용할 검색 결과
- 1분 동안의 사용자별 요청 횟수

### Rate Limit

Rate Limit은 사용자가 너무 짧은 시간에 API를 많이 호출하지 못하도록 제한하는 방식입니다. AI API는 비용이 발생할 수 있으므로, 백엔드에서 요청 횟수를 제한하는 개념을 꼭 이해해야 합니다.

기본 흐름:

```text
사용자가 API 호출
-> Redis key: rate-limit:{user_id} 값을 1 증가
-> 첫 요청이면 TTL 60초 설정
-> count가 limit 이하이면 허용
-> count가 limit 초과이면 거절
```

## Cache-aside 패턴

Cache-aside는 백엔드에서 가장 자주 쓰는 캐시 패턴 중 하나입니다.

```text
1. 요청이 들어온다.
2. Redis에 캐시가 있는지 먼저 확인한다.
3. 캐시가 있으면 Supabase를 조회하지 않고 Redis 값을 반환한다.
4. 캐시가 없으면 Supabase를 조회한다.
5. 조회 결과를 Redis에 저장하고 응답한다.
```

이 패턴은 자주 조회되지만 매번 최신일 필요는 없는 데이터에 적합합니다.

## 이 챕터의 범위

이 챕터에서 하는 것:

- Upstash Redis REST API 사용
- Redis key/value 저장
- TTL 적용
- 캐시 흐름 이해
- 요청 횟수 제한 흐름 이해

이 챕터에서 하지 않는 것:

```text
Docker로 Redis 컨테이너 실행
Redis 서버 운영
Redis persistence 설정
Redis cluster 구성
Docker Compose로 Redis 연결
운영 환경 장애 대응
```

위 내용은 `C:\aidev\06_multi-agent-service-ops`에서 다룹니다.
