# 07_multi-agent-service-ops

`07_multi-agent-service-ops`는 05~06에서 만든 Agent 코드를 서비스처럼 실행하고 운영하는 방법을 배우는 과정입니다. Docker Compose, Health Check, GitHub Actions, AWS 배포 설계, 보안 가드레일, 관측성(Observability), Auto Healing 흐름을 단계적으로 다룹니다.

## 핵심 기준

- Docker Compose는 이 과정의 핵심 실행 도구입니다.
- AWS 실제 배포는 비용이 발생할 수 있으므로 선택 실습입니다.
- GitHub Actions는 자동 배포보다 먼저 문법 검사, compose 검증, 이미지 빌드 검증에 초점을 둡니다.
- LangSmith 같은 외부 관측 도구는 선택 확장으로 두고, 기본은 로컬 로그와 Mock trace로 이해합니다.

## 수강생 진행 기준

- 필수: 역할 기반 Multi-Agent 설계, Docker Compose 구성, Health Check, 재시도/복구 흐름, 로그와 운영 대시보드 구조를 실습합니다.
- 선택: AWS 실제 배포, LangSmith 외부 관측 도구, 고급 보안 자동화는 비용과 진도에 따라 다룹니다.
- 다음 과정으로 넘어가기 전: 여러 서비스가 Compose로 함께 실행되는 구조와 장애 발생 시 감지, 복구, 검증 흐름을 설명할 수 있어야 합니다.

## 막혔을 때 바로 보기

| 막히는 지점 | 확인 문서 |
| --- | --- |
| Docker Compose 실행, 포트 충돌, `.env` 위치 | [Docker 오류 해결](../00_course-guide/08_environment-and-troubleshooting/07_docker-errors-for-later-courses.md), [SETUP.md](./SETUP.md) |
| `docker compose config` 또는 `up` 실패 | [Docker Compose multi service](./02_service-deployment-and-automation/02_docker-compose-multi-service/README.md), [compose up lab](./02_service-deployment-and-automation/10_labs/lab-02_docker-compose-up.md) |
| GitHub Actions가 실패함 | [GitHub Actions Docker build](./02_service-deployment-and-automation/10_labs/lab-04_github-actions-docker-build.md), [SETUP.md](./SETUP.md) |
| AWS 선택 실습의 비용 리스크 | [AWS deployment checklist](./02_service-deployment-and-automation/10_labs/lab-05_aws-deployment-checklist.md), [optional AWS deployment](./02_service-deployment-and-automation/10_labs/lab-06_aws-apprunner-ecs-optional-deployment.md) |

## 과정 구조

```text
07_multi-agent-service-ops
├─ README.md
├─ SETUP.md
├─ .env.example
├─ requirements.txt
├─ 00_references
├─ 01_multi-agent-collaboration
├─ 02_service-deployment-and-automation
├─ 03_ai-security-and-guardrails
├─ 04_auto-healing-workflow
├─ 05_observability-and-ops-dashboard
└─ 99_mini-project
```

## 권장 진행 순서

1. [SETUP.md](./SETUP.md)를 보고 Python `.venv`, Docker Desktop, Docker Compose를 확인합니다.
2. [00_references](./00_references/README.md)에서 운영형 Agent 서비스의 큰 그림을 확인합니다.
3. [01_multi-agent-collaboration](./01_multi-agent-collaboration/README.md)에서 역할 기반 Agent 협업을 설계합니다.
4. [02_service-deployment-and-automation](./02_service-deployment-and-automation/README.md)에서 Docker와 GitHub Actions 흐름을 익힙니다.
5. [03_ai-security-and-guardrails](./03_ai-security-and-guardrails/README.md)에서 정책, 권한, 안전 장치를 정리합니다.
6. [04_auto-healing-workflow](./04_auto-healing-workflow/README.md)에서 장애 감지와 복구 전략을 설계합니다.
7. [05_observability-and-ops-dashboard](./05_observability-and-ops-dashboard/README.md)에서 로그, trace, 운영 대시보드 흐름을 확인합니다.
8. [99_mini-project](./99_mini-project/README.md)에서 운영형 미니 프로젝트로 정리합니다.

## 빠른 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

VS Code에서 `C:\aidev\07_multi-agent-service-ops` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다.
