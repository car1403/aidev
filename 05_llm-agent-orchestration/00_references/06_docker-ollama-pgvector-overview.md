# 06 Docker, Ollama, pgvector Overview

이 과정에서 Docker는 두 가지 실습에 사용됩니다.

```text
Ollama로 로컬 Llama 실행
pgvector PostgreSQL 실행
```

## Docker Compose를 꼭 써야 하나요?

아니요. 04 과정에서는 Docker Compose를 사용하지 않습니다.

서비스 하나를 실행할 때는 `docker run`이 초보자에게 더 직접적입니다.

```text
Ollama 하나 실행 -> docker run
pgvector PostgreSQL 하나 실행 -> docker run
여러 서비스를 묶어 운영 -> 07 과정에서 Docker Compose
```

## Ollama

Ollama는 로컬에서 Llama 같은 모델을 실행할 수 있게 해줍니다.

실행:

```powershell
docker run -d `
 --name ollama-llm `
 -p 11434:11434 `
 -v ollama-data:/root/.ollama `
 ollama/ollama:latest
```

확인:

```powershell
docker exec -it ollama-llm ollama list
```

모델 다운로드:

```powershell
docker exec -it ollama-llm ollama pull llama3.2
```

## pgvector

pgvector는 PostgreSQL에서 벡터를 저장하고 검색할 수 있게 해주는 확장입니다. 04 과정에서는 PostgreSQL을 직접 설치하지 않고, pgvector가 포함된 Docker 이미지를 사용합니다.

실행:

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

확인:

```powershell
docker exec -it rag-pgvector psql -U rag_user -d rag_db
```

## 컨테이너 중지와 재시작

중지:

```powershell
docker stop ollama-llm rag-pgvector
```

재시작:

```powershell
docker start ollama-llm rag-pgvector
```

삭제:

```powershell
docker rm ollama-llm rag-pgvector
```

데이터 volume까지 삭제:

```powershell
docker volume rm ollama-data rag-pgvector-data
```

## 초보자 주의점

- Docker Desktop이 켜져 있어야 합니다.
- 같은 이름의 컨테이너가 이미 있으면 새로 만들 수 없습니다.
- 같은 포트를 다른 프로그램이 쓰고 있으면 실행이 실패합니다.
- 모델과 DB 데이터는 Docker volume에 저장합니다.
- volume을 삭제하면 모델 파일과 pgvector PostgreSQL 데이터가 함께 사라집니다.
- Compose는 05에서 쓰지 않고 07에서 배웁니다.
