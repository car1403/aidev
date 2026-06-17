# 자주 발생하는 오류

## port is already allocated

이미 같은 포트를 사용하는 컨테이너가 실행 중입니다.

```powershell
docker ps
docker stop aidev-postgres
```

## password authentication failed

DB 사용자 또는 비밀번호가 맞지 않습니다.

확인할 것:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- 연결 문자열

## connection refused

컨테이너가 실행 중이 아니거나 포트 매핑이 잘못되었습니다.

```powershell
docker ps
docker logs aidev-postgres
```

## Redis connection error

Redis 컨테이너와 포트를 확인합니다.

```powershell
docker ps
docker logs aidev-redis
```

