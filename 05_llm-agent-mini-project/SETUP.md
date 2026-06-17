# SETUP

`05_llm-agent-mini-project` 실행 환경 설정 안내입니다.

이 과정은 `04_llm-agent-orchestration` 이후에 진행하는 LLM Agent 미니 프로젝트입니다. 기본 실행은 Python 가상환경과 Streamlit으로 진행하고, Docker는 필요한 경우에만 04에서 배운 `docker run` 방식으로 사용합니다.

Docker Compose, AWS 배포, GitHub Actions, 서비스 운영 자동화는 `06_multi-agent-service-ops`에서 진행합니다.

## 1. 작업 위치

```powershell
cd C:\aidev\05_llm-agent-mini-project
```

## 1-1. Docker 사용 기준 확인

05 과정의 기본 실행에는 Docker가 필수는 아닙니다.

```text
기본 미니 프로젝트:
- Python 가상환경
- Mock data
- LangGraph
- Streamlit

선택 확장:
- Ollama 컨테이너로 로컬 Llama 실행
- pgvector PostgreSQL 컨테이너로 RAG/Memory 저장
```

Docker Compose, AWS 배포, GitHub Actions, 서비스 운영 자동화는 06 과정에서 다룹니다.

## 1-2. Docker Desktop 설치와 첫 확인

Docker 확장을 사용할 팀은 Docker Desktop이 설치되어 있어야 합니다.

아직 설치하지 않았다면 아래 순서로 준비합니다.

1. Docker 공식 Windows 설치 문서를 엽니다.
2. Docker Desktop Installer를 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 설치 중 WSL 2 안내가 나오면 기본 안내에 따라 진행합니다.
5. 설치가 끝나면 Windows를 재부팅합니다.
6. Docker Desktop을 실행합니다.
7. Docker Desktop이 정상 실행 상태인지 확인합니다.

공식 문서:

```text
https://docs.docker.com/desktop/setup/install/windows-install/
https://docs.docker.com/desktop/features/wsl/
```

PowerShell에서 Docker 동작을 확인합니다.

```powershell
docker --version
docker ps
```

처음 설치한 학생은 아래 테스트도 실행합니다.

```powershell
docker run hello-world
```

`hello-world` 컨테이너는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

WSL 관련 오류가 나오면 아래 명령으로 상태를 확인합니다.

```powershell
wsl --status
wsl --list --verbose
```

## 2. 가상환경 만들기

```powershell
python -m venv .venv
```

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. 패키지 설치

```powershell
pip install -r requirements.txt
```

`requirements.txt`에는 기본 Agent 미니 프로젝트에 필요한 패키지와, 선택 확장인 pgvector PostgreSQL 연결용 `psycopg[binary]`가 포함되어 있습니다.

주의할 점은 `pip install -r requirements.txt`가 PostgreSQL 서버를 설치하는 것은 아니라는 점입니다. PostgreSQL은 필요한 경우 Docker의 `rag-pgvector` 컨테이너로 실행합니다.

## 5. 환경변수 만들기

```powershell
Copy-Item .env.example .env
```

`.env` 파일에 실제 값을 입력합니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

API Key가 없어도 일부 Mock 기반 LangGraph 흐름은 실행할 수 있습니다. 단, LLM 응답 생성 기능은 API Key가 있을 때 동작합니다.

## 6. 선택 사항: 로컬 Llama 모델 준비

OpenAI API 대신 로컬 LLM을 실험하고 싶다면 Docker Desktop을 실행한 뒤 04에서 배운 방식처럼 Ollama 컨테이너를 실행합니다.

```powershell
docker run -d `
  --name ollama-llm `
  -p 11434:11434 `
  -v ollama-data:/root/.ollama `
  ollama/ollama:latest
```

컨테이너가 실행되면 Llama 계열 모델을 내려받습니다.

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

정상 실행 여부는 아래 주소로 확인할 수 있습니다.

```text
http://localhost:11434
```

`.env`에는 필요할 때 아래 값을 추가합니다.

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

초보자 수업에서는 먼저 OpenAI API 또는 Mock 응답으로 Agent 흐름을 이해한 뒤, 로컬 Llama 실행은 확장 실습으로 진행하는 것을 권장합니다.

## 7. 선택 사항: pgvector 컨테이너 준비

팀 프로젝트에서 RAG 또는 장기 기억을 Vector DB에 저장하려면 로컬 pgvector 컨테이너를 사용할 수 있습니다.

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

이 컨테이너는 선택 사항입니다. 기본 미니 프로젝트는 Mock data와 Python 코드만으로도 진행할 수 있습니다.

PostgreSQL은 PC에 직접 설치하지 않습니다. `pgvector/pgvector:pg16` 이미지는 PostgreSQL과 pgvector 확장을 함께 제공하므로, Docker 컨테이너만 실행하면 됩니다.

`rag-pgvector-data` volume은 PostgreSQL 데이터를 보존하는 공간입니다. 컨테이너를 삭제해도 이 volume을 삭제하지 않으면 이전 실습 데이터가 남아 있을 수 있습니다.

`.env`에는 필요할 때 아래 값을 추가합니다.

```env
PGVECTOR_DATABASE_URL=postgresql://rag_user:rag_password@localhost:5433/rag_db
```

pgvector를 Python에서 직접 연결할 때 사용하는 패키지는 최상위 `requirements.txt`에 이미 포함되어 있습니다.

혹시 팀별 가상환경을 따로 만들었거나 `requirements.txt`를 사용하지 않았다면 아래처럼 별도로 설치할 수 있습니다.

```powershell
pip install "psycopg[binary]"
```

pgvector 컨테이너 접속 확인:

```powershell
docker exec -it rag-pgvector psql -U rag_user -d rag_db
```

psql 종료:

```text
\q
```

## 8. 강사 샘플 프로젝트 실행

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

Streamlit UI 실행:

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8701
```

확인:

```text
http://127.0.0.1:8701
```

## 9. 팀 템플릿 실행

```powershell
cd C:\aidev\05_llm-agent-mini-project\99_team-projects\llm-agent-team-template
..\..\.venv\Scripts\Activate.ps1
python backend\graph.py
streamlit run frontend\app.py --server.port 8702
```

확인:

```text
http://127.0.0.1:8702
```

## 10. 팀 프로젝트 권장 순서

```text
1. 주제 선정
2. 사용자 요청 예시 작성
3. Agent State 설계
4. Tool 함수 설계
5. LangGraph Node/Edge 설계
6. Streamlit 화면 구성
7. 테스트 체크리스트 작성
8. README/API 문서/발표 자료 작성
```

## 11. 이 과정에서 하지 않는 것

05는 LLM Agent 미니 프로젝트 완성에 집중합니다. 아래 내용은 06에서 별도 과정으로 다룹니다.

```text
Docker Compose로 여러 서비스 묶기
AWS에 서비스 배포하기
GitHub Actions로 자동 빌드/배포하기
서비스 로그와 Health Check 운영하기
장애 감지, 재시도, 자동 복구 흐름 만들기
```

## 12. Docker 오류가 날 때 먼저 볼 것

```text
1. Docker Desktop이 설치되어 있는가?
2. Docker Desktop이 실행 중인가?
3. PowerShell을 새로 열었는가?
4. docker --version이 동작하는가?
5. docker ps가 오류 없이 실행되는가?
6. 컨테이너 이름이 이미 사용 중이지 않은가?
7. 포트 11434 또는 5433을 다른 프로그램이 사용 중이지 않은가?
8. WSL 2 관련 오류가 나오지는 않는가?
```

자세한 Docker 설치와 오류 대응은 아래 문서를 참고합니다.

```text
00_references/05_docker-local-extension-guide.md
```
