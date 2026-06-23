# 06. Upstash Redis 캐시와 세션

이 챕터에서는 Redis를 직접 설치하지 않고, 관리형 Redis 서비스인 Upstash Redis를 사용합니다.

`01_supabase-ai-backend` 과정의 기본 방향은 Supabase 중심입니다. Supabase는 오래 보관해야 하는 사용자 정보, 대화 이력, 서비스 로그를 저장합니다. Upstash Redis는 빠르게 읽고 쓰지만 오래 보관할 필요가 없는 임시 데이터에 사용합니다.

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
- Python 코드에서 Redis에 값을 저장하고 조회할 수 있습니다.
- TTL을 사용해 일정 시간이 지나면 데이터가 자동으로 사라지게 만들 수 있습니다.
- 사용자별 요청 횟수 제한 흐름을 이해할 수 있습니다.
- FastAPI endpoint 앞에 rate limit 의존성을 적용하는 흐름을 이해할 수 있습니다.

## Upstash Redis 준비 순서

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

| 파일 | 내용 |
| --- | --- |
| `01_check_upstash_env.py` | `.env`에 Upstash Redis 값이 들어 있는지 확인합니다. |
| `02_cache_set_get_ttl.py` | Redis에 값을 저장하고 TTL이 적용되는지 확인합니다. |
| `03_rate_limit_example.py` | 사용자별 요청 횟수를 Redis에 저장해 간단한 rate limit을 실습합니다. |
| `04_session_state_example.py` | 사용자별 임시 세션 상태를 Redis에 저장하고 TTL로 자동 만료되게 합니다. |
| `05_cache_aside_mock.py` | Redis cache-aside 패턴을 mock 데이터로 연습합니다. |
| `06_fastapi_rate_limit_dependency.py` | FastAPI endpoint 앞에서 Redis 기반 요청 제한을 적용하는 구조를 실습합니다. |

## 실행 방법

최상위 과정 폴더에서 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\01_check_upstash_env.py
```

값 저장, 조회, TTL 확인:

```powershell
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\02_cache_set_get_ttl.py
```

요청 횟수 제한 확인:

```powershell
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\03_rate_limit_example.py
```

임시 세션 상태 저장:

```powershell
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\04_session_state_example.py
```

Cache-aside 패턴 확인:

```powershell
python .\06_supabase-db-and-auth\06_upstash-redis-cache-and-session\05_cache_aside_mock.py
```

FastAPI rate limit 예제 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\06_upstash-redis-cache-and-session
..\..\.venv\Scripts\Activate.ps1
uvicorn 06_fastapi_rate_limit_dependency:app --reload --host 127.0.0.1 --port 8001
```

Swagger UI:

```text
http://127.0.0.1:8001/docs
```

## 핵심 개념

### Redis

Redis는 데이터를 메모리 중심으로 빠르게 저장하고 조회하는 저장소입니다. 일반적인 데이터베이스처럼 오래 보관하는 용도보다는 빠른 캐시, 임시 상태, 요청 제한 같은 곳에 많이 사용합니다.

| 개념 | 의미 | 예시 |
| --- | --- | --- |
| key | 값을 찾기 위한 이름 | `course:01:session:student01` |
| value | key에 저장되는 실제 데이터 | 사용자 상태 JSON |
| TTL | 값이 살아 있는 시간 | 300초 후 자동 삭제 |
| INCR | 숫자를 1 증가시키는 명령 | 요청 횟수 카운트 |

### Redis key 이름 짓기

Redis는 key/value 저장소이므로 key 이름을 잘 정하는 것이 중요합니다.

```text
course:01:cache:profile:student01
course:01:session:student01
course:01:rate-limit:student01
```

앞부분에 과정명이나 기능명을 붙이면 서로 다른 실습 데이터가 섞이는 것을 줄일 수 있습니다.

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

### Cache-aside 패턴

Cache-aside는 백엔드에서 자주 쓰는 캐시 패턴입니다.

```text
1. 요청이 들어옵니다.
2. Redis에 캐시가 있는지 먼저 확인합니다.
3. 캐시가 있으면 Supabase를 조회하지 않고 Redis 값을 반환합니다.
4. 캐시가 없으면 Supabase를 조회합니다.
5. 조회 결과를 Redis에 저장하고 응답합니다.
```

자주 조회되지만 매번 최신일 필요는 없는 데이터에 적합합니다.

## 자주 만나는 문제

### Upstash Redis environment values are missing

`.env`에 아래 값이 없거나 예시 값으로 남아 있을 수 있습니다.

```env
UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
```

Upstash Dashboard에서 실제 REST URL과 token을 복사해 넣습니다.

### 401 Unauthorized

REST token이 잘못되었거나 복사 중 일부가 빠졌을 가능성이 큽니다. Upstash Dashboard에서 token을 다시 복사합니다.

### TTL이 바로 -2로 나오는 경우

Redis에서 `-2`는 key가 없다는 뜻입니다. key가 만료되었거나 key 이름이 다를 수 있습니다.

### 한글이나 JSON 값 저장이 실패하는 경우

예제 코드는 URL 경로에 들어가는 값을 안전하게 인코딩합니다. 직접 URL을 만들 때는 공백, 한글, JSON 문자열이 URL에서 깨지지 않도록 인코딩이 필요합니다.

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

## 완료 체크리스트

```text
[ ] Upstash Redis database를 만들었습니다.
[ ] .env에 UPSTASH_REDIS_REST_URL을 입력했습니다.
[ ] .env에 UPSTASH_REDIS_REST_TOKEN을 입력했습니다.
[ ] 01_check_upstash_env.py를 실행했습니다.
[ ] SET/GET/TTL 흐름을 확인했습니다.
[ ] Rate Limit 흐름을 확인했습니다.
[ ] Supabase와 Redis에 저장할 데이터를 구분할 수 있습니다.
```
