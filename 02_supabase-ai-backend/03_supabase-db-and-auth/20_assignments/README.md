# 20_assignments

이 폴더는 `03_supabase-db-and-auth` 과정의 과제를 정리하는 공간입니다.

`10_labs`가 함께 따라 하며 확인하는 실습이라면, `20_assignments`는 학습 내용을 바탕으로 스스로 설계하고 설명하는 제출 과제입니다. 과제의 목적은 단순히 코드가 실행되는지 확인하는 것이 아니라, Supabase와 Upstash Redis를 어떤 기준으로 나누어 사용하는지 설명할 수 있게 만드는 것입니다.

Docker, Docker Compose, 로컬 PostgreSQL, 로컬 Redis 운영은 이 과정의 과제 범위가 아닙니다. Docker 기반 운영 과제는 `C:\aidev\07_multi-agent-service-ops`에서 진행합니다.

## 과제 목록

| 순서 | 폴더 | 주제 | 핵심 제출물 |
|---|---|---|---|
| 1 | `assignment-01_supabase-project-env-report` | Supabase 프로젝트와 환경변수 준비 | 환경 준비 보고서 |
| 2 | `assignment-02_schema-design-and-sql` | 테이블 설계와 SQL 작성 | 테이블 설계 문서, SQL |
| 3 | `assignment-03_fastapi-supabase-crud-api` | FastAPI와 Supabase CRUD API | API 설계 문서, 실행 결과 |
| 4 | `assignment-04_auth-rls-access-control` | Auth/RLS 접근 제어 | 인증/권한 설계 문서 |
| 5 | `assignment-05_conversation-service-log-design` | 대화 이력과 서비스 로그 설계 | 저장 흐름 설계서 |
| 6 | `assignment-06_upstash-redis-cache-rate-limit` | Upstash Redis 캐시와 요청 제한 | Redis 사용 설계서 |
| 7 | `assignment-07_integrated-db-auth-cache-plan` | Supabase + Auth + Redis 통합 설계 | 통합 아키텍처 문서 |
| 99 | `assignment-99_supabase-db-auth-mini-design` | 최종 미니 설계 과제 | 미니 프로젝트 설계서 |

## 공통 제출 형식

과제 제출 문서는 Markdown 형식으로 작성합니다.

```text
제목
목표
구현 또는 설계 내용
실행 방법
실행 결과
오류와 해결 과정
정리한 내용
```

환경변수와 API key는 절대 문서에 그대로 적지 않습니다.

잘못된 예:

```text
SUPABASE_SERVICE_ROLE_KEY=실제-service-role-key-값
```

올바른 예:

```text
SUPABASE_SERVICE_ROLE_KEY=설정 완료, 실제 값은 제출하지 않음
```

## 공통 평가 기준

- Supabase에 저장할 데이터와 Redis에 저장할 데이터를 구분했는가?
- `anon key`와 `service role key`의 사용 위치를 올바르게 설명했는가?
- FastAPI endpoint의 URL, HTTP Method, Request/Response 구조가 명확한가?
- Auth/RLS가 필요한 이유를 사용자 데이터 보호 관점에서 설명했는가?
- Redis TTL, 캐시, rate limit을 AI 서비스 비용과 안정성 관점에서 설명했는가?
- 오류 발생 시 원인과 해결 과정을 기록했는가?

## 과제 진행 전 확인

아래 명령으로 가상환경을 활성화합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

필요 패키지는 앞선 과정에서 `requirements.txt`로 설치되어 있다는 전제로 진행합니다.

```powershell
pip install -r requirements.txt
```

Supabase 테이블이 없다면 아래 SQL 파일을 Supabase SQL Editor에서 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

## 제출 전 최종 점검

- 실제 API key를 문서나 GitHub에 올리지 않았습니다.
- 실행 화면 또는 터미널 결과를 캡처하거나 텍스트로 정리했습니다.
- Supabase Table Editor에서 데이터 저장 결과를 확인했습니다.
- Upstash Redis를 사용한 경우 TTL 또는 요청 횟수 제한 결과를 확인했습니다.
- 오류가 발생했다면 오류 메시지와 해결 과정을 함께 기록했습니다.

## Legacy Docker Assignments

이전 Docker/PostgreSQL/Redis 직접 실행 과제는 아래 참고 폴더에 남겨 두었습니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_legacy-docker-postgresql-redis-reference\assignments
```

현재 과정의 기준은 Supabase와 Upstash Redis입니다.
