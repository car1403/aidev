# 07. First Run Checklist

처음 실습을 시작하기 전에 아래 항목을 확인합니다.

## 계정

- [ ] GitHub 계정을 만들었다.
- [ ] GitHub 이메일 인증을 완료했다.
- [ ] VS Code에서 GitHub 계정으로 로그인했다.
- [ ] GitHub Copilot Chat 사용 가능 여부를 확인했다.

## 설치

- [ ] Python이 설치되어 있다.
- [ ] VS Code가 설치되어 있다.
- [ ] VS Code에서 `C:\aidev` 폴더를 열었다.
- [ ] Python 확장을 설치했다.
- [ ] GitHub Copilot / Copilot Chat 확장을 설치했다.
- [ ] Markdown Preview를 열 수 있다.
- [ ] PowerShell 터미널을 열 수 있다.

## Python 확인

```powershell
python --version
pip --version
```

## 첫 과정 실행 준비

```powershell
cd C:\aidev\01_supabase-ai-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 보안 확인

- [ ] `.env` 파일은 GitHub에 올리면 안 된다는 것을 이해했다.
- [ ] `.venv` 폴더는 GitHub에 올리면 안 된다는 것을 이해했다.
- [ ] API Key는 화면 공유나 README에 노출하지 않는다.
