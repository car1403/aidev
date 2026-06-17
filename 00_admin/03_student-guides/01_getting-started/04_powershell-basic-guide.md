# 04. PowerShell Basic Guide

PowerShell은 Windows에서 명령어를 실행하는 터미널입니다.

이 수업에서는 Python 실행, `.venv` 활성화, 패키지 설치, FastAPI/Streamlit 실행을 PowerShell에서 진행합니다.

## 1. PowerShell 열기

VS Code에서 여는 방법:

```text
Terminal -> New Terminal
```

Windows에서 직접 여는 방법:

```text
시작 메뉴 -> PowerShell 검색 -> Windows PowerShell 실행
```

## 2. 현재 위치 확인

```powershell
pwd
```

예:

```text
Path
----
C:\aidev
```

## 3. 폴더 이동

```powershell
cd C:\aidev
```

01 과정으로 이동:

```powershell
cd C:\aidev\01_supabase-ai-backend
```

상위 폴더로 이동:

```powershell
cd ..
```

## 4. 파일 목록 보기

```powershell
dir
```

또는:

```powershell
Get-ChildItem
```

## 5. 명령 취소

서버 실행을 멈추거나 잘못 실행한 명령을 중단할 때:

```text
Ctrl + C
```

FastAPI나 Streamlit 서버를 멈출 때도 `Ctrl + C`를 사용합니다.

## 6. 붙여넣기 주의

PowerShell에 여러 줄 명령을 붙여넣을 때 줄이 잘려 들어가지 않았는지 확인합니다.

특히 아래처럼 백틱(`)이 있는 명령은 줄 끝 공백에 주의합니다.

```powershell
docker run -d `
  --name example `
  -p 8000:8000 `
  image-name
```

초보자는 가능하면 한 줄 명령부터 익히는 것이 좋습니다.

## 7. 실행 정책 오류

`.venv` 활성화 중 아래와 비슷한 오류가 날 수 있습니다.

```text
running scripts is disabled on this system
```

해결 명령:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

실행 후 `Y`를 입력합니다.

다시 `.venv`를 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

## 8. 수업에서 자주 쓰는 명령

```powershell
python --version
pip --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run app.py
deactivate
```

## 9. 현재 위치가 중요한 이유

같은 명령어도 어느 폴더에서 실행하느냐에 따라 결과가 달라집니다.

예:

```powershell
pip install -r requirements.txt
```

이 명령은 현재 폴더에 `requirements.txt`가 있어야 성공합니다.

실패하면 먼저 확인합니다.

```powershell
pwd
dir
```
