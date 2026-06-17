# Lab 03. Health Check and Logs

## 목표

서비스 상태와 로그를 확인합니다.

## 실습

```powershell
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

## 확인 질문

- 어떤 서비스가 가장 먼저 실행되어야 하는가?
- backend가 죽으면 frontend와 monitor에는 어떤 영향이 있는가?
- Health Check는 왜 필요한가?
