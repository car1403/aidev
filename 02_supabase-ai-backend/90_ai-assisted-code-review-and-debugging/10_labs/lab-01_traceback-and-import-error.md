# Lab 01. Traceback and Import Error

## 목표

`ModuleNotFoundError`, `ImportError`가 났을 때 먼저 가상환경과 설치 패키지를 확인합니다.

## 확인 명령

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
pip show fastapi
pip install -r requirements.txt
```

## Codex 질문 예시

```text
ModuleNotFoundError가 발생했습니다.
현재 Python 경로와 pip show 결과는 아래와 같습니다.
원인을 초보자 기준으로 설명하고, 확인 순서를 알려주세요.
아직 파일은 수정하지 말아주세요.
```
