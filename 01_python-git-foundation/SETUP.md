# SETUP

`01_python-git-foundation` 과정의 개발 환경 설정 문서입니다.

이 과정은 Python 기초와 Git/GitHub 실습을 위한 독립 선행 과정입니다. Supabase, Gemini API, FastAPI, Redis 설정은 다음 과정인 `02_supabase-ai-backend`부터 진행합니다.

## 공통 개발 환경 안내 문서

Python 설치, VS Code 설치, 확장 프로그램, PowerShell 사용법, Markdown 문서 보기처럼 더 구체적인 준비 방법은 아래 공통 안내 문서를 참고합니다.

| 필요한 내용 | 참고 문서 |
| --- | --- |
| Python 설치와 버전 확인 | [`../00_course-guide/03_student-guides/01_getting-started/01_python-install-guide.md`](../00_course-guide/03_student-guides/01_getting-started/01_python-install-guide.md) |
| VS Code 설치 | [`../00_course-guide/03_student-guides/01_getting-started/02_vscode-install-guide.md`](../00_course-guide/03_student-guides/01_getting-started/02_vscode-install-guide.md) |
| VS Code 확장 프로그램 설치 | [`../00_course-guide/03_student-guides/01_getting-started/03_vscode-extensions-guide.md`](../00_course-guide/03_student-guides/01_getting-started/03_vscode-extensions-guide.md) |
| PowerShell 기본 사용법 | [`../00_course-guide/03_student-guides/01_getting-started/04_powershell-basic-guide.md`](../00_course-guide/03_student-guides/01_getting-started/04_powershell-basic-guide.md) |
| `.venv`, `pip`, `requirements.txt` 사용법 | [`../00_course-guide/03_student-guides/01_getting-started/05_venv-and-pip-guide.md`](../00_course-guide/03_student-guides/01_getting-started/05_venv-and-pip-guide.md) |
| Markdown 미리보기와 문서 작성법 | [`../00_course-guide/03_student-guides/01_getting-started/06_markdown-preview-guide.md`](../00_course-guide/03_student-guides/01_getting-started/06_markdown-preview-guide.md) |
| 첫 실행 전 점검표 | [`../00_course-guide/03_student-guides/01_getting-started/07_first-run-checklist.md`](../00_course-guide/03_student-guides/01_getting-started/07_first-run-checklist.md) |

## 1. 작업 위치로 이동

PowerShell을 열고 과정 폴더로 이동합니다.

```powershell
cd C:\aidev\01_python-git-foundation
```

현재 위치를 확인합니다.

```powershell
Get-Location
```

결과가 아래와 비슷하면 됩니다.

```text
C:\aidev\01_python-git-foundation
```

## 2. Python 가상환경 만들기

이 과정에서는 `01_python-git-foundation` 최상위의 `.venv` 하나를 사용합니다. `01_python-basic`, `02_python-advanced`, `03_git-github` 하위 폴더 안에는 별도 `.venv`를 만들지 않습니다.

```powershell
python -m venv .venv
```

이미 `.venv` 폴더가 있으면 다시 만들 필요는 없습니다.

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 줄 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

확인 명령:

```powershell
python --version
pip --version
```

PowerShell 실행 정책 오류가 나오면 다음 명령을 한 번 실행한 뒤 다시 활성화합니다.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 4. 패키지 설치

기초 실습과 테스트에 필요한 패키지를 설치합니다.

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

설치 확인:

```powershell
python -c "import pytest, dotenv; print('packages ok')"
```

## 5. 예제 실행

```powershell
python .\01_python-basic\01_python-start\01_hello_python.py
python .\02_python-advanced\01_function-advanced\01_args_kwargs_api_options.py
python -m pytest .\02_python-advanced\08_testing-code-quality
```

## 6. Git/GitHub 준비

Git 설치 여부를 확인합니다.

```powershell
git --version
```

GitHub 계정 준비와 VS Code Source Control 사용법은 `03_git-github`에서 단계적으로 실습합니다.

```text
03_git-github
```

## 체크리스트

```text
[ ] 01_python-git-foundation 최상위에서 .venv를 만들었는가?
[ ] .venv가 활성화된 상태에서 pip install -r requirements.txt를 실행했는가?
[ ] 01_python-basic 예제가 실행되는가?
[ ] 02_python-advanced 테스트가 실행되는가?
[ ] git --version으로 Git 설치를 확인했는가?
```
