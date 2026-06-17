# 02 Environment Checklist

06 과정을 시작하기 전에 환경을 확인합니다.

이 과정은 Docker Compose, GitHub Actions, AWS 배포 흐름을 다루므로 수업 전에 환경을 미리 확인하는 것이 중요합니다.

## Python 확인

```powershell
python --version
pip --version
```

권장:

```text
Python 3.11 이상
```

## 가상환경 확인

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

## Docker 확인

```powershell
docker --version
docker compose version
docker ps
```

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 확인합니다.

처음 설치한 학생은 기본 컨테이너 실행도 확인합니다.

```powershell
docker run hello-world
```

## Docker Compose 확인

Compose 실습 폴더에서 설정을 검증합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\02_ch2_docker-compose-multi-service
Copy-Item .env.example .env
docker compose config
```

`docker compose config`가 성공하면 `docker-compose.yml` 문법과 `.env` 연결이 기본적으로 정상입니다.

## Git 확인

```powershell
git --version
```

GitHub Actions 단원에서는 GitHub 저장소와 연동할 수 있어야 합니다.

GitHub Actions workflow는 저장소 최상위 `.github/workflows` 아래에 있어야 자동 실행됩니다.

## AWS 확인

AWS 배포 실습을 진행할 학생은 아래 명령을 확인합니다.

```powershell
aws --version
aws sts get-caller-identity
```

AWS 실습은 비용이 발생할 수 있으므로 강사 안내가 있을 때만 진행합니다.

## VS Code 또는 Cursor 확인

확인할 것:

- 터미널이 PowerShell로 열리는가?
- 폴더 `C:\aidev\06_multi-agent-service-ops`를 열 수 있는가?
- `.env` 파일을 만들고 편집할 수 있는가?
- `docker-compose.yml` 파일 들여쓰기를 깨뜨리지 않고 편집할 수 있는가?

## 포트 확인

06 과정에서 자주 쓰는 포트입니다.

| 포트 | 용도 |
| --- | --- |
| 8000 | FastAPI backend |
| 8801 | Streamlit frontend |
| 8802 | Streamlit monitor |
| 8803 | 단원 실습용 dashboard |

포트 충돌이 나면 기존 서버나 컨테이너를 종료합니다.

```powershell
docker ps
docker compose down
```

## 수업 전 최종 체크

- [ ] Python이 설치되어 있다.
- [ ] `.venv`가 활성화된다.
- [ ] `pip install -r requirements.txt`가 성공한다.
- [ ] Docker Desktop이 설치되어 있다.
- [ ] Docker Desktop이 실행된다.
- [ ] `docker compose version`이 동작한다.
- [ ] `docker compose config`가 성공한다.
- [ ] Git이 설치되어 있다.
- [ ] GitHub Actions workflow 위치를 이해했다.
- [ ] AWS 실습 시 비용과 리소스 삭제 계획을 확인했다.
