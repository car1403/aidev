# 04 Docker Compose and Service Ops

Docker Compose는 여러 컨테이너 서비스를 하나의 파일로 실행하는 도구입니다.

06 과정에서는 Docker Compose를 서비스 운영 구조 학습의 핵심 도구로 사용합니다.

## Docker와 Docker Compose 차이

```text
Docker: 컨테이너 하나를 빌드하고 실행
Docker Compose: 여러 컨테이너를 하나의 서비스 묶음으로 실행
```

## 06 과정의 Compose 예시

```text
backend
frontend
worker
monitor
```

## 기본 실행 흐름

```powershell
Copy-Item.env.example.env
docker compose config
docker compose up --build
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

## 상태 확인

```powershell
docker compose ps
docker ps
docker stats
```

## 운영 관점에서 중요한 것

- 컨테이너가 실행 중인가?
- Health Check가 통과하는가?
- 로그에 오류가 반복되는가?
- 포트가 충돌하지 않는가?
- 환경 변수가 올바르게 들어갔는가?
