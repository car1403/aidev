# 05. venv and pip Guide

`.venv`는 프로젝트별 Python 실행 환경입니다.

이번 과정에서는 기본적으로 과정 폴더마다 최상위에 `.venv`를 하나 만들고, 그 안에 필요한 Python 패키지를 설치합니다. 다만 `05_llm-agent-orchestration`은 단원별 의존성이 달라질 수 있어 단원별 `.venv` 방식을 우선 권장합니다.

## 1. 왜 .venv를 사용하나요?

Python 프로젝트마다 필요한 패키지가 다를 수 있습니다.

예를 들어 과정마다 사용하는 패키지가 다릅니다.

```text
01 과정: python-dotenv, pytest
02 과정: fastapi, supabase, pydantic, google-generativeai
03 과정: streamlit, httpx, pandas
04 과정: fastapi, streamlit, supabase, sse 관련 패키지
05 과정: langchain, langgraph, openai, pgvector 관련 패키지
06 과정: LangGraph 기반 Agent 프로젝트 패키지
07 과정: fastapi, streamlit, Docker Compose 실습용 패키지
08 과정: Multi-Agent 서비스 미니 프로젝트 패키지
```

모든 패키지를 PC 전체에 섞어서 설치하면 버전 충돌이 생길 수 있습니다. 그래서 과정마다 `.venv`를 따로 사용합니다.

## 2. 과정별 .venv 기준

예시:

```text
01_python-git-foundation/.venv
02_supabase-ai-backend/.venv
03_supabase-ai-frontend/.venv
04_supabase-ai-mini-project/.venv
05_llm-agent-orchestration/.venv
06_llm-agent-mini-project/.venv
07_multi-agent-service-ops/.venv
08_multi-agent-service-mini-project/.venv
```

중요한 기준:

```text
01_python-git-foundation 아래의 하위 실습 폴더마다 .venv를 만들지 않습니다.
02_supabase-ai-backend 아래의 하위 실습 폴더마다 .venv를 만들지 않습니다.
03_supabase-ai-frontend 아래의 각 실습 폴더마다 .venv를 만들지 않습니다.
04, 06, 07, 08도 과정 폴더 최상위에 .venv 하나만 사용합니다.
05_llm-agent-orchestration은 단원별 .venv를 우선 권장합니다.
```

## 3. .venv 만들기

예를 들어 01 과정에서 가상환경을 만들려면 PowerShell에서 아래처럼 실행합니다.

```powershell
cd C:\aidev\01_python-git-foundation
python -m venv .venv
```

이미 `.venv` 폴더가 있다면 다시 만들 필요는 없습니다.

## 4. .venv 활성화

Windows PowerShell에서는 아래 명령으로 `.venv`를 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

정상적으로 활성화되면 PowerShell 앞쪽에 `(.venv)`가 보입니다.

```text
(.venv) PS C:\aidev\01_python-git-foundation>
```

## 5. pip 업그레이드

가상환경을 만든 뒤에는 pip를 최신 상태로 맞춥니다.

```powershell
python -m pip install --upgrade pip
```

## 6. 패키지 설치 방법 1: requirements.txt로 한 번에 설치

```powershell
pip install -r requirements.txt
```

`requirements.txt`는 이 과정에서 필요한 패키지 목록입니다.

## 7. 패키지 설치 방법 2: 하나씩 직접 설치

필요한 패키지를 하나씩 직접 설치할 수도 있습니다.

```powershell
pip install fastapi
pip install uvicorn
pip install streamlit
```

여러 개를 한 줄에 설치할 수도 있습니다.

```powershell
pip install fastapi uvicorn pydantic
```

| 방식 | 언제 사용하나요? |
| --- | --- |
| `pip install -r requirements.txt` | 과정 폴더에 필요한 패키지 목록이 준비되어 있을 때 사용합니다. |
| `pip install fastapi` | 특정 패키지 하나만 추가로 설치하고 싶을 때 사용합니다. |
| `pip install fastapi uvicorn` | 몇 개의 패키지를 직접 골라 설치하고 싶을 때 사용합니다. |

## 8. 설치된 패키지 확인

```powershell
pip list
pip show fastapi
```

## 9. .venv 비활성화

```powershell
deactivate
```

## 10. 자주 만나는 오류

### requirements.txt를 찾을 수 없습니다

현재 폴더가 잘못된 경우입니다.

```powershell
pwd
dir
```

`requirements.txt`가 보이는 폴더로 이동한 뒤 다시 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
pip install -r requirements.txt
```

### ModuleNotFoundError

필요한 패키지가 설치되지 않은 경우입니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

또는 필요한 패키지만 하나씩 설치합니다.

```powershell
pip install fastapi
```

### pip 명령이 실행되지 않을 때

```powershell
python --version
python -m pip --version
python -m pip install -r requirements.txt
```

## 11. .venv를 GitHub에 올리면 안 되는 이유

`.venv`는 개인 PC의 실행 환경입니다. 용량이 크고, 다른 사람 PC에서는 그대로 쓰기 어렵습니다.

GitHub에는 아래 파일을 올립니다.

```text
requirements.txt
.env.example
README.md
코드 파일
```

GitHub에 올리지 않는 것:

```text
.venv
.env
__pycache__
```

## 12. 권장 사용 흐름

```powershell
cd C:\aidev\02_supabase-ai-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

다른 과정도 같은 방식으로 진행합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

이미 `.venv`가 있는 과정은 새로 만들지 않고 활성화만 합니다.

## 13. 최종 체크리스트

- [ ] 과정 폴더 최상위에서 `.venv`를 만들었다.
- [ ] `.venv`를 활성화했다.
- [ ] PowerShell 앞에 `(.venv)`가 보인다.
- [ ] `python -m pip install --upgrade pip`를 실행했다.
- [ ] `requirements.txt`로 패키지를 한 번에 설치할 수 있다.
- [ ] `pip install 패키지이름`으로 패키지를 하나씩 설치할 수 있다.
- [ ] `pip list`로 설치된 패키지를 확인할 수 있다.
- [ ] `.venv` 폴더를 GitHub에 올리면 안 된다는 것을 이해했다.
