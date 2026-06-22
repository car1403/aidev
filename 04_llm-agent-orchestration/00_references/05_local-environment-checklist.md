# 05 Local Environment Checklist

이 과정은 Python, Docker, OpenAI API, Streamlit, LangGraph 등을 사용합니다.

수업 전에 아래 항목을 확인하면 실습 중 오류를 줄일 수 있습니다.

## Python

```powershell
python --version
pip --version
```

권장:

```text
Python 3.11 이상
```

## 가상 환경

각 단원 폴더에서 가상 환경을 만드는 방식을 권장합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

단원별로 패키지가 다르기 때문에, 초보자 수업에서는 단원별 가상 환경이 오류 추적에 더 쉽습니다.

## Docker

Docker Desktop이 설치되어 있어야 합니다.

```powershell
docker --version
docker ps
```

Docker Desktop이 실행 중이어야 합니다.

Docker를 처음 설치한 수업 참여자는 아래 문서를 먼저 확인합니다.

```text
00_references/09_docker-desktop-install-for-beginners.md
```

설치 후에는 기본 테스트 컨테이너를 한 번 실행해 봅니다.

```powershell
docker run hello-world
```

`hello-world` 컨테이너는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

## OpenAI API Key

`.env` 파일에 다음 값이 있어야 합니다.

```text
OPENAI_API_KEY=your-openai-api-key
```

## Ollama

로컬 Llama 실습에서는 Ollama 컨테이너가 필요합니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

## pgvector

RAG 실습에서는 pgvector PostgreSQL이 필요합니다.

PostgreSQL은 PC에 직접 설치하지 않고, pgvector가 포함된 PostgreSQL Docker 컨테이너로 실행합니다.

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

## 자주 사용하는 포트

| 포트 | 용도 |
| --- | --- |
| 11434 | Ollama |
| 5433 | RAG용 pgvector PostgreSQL |
| 8601 | 99 샘플 Streamlit 앱 |

## 수업 전 최종 체크

- [ ] Python이 설치되어 있다.
- [ ] Docker Desktop이 설치되어 있다.
- [ ] Docker Desktop이 실행된다.
- [ ] `docker --version`이 정상 동작한다.
- [ ] `docker ps`가 오류 없이 실행된다.
- [ ] `docker run hello-world`가 성공한다.
- [ ] OpenAI API Key가 준비되어 있다.
- [ ] `.env` 파일을 만들 수 있다.
- [ ] PowerShell에서 가상 환경을 활성화할 수 있다.
- [ ] 브라우저에서 localhost 주소를 열 수 있다.
