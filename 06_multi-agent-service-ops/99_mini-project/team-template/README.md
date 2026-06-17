# Team Template

Docker Compose 기반 Auto Healing Multi-Agent 서비스입니다.

## 서비스 구성

- ackend: FastAPI API 서버, Agent 실행 상태 제공
- rontend: Streamlit 사용자 화면
- worker: Auto Healing 작업 실행기
- monitor: 운영 상태와 이벤트 확인 화면

## 실행

``powershell
cd C:\aidev\06_multi-agent-service-ops\99_mini-project\team-template
Copy-Item .env.example .env
docker compose up --build
``

## 확인 주소

``text
Backend: http://127.0.0.1:8000/health
Frontend: http://127.0.0.1:8801
Monitor: http://127.0.0.1:8802
``

## 종료

``powershell
docker compose down
``
