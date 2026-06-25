# 07. Docker Errors For Later Courses

Docker는 05 과정부터 사용하고, Docker Compose는 07 과정에서 본격적으로 다룹니다.

## docker 명령이 안 보일 때

```powershell
docker --version
docker ps
```

확인할 것:

```text
Docker Desktop이 설치되어 있는가?
Docker Desktop이 실행 중인가?
Windows에서 WSL 관련 설정이 필요한가?
```

## 컨테이너가 안 보일 때

```powershell
docker ps
docker ps -a
```

`docker ps`는 실행 중인 컨테이너만 보여 줍니다. 종료된 컨테이너까지 보려면 `docker ps -a`를 사용합니다.

## 포트가 이미 사용 중일 때

이미 같은 포트를 쓰는 서버가 켜져 있을 수 있습니다.

```powershell
docker ps
```

필요하면 기존 컨테이너를 중지합니다.

```powershell
docker stop 컨테이너이름
```

## Docker Compose 오류

Docker Compose는 07 과정에서 다룹니다. 05 과정에서는 여러 서비스를 한 번에 운영하기보다, `docker run`으로 필요한 컨테이너를 하나씩 실행하는 감각을 먼저 익힙니다.
