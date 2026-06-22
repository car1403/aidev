# 02_ch2_ollama-docker-llama

이 챕터에서는 Docker Desktop에서 Ollama 컨테이너를 실행하고 로컬 Llama 모델을 호출합니다.

## 핵심 개념

- Ollama는 로컬 LLM을 쉽게 실행하게 해주는 도구입니다.
- 04 과정에서는 Ollama를 PC에 직접 설치하지 않고 Docker 컨테이너로 실행합니다.
- OpenAI API와 달리 로컬 Llama는 내 PC의 자원을 사용합니다.

## 실행 전 준비

최상위 `SETUP.md`의 Ollama 실행 명령을 먼저 완료합니다.

```powershell
docker ps
docker exec -it ollama-llm ollama list
```

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python.\02_ch2_ollama-docker-llama\01_ollama-health-check.py
python.\02_ch2_ollama-docker-llama\02_ollama-generate.py
```

## 확인 질문

- Docker 컨테이너는 어떤 역할을 하나요?
- 로컬 Llama는 인터넷 API 호출과 무엇이 다른가요?
- Ollama 서버가 켜져 있는지 어떻게 확인할 수 있나요?

