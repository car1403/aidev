# 02. Environment Checklist

06 과정을 시작하기 전에 아래 환경을 확인합니다.

## Python 확인

```powershell
python --version
```

가상환경:

```powershell
cd C:\aidev\06_multi-agent-service-ops
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## Docker 확인

Docker Desktop을 실행한 뒤 확인합니다.

```powershell
docker --version
docker compose version
docker ps
docker run hello-world
```

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 먼저 확인합니다.

## Docker Compose 확인

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
```

`docker compose config`가 성공하면 `docker-compose.yml` 문법과 `.env` 연결이 기본적으로 정상입니다.

## Git 확인

```powershell
git --version
git config --global user.name
git config --global user.email
```

아직 설정하지 않았다면:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## AWS 확인

AWS 실습은 선택입니다. 실제 배포 전에 비용과 리소스 정리 방법을 확인합니다.

```powershell
aws --version
aws sts get-caller-identity
```

## 자주 쓰는 포트

| Port | 용도 |
| --- | --- |
| 8000 | FastAPI backend |
| 8801 | Streamlit frontend |
| 8802 | monitor dashboard |
| 8803 | observability dashboard |

포트 충돌이 나면 기존 서버나 컨테이너를 종료합니다.

```powershell
docker ps
docker stop <container_id>
```
