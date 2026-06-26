# SETUP

`07_multi-agent-service-ops` 실행 환경 설정 문서입니다.

07 과정은 05, 06에서 만든 Agent 코드를 **서비스처럼 실행하고 운영하는 방법**을 배우는 과정입니다. 따라서 Python 가상환경뿐 아니라 Docker Desktop, Docker Compose, Git, GitHub Actions, AWS 배포 준비까지 순서대로 확인합니다.

## 1. 이 과정에서 사용하는 도구

| 도구 | 사용하는 이유 |
| --- | --- |
| Python `.venv` | 로컬에서 예제 Python 파일을 실행합니다. |
| Dockerfile | Python 서비스를 Docker image로 패키징합니다. |
| Docker Compose | backend, frontend, worker, monitor를 함께 실행합니다. |
| Git | 코드 변경 이력을 관리합니다. |
| GitHub Actions | push/pull request 시 자동 build와 기본 검증을 실행합니다. |
| AWS | Docker image를 클라우드 서비스로 배포하는 흐름을 이해합니다. |

05, 06에서는 Docker를 선택적으로 사용했지만, 07에서는 Docker와 Docker Compose가 핵심 실습 도구입니다.

## 2. 작업 위치

```powershell
cd C:\aidev\07_multi-agent-service-ops
```

## 3. Python 가상환경 준비

이미 `.venv`가 있다면 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

활성화 후 현재 Python이 이 과정의 `.venv`를 사용하는지 확인합니다.

```powershell
echo $env:VIRTUAL_ENV
python -c "import sys; print(sys.executable)"
```

정상이라면 아래 경로를 가리켜야 합니다.

```text
C:\aidev\07_multi-agent-service-ops\.venv
C:\aidev\07_multi-agent-service-ops\.venv\Scripts\python.exe
```

처음이라면 아래 순서로 만듭니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python --version
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

VS Code에서 `C:\aidev\07_multi-agent-service-ops` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다. `C:\aidev` 루트를 열어 수업을 진행할 때는 새 터미널을 연 뒤 위 확인 명령으로 현재 Python 경로가 이 과정의 `.venv`를 가리키는지 먼저 확인합니다.

PowerShell에서 실행 정책 오류가 나면 아래 명령을 한 번 실행합니다.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 4. 환경변수 파일 준비

```powershell
Copy-Item .env.example .env
```

`.env`에는 실제 값을 넣습니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
API_BASE_URL=http://127.0.0.1:8000
```

주의:

- `.env`는 GitHub에 올리지 않습니다.
- `.env.example`에는 예시 값만 둡니다.
- API Key, AWS Access Key, 비밀번호는 코드와 README에 적지 않습니다.

## 5. Docker Desktop 확인

Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

처음 설치했다면 아래 테스트도 실행합니다.

```powershell
docker run hello-world
```

`hello-world`는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

## 6. Docker Compose 기본 개념

Docker Compose는 여러 컨테이너를 하나의 `docker-compose.yml` 파일로 함께 실행하는 도구입니다.

06의 기본 서비스 구성은 다음과 같습니다.

```text
backend  FastAPI API 서버
frontend Streamlit 사용자 화면
worker   백그라운드 Agent 작업
monitor  운영 상태 대시보드
```

자주 쓰는 명령:

```powershell
docker compose up --build
docker compose up --build -d
docker compose ps
docker compose logs backend
docker compose logs -f worker
docker compose down
docker compose config
```

`docker compose config`는 `docker-compose.yml` 문법과 최종 설정을 확인할 때 유용합니다.

## 7. 단일 Docker 서비스 실행

먼저 backend 하나만 Docker image로 만들고 실행합니다.

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\01_docker-service-packaging
docker build -t aidev-agent-backend:local .
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

실행 중인 PowerShell에서 `Ctrl + C`를 누르면 종료됩니다.

## 8. Docker Compose 멀티 서비스 실행

```powershell
cd C:\aidev\07_multi-agent-service-ops\02_service-deployment-and-automation\02_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

브라우저 또는 PowerShell에서 확인합니다.

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

종료:

```powershell
docker compose down
```

## 9. Git 확인

```powershell
git --version
```

처음 한 번 설정합니다.

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

기본 흐름:

```powershell
cd C:\aidev
git status
git add 07_multi-agent-service-ops
git commit -m "docs: update service ops course"
git push
```

## 10. GitHub Actions 준비

실습 workflow 예시는 아래 위치에 있습니다.

```text
02_service-deployment-and-automation/04_github-actions-cicd/.github/workflows/docker-build-check.yml
```

GitHub에서 자동 실행하려면 저장소 기준으로 `.github/workflows` 아래에 workflow 파일이 있어야 합니다.

예시:

```text
C:\aidev\.github\workflows\docker-build-check.yml
```

07 과정만 별도 GitHub 저장소로 운영한다면 아래 위치도 가능합니다.

```text
C:\aidev\07_multi-agent-service-ops\.github\workflows\docker-build-check.yml
```

처음에는 배포 자동화보다 아래 CI 흐름을 먼저 확인합니다.

```text
push 또는 pull request
-> GitHub Actions 실행
-> Python 문법 검사
-> Docker image build
-> 성공/실패 확인
```

## 11. AWS CLI와 배포 준비

AWS 실습은 비용이 발생할 수 있으므로 안내에 따라 진행합니다.

AWS CLI 확인:

```powershell
aws --version
aws configure
aws sts get-caller-identity
```

초보자 기준 AWS 배포 흐름:

```text
1. 로컬에서 Docker image build
2. 로컬에서 container 실행 확인
3. /health endpoint 확인
4. Docker image를 Amazon ECR에 push
5. App Runner 또는 ECS에서 image 실행
6. 환경변수와 port 설정
7. 외부 URL로 /health 확인
8. CloudWatch Logs 확인
9. 실습 후 리소스 정리
```

AWS에서 연결되는 주요 서비스:

| 서비스 | 역할 |
| --- | --- |
| ECR | Docker image 저장소 |
| ECS | 컨테이너 실행/관리 서비스 |
| App Runner | 컨테이너 앱을 비교적 간단히 배포하는 서비스 |
| CloudWatch | 로그와 지표 확인 |
| IAM | 권한 관리 |
| Secrets Manager | 비밀 값 관리 |
| Parameter Store | 설정 값 관리 |

## 12. 비용과 보안 주의

- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- 실습 후 App Runner, ECS Service, Load Balancer, ECR image, CloudWatch Log Group을 정리합니다.
- AWS Access Key는 코드, README, 발표 자료, GitHub Actions 로그에 노출하지 않습니다.
- GitHub Actions에서 AWS에 접근할 때는 장기 Access Key보다 OIDC 기반 인증을 권장합니다.
- `.env`, `.venv`, 로그 파일, 개인 키 파일은 커밋하지 않습니다.

## 13. 첫 실행 추천 순서

```text
1. .venv 활성화
2. pip install 확인
3. Docker Desktop 실행
4. docker run hello-world
5. 단일 backend Docker build/run
6. /health 확인
7. Docker Compose config 확인
8. Docker Compose up
9. backend/frontend/monitor 확인
10. logs 확인
11. docker compose down
```

## 14. 자주 막히는 지점

| 증상 | 확인할 것 |
| --- | --- |
| `docker` 명령을 찾을 수 없음 | Docker Desktop 설치와 재시작 여부 |
| `docker ps` 실패 | Docker Desktop 실행 여부 |
| `docker compose config` 실패 | `docker-compose.yml` 들여쓰기, `.env` 파일 존재 여부 |
| port already allocated | 기존 컨테이너나 서버가 같은 포트를 쓰고 있는지 확인 |
| API Key 오류 | `.env` 파일 위치와 변수명 확인 |
| AWS 비용 걱정 | 선택 실습으로 진행하고 실습 후 리소스 정리 |
