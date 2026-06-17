# 02_ch2_pgvector-basic

이 챕터에서는 Docker run으로 실행한 pgvector PostgreSQL 컨테이너에 벡터를 저장하고 검색합니다.

## 핵심 개념

- pgvector는 PostgreSQL에서 벡터 검색을 가능하게 하는 확장입니다.
- 04 과정에서는 PostgreSQL을 PC에 직접 설치하지 않습니다.
- `rag-pgvector` 컨테이너를 사용해 실습합니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
Get-Content .\02_ch2_pgvector-basic\01_create-extension-and-tables.sql | docker exec -i rag-pgvector psql -U rag_user -d rag_db
python .\02_ch2_pgvector-basic\01_insert-sample-vectors.py
python .\02_ch2_pgvector-basic\02_search-similar-vectors.py
```

## 확인 질문

- pgvector는 일반 PostgreSQL과 무엇이 다른가요?
- 벡터 검색 결과는 어떤 기준으로 정렬되나요?

