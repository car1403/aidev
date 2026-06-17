# 09. AI Workflow Mini Project Plan

대상 폴더:

```text
C:\aidev\09_ai-workflow-mini-project
```

## 수업 목표

```text
노코드/로코드 기반 AI Workflow 프로젝트를 진행한다.
AIPP, n8n, Dify 중 하나 이상을 활용한다.
RAG/Data Node, 보안 필터, 운영 품질 기준을 문서화한다.
노코드 워크플로우 설계서, RAG 아키텍처 설계서, 워크플로우 실행 결과서를 작성한다.
최종 발표와 시연을 진행한다.
```

## 강의 순서

```text
1. 프로젝트 목표 설명
2. 팀 주제 선정
3. 이미지 기준 산출물 3종 설명
4. 노코드 워크플로우 설계서 작성
5. RAG 아키텍처 설계서 작성
6. 도구 선택: AIPP, n8n, Dify, FastAPI, Streamlit
7. 구현 또는 화면 설계
8. 정상/예외 테스트와 실행 결과서 작성
9. 발표 자료 작성
10. 최종 시연
```

## 평가 포인트

```text
Workflow 구조가 명확한가?
도구 선택 이유가 타당한가?
보안과 품질 기준이 있는가?
운영 관점 개선 방향이 있는가?
```

## 필수 산출물

```text
docs/no-code-workflow-design.md
docs/rag-architecture.md
docs/workflow-execution-result.md
docs/ops-quality-plan.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 산출물별 확인 질문

### 노코드 워크플로우 설계서

```text
Trigger -> 처리 -> 출력 흐름이 기술 지원 업무 로직에 맞는가?
분기, 반복, 병렬 구조를 사용했다면 이유가 설명되어 있는가?
Slack, Email, Jira, Notion, Database, API 연동 노드가 정의되어 있는가?
OAuth, API Key, Webhook Secret 같은 인증 방식과 오류 처리가 설명되어 있는가?
노드 간 payload 스키마, Mapper/Formatter, 필수/선택 필드가 작성되어 있는가?
```

### RAG 아키텍처 설계서

```text
원본 문서의 길이, 구조, 언어, 형식이 정리되어 있는가?
chunking 단위, chunk size, overlap 설정과 근거가 있는가?
embedding 모델 후보와 선택 이유가 설명되어 있는가?
vector dimension, 거리 계산 방식, 컬렉션/인덱스 명명 규칙이 작성되어 있는가?
metadata, 백업/복구, 대용량 데이터 확장 전략이 포함되어 있는가?
```

### 워크플로우 실행 결과서

```text
정상 시나리오와 예외 시나리오 실행 로그가 있는가?
각 테스트의 입력, 기대 결과, 실제 결과, 성공 여부가 작성되어 있는가?
RAG 검색 결과가 최종 답변에 어떻게 반영되었는가?
외부 서비스 연동 결과가 성공/실패/미사용으로 구분되어 있는가?
실패 시 재시도, fallback, 담당자 알림, 다음 개선 계획이 정리되어 있는가?
```
