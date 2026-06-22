# Redis Docker 실행

## image 받기

```powershell
docker pull redis
```

## container 실행

```powershell
docker run --name aidev-redis `
 -p 6379:6379 `
 -d redis
```

## 접속 확인

```powershell
docker exec -it aidev-redis redis-cli
```

## 기본 명령

```text
SET name Alice
GET name
EXPIRE name 60
TTL name
DEL name
```

