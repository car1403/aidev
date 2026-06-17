# SETUP

`02_python-advanced` 실행 환경 설정 안내입니다.

## 1. 작업 폴더로 이동

```powershell
cd C:\aidev\02_python-advanced
```

## 2. Python 확인

```powershell
python --version
pip --version
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

```powershell
pip install -r requirements.txt
```

## 6. 첫 예제 실행

```powershell
python .\01_function-advanced\01_args_kwargs.py
```

## 7. 테스트 실행

```powershell
python -m pytest .\08_testing-code-quality
```
