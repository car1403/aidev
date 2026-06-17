# 04_llm-agent-orchestration

이 과정은 LLM Agent를 만들기 위한 오케스트레이션 수업입니다.

학생은 OpenAI API와 로컬 Llama 모델을 비교하면서 LLM 호출 방식을 이해하고, Prompt Engineering, Structured Output, Function Calling, Tool Use, RAG, Memory, LangGraph 상태 흐름을 순서대로 학습합니다.

이 과정의 로컬 실행 환경은 **Docker Desktop + `docker run`** 방식을 사용합니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 `06_multi-agent-service-ops`에서 다룹니다.

## 과정 방향

`04_llm-agent-orchestration`은 Supabase 중심 과정이 아닙니다.

앞의 `01`, `02`, `03`에서는 Supabase를 사용해 백엔드, 프론트엔드, 미니 프로젝트를 만들었습니다. 하지만 이 과정의 핵심은 데이터베이스 서비스가 아니라 **LLM이 도구를 호출하고, 여러 단계를 거쳐 판단하고, 상태를 유지하며, RAG 검색 결과를 활용하는 구조**입니다.

그래서 이 과정에서는 Supabase 대신 다음 로컬 도구를 Docker Desktop에서 단일 컨테이너로 실행합니다.

```text
Ollama 컨테이너        -> 로컬 Llama 모델 실행
pgvector 컨테이너     -> RAG 벡터 검색 실습
```

pgvector 컨테이너는 PostgreSQL에 pgvector 확장이 포함된 Docker 이미지입니다. 따라서 04 과정에서는 PostgreSQL을 Windows에 직접 설치하지 않습니다.

## 04와 06의 역할 구분

```text
04_llm-agent-orchestration
-> Docker Desktop에서 docker run으로 필요한 도구만 실행
-> LLM, Agent, Tool Calling, RAG, LangGraph 원리 학습

06_multi-agent-service-ops
-> Dockerfile, Docker Compose, Health Check, AWS, GitHub Actions
-> 서비스 운영, 배포, 자동 복구, 모니터링 학습
```

04에서는 컨테이너를 “에이전트 실습에 필요한 도구를 띄우는 방법”으로만 사용합니다. 여러 컨테이너를 파일로 묶어 실행하는 Compose는 06에서 본격적으로 학습합니다.

## 학습 목표

이 과정을 마치면 학생은 다음 내용을 설명하고 구현할 수 있어야 합니다.

- OpenAI API와 로컬 Llama 호출 방식의 차이를 설명할 수 있다.
- Docker Desktop에서 `docker run`으로 Ollama 컨테이너를 실행할 수 있다.
- Llama 모델을 다운로드하고 Python에서 Ollama REST API를 호출할 수 있다.
- 역할, 지시문, 맥락 기반 프롬프트를 설계할 수 있다.
- JSON Schema와 Pydantic 기반 Structured Output을 만들 수 있다.
- Function Calling 구조와 Tool Use 흐름을 구현할 수 있다.
- 여러 도구 결과를 조합하는 Multi-Tool Agent 흐름을 만들 수 있다.
- Embedding, Vector DB, RAG의 기본 구조를 설명할 수 있다.
- Docker run으로 pgvector PostgreSQL 컨테이너를 실행하고 벡터 검색을 실습할 수 있다.
- LangGraph의 Node, Edge, State 구조로 Agent 실행 흐름을 구성할 수 있다.
- 일정 조정 에이전트 미니 프로젝트를 구현하고 발표할 수 있다.

## 과정 구조

```text
04_llm-agent-orchestration
├─ README.md
├─ SETUP.md
├─ 00_references
├─ 01_llm-api-and-prompt-basics
├─ 02_advanced-prompting-and-reasoning
├─ 03_langchain-basics
├─ 04_function-calling-and-tool-use
├─ 05_rag-memory-and-vector-search
├─ 06_langgraph-state-flow
└─ 99_agent-mini-project
```

문서 구조는 학생들이 수업 중 헷갈리지 않도록 단순하게 유지합니다.

- `README.md`: 과정 전체 흐름, 학습 목표, 단원 요약, 실행 방향
- `SETUP.md`: Python, 가상환경, Docker Desktop, Ollama, pgvector 실행 방법
- `00_references`: 수업 전후에 참고할 개념 설명과 점검 자료
- `01`~`99` 단원별 `README.md`: 각 단원에서 무엇을 배우고 어떤 파일을 실행하는지 안내

각 단원 폴더에는 실습 코드, 필요한 설정 파일, 단원별 `README.md`를 둡니다. 세부 개념 설명과 전체 기준은 최상위 README, SETUP, `00_references`에서 확인합니다.

## 권장 학습 순서

```text
00_references
-> 01_llm-api-and-prompt-basics
-> 02_advanced-prompting-and-reasoning
-> 03_langchain-basics
-> 04_function-calling-and-tool-use
-> 05_rag-memory-and-vector-search
-> 06_langgraph-state-flow
-> 99_agent-mini-project
```

## 처음 시작하는 학생용 순서

아래 순서대로 진행하면 됩니다.

1. [SETUP.md](./SETUP.md)를 열고 Python과 Docker Desktop을 확인합니다.
2. `01_llm-api-and-prompt-basics` 폴더에서 `.venv`를 만듭니다.
3. `.env.example`을 `.env`로 복사합니다.
4. OpenAI API Key가 있으면 `.env`에 입력합니다.
5. Docker Desktop을 실행합니다.
6. `docker ps` 명령으로 Docker가 동작하는지 확인합니다.
7. `docker run`으로 Ollama 컨테이너를 실행합니다.
8. `llama3.2` 모델을 다운로드합니다.
9. Python 예제로 Ollama 연결을 확인합니다.
10. OpenAI API 호출 예제와 Llama 호출 예제를 비교합니다.
11. 이후 프롬프트, Tool Calling, RAG, LangGraph 순서로 진행합니다.

OpenAI API Key가 아직 없으면 OpenAI 호출 실습은 건너뛰고, Docker/Ollama/Llama 실습부터 진행해도 됩니다.

## 단원 요약

| 단원 | 핵심 내용 |
| --- | --- |
| `01_llm-api-and-prompt-basics` | OpenAI API, Docker/Ollama Llama, 모델 비교 |
| `02_advanced-prompting-and-reasoning` | Role/Instruction/Context, CoT/ReAct, Structured Output, Prompt Injection |
| `03_langchain-basics` | LangChain 개념, PromptTemplate, Runnable, Chain, Document Loader |
| `04_function-calling-and-tool-use` | Function Calling, 외부 API Tool, Multi-Tool Agent, MCP 개념 |
| `05_rag-memory-and-vector-search` | Embedding, pgvector, Chunking, RAG, Memory |
| `06_langgraph-state-flow` | LangGraph Node/Edge/State, 조건 라우팅, Tool/RAG Node, LangSmith |
| `99_agent-mini-project` | 일정 조정 Agent 미니 프로젝트 |

## 커리큘럼 점검 요약

이 과정은 이미지 기준 커리큘럼의 핵심 흐름을 다음과 같이 반영합니다.

| 구분 | 반영 내용 |
| --- | --- |
| 고급 프롬프트 및 추론 전략 | Role, Instruction, Context, CoT, ReAct, Structured Output, Prompt Injection |
| Function Calling 및 오케스트레이션 | Python 함수 Tool, 외부 API Tool, Multi-Tool Agent, MCP 개념 비교 |
| 지식 저장소 및 장기 기억 | Embedding, pgvector, RAG, Session Memory, Long-term Memory, Hybrid Search/RRF |
| 상태 기계 기반 흐름 제어 | LangGraph Node, Edge, State, 조건 분기, Self-Reflection, Planning, Tracing |
| 미니 프로젝트 | 일정 조정 Agent를 통해 Tool, Memory, Graph 흐름 통합 |

세부 점검표와 lab 운영 기준은 [00_references/10_curriculum-and-lab-review.md](./00_references/10_curriculum-and-lab-review.md)에 정리합니다.

## 단원별 가상환경 기준

이 과정은 단원별 `.venv` 방식을 권장합니다.

앞 과정의 Supabase 프로젝트들은 과정 최상위 `.venv` 하나로 진행해도 충분했습니다. 하지만 04 과정은 OpenAI SDK, LangChain, LangGraph, psycopg, pydantic 등 단원별 의존성이 달라질 수 있습니다.

따라서 각 단원 폴더에서 다음 흐름으로 시작하는 것이 좋습니다.

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install openai python-dotenv httpx
```

전체 과정을 하나의 가상환경에서 실습하고 싶다면 최상위 [requirements.txt](C:/aidev/04_llm-agent-orchestration/requirements.txt)를 사용할 수 있습니다.

```powershell
cd C:\aidev\04_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

강의에서는 단원별 `.venv`를 기본으로 안내하고, 빠른 통합 실습이나 복습용으로만 최상위 `requirements.txt`를 사용하는 것을 권장합니다.

## Docker run으로 Ollama 실행

Docker Desktop을 먼저 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

Ollama 컨테이너를 실행합니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

Llama 모델을 다운로드합니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

모델 목록을 확인합니다.

```powershell
docker exec -it ollama-llm ollama list
```

Python 예제를 실행합니다.

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python .\02_ch2_ollama-docker-llama\01_ollama-health-check.py
python .\02_ch2_ollama-docker-llama\02_ollama-generate.py
```

## Docker run으로 pgvector 실행

RAG 단원에서는 벡터를 저장하고 검색하기 위해 pgvector PostgreSQL 컨테이너를 사용합니다.

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

`-v rag-pgvector-data:/var/lib/postgresql/data`는 PostgreSQL 데이터를 Docker volume에 저장한다는 뜻입니다. 컨테이너를 삭제해도 이 volume을 지우지 않으면 실습 데이터가 남아 있습니다.

접속 확인:

```powershell
docker exec -it rag-pgvector psql -U rag_user -d rag_db
```

psql에서 빠져나올 때:

```text
\q
```

## Compose를 사용하지 않는 이유

04 과정에서는 Docker Compose를 사용하지 않습니다.

이유는 단순합니다. 04의 목적은 인프라 운영이 아니라 Agent 구조 학습입니다. 초보자가 처음부터 Compose까지 함께 배우면 다음 개념이 동시에 섞입니다.

- LLM API 호출
- Tool Calling
- RAG
- LangGraph
- Docker 컨테이너
- Docker 네트워크
- Compose 서비스 정의

그래서 04에서는 `docker run`으로 컨테이너 한 개씩 직접 실행합니다. 여러 서비스를 묶고, health check를 붙이고, 장애 대응과 배포까지 연결하는 내용은 `06_multi-agent-service-ops`에서 다룹니다.

## 자주 사용하는 Docker 명령

실행 중인 컨테이너 확인:

```powershell
docker ps
```

중지:

```powershell
docker stop ollama-llm
docker stop rag-pgvector
```

다시 시작:

```powershell
docker start ollama-llm
docker start rag-pgvector
```

삭제:

```powershell
docker rm ollama-llm
docker rm rag-pgvector
```

데이터 volume까지 삭제:

```powershell
docker volume rm ollama-data
docker volume rm rag-pgvector-data
```

주의: `rag-pgvector-data` volume을 삭제하면 pgvector PostgreSQL에 저장한 벡터, 문서 chunk, 대화 메모리 데이터가 함께 삭제됩니다.

전체 컨테이너 목록 확인:

```powershell
docker ps -a
```

## 새롭게 나오는 기술 설명

### LLM

LLM은 Large Language Model의 줄임말입니다. 자연어 질문을 이해하고 답변, 요약, 분류, 코드 작성 같은 작업을 수행하는 모델입니다.

### OpenAI API

OpenAI API는 클라우드에 있는 LLM을 HTTP API로 호출하는 방식입니다. 모델 실행은 OpenAI 서버에서 이루어지고, 우리는 요청과 응답을 주고받습니다.

### Llama

Llama는 Meta에서 공개한 오픈소스 계열 LLM입니다. 이 과정에서는 Llama 모델을 내 PC에서 직접 실행해 클라우드 LLM과 비교합니다.

### Ollama

Ollama는 Llama 같은 로컬 LLM을 쉽게 실행할 수 있게 도와주는 도구입니다. 이 과정에서는 Ollama를 PC에 직접 설치하지 않고 Docker 컨테이너로 실행합니다.

### Docker

Docker는 실행 환경을 컨테이너로 분리해서 실행하는 도구입니다. 04 과정에서는 Docker를 운영 배포 도구로 깊게 배우기보다, 로컬 LLM과 pgvector를 간단히 실행하는 도구로 사용합니다.

### Docker Image

Docker Image는 컨테이너를 만들기 위한 템플릿입니다. 예를 들어 `ollama/ollama:latest` 이미지는 Ollama 서버를 실행할 준비가 된 이미지입니다.

### Docker Container

Container는 이미지로부터 실제 실행된 환경입니다. `ollama-llm` 컨테이너는 로컬 Llama 모델을 실행하는 서버 역할을 합니다.

### Docker Volume

Volume은 컨테이너 밖에 데이터를 저장하는 공간입니다. `ollama-data` 볼륨에는 다운로드한 Llama 모델 파일이 저장되고, `rag-pgvector-data` 볼륨에는 PostgreSQL 데이터가 저장됩니다. 컨테이너를 삭제해도 볼륨을 지우지 않으면 모델 파일과 DB 데이터가 남아 있을 수 있습니다.

### Prompt Engineering

Prompt Engineering은 LLM에게 원하는 방식으로 응답하도록 역할, 지시문, 맥락, 출력 형식을 설계하는 작업입니다.

### Structured Output

Structured Output은 LLM 응답을 자유 문장이 아니라 JSON 같은 정해진 구조로 받는 방식입니다. API나 프로그램에서 LLM 응답을 안정적으로 처리할 때 중요합니다.

### Function Calling

Function Calling은 LLM이 직접 모든 답을 만들지 않고, 필요한 함수를 선택해 호출하도록 만드는 구조입니다. 예를 들어 날씨 조회, 계산, 일정 검색 같은 작업을 Tool로 분리할 수 있습니다.

### Tool

Tool은 LLM이 사용할 수 있는 외부 기능입니다. Python 함수, 외부 API, 검색 함수, 계산 함수, DB 조회 함수가 Tool이 될 수 있습니다.

### MCP

MCP는 Model Context Protocol의 줄임말입니다. LLM이 외부 도구나 데이터 소스와 표준화된 방식으로 연결되도록 돕는 개념입니다. 04 과정에서는 MCP를 깊게 구현하기보다 Function Calling과 비교하며 구조를 이해합니다.

### Embedding

Embedding은 문장을 숫자 벡터로 바꾸는 기술입니다. 의미가 비슷한 문장은 벡터 공간에서도 가까운 위치에 놓이도록 만듭니다.

### Vector DB

Vector DB는 embedding 벡터를 저장하고 비슷한 벡터를 빠르게 검색하는 저장소입니다.

### pgvector

pgvector는 PostgreSQL에서 벡터를 저장하고 검색할 수 있게 해주는 확장입니다. 이 과정에서는 PostgreSQL을 직접 설치하지 않고, Docker run으로 pgvector PostgreSQL 컨테이너를 실행해 RAG 검색 원리를 실습합니다.

### RAG

RAG는 Retrieval-Augmented Generation의 줄임말입니다. LLM이 바로 답을 생성하기 전에 관련 문서를 검색하고, 검색 결과를 참고해 답변을 만드는 구조입니다.

### Memory

Memory는 Agent가 이전 대화나 작업 상태를 기억하는 구조입니다. 단기 메모리는 현재 대화 흐름을 유지하고, 장기 메모리는 나중에 다시 찾을 정보를 저장합니다.

### LangChain

LangChain은 LLM 호출, 프롬프트, 출력 파서, 도구, 체인을 연결하는 Python 프레임워크입니다.

### LangGraph

LangGraph는 Agent의 실행 흐름을 그래프처럼 구성하는 도구입니다. Node, Edge, State를 사용해 조건 분기, 반복 실행, Tool 호출 흐름을 만들 수 있습니다.

### LangSmith

LangSmith는 LangChain/LangGraph 실행 과정을 추적하고 디버깅하는 도구입니다. 이 과정에서는 선택 도구로 다룹니다.

## 오류가 날 때 먼저 볼 것

1. 현재 폴더가 맞는가?
2. `.venv`가 활성화되어 있는가?
3. 필요한 패키지를 설치했는가?
4. `.env` 파일이 있는가?
5. Docker Desktop이 실행 중인가?
6. `docker ps`가 정상 동작하는가?
7. 컨테이너 이름이 중복되지 않는가?
8. 포트 `11434` 또는 `5433`이 이미 사용 중이지 않은가?
9. Llama 모델을 다운로드했는가?
10. OpenAI API Key가 필요한 실습인지 확인했는가?

## 최종 목표

학생은 이 과정을 마친 뒤 다음을 말로 설명하고 코드로 구현할 수 있어야 합니다.

```text
LLM은 언제 직접 답하고, 언제 Tool을 호출해야 하는가?
로컬 Llama와 OpenAI API는 어떤 차이가 있는가?
RAG는 왜 필요한가?
Agent의 상태 흐름은 어떻게 설계하는가?
Docker run으로 로컬 LLM/RAG 실습 환경을 어떻게 준비하는가?
Compose와 운영 배포는 왜 06 과정에서 따로 배우는가?
```
