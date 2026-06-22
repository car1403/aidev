# 06. Project Output Alignment

이 문서는 이미지의 `09_ai-workflow-mini-project` 산출물 기준을 실제 제출 문서와 연결하기 위한 점검표입니다.

09 과정은 08에서 배운 AIPP, n8n, Dify, RAG, Tool, API 연동, 운영 안정화 내용을 하나의 팀 프로젝트로 묶는 단계입니다.
화면을 만드는 것에서 멈추지 않고, 설계 근거와 실행 검증 결과를 문서로 남겨야 합니다.

## 이미지 기준 프로젝트 주제

```text
노코드·로코드 기반 기업형 지능형 기술 지원 자동화(Tech Support) 워크플로우 구축
```

## 이미지 기준 핵심 수행 내용

| 순서 | 수행 내용 | 현재 작성 위치 |
| --- | --- | --- |
| 1 | 노코드·로코드 기반 RAG 및 도구 노드 구현 | `docs/no-code-workflow-design.md`, `docs/rag-architecture.md` |
| 2 | 멀티 에이전트 오케스트레이션 구현 | `docs/workflow-design.md`, `docs/ops-quality-plan.md` |
| 3 | 운영 안정화 및 예외 처리(Error Handling) | `docs/ops-quality-plan.md`, `docs/workflow-execution-result.md` |
| 4 | 서비스 테스트 및 결과 검증 | `docs/workflow-execution-result.md`, `docs/test-checklist.md` |

## 산출물 1. 노코드 워크플로우 설계서

작성 파일:

```text
99_team-projects/ai-workflow-team-template/docs/no-code-workflow-design.md
```

확인 질문:

```text
[ ] Trigger -> 처리 -> 출력의 전체 흐름이 기술 지원 업무 로직에 맞게 연결되어 있는가?
[ ] 조건 분기, 반복, 병렬 처리 구조를 사용했다면 왜 필요한지 설명되어 있는가?
[ ] Slack, Email, Jira, Notion, Database, API 같은 외부 서비스 연동 노드가 정의되어 있는가?
[ ] 외부 서비스 연동 노드에 OAuth, API Key, Webhook Secret 같은 인증 방식이 설명되어 있는가?
[ ] 인증 실패, API 오류, 알림 실패 같은 오류 처리 기준이 포함되어 있는가?
[ ] 노드 간 전달되는 payload 스키마가 문서화되어 있는가?
[ ] Mapper/Formatter 같은 데이터 변환 로직이 정리되어 있는가?
[ ] 필수/선택 필드와 예시 payload가 각 연결선(edge) 기준으로 작성되어 있는가?
```

## 산출물 2. RAG 아키텍처 설계서

작성 파일:

```text
99_team-projects/ai-workflow-team-template/docs/rag-architecture.md
```

확인 질문:

```text
[ ] 원본 문서의 특성(길이, 구조, 언어, 형식)이 정리되어 있는가?
[ ] chunking 단위가 문장, 단락, 토큰, 의미 단위 중 무엇인지 설명되어 있는가?
[ ] chunk size와 overlap 설정값 및 근거가 작성되어 있는가?
[ ] embedding 모델 후보와 선택 이유가 설명되어 있는가?
[ ] OpenAI text-embedding-3, bge, multilingual-e5 등 후보를 비교했는가?
[ ] vector dimension과 거리 계산 방식(cosine, euclidean, dot product)이 명시되어 있는가?
[ ] 컬렉션/인덱스 명명 규칙이 있는가?
[ ] partition, sharding, metadata 저장 구조가 정리되어 있는가?
[ ] 백업/복구 정책과 대용량 데이터 확장 전략이 포함되어 있는가?
```

## 산출물 3. 워크플로우 실행 결과서

작성 파일:

```text
99_team-projects/ai-workflow-team-template/docs/workflow-execution-result.md
```

확인 질문:

```text
[ ] 주요 정상 시나리오 실행 로그가 포함되어 있는가?
[ ] 인증 실패, 검색 결과 없음, 외부 API 실패, 부적절한 입력 같은 예외 테스트 결과가 포함되어 있는가?
[ ] 각 테스트의 입력, 기대 결과, 실제 결과, 성공 여부가 작성되어 있는가?
[ ] RAG 검색 결과가 최종 답변에 어떻게 반영되었는지 설명되어 있는가?
[ ] Slack, Email, Jira, Notion, Database, API 연동 결과가 정리되어 있는가?
[ ] 실패 시 재시도, fallback, 담당자 알림 결과가 기록되어 있는가?
[ ] 실행 결과를 근거로 다음 개선 계획이 작성되어 있는가?
```

## 수업 진행 메모

직접 구현을 완성하지 못해도 아래 세 가지를 설명할 수 있으면 프로젝트 학습 목표에 도달한 것입니다.

```text
1. 어떤 업무를 자동화하려고 했는가?
2. 어떤 노드와 데이터 흐름으로 자동화하려고 했는가?
3. 실행 결과와 예외 상황을 어떤 근거로 검증했는가?
```

반대로 화면은 있어도 Trigger, payload, RAG 구조, 오류 처리, 실행 결과가 설명되지 않으면 프로젝트 완성도가 낮습니다.
수업 진행에서는 발표 피드백을 할 때 결과 화면보다 설계 근거와 검증 근거를 중심으로 질문합니다.
