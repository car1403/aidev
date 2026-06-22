# 01_ch1_docker-service-packaging

Python AI 서비스 코드를 Docker 이미지로 패키징하는 방법을 학습합니다.

## 핵심 개념

Dockerfile은 애플리케이션 실행 환경을 이미지로 만들기 위한 설명서입니다.

```text
Python 버전 선택
-> 작업 폴더 설정
-> requirements 설치
-> 소스 코드 복사
-> 실행 명령 지정
```

## 먼저 로컬에서 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\02_service-deployment-and-automation\01_ch1_docker-service-packaging
..\..\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

확인:

```text
http://127.0.0.1:8000/health
```

## Docker 이미지 빌드

```powershell
docker build -t ai-service-packaging-demo.
```

## Docker 컨테이너 실행

```powershell
docker run --rm -p 8000:8000 ai-service-packaging-demo
```

## 자주 나는 오류

| 오류 | 확인할 것 |
| --- | --- |
| docker 명령이 없음 | Docker Desktop 설치 여부 |
| Cannot connect to Docker daemon | Docker Desktop 실행 여부 |
| 포트 충돌 | 이미 8000 포트를 쓰는 프로그램이 있는지 확인 |
| ModuleNotFoundError | requirements.txt에 패키지가 있는지 확인 |
