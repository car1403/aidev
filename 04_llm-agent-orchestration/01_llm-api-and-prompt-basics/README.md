# 01 LLM API and Prompt Basics

이 단원은 04 과정의 첫 번째 실습입니다. 클라우드 LLM인 OpenAI API와 Docker/Ollama로 실행하는 로컬 Llama를 비교하면서 LLM 호출 방식의 차이를 이해합니다.

04 과정에서는 01~03 과정과 달리 Supabase를 사용하지 않습니다. 이 단원부터는 Agent 구조 학습을 위해 Docker Desktop과 `docker run` 기반 로컬 실습 환경을 함께 사용합니다.

이 단원에서 가장 중요한 기준은 다음입니다.

```text
OpenAI API -> 인터넷을 통해 OpenAI 서버의 모델을 호출
Ollama/Llama -> Docker 컨테이너 안에서 로컬 LLM 서버를 실행하고 호출
```

OpenAI API Key가 준비되지 않아도 `02_ollama-docker-llama` 실습은 진행할 수 있습니다. 반대로 Docker Desktop이 아직 준비되지 않았다면 `01_openai-api-basic`만 먼저 진행할 수 있습니다.

## 학습 목표

- `.env` 파일에 API Key와 모델명을 설정하는 방법을 이해합니다.
- OpenAI API를 Python에서 호출하는 기본 흐름을 익힙니다.
- Docker Desktop에서 Ollama 컨테이너를 실행하고 Llama 모델을 호출합니다.
- 같은 질문을 OpenAI와 Llama에 보내고 응답 차이를 비교합니다.
- LLM을 사용할 때 클라우드 모델과 로컬 모델의 장단점을 구분합니다.

## 폴더 구성

```text
01_llm-api-and-prompt-basics
├─ .env.example
├─ 00_references
│  └─ README.md
├─ 01_openai-api-basic
│  ├─ README.md
│  ├─ 01_check-env.py
│  ├─ 02_openai-basic-response.py
│  └─ 03_openai-message-style.py
├─ 02_ollama-docker-llama
│  ├─ README.md
│  ├─ 01_ollama-health-check.py
│  └─ 02_ollama-generate.py
├─ 03_openai-vs-llama-comparison
│  ├─ README.md
│  ├─ 01_compare-basic-answer.py
│  └─ 02_compare-prompt-style.py
├─ 10_labs
└─ 20_assignments
```

## 실습 시작 순서

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv httpx
Copy-Item .env.example .env
```

이 단원의 `.env`는 `C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics\.env` 파일입니다. 다른 단원이나 다른 프로젝트의 `.env`가 아니라, 현재 단원 폴더 안의 `.env`를 사용합니다.

`.env` 파일을 열어 OpenAI API Key가 있으면 입력합니다. OpenAI API Key가 없어도 Ollama/Llama 실습은 진행할 수 있습니다.

## 1단계. OpenAI API 기본 호출

```powershell
python .\01_openai-api-basic\01_check-env.py
python .\01_openai-api-basic\02_openai-basic-response.py
python .\01_openai-api-basic\03_openai-message-style.py
```

`01_check-env.py`는 실제 API Key 값을 출력하지 않고 설정 여부만 알려줍니다. API Key가 없으면 나머지 OpenAI 예제는 안전하게 호출을 건너뜁니다.

## 2단계. Docker/Ollama/Llama 실행

Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

Ollama 컨테이너가 아직 없다면 다음 명령으로 실행합니다.

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
docker exec -it ollama-llm ollama list
```

그 다음 로컬 Llama 예제를 실행합니다.

```powershell
python .\02_ollama-docker-llama\01_ollama-health-check.py
python .\02_ollama-docker-llama\02_ollama-generate.py
```

## 3단계. OpenAI와 Llama 비교

마지막으로 두 모델의 응답 차이를 비교합니다. OpenAI API Key가 없으면 OpenAI 결과에는 “호출하지 않았습니다”라는 안내가 나오고, Llama 결과만 확인할 수 있습니다.

```powershell
python .\03_openai-vs-llama-comparison\01_compare-basic-answer.py
python .\03_openai-vs-llama-comparison\02_compare-prompt-style.py
```

## 실습 결과를 볼 때의 기준

| 기준 | OpenAI API | 로컬 Llama |
| --- | --- | --- |
| 실행 위치 | OpenAI 클라우드 서버 | 내 PC의 Docker 컨테이너 |
| 준비물 | API Key, 인터넷 연결 | Docker Desktop, Ollama 컨테이너, 모델 다운로드 |
| 비용 | API 사용량에 따라 비용 발생 가능 | API 비용은 없지만 PC 자원 사용 |
| 장점 | 응답 품질과 안정성이 높음 | 로컬 실행 구조를 직접 이해하기 좋음 |
| 주의점 | Key 관리와 비용 관리 필요 | 모델 다운로드와 PC 성능 확인 필요 |

## 수업 중 확인 질문

- OpenAI API와 로컬 Llama는 실행 위치가 어떻게 다른가요?
- `.env` 파일에 API Key를 넣는 이유는 무엇인가요?
- 같은 질문을 보내도 모델별 답변이 달라지는 이유는 무엇인가요?
- 로컬 Llama는 비용과 보안 측면에서 어떤 장점이 있나요?
- 앞으로 Tool Calling이나 RAG를 만들 때 어떤 상황에서 클라우드 모델과 로컬 모델을 선택하면 좋을까요?
