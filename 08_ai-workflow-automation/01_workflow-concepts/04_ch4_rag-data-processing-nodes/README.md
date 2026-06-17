# 04_ch4_rag-data-processing-nodes

RAG 노드와 데이터 처리 노드의 역할을 학습하는 챕터입니다.

AI 워크플로우에서는 LLM 노드만 중요한 것이 아닙니다. 좋은 답변을 만들려면 입력 데이터를 정리하고, 필요한 문서를 검색하고, 검색 결과를 LLM에 전달하고, 최종 결과를 검증하는 노드가 함께 필요합니다.

## 학습 목표

- RAG 노드가 검색과 생성 흐름에서 어떤 역할을 하는지 이해합니다.
- 전처리, 변환, 집계, 후처리 데이터 노드의 차이를 설명할 수 있습니다.
- LLM 노드와 RAG 노드, 데이터 처리 노드의 연결 흐름을 설계할 수 있습니다.
- 노코드 워크플로우 도구에서 데이터 노드가 왜 중요한지 이해합니다.

## 기본 구조

```text
User Input
-> Preprocess Node
-> Query Transform Node
-> RAG Retrieval Node
-> LLM Generation Node
-> Postprocess Node
-> Output Validation Node
```

## 노드 역할

| 노드 | 역할 |
| --- | --- |
| Preprocess Node | 입력값 정리, 공백 제거, 필수 필드 확인 |
| Query Transform Node | 검색에 적합한 키워드나 질문으로 변환 |
| RAG Retrieval Node | Knowledge나 문서 저장소에서 관련 문서 검색 |
| LLM Generation Node | 검색 결과를 바탕으로 답변 생성 |
| Postprocess Node | 출력 형식 정리, 필드명 통일 |
| Output Validation Node | 응답 형식과 정책 위반 여부 검증 |

## 실행 예제

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\04_ch4_rag-data-processing-nodes\01_rag_data_processing_nodes.py
```

## 수업 질문

- RAG 노드 없이 LLM만 사용하면 어떤 문제가 생길 수 있는가?
- 전처리와 후처리는 각각 어느 단계에서 필요한가?
- 검색 결과가 없을 때 어떤 fallback을 사용해야 하는가?
