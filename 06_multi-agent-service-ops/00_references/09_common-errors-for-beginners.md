# 09 Common Errors for Beginners

06 과정에서 자주 만나는 오류와 확인 방법입니다.

## docker 명령이 없음

확인:

```powershell
docker --version
```

해결:

- Docker Desktop 설치
- PowerShell 새로 열기
- PC 재부팅

## Docker Desktop이 실행 중이 아님

오류 예시:

```text
Cannot connect to the Docker daemon
```

해결:

- Docker Desktop 실행
- `docker ps` 다시 실행

## 포트 충돌

증상:

```text
port is already allocated
```

확인:

```powershell
docker ps
```

해결:

```powershell
docker compose down
```

또는 다른 포트를 사용합니다.

## .env 파일 없음

증상:

```text
env file .env not found
```

해결:

```powershell
Copy-Item .env.example .env
```

## Python 패키지 없음

증상:

```text
ModuleNotFoundError
```

해결:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## docker compose config 실패

확인할 것:

- `docker-compose.yml` 파일 위치가 맞는가?
- `.env` 파일이 있는가?
- 들여쓰기가 올바른가?
- 포트 형식이 문자열로 되어 있는가?

해결 순서:

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
```

## Docker build 실패

확인할 것:

- Dockerfile 위치가 맞는가?
- requirements.txt가 image 안으로 복사되는가?
- `pip install -r requirements.txt`가 성공하는가?
- 실행 명령의 모듈 경로가 맞는가?

해결:

```powershell
docker build --no-cache -t aidev-agent-backend:local .
```

## GitHub Actions가 실행되지 않음

확인할 것:

- workflow 파일이 `.github/workflows` 아래에 있는가?
- 파일 확장자가 `.yml` 또는 `.yaml`인가?
- push한 branch가 workflow의 `branches` 조건과 맞는가?
- GitHub 저장소에서 Actions 기능이 켜져 있는가?

## GitHub Actions에서 secret이 필요한 경우

확인할 것:

- API Key를 workflow 파일에 직접 적지 않았는가?
- Repository Secrets에 등록했는가?
- 로그에 비밀 값이 출력되지 않는가?

## AWS CLI 인증 실패

확인:

```powershell
aws sts get-caller-identity
```

확인할 것:

- `aws configure`를 완료했는가?
- region이 맞는가?
- IAM 권한이 충분한가?
- Access Key를 GitHub나 README에 올리지 않았는가?

## AWS 배포 후 health check 실패

확인할 것:

- 컨테이너 port가 맞는가?
- `/health` 경로가 존재하는가?
- AWS 서비스의 health check path가 `/health`로 설정되어 있는가?
- 환경변수가 누락되지 않았는가?
- CloudWatch Logs에 오류가 있는가?

## 비용이 계속 발생할 수 있음

AWS 실습 후 확인할 것:

- App Runner Service 삭제
- ECS Service/Task 정리
- Load Balancer 삭제
- ECR image 정리
- CloudWatch Log Group 정리
