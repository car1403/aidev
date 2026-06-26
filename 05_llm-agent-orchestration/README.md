# 05_llm-agent-orchestration

LLM Agent를 만들기 위한 오케스트레이션 과정을 학습하는 폴더입니다.

OpenAI API와 로컬 Llama 모델을 비교하면서 LLM 호출 방식을 이해하고, Prompt Engineering, Structured Output, Function Calling, Tool Use, RAG, Memory, LangGraph 상태 흐름을 순서대로 학습합니다.

이 과정의 로컬 실행 환경은 **Docker Desktop + `docker run`** 방식을 사용합니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 과정 방향

`05_llm-agent-orchestration`은 Supabase 중심 과정이 아닙니다.

앞의 `02`, `03`, `04`에서는 Supabase를 사용해 백엔드, 프론트엔드, 미니 프로젝트를 만들었습니다. 하지만 이 과정의 핵심은 데이터베이스 서비스가 아니라 **LLM이 도구를 호출하고, 여러 단계를 거쳐 판단하고, 상태를 유지하며, RAG 검색 결과를 활용하는 구조**입니다.

그래서 이 과정에서는 Supabase 대신 다음 로컬 도구를 Docker Desktop에서 단일 컨테이너로 실행합니다.

```text
Ollama 컨테이너 -> 로컬 Llama 모델 실행
pgvector 컨테이너 -> RAG 벡터 검색 실습
```

pgvector 컨테이너는 PostgreSQL에 pgvector 확장이 포함된 Docker 이미지입니다. 따라서 05 과정에서는 PostgreSQL을 Windows에 직접 설치하지 않습니다.

## 05와 07의 역할 구분

```text
05_llm-agent-orchestration
-> Docker Desktop에서 docker run으로 필요한 도구만 실행
-> LLM, Agent, Tool Calling, RAG, LangGraph 원리 학습

07_multi-agent-service-ops
-> Dockerfile, Docker Compose, Health Check, AWS, GitHub Actions
-> 서비스 운영, 배포, 자동 복구, 모니터링 학습
```

05에서는 컨테이너를 “에이전트 실습에 필요한 도구를 띄우는 방법”으로만 사용합니다. 여러 컨테이너를 파일로 묶어 실행하는 Compose는 07에서 본격적으로 학습합니다.

## 수강생 진행 기준

- 필수: OpenAI/Ollama 호출 방식 비교, 프롬프트 패턴, structured output, tool use, RAG/Memory 개념, LangGraph 상태 흐름을 실습합니다.
- 선택: LangSmith, MCP 심화, 단원별 추가 provider 비교는 수업 상황에 따라 다룹니다.
- 다음 과정으로 넘어가기 전: 단일 Agent가 상태, 도구 호출, 검색 결과를 어떤 흐름으로 사용해야 하는지 다이어그램이나 코드로 설명할 수 있어야 합니다.

## 막혔을 때 바로 보기

| 막히는 지점 | 확인 문서 |
| --- | --- |
| OpenAI API key, 비용, 호출 제한 | [OpenAI 계정과 결제 안내](../00_course-guide/02_learning-guide/environment-guide.md), [OpenAI 기본 호출](./01_llm-api-and-prompt-basics/01_openai-api-basic/README.md) |
| Docker Desktop 또는 `docker run` 오류 | [Docker 오류 해결](../00_course-guide/02_learning-guide/troubleshooting.md), [Docker Desktop 설치 안내](./00_references/09_docker-desktop-install-for-beginners.md) |
| LangGraph 상태 흐름 이해가 어려움 | [LangGraph state flow](./06_langgraph-state-flow/README.md), [Tool/RAG node flow](./06_langgraph-state-flow/03_tool-and-rag-node-flow/README.md) |
| 단원별 `.venv` 방식이 헷갈림 | [SETUP.md](./SETUP.md), [로컬 환경 체크리스트](./00_references/05_local-environment-checklist.md) |

## 학습 목표

- OpenAI API와 로컬 Llama 호출 방식의 차이를 설명할 수 있습니다.
- Docker Desktop에서 `docker run`으로 Ollama 컨테이너를 실행할 수 있습니다.
- Llama 모델을 다운로드하고 Python에서 Ollama REST API를 호출할 수 있습니다.
- 역할, 지시문, 맥락 기반 프롬프트를 설계할 수 있습니다.
- JSON Schema와 Pydantic 기반 Structured Output을 만들 수 있습니다.
- Function Calling 구조와 Tool Use 흐름을 구현할 수 있습니다.
- 여러 도구 결과를 조합하는 Multi-Tool Agent 흐름을 만들 수 있습니다.
- Embedding, Vector DB, RAG의 기본 구조를 설명할 수 있습니다.
- LangGraph의 Node, Edge, State 구조로 Agent 실행 흐름을 구성할 수 있습니다.

## 과정 구조

```text
05_llm-agent-orchestration
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

## 단원별 가상환경 기준

05 과정부터는 앞 과정과 가상환경 운영 기준이 달라집니다. `01`부터 `04`까지는 과정 최상위 `.venv` 하나로 진행하지만, 05 과정은 단원별 `.venv` 방식을 우선 권장합니다.

앞 과정의 Python/Git과 Supabase 프로젝트들은 과정 최상위 `.venv` 하나로 진행해도 충분했습니다. 하지만 05 과정은 OpenAI SDK, LangChain, LangGraph, psycopg, pydantic 등 단원별 의존성이 달라질 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
```

전체 과정을 하나의 가상환경에서 실습하고 싶다면 최상위 `requirements.txt`를 사용할 수 있습니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

정리하면 아래처럼 기억하면 됩니다.

```text
01~04: 과정 최상위 .venv 하나 사용
05: 단원별 .venv 우선 권장
06~08: 다시 과정 최상위 .venv 하나 사용
```

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

Python 예제를 실행합니다.

```powershell
cd C:\aidev\05_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python .\02_ollama-docker-llama\01_ollama-health-check.py
python .\02_ollama-docker-llama\02_ollama-generate.py
```
