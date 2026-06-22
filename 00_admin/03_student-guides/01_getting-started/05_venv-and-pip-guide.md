# 05. venv and pip Guide

`.venv`는 프로젝트별 Python 실행 환경입니다.

수업에서는 과정 폴더마다 최상위에 `.venv`를 하나 만들고, 그 안에 필요한 Python 패키지를 설치합니다.

## 1. 왜 .venv를 사용하나요?

Python 프로젝트마다 필요한 패키지가 다를 수 있습니다.

예를 들어 아래처럼 과정마다 사용하는 패키지가 다릅니다.

```text
01 과정: fastapi, supabase, pydantic
02 과정: streamlit, httpx, pandas
04 과정: langchain, langgraph, openai
06 과정: docker 관련 도구, 운영 관련 패키지
08 과정: AIPP/n8n/Dify 실습 보조 스크립트, fastapi, streamlit
09 과정: 미니 프로젝트 샘플 실행용 fastapi, streamlit
```

모든 패키지를 PC 전체에 섞어서 설치하면 버전 충돌이 생길 수 있습니다. 그래서 과정마다 `.venv`를 따로 사용합니다.

## 2. 과정별 .venv 기준

하위 실습 폴더마다 `.venv`를 만들지 않습니다.

과정 폴더의 최상위에 하나만 만듭니다.

예시:

```text
01_supabase-ai-backend/.venv
02_supabase-ai-frontend/.venv
03_supabase-ai-mini-project/.venv
04_llm-agent-orchestration/.venv
05_llm-agent-mini-project/.venv
06_multi-agent-service-ops/.venv
07_multi-agent-service-mini-project/.venv
08_ai-workflow-automation/.venv
09_ai-workflow-mini-project/.venv
```

중요한 기준은 다음과 같습니다.

```text
01_supabase-ai-backend 아래의 01_python-basic 같은 하위 폴더마다 .venv를 만들지 않습니다.
02_supabase-ai-frontend 아래의 각 실습 폴더마다 .venv를 만들지 않습니다.
03~09도 과정 폴더 최상위에 .venv 하나만 사용합니다.
```

## 3. .venv 만들기

예를 들어 01 과정에서 가상환경을 만들려면 PowerShell에서 아래처럼 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
python -m venv .venv
```

이미 `.venv` 폴더가 있다면 다시 만들 필요는 없습니다.

## 4. .venv 활성화

Windows PowerShell에서는 아래 명령으로 `.venv`를 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

정상적으로 활성화되면 PowerShell 앞쪽에 `(.venv)`가 보입니다.

예시:

```text
(.venv) PS C:\aidev\01_supabase-ai-backend>
```

이 표시가 보이면 현재 터미널은 해당 과정의 가상환경을 사용하고 있는 상태입니다.

## 5. 패키지 설치 방법 1: requirements.txt로 한 번에 설치

수업에서는 보통 `requirements.txt` 파일을 사용해 필요한 패키지를 한 번에 설치합니다.

```powershell
pip install -r requirements.txt
```

`requirements.txt`는 이 과정에서 필요한 패키지 목록입니다.

예시:

```text
fastapi
uvicorn
pydantic
python-dotenv
```

위와 같은 내용이 `requirements.txt`에 들어 있으면, `pip install -r requirements.txt` 명령은 목록에 적힌 패키지를 한 번에 설치합니다.

## 6. 패키지 설치 방법 2: 하나씩 직접 설치

패키지는 `requirements.txt`로만 설치할 수 있는 것이 아닙니다. 필요한 패키지를 하나씩 직접 설치할 수도 있습니다.

형식:

```powershell
pip install 패키지이름
```

예시:

```powershell
pip install fastapi
pip install uvicorn
pip install streamlit
pip install pandas
```

여러 개를 한 줄에 설치할 수도 있습니다.

```powershell
pip install fastapi uvicorn pydantic
```

초보자는 아래처럼 이해하면 됩니다.

| 방식 | 언제 사용하나요? |
| --- | --- |
| `pip install -r requirements.txt` | 수업 폴더에 필요한 패키지 목록이 이미 준비되어 있을 때 사용합니다. |
| `pip install fastapi` | 특정 패키지 하나만 추가로 설치하고 싶을 때 사용합니다. |
| `pip install fastapi uvicorn` | 몇 개의 패키지를 직접 골라 설치하고 싶을 때 사용합니다. |

## 7. 하나씩 설치한 패키지를 requirements.txt에 기록하기

패키지를 하나씩 설치했다면, 나중에 다른 참여자나 다른 PC에서도 같은 환경을 만들 수 있도록 `requirements.txt`에 기록하는 것이 좋습니다.

현재 설치된 패키지 목록을 파일로 저장하려면 아래 명령을 사용합니다.

```powershell
pip freeze > requirements.txt
```

단, 이 명령은 현재 `.venv`에 설치된 모든 패키지를 기록합니다. 수업에서는 수업에서 제공한 `requirements.txt`를 우선 사용하고, 팀 프로젝트나 개인 프로젝트에서 패키지를 추가했을 때만 신중하게 사용합니다.

## 8. 설치된 패키지 확인

현재 `.venv`에 설치된 패키지를 확인합니다.

```powershell
pip list
```

특정 패키지가 설치되었는지 확인하려면 아래처럼 볼 수 있습니다.

```powershell
pip show fastapi
```

설치되어 있으면 버전, 위치, 설명이 표시됩니다. 설치되어 있지 않으면 아무 정보도 나오지 않거나 경고가 표시됩니다.

## 9. .venv 비활성화

작업이 끝나면 가상환경을 비활성화할 수 있습니다.

```powershell
deactivate
```

비활성화되면 PowerShell 앞쪽의 `(.venv)` 표시가 사라집니다.

## 10. 자주 만나는 오류

### requirements.txt를 찾을 수 없습니다

현재 폴더가 잘못된 경우입니다.

확인:

```powershell
pwd
dir
```

`requirements.txt`가 보이는 폴더로 이동한 뒤 다시 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
pip install -r requirements.txt
```

### ModuleNotFoundError

필요한 패키지가 설치되지 않은 경우입니다.

예시 오류:

```text
ModuleNotFoundError: No module named 'fastapi'
```

해결:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

또는 필요한 패키지만 하나씩 설치할 수도 있습니다.

```powershell
pip install fastapi
```

### pip 명령이 실행되지 않을 때

Python 설치 또는 PATH 설정 문제일 수 있습니다.

먼저 아래 명령을 확인합니다.

```powershell
python --version
python -m pip --version
```

`pip` 명령이 안 되지만 `python -m pip`는 되는 경우 아래처럼 실행할 수 있습니다.

```powershell
python -m pip install -r requirements.txt
python -m pip install fastapi
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

## 12. 수업 중 권장 사용 흐름

수업에서는 보통 아래 순서로 진행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

추가 패키지가 필요하면 수업 안내에 따라 하나씩 설치합니다.

예시:

```powershell
pip install requests
```

그 뒤 필요한 경우 `requirements.txt`에 반영합니다.

다른 과정도 같은 방식으로 진행합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```powershell
cd C:\aidev\08_ai-workflow-automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

이미 `.venv`가 있는 과정은 새로 만들지 않고 활성화만 합니다.

## 13. 최종 체크리스트

아래 항목을 확인합니다.

```text
[ ] 과정 폴더 최상위에서 .venv를 만들었다.
[ ] .venv를 활성화했다.
[ ] PowerShell 앞에 (.venv)가 보인다.
[ ] requirements.txt로 패키지를 한 번에 설치할 수 있다.
[ ] pip install 패키지이름으로 패키지를 하나씩 설치할 수 있다.
[ ] pip list로 설치된 패키지를 확인할 수 있다.
[ ] .venv 폴더를 GitHub에 올리면 안 된다는 것을 이해했다.
```
