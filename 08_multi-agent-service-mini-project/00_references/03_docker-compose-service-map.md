# 03. Docker Compose Service Map

07 프로젝트는 Docker Compose로 여러 서비스를 함께 실행합니다.

## 기본 서비스 구조

```text
docker-compose.yml
├─ backend  : FastAPI API 서버
├─ frontend : Streamlit 사용자 화면
├─ worker   : 장애 감지와 복구 작업
└─ monitor  : 운영 상태와 로그 대시보드
```

## 포트 기준

| 서비스 | 내부 포트 | 외부 포트 | 확인 주소 |
| --- | --- | --- | --- |
| backend | 8000 | 8000 | `http://127.0.0.1:8000/health` |
| frontend | 8501 | 8801 | `http://127.0.0.1:8801` |
| monitor | 8501 | 8802 | `http://127.0.0.1:8802` |
| worker | 없음 | 없음 | `docker compose logs worker` |

## 실행 순서

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

`docker compose config`는 실제 실행 전에 Compose 문법과 환경변수 연결이 맞는지 확인하는 명령입니다. 실행 전에 반드시 확인하는 습관을 들이는 것이 좋습니다.

## 로그 확인

```powershell
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
docker compose logs -f worker
```

## 종료

```powershell
docker compose down
```

## 설계할 때 확인할 것

- 서비스 이름이 명확한가?
- 환경변수는 `.env`에서 관리되는가?
- API 주소는 컨테이너 내부 통신 기준과 브라우저 접속 기준을 구분했는가?
- Health Check 주소가 정해져 있는가?
- worker가 실패했을 때 로그로 원인을 확인할 수 있는가?
- monitor가 운영 이벤트를 보여주는가?
