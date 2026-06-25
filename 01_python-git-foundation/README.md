# 01_python-git-foundation

Python 기초, Python 심화, Git/GitHub를 먼저 분리해서 학습하는 선행 과정입니다.

이 과정은 이후 `02_supabase-ai-backend`, `03_supabase-ai-frontend`, `04_supabase-ai-mini-project`를 진행하기 전에 필요한 공통 기반을 다집니다. Supabase, Gemini API, FastAPI 서버 구현은 다음 과정부터 본격적으로 다룹니다.

## 과정 목표

- Python 기본 문법, 자료형, 조건문, 반복문, 함수를 이해합니다.
- 파일/JSON 처리, 함수 심화, 모듈/패키지, 예외 처리, OOP, 테스트를 익힙니다.
- Git/GitHub로 변경 이력을 관리하고 VS Code Source Control을 사용할 수 있습니다.
- README 작성, `.gitignore`, `.env`와 API key 보안 기준을 이해합니다.
- 이후 백엔드 과정에서 코드를 읽고 실행할 수 있는 최소 개발 습관을 만듭니다.

## 처음 시작하는 순서

1. [SETUP.md](./SETUP.md)를 보고 `01_python-git-foundation` 폴더에 `.venv`를 만듭니다.
2. PowerShell에서 `.venv`를 활성화합니다.
3. `pip install -r requirements.txt`로 기초 실습 패키지를 설치합니다.
4. `01_python-basic`부터 예제를 실행합니다.
5. `02_python-advanced`에서 함수, 모듈, 예외 처리, 테스트를 확장합니다.
6. `03_git-github`에서 Git/GitHub와 VS Code Source Control을 실습합니다.

이 과정에서는 단원별 `.venv`를 만들지 않고, `01_python-git-foundation` 최상위의 `.venv` 하나를 사용합니다.

## 과정 구조

```text
01_python-git-foundation
├─ .venv
├─ requirements.txt
├─ README.md
├─ SETUP.md
├─ 01_python-basic
├─ 02_python-advanced
└─ 03_git-github
```

## 단원 요약

| 단원 | 역할 |
| --- | --- |
| `01_python-basic` | 변수, 자료형, 입출력, 조건문, 반복문, 함수, 파일/JSON 기초를 학습합니다. |
| `02_python-advanced` | 함수 심화, 모듈/패키지, 예외 처리, OOP, 테스트, 프로젝트 구조를 학습합니다. |
| `03_git-github` | Git/GitHub, 커밋/브랜치, VS Code Source Control, README/문서 작성, 민감정보 보호 기준을 학습합니다. |

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

```powershell
cd C:\aidev\01_python-git-foundation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 예제 실행 방법

항상 과정 최상위 폴더에서 실행하면 경로 혼선을 줄일 수 있습니다.

```powershell
cd C:\aidev\01_python-git-foundation
.\.venv\Scripts\Activate.ps1
python .\01_python-basic\01_python-start\01_hello_python.py
python .\02_python-advanced\01_function-advanced\01_args_kwargs_api_options.py
python -m pytest .\02_python-advanced\08_testing-code-quality
```

## 다음 과정과의 연결

`01_python-git-foundation`을 마친 뒤에는 [02_supabase-ai-backend](../02_supabase-ai-backend/README.md)로 이동합니다.

다음 과정에서는 Python/Git 자체를 다시 길게 설명하지 않고, FastAPI, Supabase, Gemini API, Upstash Redis를 사용해 AI 백엔드 구조를 만드는 데 집중합니다.
