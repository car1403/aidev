# 07_supabase-redis-debugging-with-codex

이 단원에서는 Codex를 활용해 Supabase와 Upstash Redis 실습에서 발생하는 오류를 분석하는 방법을 학습합니다.

Supabase와 Redis 오류는 코드 한 줄의 문제가 아닐 때가 많습니다. `.env` 파일 위치, 환경 변수 이름, 테이블 생성 여부, 컬럼명, 권한, TTL 설정처럼 코드 밖의 설정이 함께 연결되어 있습니다. 그래서 오류 메시지만 보고 바로 코드를 고치기보다, 원인 후보를 순서대로 좁혀 가는 방식이 필요합니다.

## 이 단원에서 다루는 내용

- Supabase 연결 오류를 확인하는 방법
- Supabase 테이블명, 컬럼명, SQL 스키마 불일치 문제를 찾는 방법
- Supabase Auth와 RLS 정책 관련 오류를 구분하는 방법
- insert, select, update, delete 결과가 비어 있을 때 확인할 내용
- Upstash Redis URL, token, key, TTL 문제를 확인하는 방법
- cache, session, rate limit 코드에서 자주 발생하는 오류를 추적하는 방법
- Codex에게 오류 분석을 요청할 때 필요한 정보를 정리하는 방법

## 디버깅 기본 순서

Supabase와 Redis 오류가 발생하면 다음 순서로 확인합니다.

1. 실행한 명령을 기록합니다.
2. 전체 오류 메시지를 복사합니다.
3. 오류가 발생한 파일 경로를 확인합니다.
4. `.env` 파일 위치와 변수명을 확인합니다.
5. 외부 서비스의 프로젝트 URL, key, token이 맞는지 확인합니다.
6. Supabase SQL Editor에서 테이블과 컬럼이 실제로 존재하는지 확인합니다.
7. Redis key가 생성되는지, TTL이 설정되는지 확인합니다.
8. 수정 후 같은 명령으로 다시 실행합니다.

디버깅에서 가장 중요한 것은 "무엇을 실행했을 때 어떤 오류가 났는지"를 남기는 것입니다.

## Codex에게 오류를 전달할 때 필요한 정보

Codex에게 오류를 물어볼 때는 오류 메시지만 붙여 넣는 것보다 아래 정보를 함께 제공해야 합니다.

```text
Supabase 또는 Upstash Redis 실습 중 오류가 발생했습니다.

실행한 위치:
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\03_fastapi-supabase-integration

실행한 명령:
uvicorn main:app --reload

오류 메시지:
여기에 터미널 오류 메시지를 붙여 넣습니다.

관련 파일:
- main.py
- .env.example
- schema.sql

확인하고 싶은 것:
1. 환경 변수 이름이 맞는지
2. 테이블명과 컬럼명이 맞는지
3. Supabase key 사용 위치가 맞는지
4. 초보자가 따라 할 수 있는 확인 순서

바로 수정하지 말고, 원인 후보와 확인 순서를 먼저 정리해주세요.
```

이렇게 요청하면 Codex가 코드와 설정을 함께 보면서 원인을 나누어 설명할 수 있습니다.

## Supabase 환경 변수 오류

Supabase 연동에서 가장 흔한 오류는 환경 변수 이름이나 위치 문제입니다.

확인할 항목은 다음과 같습니다.

- `.env` 파일이 실행하는 폴더에 있는가?
- `.env.example`만 있고 실제 `.env`가 없는 것은 아닌가?
- 변수명이 코드와 정확히 일치하는가?
- 값 앞뒤에 불필요한 공백이나 따옴표가 들어가지 않았는가?
- Supabase URL이 프로젝트 URL인지, API endpoint를 잘못 넣은 것은 아닌가?
- anon key와 service role key를 혼동하지 않았는가?

예를 들어 코드에서 `SUPABASE_URL`을 읽는데 `.env`에는 `SUPABASE_PROJECT_URL`이라고 적으면 값이 없는 것으로 처리됩니다.

## Supabase 테이블과 컬럼 오류

Supabase는 PostgreSQL 기반이므로 테이블명과 컬럼명이 정확히 맞아야 합니다.

자주 만나는 오류는 다음과 같습니다.

| 오류 상황 | 의미 | 확인할 것 |
| --- | --- | --- |
| `relation does not exist` | 테이블이 존재하지 않습니다. | SQL Editor에서 테이블 생성 여부 확인 |
| `column does not exist` | 컬럼명이 맞지 않습니다. | Python dict key와 SQL 컬럼명 비교 |
| insert 결과가 비어 있음 | 저장은 실패했지만 오류 처리가 부족할 수 있습니다. | 응답 객체와 에러 메시지 확인 |
| select 결과가 빈 배열 | 조건이 맞지 않거나 데이터가 없습니다. | `.eq(...)` 조건과 실제 데이터 확인 |
| update/delete 영향 없음 | 조건에 맞는 행이 없습니다. | id, user_id, item_id 값 확인 |

초보 단계에서는 Python 코드의 key 이름과 SQL 컬럼명을 나란히 놓고 비교하는 것이 가장 효과적입니다.

## Supabase Auth와 RLS 오류

Supabase Auth와 RLS를 사용하면 데이터 접근 권한 문제가 발생할 수 있습니다.

확인할 항목은 다음과 같습니다.

- 인증이 필요한 API인데 로그인 정보 없이 호출한 것은 아닌가?
- RLS가 켜져 있는데 select, insert, update 정책이 없는 것은 아닌가?
- 사용자별 데이터에 `user_id` 조건이 들어가는가?
- 백엔드에서 service role key를 쓰는지, 프론트엔드에서 anon key를 쓰는지 구분되는가?
- RLS 정책을 임시로 끄고 테스트한 뒤 다시 켜는 절차를 알고 있는가?

RLS 오류는 코드가 틀린 것이 아니라 권한 정책이 막고 있는 경우가 많습니다. 따라서 "코드 문제인지, 정책 문제인지"를 나누어 확인해야 합니다.

## Upstash Redis 연결 오류

Upstash Redis는 REST URL과 REST token을 사용합니다.

자주 만나는 오류는 다음과 같습니다.

| 오류 상황 | 의미 | 확인할 것 |
| --- | --- | --- |
| 401 Unauthorized | token이 없거나 잘못되었습니다. | `UPSTASH_REDIS_REST_TOKEN` 확인 |
| connection error | URL이 잘못되었거나 네트워크 문제가 있습니다. | `UPSTASH_REDIS_REST_URL` 확인 |
| 값이 저장되지 않음 | set 명령 또는 key 이름 문제일 수 있습니다. | Redis 콘솔에서 key 확인 |
| rate limit이 초기화되지 않음 | TTL이 없을 수 있습니다. | `expire`, `ex`, TTL 설정 확인 |
| 캐시가 계속 같은 값 | key 설계가 너무 넓을 수 있습니다. | 사용자별, 요청별 key 분리 확인 |

Redis는 빠른 임시 저장소입니다. 오래 보관해야 하는 대화 이력이나 로그는 Supabase에 저장하고, Redis에는 세션, 캐시, rate limit처럼 만료 가능한 데이터를 저장합니다.

## Redis TTL 디버깅

TTL은 key가 자동으로 사라지는 시간입니다. TTL이 없으면 임시 데이터가 계속 남아 있을 수 있습니다.

확인할 항목은 다음과 같습니다.

- 세션 key에 만료 시간이 있는가?
- rate limit key가 일정 시간이 지나면 초기화되는가?
- 캐시 key가 너무 오래 유지되지 않는가?
- TTL 단위가 초인지 밀리초인지 혼동하지 않았는가?
- 같은 key를 계속 덮어쓰면서 TTL이 사라지는 것은 아닌가?

Codex에게는 다음처럼 요청할 수 있습니다.

```text
아래 Redis 코드에서 TTL이 제대로 설정되는지 리뷰해주세요.

확인할 것:
1. set 명령에서 만료 시간이 들어가는가?
2. rate limit key가 사용자별로 분리되는가?
3. TTL이 없어서 데이터가 계속 남을 가능성이 있는가?
4. 초보자가 확인할 수 있는 테스트 방법을 알려달라.
```

## Supabase와 Redis 역할 구분

오류를 줄이려면 두 저장소의 역할을 명확히 나누는 것이 좋습니다.

| 데이터 종류 | 권장 저장 위치 | 이유 |
| --- | --- | --- |
| 사용자 프로필 | Supabase | 장기 보관이 필요합니다. |
| 대화 이력 | Supabase | 나중에 조회해야 합니다. |
| 서비스 로그 | Supabase | 운영 분석에 필요합니다. |
| 최근 응답 캐시 | Upstash Redis | 빠른 조회와 자동 만료가 필요합니다. |
| 로그인 상태 보조 정보 | Upstash Redis | 짧은 시간 유지하면 됩니다. |
| rate limit 카운터 | Upstash Redis | 시간 기반 초기화가 필요합니다. |

이 역할이 섞이면 디버깅이 어려워집니다. 특히 Redis에 오래 보관해야 할 데이터를 넣으면 나중에 데이터가 사라져도 원인을 찾기 어렵습니다.

## Codex 디버깅 요청 예시

아래 예시는 Supabase 오류를 분석할 때 사용할 수 있습니다.

```text
Supabase 실습에서 아래 오류가 발생했습니다.

실행 명령:
uvicorn main:app --reload

오류 메시지:
relation "mini_questions" does not exist

관련 코드:
테이블 이름으로 mini_questions를 사용하고 있습니다.

확인 요청:
1. 이 오류가 무엇을 의미하는지 설명해주세요.
2. Supabase SQL Editor에서 무엇을 확인해야 하나요?
3. Python 코드의 테이블명과 SQL 파일의 테이블명을 어떻게 비교해야 하나요?
4. 초보자가 따라 할 수 있는 순서로 정리해주세요.
5. 아직 코드를 수정하지 말고 원인 후보를 먼저 나눠주세요.
```

아래 예시는 Redis 오류를 분석할 때 사용할 수 있습니다.

```text
Upstash Redis 실습에서 401 오류가 발생했습니다.

실행 명령:
python redis_session_example.py

오류 메시지:
401 Unauthorized

관련 설정:
.env.example에는 UPSTASH_REDIS_REST_URL과 UPSTASH_REDIS_REST_TOKEN이 있습니다.

확인 요청:
1. 어떤 환경 변수를 먼저 확인해야 하나요?
2. URL과 token을 어디에서 발급받는지 설명해주세요.
3. 실제 token을 화면이나 GitHub에 노출하지 않는 방법을 알려주세요.
4. 수정 후 정상 연결을 확인하는 간단한 방법을 알려주세요.
```

## 디버깅 결과를 정리하는 방법

오류를 해결한 뒤에는 무엇을 고쳤는지 짧게 기록합니다.

```md
## 오류 기록

- 발생 위치: 03_supabase-db-and-auth/03_fastapi-supabase-integration
- 실행 명령: uvicorn main:app --reload
- 오류 메시지: relation "mini_questions" does not exist
- 원인: Supabase SQL Editor에서 테이블 생성 전 API를 실행함
- 해결: schema.sql 실행 후 다시 테스트
- 재확인: Swagger UI에서 POST 요청 성공 확인
```

이런 기록을 남기면 같은 오류가 다시 발생했을 때 훨씬 빠르게 해결할 수 있습니다.

## 완료 체크리스트

- [ ] Supabase 환경 변수 오류를 확인하는 순서를 설명할 수 있다.
- [ ] 테이블명과 컬럼명 불일치 오류를 찾을 수 있다.
- [ ] Supabase Auth와 RLS 오류를 코드 오류와 구분할 수 있다.
- [ ] Upstash Redis URL/token 오류를 확인할 수 있다.
- [ ] Redis TTL 누락 문제를 찾을 수 있다.
- [ ] Supabase와 Redis의 저장 역할을 구분할 수 있다.
- [ ] Codex에게 오류 메시지, 실행 명령, 관련 파일을 함께 전달할 수 있다.
- [ ] 오류 해결 후 원인과 해결 방법을 기록할 수 있다.
