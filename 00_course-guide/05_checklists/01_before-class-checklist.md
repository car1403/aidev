# 01. Before Class Checklist

수업 시작 전 함께 확인하는 체크리스트입니다.

## 공통 환경

```text
[ ] Python 설치 확인
[ ] VS Code 설치 확인
[ ] VS Code Extensions 설치 확인
[ ] C:\aidev 폴더 열기
[ ] PowerShell 열기
[ ] README.md Preview 열기
```

## Python 확인

```powershell
python --version
pip --version
```

## 과정별 .venv 확인

예: 01 과정

```powershell
cd C:\aidev\01_python-git-foundation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip list
```

자료 배포 전에는 각 과정 폴더의 `.venv`가 포함되지 않았는지 확인합니다. `.venv`는 수강생 PC에서 각 과정의 `SETUP.md`를 따라 다시 생성합니다.

## Supabase 과정 확인

```text
[ ] Supabase 계정 준비
[ ] Project URL 확인
[ ] anon key 확인
[ ] service role key 사용 위치 설명
[ ] .env.example -> .env 복사
[ ] .env는 제출하지 않는다고 안내
```

## Docker 과정 확인

05 이후 과정에서 확인합니다.

```text
[ ] Docker Desktop 실행
[ ] docker --version 확인
[ ] docker ps 확인
[ ] 필요한 이미지 또는 컨테이너 준비
```
