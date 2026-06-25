# SETUP

`04_llm-agent-orchestration` 과정의 환경 설정 안내입니다.

이 과정은 Supabase가 아니라 **Docker Desktop + docker run 기반 로컬 Agent Lab**으로 진행합니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 `06_multi-agent-service-ops`에서 다룹니다.

## 1. 필수 준비

필수 프로그램:

- Python 3.11 이상
- Docker Desktop
- VS Code 또는 Cursor

선택 프로그램/서비스:

- OpenAI API Key
- LangSmith API Key

OpenAI API Key는 OpenAI 호출 예제를 실행할 때만 필요합니다. 키가 아직 없으면 Docker Desktop, Ollama, Llama, pgvector 실습부터 먼저 진행해도 됩니다.

## 2. Python 확인

PowerShell에서 확인합니다.

```powershell
python --version
pip --version
```

권장 버전:

```text
Python 3.11 이상
```

## 3. Docker Desktop 확인

04 과정은 Docker를 처음 사용하는 경우에도 따라올 수 있도록 Docker Desktop 기준으로 진행합니다.

Docker Desktop은 Windows에서 Docker 컨테이너를 쉽게 실행할 수 있게 해주는 프로그램입니다. 04에서는 Docker를 깊게 운영 도구로 배우기보다, 로컬 Llama와 pgvector PostgreSQL을 실행하기 위한 실습 도구로 사용합니다.

### 3-1. Docker Desktop이 아직 설치되지 않은 경우

아래 순서로 설치합니다.

1. Docker 공식 설치 문서를 엽니다.
2. Windows용 Docker Desktop Installer를 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 설치 중 WSL 2 관련 안내가 나오면 안내에 따라 활성화합니다.
5. 설치가 끝나면 Windows를 재부팅합니다.
6. Docker Desktop을 실행합니다.
7. 왼쪽 아래 또는 상단 상태가 `Engine running` 또는 정상 실행 상태인지 확인합니다.

공식 문서:

```text
https://docs.docker.com/desktop/setup/install/windows-install/
https://docs.docker.com/desktop/features/wsl/
```

초보자는 설치 중 선택지가 나오면 기본값을 유지하는 것을 권장합니다. Windows에서는 Docker Desktop이 WSL 2 기반으로 Linux 컨테이너를 실행하는 방식이 일반적입니다.

### 3-2. Windows 기능 확인

Docker Desktop 실행이 안 되거나 WSL 관련 오류가 나오면 PowerShell에서 아래 명령으로 WSL 상태를 확인합니다.

```powershell
wsl --status
wsl --list --verbose
```

`wsl` 명령이 없거나 WSL 2가 준비되지 않았다는 메시지가 나오면 Windows 업데이트와 WSL 설치 상태를 먼저 확인해야 합니다.

수업에서는 Docker Desktop 설치 자체에 너무 오래 머물지 않기 위해, 가능하면 수업 전날 아래 항목을 미리 확인합니다.

```text
Docker Desktop 실행 가능
docker --version 실행 가능
docker ps 실행 가능
```

### 3-3. 설치 후 Docker 동작 확인

Docker Desktop을 먼저 실행합니다.

PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

`docker ps`가 오류 없이 실행되면 Docker Desktop이 정상 동작 중입니다.

처음 확인할 때는 아래 명령으로 아주 작은 테스트 컨테이너를 실행해 볼 수 있습니다.

```powershell
docker run hello-world
```

이 명령은 Docker가 이미지를 내려받고 컨테이너를 실행할 수 있는지 확인하는 가장 기본적인 테스트입니다. 실행 후 컨테이너가 자동 종료되는 것은 정상입니다.

테스트 후 불필요한 종료 컨테이너를 정리하려면 다음 명령을 사용할 수 있습니다.

```powershell
docker ps -a
docker rm 컨테이너ID
```

컨테이너 ID는 `docker ps -a` 결과에서 확인합니다.

## 4. 단원별 가상환경 만들기

04 과정은 단원별 `.venv`를 권장합니다.

예시:

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
```

최상위에 있는 `requirements.txt`는 전체 과정을 하나의 가상환경에서 실습하고 싶을 때 사용하는 공통 설치 파일입니다.

```powershell
cd C:\aidev\04_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

다만 초보자 수업에서는 오류 추적을 쉽게 하기 위해 단원별 `.venv` 방식을 우선 권장합니다. 예를 들어 01 단원에서 생긴 패키지 문제가 05 RAG 단원과 섞이지 않게 하기 위함입니다.

## 5. OpenAI API Key 설정

각 단원에는 `.env.example` 파일이 있습니다.

OpenAI API Key는 OpenAI 모델 호출 실습에서 사용합니다. 로컬 Llama 실습만 먼저 진행한다면 이 단계는 건너뛰어도 됩니다.

처음 실행할 때는 다음처럼 복사합니다.

```powershell
Copy-Item .env.example .env
```

`.env` 파일에 실제 API Key를 입력합니다.

```text
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

주의:

- `.env` 파일은 GitHub에 올리지 않습니다.
- `.env.example`에는 실제 키를 넣지 않습니다.
- API 호출은 비용이 발생할 수 있습니다.

## 6. Ollama Llama 실행

`01_llm-api-and-prompt-basics`에서 로컬 Llama 실습을 할 때 사용합니다.

Docker Desktop이 실행 중인 상태에서 아래 명령을 실행합니다.

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

Llama 모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

확인:

```powershell
docker exec -it ollama-llm ollama list
```

Python 연결 확인:

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python .\02_ollama-docker-llama\01_ollama-health-check.py
```

## 7. pgvector PostgreSQL 실행

`05_rag-memory-and-vector-search`에서 RAG와 벡터 검색 실습을 할 때 사용합니다.

이 컨테이너는 PostgreSQL에 pgvector 확장이 포함된 이미지입니다. 따라서 PostgreSQL을 Windows에 직접 설치하지 않아도 됩니다.

```powershell
docker run -d `
 --name rag-pgvector `
 -e POSTGRES_DB=rag_db `
 -e POSTGRES_USER=rag_user `
 -e POSTGRES_PASSWORD=rag_password `
 -p 5433:5432 `
 -v rag-pgvector-data:/var/lib/postgresql/data `
 pgvector/pgvector:pg16
```

`rag-pgvector-data` volume은 PostgreSQL 데이터를 보존하는 공간입니다. 컨테이너를 지웠다가 다시 만들어도 이 volume이 남아 있으면 이전 실습 데이터가 유지될 수 있습니다.

확인:

```powershell
docker exec -it rag-pgvector psql -U rag_user -d rag_db
```

psql 종료:

```text
\q
```

## 8. LangSmith 설정

LangSmith는 선택입니다. `06_langgraph-state-flow`에서 디버깅과 추적 개념을 설명할 때 사용합니다.

`.env` 예시:

```text
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=aidev-langgraph-practice
```

처음에는 `LANGSMITH_TRACING=false`로 두고 실습해도 됩니다.

## 9. LangChain 사용 기준

LangChain은 모든 예제를 반드시 LangChain으로 작성하기 위한 도구가 아닙니다.

이 과정에서는 다음 목적일 때 LangChain을 사용합니다.

- 프롬프트 템플릿과 출력 파서를 일관된 구조로 관리할 때
- 여러 처리 단계를 체인처럼 연결하는 감각을 익힐 때
- RAG 문서 분할, Runnable, LangGraph와 연결되는 흐름을 이해할 때

반대로 단순한 LLM 호출, 아주 작은 Tool 함수, 기본 API 호출은 Python 코드만으로 먼저 이해합니다. 이렇게 해야 LLM API 자체의 원리와 프레임워크가 해주는 일을 분리해서 볼 수 있습니다.

## 10. 단원별 설치 요약

### 01_llm-api-and-prompt-basics

```powershell
pip install openai python-dotenv httpx
```

### 02_advanced-prompting-and-reasoning

```powershell
pip install openai python-dotenv pydantic
```

### 03_langchain-basics

```powershell
pip install langchain langchain-openai langchain-text-splitters python-dotenv pydantic
```

### 04_function-calling-and-tool-use

```powershell
pip install openai python-dotenv httpx pydantic
```

### 05_rag-memory-and-vector-search

```powershell
pip install openai python-dotenv psycopg[binary] langchain-text-splitters
```

### 06_langgraph-state-flow

```powershell
pip install langgraph langchain langchain-openai langchain-core openai python-dotenv
```

### 99_agent-mini-project

```powershell
pip install -r requirements.txt
```

## 11. 자주 사용하는 포트

| 포트 | 용도 |
| --- | --- |
| 11434 | Ollama |
| 5433 | RAG용 pgvector PostgreSQL |
| 8601 | 99 샘플 Streamlit 앱 |
| 8602 | 팀 템플릿 Streamlit 앱 |

## 12. 컨테이너 관리

실행 중인 컨테이너 확인:

```powershell
docker ps
```

중지:

```powershell
docker stop ollama-llm
docker stop rag-pgvector
```

재시작:

```powershell
docker start ollama-llm
docker start rag-pgvector
```

삭제:

```powershell
docker rm ollama-llm
docker rm rag-pgvector
```

모델 파일과 DB 데이터까지 삭제:

```powershell
docker volume rm ollama-data
docker volume rm rag-pgvector-data
```

주의: `rag-pgvector-data`를 삭제하면 RAG 실습에서 저장한 벡터와 대화 메모리 데이터가 사라집니다.

## 13. 첫 실행 추천 순서

완전 초보자는 아래 순서로 실행하는 것이 좋습니다.

```text
1. README.md에서 과정 흐름 확인
2. Docker Desktop 설치 여부 확인
3. Docker Desktop 실행
4. docker --version 확인
5. docker ps 확인
6. docker run hello-world로 기본 컨테이너 실행 확인
7. 01 단원 .venv 생성
8. Ollama 컨테이너 실행
9. llama3.2 모델 다운로드
10. Python에서 Ollama health check 실행
11. OpenAI API 호출 예제 실행
12. OpenAI와 Llama 결과 비교
13. 02~06 단원 순서대로 진행
```

## 14. Docker Compose 안내

04 과정에서는 Docker Compose를 사용하지 않습니다.

여러 컨테이너를 하나의 파일로 묶어 실행하는 방법, health check, restart 정책, 서비스 운영 구조는 `06_multi-agent-service-ops`에서 다룹니다.

04에서는 아래 원칙만 기억합니다.

```text
Ollama 한 개 실행 -> docker run
pgvector 한 개 실행 -> docker run
여러 서비스 운영 -> 06 과정에서 Docker Compose
```

## 15. 오류가 날 때 먼저 볼 것

1. 현재 폴더가 맞는가?
2. 가상환경이 활성화되어 있는가?
3. 필요한 패키지를 설치했는가?
4. `.env` 파일이 있는가?
5. Docker Desktop이 실행 중인가?
6. `docker ps`가 정상 동작하는가?
7. 컨테이너 이름이 중복되지 않는가?
8. 포트가 이미 사용 중이지 않은가?
9. API Key가 실제 값으로 설정되어 있는가?

자세한 오류 해결은 다음 문서를 참고합니다.

```text
00_references/07_common-errors-for-beginners.md
```
