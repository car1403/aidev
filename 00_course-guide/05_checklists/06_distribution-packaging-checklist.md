# 06. Distribution Packaging Checklist

강의 자료를 압축하거나 다른 PC로 복사하기 전에 확인하는 배포 전 체크리스트입니다.

## 포함해야 하는 파일

```text
[ ] README.md와 SETUP.md
[ ] 각 과정의 00_references, 10_labs, 20_assignments, 99_* 템플릿
[ ] requirements.txt
[ ] .env.example
[ ] .vscode/settings.json
[ ] docs, presentation, checklists, templates 폴더
[ ] Markdown 문서에서 사용하는 이미지와 예시 파일
```

`.vscode/settings.json`은 수강생이 과정 폴더를 VS Code로 열었을 때 `.venv` 자동 활성화를 돕기 위한 설정입니다. 민감 정보가 들어가지 않는지 확인한 뒤 포함합니다.

## 제외해야 하는 파일과 폴더

```text
[ ] .env
[ ] .env.local, .env.dev, .env.prod 같은 실제 환경 파일
[ ] .venv, venv, env, ENV 같은 가상환경 폴더
[ ] __pycache__
[ ] .pytest_cache, .mypy_cache, .ruff_cache
[ ] site-packages
[ ] node_modules
[ ] build, dist, *.egg-info
[ ] *.log
[ ] tmp, temp
[ ] Thumbs.db, .DS_Store
```

실제 API Key, token, password, AWS Access Key는 코드, README, 발표 자료, 화면 캡처, 로그 파일 어디에도 남기지 않습니다.

## 배포 전 확인 명령

PowerShell에서 `C:\aidev` 루트에서 실행합니다.

```powershell
cd C:\aidev
```

불필요한 로컬 폴더 확인:

```powershell
Get-ChildItem -Path . -Recurse -Force -Directory -Include .venv,venv,env,ENV,__pycache__,.pytest_cache,.mypy_cache,.ruff_cache,site-packages,node_modules
```

단, `05_project-templates\env`처럼 `.env.example` 템플릿을 담기 위한 폴더는 가상환경이 아니므로 포함해도 됩니다. 폴더 안에 `Scripts`, `Lib`, `pyvenv.cfg`, `site-packages`가 보이면 가상환경으로 보고 제외합니다.

실제 `.env` 파일 확인:

```powershell
Get-ChildItem -Path . -Recurse -Force -File -Filter ".env"
```

Git에서 제외되는지 확인:

```powershell
git check-ignore -v .env
git check-ignore -v .venv
git check-ignore -v __pycache__
git check-ignore -v .pytest_cache
```

Git으로 관리되는 파일만 압축하려면 아래 방식을 우선 사용합니다.

```powershell
git archive --format=zip --output aidev-course.zip HEAD
```

이 방식은 Git에 추적된 파일만 포함하므로 `.env`, `.venv`, 캐시 폴더가 섞일 위험이 줄어듭니다. 단, 아직 커밋하지 않은 최신 수정은 포함되지 않으므로 배포 직전에는 `git status --short`로 상태를 확인합니다.

## 최종 눈검사

```text
[ ] 압축 파일 안에 .env가 없다.
[ ] 압축 파일 안에 .venv가 없다.
[ ] 압축 파일 안에 __pycache__와 .pytest_cache가 없다.
[ ] 압축 파일 안에 site-packages와 node_modules가 없다.
[ ] .env.example에는 예시 값만 있다.
[ ] README의 첫 시작 링크가 깨지지 않는다.
[ ] Markdown 문서에서 사용하는 이미지가 함께 포함되어 있다.
[ ] 수강생이 압축 해제 후 README.md -> SETUP.md 순서로 시작할 수 있다.
```
