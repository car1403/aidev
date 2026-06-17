# 01_ch1_docker-postgresql-setup

Docker image로 PostgreSQL 컨테이너를 실행하고 접속합니다.

## 학습 내용

- Docker image와 container
- PostgreSQL image pull
- `docker run` 환경변수
- 포트 매핑
- `psql` 접속
- 컨테이너 시작/중지/삭제

## 핵심 명령

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

