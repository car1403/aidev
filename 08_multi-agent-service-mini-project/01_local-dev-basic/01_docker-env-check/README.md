# 01_docker-env-check

Docker Desktop 실행 상태를 확인하는 실습입니다.

## 1. Docker Desktop 실행

Windows 시작 메뉴에서 Docker Desktop을 실행합니다. 오른쪽 아래 작업 표시줄에 Docker 아이콘이 보이고, 상태가 Running이면 준비된 것입니다.

## 2. PowerShell에서 확인

```powershell
docker --version
docker compose version
docker ps
```

각 명령의 의미는 다음과 같습니다.

| 명령 | 의미 |
| --- | --- |
| `docker --version` | Docker 명령어가 설치되어 있는지 확인합니다. |
| `docker compose version` | Docker Compose 기능이 사용 가능한지 확인합니다. |
| `docker ps` | 현재 실행 중인 컨테이너 목록을 확인합니다. |

## 3. 첫 테스트 컨테이너 실행

```powershell
docker run hello-world
```

이 명령은 Docker가 이미지를 내려받고 컨테이너를 실행할 수 있는지 확인합니다. 메시지가 출력되고 컨테이너가 종료되면 정상입니다.

## 4. 오류가 날 때

| 증상 | 확인할 것 |
| --- | --- |
| `docker` 명령을 찾을 수 없음 | Docker Desktop 설치 여부 확인 |
| `Cannot connect to the Docker daemon` | Docker Desktop 실행 여부 확인 |
| `docker compose`가 동작하지 않음 | Docker Desktop 최신 버전 여부 확인 |

Docker가 준비되지 않으면 07의 샘플 프로젝트와 팀 프로젝트를 실행할 수 없습니다.
