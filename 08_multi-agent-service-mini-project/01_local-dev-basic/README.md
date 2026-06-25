# 01_local-dev-basic

이 폴더는 `08_multi-agent-service-mini-project`를 시작하기 전에 로컬 실행 환경을 확인하는 단계입니다.

08 과정은 Docker Compose로 여러 서비스를 동시에 실행합니다. 프로젝트 코드를 수정하기 전에 Docker Desktop, Docker Compose, Health Check 확인 흐름을 먼저 익히는 것이 중요합니다.

## 학습 목표

- Docker Desktop이 정상 실행되는지 확인합니다.
- `docker compose config`로 Compose 설정을 검증합니다.
- backend `/health` 같은 Health Check의 의미를 이해합니다.
- 컨테이너 상태와 로그를 확인하는 기본 명령을 익힙니다.

## 진행 순서

1. [01_docker-env-check](./01_docker-env-check/README.md)
2. [02_docker-compose-check](./02_docker-compose-check/README.md)
3. [03_service-health-check](./03_service-health-check/README.md)

## 전체 흐름

```text
Docker Desktop 실행
-> docker --version 확인
-> docker compose version 확인
-> docker ps 확인
-> docker compose config 확인
-> docker compose up --build 실행
-> /health 확인
-> docker compose logs 확인
-> docker compose down 종료
```

## 자주 사용하는 명령

```powershell
docker --version
docker compose version
docker ps
docker compose config
docker compose up --build
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose down
```

처음에는 명령을 외우는 것보다 “지금 무엇을 확인하는 명령인지”를 이해하는 것이 더 중요합니다.
