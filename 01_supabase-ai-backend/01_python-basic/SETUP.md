# SETUP

`01_python-basic` 실행 환경 설정 안내입니다.

## 1. 작업 폴더로 이동

```powershell
cd C:\aidev\01_python-basic
```

## 2. Python 확인

```powershell
python --version
pip --version
```

권장 버전:

```text
Python 3.11 이상
```

## 3. 가상환경 만들기

```powershell
python -m venv .venv
```

## 4. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

## 5. 패키지 설치

기초 과정은 외부 패키지 없이 진행합니다. 그래도 같은 실습 습관을 만들기 위해 `requirements.txt`를 사용합니다.

```powershell
pip install -r requirements.txt
```

## 6. 예제 실행

```powershell
python .\01_python-start\01_hello_python.py
```

## 7. 자주 만나는 문제

### 스크립트 실행 권한 오류

PowerShell에서 `Activate.ps1` 실행이 막히면 아래 명령을 한 번 실행합니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### python 명령을 찾을 수 없음

Python이 설치되어 있는지 확인하고, 설치 시 `Add python.exe to PATH`가 선택되어 있는지 확인합니다.
