# 01_docker-postgresql-setup

Docker로 PostgreSQL 컨테이너를 실행하는 legacy 참고 챕터입니다.

현재 과정에서는 Supabase가 PostgreSQL 서버를 대신 운영해 주므로 로컬 PostgreSQL 컨테이너를 직접 실행하지 않아도 됩니다. 이 문서는 Docker 기반 DB 실행 원리를 이해하고 싶을 때 참고합니다.

## 핵심 개념

- Docker image: 실행 가능한 프로그램 묶음
- Docker container: image를 실제로 실행한 프로세스
- Port mapping: 노트북의 포트와 컨테이너 내부 포트를 연결하는 설정
- Environment variable: 컨테이너 시작 시 전달하는 설정값

## 참고 명령

```powershell
docker pull postgres
docker run --name aidev-postgres `
  -e POSTGRES_USER=aidev `
  -e POSTGRES_PASSWORD=aidev1234 `
  -e POSTGRES_DB=aidev_db `
  -p 5432:5432 `
  -d postgres
docker exec -it aidev-postgres psql -U aidev -d aidev_db
```

## 현재 과정에서의 대응

| Legacy 방식 | 현재 과정 방식 |
|---|---|
| `docker run postgres` | Supabase 프로젝트 생성 |
| `psql` 접속 | Supabase SQL Editor |
| 로컬 DB 포트 관리 | Supabase URL/key 관리 |
