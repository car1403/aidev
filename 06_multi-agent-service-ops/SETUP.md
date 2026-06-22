# SETUP

`06_multi-agent-service-ops` 실행 환경 설정 문서입니다.

06 과정은 04, 05에서 만든 Agent 코드를 “서비스처럼 실행하고 운영하는 방법”을 배우는 과정입니다. 따라서 Python 가상환경뿐 아니라 Docker Desktop, Docker Compose, Git, GitHub Actions, AWS 배포 준비까지 순서대로 확인합니다.

## 1. 이 과정에서 사용하는 도구

```text
Python.venv 로컬에서 실습 코드 실행
Dockerfile Python 서비스를 Docker image로 패키징
Docker Compose backend, frontend, worker, monitor를 함께 실행
Git 코드 변경 이력 관리
GitHub Actions push/pull request 시 자동 build 검증
AWS Docker image를 클라우드 서비스로 배포하는 흐름 이해
```

04, 05에서는 Docker를 선택적으로 사용했지만, 06에서는 Docker와 Docker Compose가 핵심 실습 도구입니다.

## 2. 작업 위치

```powershell
cd C:\aidev\06_multi-agent-service-ops
```

## 3. Python 가상환경 준비

이미 `.venv`가 있다면 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

처음이라면 아래 순서로 만듭니다.

```powershell
python -m venv.venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

## 4. 환경변수 파일 준비

```powershell
Copy-Item.env.example.env
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
backend FastAPI API 서버
frontend Streamlit 사용자 화면
worker 백그라운드 Agent 작업
monitor 운영 상태 대시보드
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
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_ch1_docker-service-packaging
docker build -t aidev-agent-backend:local.
docker run --rm -p 8000:8000 aidev-agent-backend:local
```

다른 PowerShell에서 확인합니다.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

실행 중인 PowerShell에서 `Ctrl + C`를 누르면 종료됩니다.

## 8. Docker Compose 멀티 서비스 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item.env.example.env
docker compose config
docker compose up --build
```

브라우저 또는 PowerShell에서 확인합니다.

```text
Backend health : http://127.0.0.1:8000/health
Frontend : http://127.0.0.1:8801
Monitor : http://127.0.0.1:8802
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
git add 06_multi-agent-service-ops
git commit -m "docs: update service ops course"
git push
```

## 10. GitHub Actions 준비

실습 workflow 예시는 아래 위치에 있습니다.

```text
02_service-deployment-and-automation/04_ch4_github-actions-cicd/.github/workflows/docker-build-check.yml
```

GitHub에서 자동 실행하려면 저장소 기준으로 `.github/workflows` 아래에 workflow 파일이 있어야 합니다.

예시:

```text
C:\aidev\.github\workflows\docker-build-check.yml
```

06 과정만 별도 GitHub 저장소로 운영한다면 아래 위치도 가능합니다.

```text
C:\aidev\06_multi-agent-service-ops\.github\workflows\docker-build-check.yml
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

AWS 실습은 비용이 발생할 수 있으므로 수업 안내에 따라 진행합니다.

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

```text
ECR Docker image 저장소
ECS 컨테이너 실행/관리 서비스
App Runner 컨테이너 앱을 비교적 간단히 배포하는 서비스
CloudWatch 로그와 지표 확인
IAM 권한 관리
Secrets Manager 비밀 값 관리
Parameter Store 설정 값 관리
```

## 12. 비용과 보안 주의

- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- 실습 후 App Runner, ECS Service, Load Balancer, ECR image, CloudWatch Log Group을 정리합니다.
- AWS Access Key는 코드, README, 발표 자료, GitHub Actions 로그에 노출하지 않습니다.
- GitHub Actions에서 AWS에 접근할 때는 장기 Access Key보다 OIDC 기반 인증을 권장합니다. 이 과정에서는 먼저 개념을 이해하고, 실제 적용은 수업 안내에 따릅니다.
- `.env`, `.venv`, 로그 파일, 개인 키 파일은 커밋하지 않습니다.

## 13. 첫 수업 추천 진행 순서

```text
1. Python.venv 활성화
2. requirements.txt 설치
3. Docker Desktop 실행
4. docker compose version 확인
5. 단일 Docker service build/run
6. /health 확인
7. Docker Compose multi-service up
8. compose ps/logs/down 확인
9. Git 상태 확인
10. GitHub Actions workflow 위치 이해
11. AWS 배포 흐름과 비용/보안 주의 확인
```

## 14. 오류가 날 때 먼저 볼 것

```text
Docker 오류:
- Docker Desktop이 실행 중인가?
- docker ps가 동작하는가?
- docker compose version이 동작하는가?
- 포트 8000, 8801, 8802가 이미 사용 중인가?

Compose 오류:
- 현재 폴더에 docker-compose.yml이 있는가?
-.env 파일이 있는가?
- docker compose config가 통과하는가?
- build context가 맞는가?

GitHub Actions 오류:
- workflow 파일이.github/workflows 아래에 있는가?
- YAML 들여쓰기가 맞는가?
- branch 조건이 현재 branch와 맞는가?
- secrets를 코드에 직접 적지 않았는가?

AWS 오류:
- region이 맞는가?
- IAM 권한이 충분한가?
- ECR image URI가 맞는가?
- container port와 health check path가 맞는가?
- CloudWatch Logs에 오류가 있는가?
```
