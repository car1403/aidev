# 90_legacy-docker-postgresql-redis-reference

이 폴더는 예전 과정에서 사용하던 Docker 기반 PostgreSQL/Redis 자료를 보관하는 참고 자료입니다.

현재 `01_supabase-ai-backend` 과정은 Supabase와 Upstash Redis를 기준으로 진행합니다. 따라서 이 폴더의 Docker, 로컬 PostgreSQL, 로컬 Redis 예제는 필수 실습이 아닙니다.

## 현재 과정의 기준

```text
01_supabase-ai-backend
-> Supabase managed DB/API/Auth/RLS 중심
-> Redis는 로컬 설치가 아니라 Upstash Redis 중심
-> Docker/PostgreSQL/Redis 직접 실행은 필수로 진행하지 않음
```

Docker 기반 서비스 운영은 아래 과정에서 본격적으로 다룹니다.

```text
C:\aidev\06_multi-agent-service-ops
```

## 이 폴더를 보는 경우

- Supabase 이전의 로컬 PostgreSQL 방식이 궁금할 때
- Upstash Redis 이전의 로컬 Redis 실행 방식을 비교하고 싶을 때
- Docker 명령어, 컨테이너 실행, 포트 연결 개념을 미리 훑어보고 싶을 때
- `06_multi-agent-service-ops`에서 Docker를 본격적으로 배우기 전 참고 자료가 필요할 때

## 폴더 구성

| 폴더 | 내용 | 현재 과정에서의 위치 |
|---|---|---|
| `chapters` | Docker 기반 PostgreSQL/Redis 개념 자료 | 선택 참고 |
| `labs` | Docker 컨테이너 실행과 연결 실습 | 선택 참고 |
| `assignments` | Docker 기반 DB/Redis 과제 예시 | 선택 참고 |
| `references` | Docker, PostgreSQL, Redis 명령어 참고 문서 | 선택 참고 |

## 주의할 점

- 이 폴더의 예제는 Supabase Dashboard를 사용하지 않습니다.
- 로컬 노트북에 Docker Desktop이 설치되어 있어야 실행할 수 있습니다.
- PostgreSQL은 기본적으로 `5432` 포트를 사용하고, Redis는 기본적으로 `6379` 포트를 사용합니다.
- 이미 같은 포트를 사용하는 프로그램이 있으면 컨테이너 실행이 실패할 수 있습니다.
- 현재 과정에서는 이 폴더를 먼저 실행하지 않아도 됩니다.

## Supabase 방식과 Docker 방식의 차이

| 항목 | 현재 과정 방식 | Legacy Docker 방식 |
|---|---|---|
| 데이터베이스 | Supabase managed PostgreSQL | 로컬 Docker PostgreSQL |
| 인증 | Supabase Auth | 직접 구현 또는 단순 토큰 예제 |
| Redis | Upstash Redis | 로컬 Docker Redis |
| 운영 난이도 | 낮음 | 상대적으로 높음 |
| 주요 학습 위치 | `06_supabase-db-and-auth` | `06_multi-agent-service-ops` 이후 참고 |

## 권장 흐름

처음 학습할 때는 아래 순서를 권장합니다.

```text
1. 현재 06_supabase-db-and-auth 과정에서 Supabase와 Upstash Redis를 먼저 학습
2. 03_supabase-ai-mini-project에서 통합 프로젝트로 연결
3. 04 이후 Docker 기본 사용 시작
4. 06_multi-agent-service-ops에서 Docker Compose, AWS, GitHub Actions 학습
5. 필요할 때 이 legacy 폴더를 비교 자료로 참고
```
