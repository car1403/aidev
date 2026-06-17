# 03_ch3_service-health-and-runtime

서비스 실행 상태, Health Check, Runtime 로그 확인 방법을 학습합니다.

## Health Check란?

Health Check는 서비스가 살아 있는지 확인하는 약속된 점검 방식입니다.

예시:

```text
GET /health -> {"status": "ok"}
```

Docker Compose에서는 `healthcheck` 설정으로 컨테이너 상태를 확인할 수 있습니다.

## 자주 쓰는 Docker 명령

```powershell
docker ps
docker compose ps
docker compose logs backend
docker compose logs -f backend
docker stats
```

## 운영에서 확인할 것

- 컨테이너가 실행 중인가?
- 포트가 열려 있는가?
- `/health` 응답이 정상인가?
- 로그에 반복 오류가 있는가?
- worker가 너무 자주 재시작되고 있지 않은가?

## AWS와 연결

AWS ECS나 Load Balancer에서도 Health Check가 중요합니다.

```text
Docker Compose healthcheck
-> ECS container health check
-> Load Balancer target health check
-> CloudWatch alarm
```
