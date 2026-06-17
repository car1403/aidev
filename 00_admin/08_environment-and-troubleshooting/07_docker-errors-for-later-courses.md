# 07. Docker Errors For Later Courses

Docker는 04 과정부터 사용하고, Docker Compose는 06 과정에서 본격적으로 다룹니다.

## docker 명령이 안 될 때

```powershell
docker --version
docker ps
```

확인:

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

## 포트 충돌

이미 같은 포트를 사용하는 프로그램이 있을 수 있습니다.

해결:

```text
기존 컨테이너 중지
다른 포트 사용
```
