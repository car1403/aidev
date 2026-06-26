# Environment Guide

이 과정은 Windows, PowerShell, VS Code, Python `.venv` 기준으로 설명합니다.

## Python과 `.venv`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`01`, `02`, `03`, `04`, `06`, `07`, `08`은 과정 최상위 `.venv` 하나를 기본으로 사용합니다. `05`는 단원별 의존성이 달라질 수 있어 단원별 `.venv` 방식을 우선 권장합니다.

## VS Code

`01`, `02`, `03`, `04`, `06`, `07`, `08` 과정에는 `.vscode/settings.json`이 포함되어 있습니다. 해당 과정 폴더 자체를 VS Code로 열면 새 터미널에서 `.venv`가 자동 활성화됩니다.

`C:\aidev` 루트를 열면 하위 과정의 `.vscode/settings.json`이 자동 적용되지 않을 수 있습니다.

## `.env`와 보안

```text
.env
-> 실제 실행에 사용하는 비밀 값
-> GitHub와 제출물에 포함하지 않음

.env.example
-> 필요한 환경변수 이름을 보여주는 예시
-> 실제 key를 넣지 않음
-> GitHub에 포함 가능
```

실제 API Key, Supabase service role key, AWS Access Key, 비밀번호, token은 README, 발표 자료, 화면 캡처, 로그에 남기지 않습니다.

## Docker와 AWS

- `05`부터 Docker Desktop을 사용합니다.
- `05`는 주로 `docker run`으로 Ollama, pgvector 같은 도구를 실행합니다.
- `07`부터 Docker Compose, GitHub Actions, AWS 선택 배포를 다룹니다.
- AWS 실습은 비용이 발생할 수 있으므로 선택 실습으로 진행합니다.

