# SETUP

`05_llm-agent-orchestration` 과정의 개발 환경 설정 문서입니다.

이 과정은 앞 과정과 달리 **단원별 `.venv` 방식을 우선 권장**합니다. OpenAI SDK, LangChain, LangGraph, pgvector, psycopg 등 단원별 의존성이 달라질 수 있기 때문입니다.

## 0. 가상환경 기준

```text
01~04 과정: 과정 최상위 .venv 하나 사용
05 과정   : 단원별 .venv 우선 권장
06~08 과정: 과정 최상위 .venv 하나 사용
```

전체 과정을 하나의 `.venv`로 빠르게 복습하고 싶다면 최상위 `requirements.txt`를 사용할 수 있지만, 수업 기본 흐름은 단원별 `.venv`입니다.

## 1. 작업 위치 확인

```powershell
cd C:\aidev\05_llm-agent-orchestration
```

## 2. Docker Desktop 확인

05 과정부터는 Docker Desktop을 사용합니다. 여기서는 Docker Compose 운영을 배우기보다, Agent 실습에 필요한 Ollama와 pgvector 같은 도구를 `docker run`으로 실행합니다.

```powershell
docker --version
docker ps
```

Docker Compose, AWS, GitHub Actions, 운영 자동화는 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 3. 단원별 가상환경 만들기

예를 들어 첫 단원을 시작할 때는 아래처럼 진행합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
```

정상이라면 `python -c "import sys; print(sys.executable)"` 결과가 현재 단원 폴더 아래의 `.venv\Scripts\python.exe`를 가리켜야 합니다.

```text
C:\aidev\05_llm-agent-orchestration\01_llm-api-and-prompt-basics\.venv\Scripts\python.exe
```

## 4. 선택: 최상위 requirements.txt 사용

복습이나 통합 실습을 위해 하나의 가상환경으로 진행하려면 아래 방식을 사용할 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip
pip install -r requirements.txt
```

단, 이 방식은 빠른 통합 실습용입니다. 수업에서는 단원별 `.venv`를 우선합니다.

## 5. Ollama 컨테이너 실행

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

모델을 다운로드합니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
docker exec -it ollama-llm ollama list
```

## 6. pgvector 컨테이너 실행

RAG와 벡터 검색 실습에서는 pgvector PostgreSQL 컨테이너를 사용합니다. 단원 README에서 필요한 시점에 실행합니다.

```powershell
docker run -d `
 --name aidev-pgvector `
 -p 5432:5432 `
 -e POSTGRES_PASSWORD=postgres `
 pgvector/pgvector:pg16
```

## 체크리스트

```text
[ ] Docker Desktop이 실행 중인가?
[ ] docker ps가 오류 없이 실행되는가?
[ ] 05 과정은 단원별 .venv 우선이라는 점을 확인했는가?
[ ] Ollama 컨테이너가 실행되는가?
[ ] 필요한 단원에서 pgvector 컨테이너를 실행할 수 있는가?
```
