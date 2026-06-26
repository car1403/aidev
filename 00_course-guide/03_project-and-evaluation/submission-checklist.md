# Submission Checklist

제출 전 아래 항목을 확인합니다.

## 공통 제출 기준

```text
[ ] README.md가 있다.
[ ] 실행 방법이 작성되어 있다.
[ ] requirements.txt 또는 실행 환경 설명이 있다.
[ ] .env.example이 있다.
[ ] 실제 .env는 제출하지 않는다.
[ ] 주요 기능의 실행 결과가 정리되어 있다.
[ ] 오류와 해결 과정이 기록되어 있다.
```

## 보안

```text
[ ] API Key, token, password가 코드에 직접 들어 있지 않다.
[ ] README와 발표 자료에 실제 key가 보이지 않는다.
[ ] 화면 캡처에 실제 key나 token이 보이지 않는다.
[ ] Supabase service role key는 프론트엔드에 넣지 않는다.
```

## 배포/압축 전 제외

```text
[ ] .env
[ ] .venv, venv, env, ENV 같은 가상환경 폴더
[ ] __pycache__
[ ] .pytest_cache, .mypy_cache, .ruff_cache
[ ] site-packages
[ ] node_modules
[ ] build, dist, *.egg-info
[ ] *.log
```

`05_project-templates\env`처럼 `.env.example` 템플릿을 담는 폴더는 가상환경이 아닙니다. 폴더 안에 `pyvenv.cfg`, `Scripts`, `Lib`, `site-packages`가 보이면 가상환경으로 보고 제외합니다.

## 배포 전 확인 명령

```powershell
cd C:\aidev
Get-ChildItem -Path . -Recurse -Force -File -Filter ".env"
Get-ChildItem -Path . -Recurse -Force -Directory -Include .venv,venv,ENV,__pycache__,.pytest_cache,.mypy_cache,.ruff_cache,site-packages,node_modules
```

Git으로 관리되는 파일만 압축하려면 아래 방식을 사용할 수 있습니다.

```powershell
git archive --format=zip --output aidev-course.zip HEAD
```
