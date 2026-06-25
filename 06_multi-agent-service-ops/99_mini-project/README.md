# 99 Mini Project

이 폴더는 06 과정에서 학습한 Multi-Agent 협업, Docker Compose, AI 보안/가드레일, Auto Healing, Observability를 통합하는 미니 프로젝트입니다.

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

| 폴더 | 역할 |
| --- | --- |
| `sample-auto-healing-agent` | 완성된 샘플을 실행해 전체 구조를 먼저 확인합니다. |
| `team-template` | 팀별 프로젝트를 시작할 때 복사해서 사용합니다. |

## 진행 순서

1. `sample-auto-healing-agent`를 Docker Compose로 실행합니다.
2. backend, frontend, worker, monitor 역할을 확인합니다.
3. Auto Healing 요청과 이벤트 이력을 확인합니다.
4. `team-template`을 복사해 팀 프로젝트를 시작합니다.
5. 팀별 장애 시나리오, 보안 정책, 운영 대시보드를 확장합니다.

## 샘플 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\99_mini-project\sample-auto-healing-agent
Copy-Item .env.example .env
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

종료:

```powershell
docker compose down
```

## 팀 프로젝트 시작

```powershell
cd C:\aidev\06_multi-agent-service-ops\99_mini-project
Copy-Item .\team-template .\team-01-auto-healing-agent -Recurse
cd .\team-01-auto-healing-agent
Copy-Item .env.example .env
docker compose up --build
```

## 필수 산출물

- Multi-Agent 아키텍처 설계서
- Docker Compose 실행 결과
- 장애 유형별 복구 보고서
- 보안/가드레일 점검표
- 로그/모니터링 대시보드 결과
- GitHub Actions 실행 결과 또는 검증 계획
- AWS 배포 체크리스트
- 최종 발표 문서
