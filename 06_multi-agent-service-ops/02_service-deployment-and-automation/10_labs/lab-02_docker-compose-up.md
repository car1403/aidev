# Lab 02. Docker Compose Up

## 목표

backend, frontend, worker, monitor 서비스를 Docker Compose로 함께 실행합니다.

## 실습

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item .env.example .env
docker compose up --build
```

## 확인

- Backend: http://127.0.0.1:8000/health
- Frontend: http://127.0.0.1:8801
- Monitor: http://127.0.0.1:8802
