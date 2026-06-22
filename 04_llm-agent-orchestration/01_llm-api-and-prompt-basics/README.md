# 01 LLM API and Prompt Basics

이 단원은 04 과정의 첫 번째 실습입니다. 클라우드 LLM인 OpenAI API와 Docker/Ollama로 실행하는 로컬 Llama를 비교하면서 LLM 호출 방식의 차이를 이해합니다.

04 과정에서는 01~03 과정과 달리 Supabase를 사용하지 않습니다. 이 단원부터는 Agent 구조 학습을 위해 Docker Desktop과 `docker run` 기반 로컬 실습 환경을 함께 사용합니다.

## 학습 목표

- `.env` 파일에 API Key와 모델명을 설정하는 방법을 이해합니다.
- OpenAI API를 Python에서 호출하는 기본 흐름을 익힙니다.
- Docker Desktop에서 Ollama 컨테이너를 실행하고 Llama 모델을 호출합니다.
- 같은 질문을 OpenAI와 Llama에 보내고 응답 차이를 비교합니다.
- LLM을 사용할 때 클라우드 모델과 로컬 모델의 장단점을 구분합니다.

## 폴더 구성

```text
01_llm-api-and-prompt-basics
├─.env.example
├─ 01_ch1_openai-api-basic
│ ├─ 01_check-env.py
│ ├─ 02_openai-basic-response.py
│ └─ 03_openai-message-style.py
├─ 02_ch2_ollama-docker-llama
│ ├─ 01_ollama-health-check.py
│ └─ 02_ollama-generate.py
└─ 03_ch3_openai-vs-llama-comparison
 ├─ 01_compare-basic-answer.py
 └─ 02_compare-prompt-style.py
```

## 실습 시작 순서

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
python -m venv.venv
.\.venv\Scripts\Activate.ps1
pip install openai python-dotenv httpx
Copy-Item.env.example.env
```

`.env` 파일을 열어 OpenAI API Key가 있으면 입력합니다. OpenAI API Key가 없어도 Ollama/Llama 실습은 진행할 수 있습니다.

## 실행 순서

```powershell
python.\01_ch1_openai-api-basic\01_check-env.py
python.\01_ch1_openai-api-basic\02_openai-basic-response.py
python.\01_ch1_openai-api-basic\03_openai-message-style.py
```

Docker Desktop에서 Ollama 컨테이너를 실행한 뒤 로컬 Llama 예제를 실행합니다.

```powershell
python.\02_ch2_ollama-docker-llama\01_ollama-health-check.py
python.\02_ch2_ollama-docker-llama\02_ollama-generate.py
```

마지막으로 두 모델의 응답 차이를 비교합니다.

```powershell
python.\03_ch3_openai-vs-llama-comparison\01_compare-basic-answer.py
python.\03_ch3_openai-vs-llama-comparison\02_compare-prompt-style.py
```

## 수업 중 확인 질문

- OpenAI API와 로컬 Llama는 실행 위치가 어떻게 다른가요?
- `.env` 파일에 API Key를 넣는 이유는 무엇인가요?
- 같은 질문을 보내도 모델별 답변이 달라지는 이유는 무엇인가요?
- 로컬 Llama는 비용과 보안 측면에서 어떤 장점이 있나요?

