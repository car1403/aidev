# 02_instructor-sample-project

이 폴더는 07 미니 프로젝트의 기준 샘플입니다.

backend, frontend, worker, monitor가 Docker Compose로 함께 실행되는 구조를 먼저 확인한 뒤, 99 팀 프로젝트 템플릿에서 같은 구조를 확장합니다.

## 서비스 구성

| 서비스 | 역할 | 확인 방법 |
| --- | --- | --- |
| backend | Health Check, 장애 이벤트 API, 복구 결과 API | `http://127.0.0.1:8000/health` |
| frontend | 장애 이벤트 입력과 결과 확인 화면 | `http://127.0.0.1:8801` |
| worker | 장애 분석과 복구 전략 선택 작업 | `docker compose logs worker` |
| monitor | 운영 이벤트와 서비스 상태 대시보드 | `http://127.0.0.1:8802` |

## 실행 순서

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

## 확인 주소

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

## 로그 확인

다른 PowerShell을 열고 아래 명령을 실행합니다.

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

worker 로그를 실시간으로 보려면 아래 명령을 사용합니다.

```powershell
docker compose logs -f worker
```

## 종료

```powershell
docker compose down
```

## 샘플에서 확인할 핵심

- Compose 하나로 여러 서비스가 함께 실행되는가?
- backend `/health`가 정상 응답하는가?
- frontend가 backend와 연결되는가?
- worker가 장애 이벤트를 처리하는 흐름을 로그로 남기는가?
- monitor가 상태와 이벤트를 화면에 표시하는가?
- 이 구조를 99 팀 프로젝트 템플릿으로 확장할 수 있는가?

## 팀 프로젝트로 확장할 때

샘플 프로젝트를 그대로 제출물로 사용하지 않습니다. 샘플은 구조를 이해하기 위한 기준 예제입니다.

최종 프로젝트는 아래 템플릿을 복사해서 진행합니다.

```text
99_team-projects/multi-agent-service-team-template
```
