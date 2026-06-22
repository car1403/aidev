# Lab 01. Docker Build and Run

## 목표

FastAPI 서비스를 Docker 이미지로 만들고 컨테이너로 실행합니다.

## 실습

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_ch1_docker-service-packaging
docker build -t ai-service-packaging-demo.
docker run --rm -p 8000:8000 ai-service-packaging-demo
```

## 확인

```text
http://127.0.0.1:8000/health
```
