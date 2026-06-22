# 04_ch4_rag-retrieval-and-answering

이 챕터에서는 검색된 문서 조각을 LLM에게 전달해 근거 기반 답변을 만드는 RAG 흐름을 학습합니다.

## 핵심 개념

- Retrieve는 질문과 관련 있는 문서를 찾는 단계입니다.
- Generate는 검색 결과를 context로 사용해 답변하는 단계입니다.
- Hybrid Search는 키워드 검색과 벡터 검색을 결합합니다.
- RAG 품질 평가는 답변이 근거에 충실한지 확인합니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python.\04_ch4_rag-retrieval-and-answering\01_retrieve-context.py
python.\04_ch4_rag-retrieval-and-answering\02_rag-answer.py
python.\04_ch4_rag-retrieval-and-answering\03_hybrid-search-rrf.py
python.\04_ch4_rag-retrieval-and-answering\04_rag-quality-evaluation.py
```

## 확인 질문

- LLM에게 검색 context를 제공하면 어떤 점이 좋아지나요?
- RRF는 검색 결과를 어떻게 합치나요?
- RAG 답변 품질은 어떤 기준으로 볼 수 있나요?

