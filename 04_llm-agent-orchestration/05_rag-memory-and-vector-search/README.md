# 05 RAG Memory and Vector Search

이 단원은 Agent가 외부 문서와 이전 대화 정보를 활용하는 방법을 학습합니다. 핵심은 문서를 embedding으로 변환하고, pgvector에 저장한 뒤, 질문과 관련 있는 정보를 검색해 LLM 응답에 연결하는 것입니다.

04 과정에서는 Supabase Vector가 아니라 Docker run으로 실행한 로컬 pgvector PostgreSQL 컨테이너를 사용합니다. PostgreSQL은 PC에 직접 설치하지 않습니다.

## 학습 목표

- Embedding과 벡터 유사도의 개념을 이해합니다.
- pgvector PostgreSQL 컨테이너를 실행하고 벡터를 저장합니다.
- 문서를 chunk로 나누고 검색 가능한 형태로 인덱싱합니다.
- 검색된 context를 LLM에게 전달하는 Basic RAG 흐름을 구현합니다.
- Session Memory와 Long-term Memory의 차이를 이해합니다.
- Hybrid Search, RRF, RAG 품질 평가의 기본 개념을 실습합니다.

## 폴더 구성

```text
05_rag-memory-and-vector-search
├─ .env.example
├─ 01_ch1_embedding-basics
│  ├─ 01_vector-similarity-basic.py
│  └─ 02_openai-embedding-basic.py
├─ 02_ch2_pgvector-basic
│  ├─ 01_create-extension-and-tables.sql
│  ├─ 01_insert-sample-vectors.py
│  ├─ 02_sample-vector-search.sql
│  └─ 02_search-similar-vectors.py
├─ 03_ch3_document-chunking-and-indexing
│  ├─ 01_split-sample-document.py
│  └─ 02_index-document-chunks.py
├─ 04_ch4_rag-retrieval-and-answering
│  ├─ 01_retrieve-context.py
│  ├─ 02_rag-answer.py
│  ├─ 03_hybrid-search-rrf.py
│  └─ 04_rag-quality-evaluation.py
└─ 05_ch5_conversation-memory
   ├─ 01_short-term-memory.py
   └─ 02_save-conversation-memory.py
```

## 실습 시작 순서

```powershell
cd C:\aidev\04_llm-agent-orchestration\05_rag-memory-and-vector-search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install openai python-dotenv psycopg[binary] langchain-text-splitters
Copy-Item .env.example .env
```

pgvector 컨테이너는 최상위 [SETUP.md](../SETUP.md)의 안내에 따라 실행합니다.

## 실행 순서

먼저 API Key나 DB 없이 가능한 개념 예제를 실행합니다.

```powershell
python .\01_ch1_embedding-basics\01_vector-similarity-basic.py
python .\03_ch3_document-chunking-and-indexing\01_split-sample-document.py
python .\04_ch4_rag-retrieval-and-answering\03_hybrid-search-rrf.py
python .\04_ch4_rag-retrieval-and-answering\04_rag-quality-evaluation.py
python .\05_ch5_conversation-memory\01_short-term-memory.py
```

pgvector 컨테이너와 OpenAI API Key가 준비되면 DB 연동 예제를 실행합니다.

```powershell
Get-Content .\02_ch2_pgvector-basic\01_create-extension-and-tables.sql | docker exec -i rag-pgvector psql -U rag_user -d rag_db
python .\02_ch2_pgvector-basic\01_insert-sample-vectors.py
python .\02_ch2_pgvector-basic\02_search-similar-vectors.py
python .\03_ch3_document-chunking-and-indexing\02_index-document-chunks.py
python .\04_ch4_rag-retrieval-and-answering\01_retrieve-context.py
python .\04_ch4_rag-retrieval-and-answering\02_rag-answer.py
python .\05_ch5_conversation-memory\02_save-conversation-memory.py
```

## 수업 중 확인 질문

- Embedding은 문장을 왜 숫자 벡터로 바꾸나요?
- RAG에서 chunk 크기와 overlap은 왜 중요한가요?
- Session Memory와 Long-term Memory는 각각 어떤 문제를 해결하나요?
- Hybrid Search와 RRF는 검색 품질을 어떻게 개선하나요?

