# 02 Service Deployment and Automation

이 단원은 AI 서비스를 로컬 Python 실행에서 Docker 기반 실행으로 옮기고, 여러 서비스를 Docker Compose로 묶어 실행하는 방법을 학습합니다.

06 과정에서는 Supabase가 아니라 Docker 기반 운영 흐름을 사용합니다. 따라서 이 단원은 이후 Auto Healing, 모니터링, 운영 대시보드, AWS 배포의 기반이 됩니다.

## 이 단원의 목표

- Docker Desktop 설치와 실행 상태를 확인할 수 있다.
- Python AI 서비스를 Docker 이미지로 패키징할 수 있다.
- Docker Compose로 backend, frontend, worker, monitor 같은 여러 서비스를 함께 실행할 수 있다.
- Health Check와 Runtime 상태 확인의 의미를 이해한다.
- GitHub Actions 기반 CI/CD 흐름을 이해한다.
- AWS 배포 전에 어떤 환경 변수, 포트, 로그, 헬스체크가 필요한지 정리할 수 있다.

## 학습 순서

```text
01_ch1_docker-service-packaging
-> 02_ch2_docker-compose-multi-service
-> 03_ch3_service-health-and-runtime
-> 04_ch4_github-actions-cicd
-> 05_ch5_aws-deployment-basic
-> 10_labs
-> 20_assignments
```

## 필수 환경

- Windows 10/11
- Docker Desktop
- Python 3.11 이상
- VS Code 또는 Cursor
- PowerShell

## Docker Desktop 확인

PowerShell에서 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 먼저 확인합니다.

## Docker와.venv의 차이

`.venv`는 내 컴퓨터에서 Python 패키지를 분리하는 환경입니다.

Docker는 애플리케이션 실행 환경 전체를 이미지로 묶습니다.

```text
.venv: 내 PC의 Python 실습 환경
Docker: 어디서나 같은 방식으로 실행할 수 있는 서비스 환경
Docker Compose: 여러 Docker 서비스를 한 번에 실행하는 구성 파일
```

## 이 단원의 실습 기준

처음에는 `.venv`에서 Python 파일을 실행해 동작을 확인합니다.
그다음 같은 코드를 Docker 이미지로 만들고, 마지막에는 Docker Compose로 여러 서비스를 함께 실행합니다.

## 포트 기준

| 포트 | 용도 |
| --- | --- |
| 8000 | FastAPI backend |
| 8801 | Streamlit frontend |
| 8802 | Streamlit monitor |

## 실행 흐름 요약

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item.env.example.env
docker compose up --build
```

확인 주소:

```text
Backend: http://127.0.0.1:8000/health
Frontend: http://127.0.0.1:8801
Monitor: http://127.0.0.1:8802
```

## AWS와 어떻게 연결되는가?

Docker Compose는 로컬에서 여러 서비스를 함께 실행하는 연습입니다.
AWS에서는 같은 개념이 아래 서비스로 확장될 수 있습니다.

```text
Docker image -> Amazon ECR
Container service -> ECS 또는 EC2
Environment variables -> ECS Task Definition 또는 Parameter Store
Logs -> CloudWatch Logs
Health check -> Load Balancer 또는 ECS Health Check
CI/CD -> GitHub Actions에서 build/push/deploy
```

이 단원에서는 AWS를 바로 깊게 쓰기보다, AWS 배포 전에 필요한 Docker 실행 구조를 먼저 완성합니다.
