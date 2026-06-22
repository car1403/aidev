# PostgreSQL Docker 실행

## image 받기

```powershell
docker pull postgres
```

## container 실행

```powershell
docker run --name aidev-postgres `
 -e POSTGRES_USER=aidev `
 -e POSTGRES_PASSWORD=aidev1234 `
 -e POSTGRES_DB=aidev_db `
 -p 5432:5432 `
 -d postgres
```

## 접속 확인

```powershell
docker exec -it aidev-postgres psql -U aidev -d aidev_db
```

## 중지와 재시작

```powershell
docker stop aidev-postgres
docker start aidev-postgres
```

