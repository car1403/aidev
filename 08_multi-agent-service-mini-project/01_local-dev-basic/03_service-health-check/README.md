# 03_service-health-check

서비스가 정상 실행 중인지 확인하는 Health Check 실습입니다.

## 1. 샘플 프로젝트 실행

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
docker compose up --build
```

## 2. backend Health Check 확인

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8000/health
```

정상이라면 JSON 응답이 보입니다.

```json
{
  "status": "ok"
}
```

Health Check는 운영에서 매우 중요합니다. 서비스가 살아 있는지, 배포 후 정상 동작하는지, Auto Healing 이후 복구되었는지 판단하는 기준으로 사용합니다.

## 3. 화면 확인

```text
Frontend : http://127.0.0.1:8801
Monitor  : http://127.0.0.1:8802
```

frontend는 장애 이벤트를 입력하고 결과를 확인하는 화면입니다. monitor는 운영 로그와 서비스 상태를 확인하는 화면입니다.

## 4. 로그 확인

다른 PowerShell을 열어 실행합니다.

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간으로 worker 로그를 보려면 아래 명령을 사용합니다.

```powershell
docker compose logs -f worker
```

## 5. 확인 기준

- backend `/health`가 정상 응답하는가?
- frontend 화면이 열리는가?
- monitor 화면이 열리는가?
- worker 로그가 출력되는가?
- 오류가 발생했을 때 어떤 서비스 로그를 봐야 하는지 알 수 있는가?
