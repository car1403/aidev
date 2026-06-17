# 04. Environment Checklist

## 필수 준비

```text
Python 3.11 이상
VS Code 또는 Cursor
PowerShell
Docker Desktop
Git
브라우저
```

## Python 확인

```powershell
python --version
pip --version
```

## 가상 환경

08 과정 폴더에는 `.venv`를 사용할 수 있습니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Docker 확인

```powershell
docker --version
docker compose version
docker ps
```

`docker ps`가 실패하면 Docker Desktop이 실행 중인지 확인합니다.

## 환경 변수

상위 `.env.example`에는 다음 예시 값이 있습니다.

```text
OPENAI_API_KEY
OPENAI_MODEL
AIPP_API_KEY
N8N_BASE_URL
DIFY_API_KEY
DIFY_BASE_URL
```

실제 키는 `.env`에만 넣습니다.

```powershell
Copy-Item .env.example .env
```

## 체크리스트

```text
[ ] Python 버전 확인
[ ] .venv 활성화
[ ] requirements.txt 설치
[ ] Docker Desktop 실행
[ ] Git 설치 확인
[ ] .env 생성
[ ] API Key는 코드에 직접 쓰지 않음
```
