# 02 Service Deployment And Automation

이 단원은 AI 서비스를 로컬 Python 실행에서 Docker 기반 실행으로 옮기고, 여러 서비스를 Docker Compose로 묶어 실행하는 방법을 학습합니다.

06 과정에서는 Supabase가 아니라 Docker 기반 운영 흐름을 사용합니다. 이 단원에서 익힌 Docker Compose 구조가 이후 Auto Healing, 모니터링, 운영 대시보드, AWS 배포의 기반이 됩니다.

## 학습 목표

- Docker Desktop 실행 상태를 확인합니다.
- Python AI 서비스를 Docker image로 패키징합니다.
- Docker Compose로 backend, frontend, worker, monitor를 함께 실행합니다.
- Health Check와 runtime 로그를 확인합니다.
- GitHub Actions 기반 자동 검증 흐름을 이해합니다.
- AWS 배포 전에 필요한 image, port, env, health check, log 관계를 정리합니다.

## 폴더 구조

```text
02_service-deployment-and-automation
├─ 01_docker-service-packaging
├─ 02_docker-compose-multi-service
├─ 03_service-health-and-runtime
├─ 04_github-actions-cicd
├─ 05_aws-deployment-basic
├─ 10_labs
└─ 20_assignments
```

## 진행 흐름

```text
Docker Desktop 확인
-> 단일 backend image build/run
-> /health 확인
-> Docker Compose config 확인
-> backend/frontend/worker/monitor 동시 실행
-> logs와 ps 확인
-> GitHub Actions로 자동 build 검증
-> AWS 배포 구조 이해
```

## 실행 준비

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
docker --version
docker compose version
```

## 단일 서비스 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Compose 서비스 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

확인:

```powershell
docker compose ps
docker compose logs backend
docker compose logs worker
```

종료:

```powershell
docker compose down
```

## AWS 연결 관점

Docker Compose는 로컬에서 여러 서비스를 함께 실행하는 연습입니다. AWS에서는 같은 개념이 아래 서비스로 확장됩니다.

```text
Docker image -> ECR
Container 실행 -> App Runner 또는 ECS
Service log -> CloudWatch
Secret/env -> Secrets Manager 또는 Parameter Store
권한 -> IAM
```

처음에는 AWS 배포를 필수로 진행하기보다, 로컬 Docker Compose가 안정적으로 동작하는 것을 먼저 확인합니다.
