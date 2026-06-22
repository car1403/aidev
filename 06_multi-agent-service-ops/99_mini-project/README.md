# 99 Mini Project

06 과정에서 학습한 Multi-Agent 협업, Docker Compose, AI 보안/가드레일, Auto Healing, Observability를 통합하는 미니 프로젝트입니다.

## 프로젝트 주제

```text
Auto Healing Multi-Agent Service
```

## 구성

```text
99_mini-project
├─ sample-auto-healing-agent
└─ team-template
```

## 진행 순서

1. `sample-auto-healing-agent`를 Docker Compose로 실행합니다.
2. backend, frontend, worker, monitor 역할을 확인합니다.
3. Auto Healing 요청과 이벤트 이력을 확인합니다.
4. `team-template`을 복사해 팀 프로젝트를 시작합니다.
5. 팀별 장애 시나리오, 보안 정책, 운영 대시보드를 확장합니다.

## 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\99_mini-project\sample-auto-healing-agent
Copy-Item.env.example.env
docker compose up --build
```

## 확인 주소

```text
Backend: http://127.0.0.1:8000/health
Frontend: http://127.0.0.1:8801
Monitor: http://127.0.0.1:8802
```
