# 07_multi-agent-service-ops

`07_multi-agent-service-ops`는 05~06에서 만든 Agent 코드를 서비스처럼 실행하고 운영하는 방법을 배우는 과정입니다. Docker Compose, Health Check, GitHub Actions, AWS 배포 설계, 보안 가드레일, 관측성(Observability), Auto Healing 흐름을 단계적으로 다룹니다.

## 핵심 기준

- Docker Compose는 이 과정의 핵심 실행 도구입니다.
- AWS 실제 배포는 비용이 발생할 수 있으므로 선택 실습입니다.
- GitHub Actions는 자동 배포보다 먼저 문법 검사, compose 검증, 이미지 빌드 검증에 초점을 둡니다.
- LangSmith 같은 외부 관측 도구는 선택 확장으로 두고, 기본은 로컬 로그와 Mock trace로 이해합니다.

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
