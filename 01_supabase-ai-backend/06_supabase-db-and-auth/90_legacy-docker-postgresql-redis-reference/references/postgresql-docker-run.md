# PostgreSQL Docker 실행

이 문서는 Docker로 PostgreSQL 컨테이너를 실행할 때 사용하는 기본 명령어를 정리한 legacy 참고 문서입니다.

현재 과정에서는 Supabase를 사용하므로 이 명령을 반드시 실행할 필요는 없습니다.

## Image 받기

```powershell
docker pull postgres
```

## Container 실행

```powershell
docker run --name aidev-postgres `
  -e POSTGRES_USER=aidev `
  -e POSTGRES_PASSWORD=aidev1234 `
  -e POSTGRES_DB=aidev_db `
  -p 5432:5432 `
  -d postgres
```

## 실행 상태 확인

```powershell
docker ps
docker logs aidev-postgres
```

## PostgreSQL 접속

```powershell
docker exec -it aidev-postgres psql -U aidev -d aidev_db
```

## 중지와 재시작

```powershell
docker stop aidev-postgres
docker start aidev-postgres
```

## 삭제

```powershell
docker stop aidev-postgres
docker rm aidev-postgres
```

컨테이너를 삭제하면 컨테이너 내부 데이터도 함께 사라질 수 있습니다. 실제 운영에서는 volume을 사용해 데이터를 보존합니다.
