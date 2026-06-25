# 01 Python Env Check

이 단계에서는 05 과정 최상위 `.venv`가 준비되어 있는지 확인합니다.

## 처음 한 번만 만드는 경우

```powershell
cd C:\aidev\05_llm-agent-mini-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 이미 `.venv`가 있는 경우

이미 `.venv`가 만들어져 있다면 다시 만들 필요가 없습니다. 활성화부터 진행합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
.\.venv\Scripts\Activate.ps1
python --version
pip --version
```

## 확인 기준

- Python 3.11 이상이면 좋습니다.
- `.venv`가 활성화되면 PowerShell 프롬프트 앞에 `(.venv)`가 표시됩니다.
- `pip install -r requirements.txt`가 오류 없이 끝납니다.

## 자주 만나는 문제

`.\.venv\Scripts\Activate.ps1` 실행이 막히면 PowerShell 실행 정책 문제일 수 있습니다. 관리자 권한 없이 현재 사용자 범위에서 아래 명령을 실행한 뒤 다시 시도합니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
