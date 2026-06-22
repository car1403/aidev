# 07. First Run Checklist

첫 수업 환경 자가 체크리스트입니다.

아래 항목을 순서대로 확인합니다. 체크리스트는 "설치가 끝났다"를 확인하는 문서가 아니라, **수업을 따라갈 준비가 되었는지 확인하는 문서**입니다.

## 1. 기본 설치 확인

```text
[ ] Python이 설치되어 있다.
[ ] VS Code가 설치되어 있다.
[ ] VS Code에서 C:\aidev 폴더를 열었다.
[ ] Python Extension이 설치되어 있다.
[ ] Pylance Extension이 설치되어 있다.
[ ] Markdown All in One Extension이 설치되어 있다.
[ ] README.md 파일을 Markdown Preview로 열어 볼 수 있다.
```

## 2. Codex 사용 준비 확인

Codex를 수업에서 사용할 경우 아래 항목을 확인합니다.

```text
[ ] Codex App 또는 VS Code Codex 확장을 설치했다.
[ ] ChatGPT 계정으로 로그인할 수 있다.
[ ] Codex에서 C:\aidev 폴더를 열어 볼 수 있다.
[ ] Codex에게 파일을 수정하게 하기 전, 어떤 파일을 수정하는지 확인하는 습관을 이해했다.
```

Codex 설치와 로그인은 아래 문서를 참고합니다.

```text
03_student-guides/01_getting-started/08_codex-install-and-login-guide.md
```

## 3. OpenAI 계정과 결제 구분 확인

수업 전에 아래 개념을 구분합니다.

```text
[ ] ChatGPT 구독 결제와 OpenAI API Platform 결제가 다르다는 것을 이해했다.
[ ] API Key는 비밀번호처럼 보호해야 한다는 것을 이해했다.
[ ] API Key는 코드에 직접 적지 않고 .env 파일에 넣어야 한다는 것을 이해했다.
[ ] 개인 결제가 필요한 실습은 진행자가 별도로 안내한다는 것을 확인했다.
```

자세한 내용은 아래 문서를 참고합니다.

```text
03_student-guides/01_getting-started/09_openai-account-billing-guide.md
```

## 4. PowerShell 확인

PowerShell을 열고 아래 명령을 실행합니다.

```powershell
python --version
pip --version
pwd
```

정상 기준:

```text
Python 버전이 표시된다.
pip 버전이 표시된다.
현재 위치가 표시된다.
```

`python --version`에서 오류가 나오면 Python 설치 또는 PATH 설정을 다시 확인합니다.

## 5. README Preview 확인

```text
[ ] 00_admin/README.md를 열었다.
[ ] Ctrl + Shift + V로 Preview를 열었다.
[ ] 코드블록과 표가 보기 좋게 표시된다.
```

Markdown 문서는 수업 교재처럼 사용합니다. `.md` 파일을 그냥 텍스트로만 보지 말고 Preview로 보는 습관을 들입니다.

## 6. 01 과정 .venv 준비

```powershell
cd C:\aidev\01_supabase-ai-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

이미 `.venv`가 있으면 `python -m venv .venv`를 다시 하지 않아도 됩니다.

프롬프트 앞에 `(.venv)`가 보이면 가상환경이 활성화된 상태입니다.

## 7. 첫 Python 파일 실행

예:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\01_python-basic\01_python-start\01_hello_python.py
```

정상 기준:

```text
터미널에 Python 예제 출력이 표시된다.
```

## 8. 오류가 나면

아래 순서로 확인합니다.

```text
1. 현재 폴더가 맞는가?
2. .venv가 활성화되어 있는가?
3. requirements.txt를 설치했는가?
4. 파일 경로가 맞는가?
5. 오류 메시지를 끝까지 읽었는가?
6. API Key가 필요한 실습인데 .env 파일을 만들지 않은 것은 아닌가?
7. Codex 또는 OpenAI 계정 로그인이 필요한 실습인지 확인했는가?
```

그래도 해결하지 못하면 오류 메시지 전체를 진행자에게 보여줍니다. 오류 메시지는 일부만 보여주면 원인을 찾기 어렵습니다.
