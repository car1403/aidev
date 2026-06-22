# Multi-Agent Service Team Template

Docker Compose 기반 Auto Healing Multi-Agent 서비스 팀 프로젝트 템플릿입니다.

이번 팀 프로젝트의 기준 주제는 **에러 자가 치유(Auto Healing) 워크플로우**입니다. 이 템플릿은 `06_multi-agent-service-ops`에서 배운 Multi-Agent 협업, Docker Compose, 장애 복구, 파이프라인, 운영 알림 구조를 팀 프로젝트로 구현하기 위한 시작점입니다.

## 프로젝트 진행 방향

```text
1. 에이전트 협업 시나리오 및 구조 설계
2. 장애 유형별 복구 로직 및 자동화 파이프라인 구현
3. 협업 기반 실행 흐름 통합 구현
4. 서비스 배포 및 결과 검증
```

## 서비스 구성

```text
backend FastAPI API 서버, Health Check, Auto Healing 요청 처리
frontend Streamlit 사용자 화면
worker 백그라운드 장애 감지와 복구 작업
monitor 운영 상태와 이벤트 확인 화면
```

## 필수 산출물

| 산출물 | 파일 |
| --- | --- |
| 멀티 에이전트 아키텍처 설계서 | `docs/multi-agent-architecture.md` |
| 배포 및 장애 복구 보고서 | `docs/deployment-recovery-report.md` |
| 파이프라인 구현 결과 보고서 | `docs/pipeline-result-report.md` |

## 실행 전 준비

Docker Desktop이 실행 중인지 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

## 실행

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
Copy-Item.env.example.env
docker compose config
docker compose up --build
```

## 확인 주소

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
```

## 로그 확인

다른 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간 worker 로그:

```powershell
docker compose logs -f worker
```

## 종료

```powershell
docker compose down
```

## 팀에서 수정할 주요 파일

```text
backend/main.py Health Check, 장애 이벤트 API
worker/main.py 장애 감지, Retry, Restart, Fallback 로직
frontend/app.py 사용자 입력과 실행 결과 화면
monitor/app.py 운영 이벤트와 상태 대시보드
docker-compose.yml 서비스 구성, 포트, healthcheck
docs/test-checklist.md 테스트 체크리스트
```

## 필수 구현 기준

- Docker Compose로 서비스 3개 이상 실행
- backend `/health` 정상 응답
- 장애 유형 3개 이상
- 복구 전략 2개 이상
- Agent 역할 4개 이상
- Agent 간 Handoff/Context 설계
- Feedback Loop 기반 결과 검증
- Auto Healing 요청 실행 흐름
- worker 또는 monitor 로그 확인
- 감사 로그 또는 정책 위반 추적 항목
- 멀티 에이전트 아키텍처 설계서
- 배포 및 장애 복구 보고서
- 파이프라인 구현 결과 보고서

## 선택 구현 기준

- GitHub Actions Docker build check
- AWS 배포 체크리스트
- Guardrail 또는 위험 명령 제한
- MCP/Tool 연결 설계
- LangSmith식 trace/run/span 추적 계획
- 보안 Runbook
- Guardrails AI 통합 검증 설계
- CloudWatch 로그 설계
- 비용/보안 주의 사항 정리

## GitHub Actions

예시 workflow의 권장 위치는 아래와 같습니다.

```text
.github/workflows/docker-compose-check.yml
```

실제 GitHub 저장소에서 자동 실행하려면 이 파일이 저장소 최상위 `.github/workflows` 아래에 있어야 합니다.

현재 workflow 목표:

```text
Python 문법 검사
docker compose config 검증
Docker image build 검증
```

## AWS 배포 체크리스트

실제 AWS 배포는 필수가 아닙니다. 다만 팀 문서에는 아래 내용을 정리하는 것을 권장합니다.

```text
ECR image 저장 전략
App Runner 또는 ECS 중 배포 후보 선택
환경변수와 secret 관리 방식
/health 기반 Health Check
CloudWatch Logs 확인 방식
실습 후 삭제할 리소스 목록
```
