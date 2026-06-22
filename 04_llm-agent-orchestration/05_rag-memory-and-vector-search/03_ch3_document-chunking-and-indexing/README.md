# 03_ch3_document-chunking-and-indexing

이 챕터에서는 문서를 chunk로 나누고 embedding으로 변환해 저장하는 흐름을 학습합니다.

## 핵심 개념

- 긴 문서는 작은 chunk로 나누어야 검색하기 쉽습니다.
- chunk는 embedding으로 변환된 뒤 Vector DB에 저장됩니다.
- chunk 크기와 overlap은 검색 품질에 영향을 줍니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\05_rag-memory-and-vector-search
.\.venv\Scripts\Activate.ps1
python.\03_ch3_document-chunking-and-indexing\01_split-sample-document.py
python.\03_ch3_document-chunking-and-indexing\02_index-document-chunks.py
```

## 확인 질문

- chunk를 너무 작게 나누면 어떤 문제가 생기나요?
- overlap은 왜 필요한가요?

