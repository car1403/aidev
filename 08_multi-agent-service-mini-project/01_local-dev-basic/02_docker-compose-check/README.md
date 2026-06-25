# 02_docker-compose-check

Docker Compose 설정을 실행 전에 검증하는 실습입니다.

## 1. 샘플 프로젝트 폴더로 이동

```powershell
cd C:\aidev\08_multi-agent-service-mini-project\02_instructor-sample-project
```

## 2. 환경변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

`.env.example`은 예시 파일이고, 실제 실행 시에는 `.env` 파일을 사용합니다. `.env`에는 API Key나 포트 같은 실행 환경 값을 적습니다.

## 3. Compose 설정 검증

```powershell
docker compose config
```

이 명령은 컨테이너를 실행하지 않고 `docker-compose.yml` 문법과 환경변수 연결을 먼저 확인합니다.

정상이라면 Compose 설정이 길게 출력됩니다. 오류가 있다면 보통 아래를 확인합니다.

- `.env` 파일이 있는가?
- `docker-compose.yml` 파일이 현재 폴더에 있는가?
- 들여쓰기나 콜론(`:`) 문법이 맞는가?
- 포트 번호가 숫자로 되어 있는가?

## 4. Compose 실행

```powershell
docker compose up --build
```

`--build`는 Dockerfile을 기준으로 이미지를 다시 빌드하라는 뜻입니다. 코드가 바뀌었을 때 자주 사용합니다.

## 5. 종료

```powershell
docker compose down
```

실습이 끝나면 컨테이너를 종료합니다. 종료하지 않으면 포트가 계속 사용 중일 수 있습니다.
