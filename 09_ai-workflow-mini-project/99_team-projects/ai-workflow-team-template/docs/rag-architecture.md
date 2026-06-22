# RAG Architecture

이 문서는 팀 프로젝트의 RAG 아키텍처 설계서입니다.

RAG를 실제로 구현하지 못하더라도, 어떤 문서를 어떤 기준으로 나누고, 어떤 embedding 모델로 벡터화하며, 어떤 방식으로 검색할지 설명할 수 있어야 합니다.

## 1. RAG 사용 목적

| 항목 | 내용 |
| --- | --- |
| RAG 사용 여부 | 사용 / 미사용 / 선택 예정 |
| 검색 대상 문서 | FAQ / 장애 대응 매뉴얼 / 설치 가이드 / 계정 처리 절차 / 기타 |
| RAG가 필요한 이유 | |
| RAG가 필요하지 않다면 이유 | |

예시:

```text
기술 지원 답변은 매뉴얼과 장애 대응 절차를 근거로 생성되어야 하므로 RAG를 사용한다.
```

## 2. 원본 문서 특성

| 문서명 | 형식 | 특징 | 예상 크기 |
| --- | --- | --- | --- |
| VPN 장애 대응 매뉴얼 | PDF/Markdown | 절차 중심 문서 | 20쪽 |
| 계정 잠금 FAQ | CSV/Markdown | 짧은 질문과 답변 | 50개 항목 |
| 소프트웨어 설치 가이드 | PDF/HTML | 이미지와 단계 설명 포함 | 30쪽 |

## 3. Chunking 전략

| 항목 | 설정 |
| --- | --- |
| chunking 단위 | 문장 / 단락 / 토큰 / 의미 단위 |
| chunk size | |
| overlap | |
| 설정 이유 | |

예시:

```text
장애 대응 매뉴얼은 절차가 단락 단위로 설명되어 있으므로 단락 중심으로 나눈다.
한 chunk는 약 500~800자 정도로 유지하고, 앞뒤 문맥이 끊기지 않도록 100자 정도 overlap을 둔다.
```

## 4. Embedding 모델

| 항목 | 내용 |
| --- | --- |
| 후보 모델 | OpenAI text-embedding-3-small / bge-m3 / multilingual-e5 / 기타 |
| 선택 모델 | |
| 선택 이유 | 성능 / 한국어 지원 / 비용 / 속도 / 운영 편의성 |
| vector dimension | |
| 거리 계산 방식 | cosine / euclidean / dot product |

예시:

```text
한국어 기술 지원 문서가 많으므로 다국어 검색 성능이 좋은 embedding 모델을 우선 고려한다.
비용과 구현 난이도를 고려해 수업에서는 관리형 Knowledge 기능 또는 OpenAI embedding API를 사용할 수 있다.
```

### 4.1 embedding 모델 선택 근거

| 후보 모델 | 장점 | 주의할 점 | 선택 여부 |
| --- | --- | --- | --- |
| OpenAI text-embedding-3 계열 | API로 쉽게 사용 가능, 문서가 많음 | API 비용과 키 관리 필요 | |
| bge 계열 | 검색 성능이 좋고 로컬/오픈소스 활용 가능 | 실행 환경 구성이 더 필요할 수 있음 | |
| multilingual-e5 계열 | 다국어 문서 검색에 적합 | 모델 선택과 벡터 차원 확인 필요 | |
| Dify Knowledge 기본 embedding | 노코드 도구 안에서 쉽게 사용 가능 | 내부 동작을 세밀하게 제어하기 어려울 수 있음 | |

선택 이유에는 다음을 포함합니다.

```text
성능:
한국어 또는 다국어 지원:
비용:
구현 난이도:
vector dimension:
거리 계산 방식:
```

## 5. Vector DB 또는 Knowledge 저장소

| 항목 | 내용 |
| --- | --- |
| 저장소 | Dify Knowledge / Supabase pgvector / Chroma / Qdrant / 기타 |
| 컬렉션 또는 인덱스 이름 | |
| 명명 규칙 | |
| partition 또는 sharding 전략 | |
| metadata 저장 방식 | |

metadata 예시:

```json
{
 "doc_id": "vpn-guide-01",
 "title": "VPN 접속 오류 처리 절차",
 "category": "network",
 "version": "2026.06",
 "source": "internal-manual"
}
```

명명 규칙 예시:

```text
collection: tech_support_faq_2026
index: idx_tech_support_embedding_cosine
metadata key: doc_id, category, version, source, updated_at
```

partition 또는 sharding은 초보자 과정에서 반드시 구현하지 않아도 됩니다.
다만 문서가 늘어났을 때 카테고리별로 나눌지, 버전별로 나눌지, 오래된 문서를 archive할지 정도는 설계서에 적습니다.

## 6. 검색 흐름

```text
사용자 문의
-> 검색 query 생성
-> embedding 변환
-> vector search
-> 관련 문서 top-k 조회
-> LLM context로 전달
-> 답변 생성
```

| 단계 | 입력 | 출력 | 설명 |
| --- | --- | --- | --- |
| Query 생성 | 사용자 문의 | search_query | 검색에 적합한 문장으로 변환 |
| Vector Search | search_query | retrieved_chunks | 관련 문서 조각 조회 |
| Rerank 선택 | retrieved_chunks | selected_context | 가장 관련 있는 문서 선택 |
| 응답 생성 | selected_context | answer | 근거 기반 답변 생성 |

## 7. 백업과 복구

| 항목 | 전략 |
| --- | --- |
| 원본 문서 백업 | |
| vector index 백업 | |
| metadata 백업 | |
| 문서 버전 관리 | |
| 장애 발생 시 복구 방식 | |

## 8. 확장 전략

문서가 늘어날 경우를 대비해 아래 항목을 정리합니다.

- 문서 카테고리별 컬렉션 분리 여부
- 오래된 문서의 archive 처리 기준
- 대용량 문서 추가 시 재색인 방식
- 검색 속도가 느려질 때의 개선 방법
- 비용 증가를 줄이기 위한 캐시 전략

## 9. 최종 점검

- 어떤 문서를 검색하는지 명확한가?
- chunking 설정에 근거가 있는가?
- embedding 모델을 왜 선택했는지 설명할 수 있는가?
- vector dimension과 거리 계산 방식이 작성되어 있는가?
- vector DB 구조와 metadata가 정의되어 있는가?
- 백업, 복구, 확장 전략이 포함되어 있는가?
