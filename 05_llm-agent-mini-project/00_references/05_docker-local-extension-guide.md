# 05 Docker Local Extension Guide

이 문서는 `05_llm-agent-mini-project`에서 Docker를 선택적으로 사용하는 팀을 위한 안내입니다.

05의 기본 목표는 LLM Agent 미니 프로젝트를 완성하는 것입니다. Docker는 필수가 아니라, 04에서 배운 로컬 실행 환경을 프로젝트에 붙이고 싶을 때 사용하는 확장 도구입니다.

## 05에서 Docker를 쓰는 경우

```text
OpenAI API 대신 로컬 Llama 응답을 실험하고 싶다
-> Ollama 컨테이너 사용

RAG 문서나 장기 메모리를 Vector DB에 저장하고 싶다
-> pgvector PostgreSQL 컨테이너 사용
```

기본 프로젝트는 Mock data와 Python 코드만으로도 진행할 수 있습니다. 초보자 팀은 먼저 Mock data로 Agent 흐름을 완성한 뒤 Docker 확장을 붙이는 것을 권장합니다.

## 설치 전 이해할 것

```text
Docker Desktop:
- Windows에서 Docker 컨테이너를 실행하는 프로그램

WSL 2:
- Windows 안에서 Linux 실행 환경을 제공하는 기능
- Docker Desktop은 Windows에서 Linux 컨테이너를 실행할 때 WSL 2를 주로 사용

Image:
- 컨테이너를 만들기 위한 템플릿

Container:
- Image를 실제로 실행한 것

Volume:
- 컨테이너 밖에 데이터를 저장하는 공간
```

## Docker Desktop 설치

아직 Docker Desktop이 없다면 아래 순서로 설치합니다.

1. Docker 공식 Windows 설치 문서를 엽니다.
2. Docker Desktop Installer를 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 설치 중 WSL 2 안내가 나오면 기본 안내에 따라 진행합니다.
5. 설치가 끝나면 Windows를 재부팅합니다.
6. Docker Desktop을 실행합니다.

공식 문서:

```text
https://docs.docker.com/desktop/setup/install/windows-install/
https://docs.docker.com/desktop/features/wsl/
```

## 설치 후 확인

PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

처음 설치했다면 기본 테스트 컨테이너를 실행합니다.

```powershell
docker run hello-world
```

`hello-world`는 메시지를 출력하고 바로 종료됩니다. 계속 실행되지 않아도 정상입니다.

## Ollama 컨테이너

로컬 Llama 모델을 실험할 때 사용합니다.

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

## pgvector PostgreSQL 컨테이너

RAG 또는 장기 메모리를 저장할 때 사용합니다.

PostgreSQL은 PC에 직접 설치하지 않습니다. `pgvector/pgvector:pg16` 이미지에 PostgreSQL과 pgvector 확장이 함께 들어 있습니다.

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

접속 확인:

```powershell
docker exec -it rag-pgvector psql -U rag_user -d rag_db
```

psql 종료:

```text
\q
```

## 자주 쓰는 Docker 명령

```powershell
docker ps
docker ps -a
docker stop ollama-llm
docker start ollama-llm
docker stop rag-pgvector
docker start rag-pgvector
docker rm ollama-llm
docker rm rag-pgvector
```

데이터까지 삭제할 때만 volume을 삭제합니다.

```powershell
docker volume rm ollama-data
docker volume rm rag-pgvector-data
```

주의: `rag-pgvector-data`를 삭제하면 pgvector PostgreSQL에 저장한 RAG 문서와 대화 메모리 데이터가 사라집니다.

## 오류가 날 때

### docker 명령을 찾을 수 없는 경우

```text
1. Docker Desktop 설치 여부 확인
2. Docker Desktop 실행
3. PowerShell을 닫고 다시 열기
4. docker --version 다시 실행
5. 계속 실패하면 PC 재부팅
```

### Docker daemon 오류가 나는 경우

```text
1. Docker Desktop 실행
2. Docker Desktop이 완전히 실행될 때까지 기다림
3. docker ps 다시 실행
4. Docker Desktop 재시작
5. PC 재부팅
```

### WSL 관련 오류가 나는 경우

```powershell
wsl --status
wsl --list --verbose
```

WSL 2가 준비되지 않았다는 메시지가 나오면 Docker 공식 WSL 문서와 Windows 업데이트 상태를 확인합니다.

## 05와 06의 경계

05에서는 아래까지만 사용합니다.

```text
docker run
docker exec
docker ps
docker stop
docker start
docker rm
docker volume rm
```

아래 내용은 06에서 다룹니다.

```text
Dockerfile
Docker Compose
Health Check
Restart Policy
AWS 배포
GitHub Actions
서비스 운영 자동화
```

## 직접 기억할 문장

```text
05에서 Docker는 프로젝트 확장 도구입니다.
먼저 Mock data로 Agent 흐름을 완성하고, 필요한 팀만 Ollama 또는 pgvector를 붙입니다.
```
