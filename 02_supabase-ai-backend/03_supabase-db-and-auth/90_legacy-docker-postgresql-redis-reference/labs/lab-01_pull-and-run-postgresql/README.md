# Lab 01 - PostgreSQL 컨테이너 실행

Docker로 PostgreSQL 컨테이너를 실행하는 legacy lab입니다.

현재 Supabase 과정에서는 필수로 실행하지 않습니다. 로컬 DB 컨테이너 실행 방식을 비교하고 싶을 때 참고합니다.

## 목표

- `postgres` Docker image를 다운로드합니다.
- `aidev-postgres` 컨테이너를 실행합니다.
- `docker ps`로 실행 상태를 확인합니다.
- `psql`로 컨테이너 내부 PostgreSQL에 접속합니다.

## 참고 명령

```powershell
docker pull postgres
docker run --name aidev-postgres `
  -e POSTGRES_USER=aidev `
  -e POSTGRES_PASSWORD=aidev1234 `
  -e POSTGRES_DB=aidev_db `
  -p 5432:5432 `
  -d postgres
docker ps
docker exec -it aidev-postgres psql -U aidev -d aidev_db
```

## 현재 과정에서의 대응

Supabase 과정에서는 PostgreSQL 컨테이너 실행 대신 Supabase 프로젝트를 생성합니다.
