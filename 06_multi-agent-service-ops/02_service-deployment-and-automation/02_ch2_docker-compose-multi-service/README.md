# 02_ch2_docker-compose-multi-service

Docker Compose로 여러 서비스를 한 번에 실행하는 방법을 학습합니다.

## 왜 Docker Compose가 필요한가?

실제 AI 서비스는 하나의 Python 파일로만 끝나지 않습니다.

```text
backend: API 요청 처리
frontend: 사용자 화면
worker: 오래 걸리는 Agent 작업 처리
monitor: 서비스 상태 확인
```

Docker Compose는 이런 여러 컨테이너를 하나의 `docker-compose.yml`로 관리합니다.

## 실행 전 확인

```powershell
docker --version
docker compose version
docker ps
```

## 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

`docker compose config`는 실제 실행 전에 `docker-compose.yml`과 `.env` 설정이 올바른지 확인하는 명령입니다.

백그라운드에서 실행하려면 아래처럼 실행합니다.

```powershell
docker compose up --build -d
```

## 확인 주소

```text
Backend health: http://127.0.0.1:8000/health
Frontend: http://127.0.0.1:8801
Monitor: http://127.0.0.1:8802
```

## 종료

```powershell
docker compose down
```

## 로그 확인

```powershell
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간 로그를 보려면 `-f` 옵션을 사용합니다.

```powershell
docker compose logs -f backend
```

## 강의 중 확인 질문

- `docker build`와 `docker compose up --build`는 어떤 차이가 있는가?
- backend, frontend, worker, monitor는 각각 어떤 역할인가?
- `/health` endpoint가 없으면 운영에서 무엇이 어려워지는가?
- `docker compose down`을 하지 않으면 어떤 문제가 생길 수 있는가?
