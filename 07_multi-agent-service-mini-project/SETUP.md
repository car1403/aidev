# SETUP

`07_multi-agent-service-mini-project` 실행 환경 설정 안내입니다.

07 과정은 `06_multi-agent-service-ops`에서 배운 Docker Compose, Health Check, Auto Healing, Observability, GitHub Actions, AWS 배포 흐름을 팀 미니 프로젝트로 구현하는 단계입니다.

## 1. 작업 위치

```powershell
cd C:\aidev\07_multi-agent-service-mini-project
```

## 2. 이 과정에서 사용하는 도구

```text
Python .venv       보조 스크립트와 로컬 확인용
Dockerfile         프로젝트 서비스를 Docker image로 패키징
Docker Compose     backend, frontend, worker, monitor를 함께 실행
Git                팀 프로젝트 변경 이력 관리
GitHub Actions     Docker Compose 설정과 build 자동 검증
AWS                배포 체크리스트와 최종 확장 설계
```

07의 핵심 실행 방식은 Docker Compose입니다. Python `.venv`는 패키지 확인이나 보조 스크립트 실행에 사용하고, 실제 서비스는 Compose로 실행합니다.

## 3. Python 가상환경

이미 `.venv`가 있으면 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

처음이라면 아래 순서로 만듭니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

## 4. Docker Desktop 확인

Docker Desktop을 실행한 뒤 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

처음 설치한 수업 참여자는 기본 테스트 컨테이너도 실행합니다.

```powershell
docker run hello-world
```

`hello-world`는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

## 5. 환경변수 파일 만들기

최상위 실습용:

```powershell
Copy-Item .env.example .env
```

수업용 샘플 또는 팀 템플릿을 실행할 때는 해당 폴더 안에서 `.env.example`을 `.env`로 복사합니다.

```powershell
Copy-Item .env.example .env
```

주의:

- `.env`는 GitHub에 올리지 않습니다.
- `.env.example`에는 예시 값만 둡니다.
- API Key, AWS Access Key, 비밀번호는 README나 발표 자료에 적지 않습니다.

## 6. 수업용 샘플 프로젝트 실행

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
docker compose config
docker compose up --build
```

확인 주소:

```text
Backend health : http://127.0.0.1:8000/health
Frontend       : http://127.0.0.1:8801
Monitor        : http://127.0.0.1:8802
```

다른 PowerShell에서 상태와 로그를 확인합니다.

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\02_instructor-sample-project
docker compose ps
docker compose logs backend
docker compose logs worker
docker compose logs monitor
```

실시간 로그:

```powershell
docker compose logs -f worker
```

종료:

```powershell
docker compose down
```

## 7. 팀 템플릿 실행

```powershell
cd C:\aidev\07_multi-agent-service-mini-project\99_team-projects\multi-agent-service-team-template
Copy-Item .env.example .env
docker compose config
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

## 8. GitHub Actions 준비

07 팀 프로젝트에서는 GitHub Actions를 선택 제출 항목으로 둡니다. 목표는 자동 배포가 아니라, 먼저 Docker Compose 설정과 Docker build가 깨지지 않았는지 자동 검증하는 것입니다.

팀 템플릿에는 workflow 예시가 들어 있습니다.

```text
99_team-projects/multi-agent-service-team-template/.github/workflows/docker-compose-check.yml
```

실제 GitHub 저장소에서 자동 실행하려면 workflow 파일이 저장소 최상위의 `.github/workflows` 아래에 있어야 합니다.

확인 흐름:

```text
push 또는 pull request
-> GitHub Actions 실행
-> Python 문법 검사
-> docker compose config
-> Docker image build
```

## 9. AWS 배포 체크리스트

07에서 AWS 실제 배포는 필수가 아닙니다. 다만 최종 프로젝트 문서에는 AWS 배포 시 어떤 구조로 확장할지 정리하는 것을 권장합니다.

기본 흐름:

```text
1. 로컬에서 docker compose up --build 검증
2. backend /health 확인
3. Docker image build
4. Amazon ECR에 image push
5. App Runner 또는 ECS에서 image 실행
6. 환경변수와 port 설정
7. 외부 URL로 /health 확인
8. CloudWatch Logs 확인
9. 실습 후 리소스 삭제
```

AWS CLI 확인:

```powershell
aws --version
aws sts get-caller-identity
```

AWS는 비용이 발생할 수 있으므로 실제 배포는 수업 안내에 따라 진행합니다.

## 10. 비용과 보안 주의

- OpenAI API 호출은 비용이 발생할 수 있습니다.
- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- `.env`, `.venv`, API Key, AWS Access Key는 커밋하지 않습니다.
- GitHub Actions 로그에 비밀 값이 출력되지 않게 합니다.
- 실습 후 `docker compose down`으로 컨테이너를 종료합니다.
- AWS 실습 후 App Runner, ECS, Load Balancer, ECR image, CloudWatch Log Group 등을 정리합니다.

## 11. 첫 수업 추천 진행 순서

```text
1. Python .venv 활성화
2. requirements.txt 설치
3. Docker Desktop 실행
4. docker compose version 확인
5. 수업용 샘플 docker compose config 확인
6. 수업용 샘플 docker compose up --build 실행
7. backend /health 확인
8. frontend와 monitor 화면 확인
9. worker logs 확인
10. 팀 템플릿 복사
11. 장애 유형, 복구 전략, Agent 역할 설계
12. Handoff/Context, Feedback Loop, Guardrails 기준 작성
13. LangSmith식 Trace와 감사 로그 설계
14. GitHub Actions build check 추가 여부 결정
15. AWS 배포 체크리스트 작성
```

## 12. 오류가 날 때 먼저 볼 것

```text
Docker 오류:
- Docker Desktop이 실행 중인가?
- docker ps가 동작하는가?
- docker compose version이 동작하는가?

Compose 오류:
- 현재 폴더에 docker-compose.yml이 있는가?
- .env 파일이 있는가?
- docker compose config가 통과하는가?
- 포트 8000, 8801, 8802가 이미 사용 중이지 않은가?

서비스 오류:
- backend /health가 정상 응답하는가?
- worker 로그에 오류가 있는가?
- monitor가 backend 주소를 올바르게 보고 있는가?

GitHub Actions 오류:
- workflow 파일이 .github/workflows 아래에 있는가?
- branch 조건이 맞는가?
- secrets를 코드에 직접 적지 않았는가?

AWS 오류:
- region이 맞는가?
- IAM 권한이 충분한가?
- health check path가 /health인가?
- CloudWatch Logs에 오류가 있는가?
```
