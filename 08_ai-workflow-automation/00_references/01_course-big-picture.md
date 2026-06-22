# 01. Course Big Picture

## 과정 목표

`08_ai-workflow-automation`은 AI 워크플로우 도구를 활용해 업무 자동화 흐름을 설계하고 구현하는 과정입니다.

이 과정에서는 AIPP, n8n, Dify를 모두 같은 관점에서 바라봅니다.

```text
업무 이벤트 발생
-> 데이터 수집
-> 조건 판단
-> AI 분석/생성
-> Tool 또는 API 실행
-> 결과 검증
-> 사용자 또는 운영자에게 전달
-> 로그와 품질 지표 기록
```

## 왜 이 과정이 필요한가?

AI 서비스는 단순히 챗봇 하나를 만드는 것으로 끝나지 않습니다.

실제 업무에서는 다음이 필요합니다.

```text
문의 접수 자동화
문서 검색 기반 답변 생성
외부 API 호출
승인/검토 흐름
운영 로그 수집
오류 처리
비용 관리
품질 개선
```

## 단원 연결

```text
01_workflow-concepts:
 AI 워크플로우의 공통 구조 학습

02_aipp-workflow:
 AIPP식 노드 기반 AI 워크플로우 설계

03_n8n-ai-workflow:
 Webhook, IF, HTTP Request 기반 자동화 흐름

04_dify-ai-workflow:
 AI 앱, Chatflow, Workflow, Knowledge/RAG 설계

05_workflow-ops-and-quality:
 버전, 비용, 오류, 로그, 품질 관리

99_mini-project:
 기술 지원 자동화 워크플로우 통합 프로젝트
```

## 최종적으로 만들 수 있는 것

```text
고객 문의 자동 분류 시스템
기술 지원 답변 초안 생성기
n8n Webhook 기반 자동화
Dify Knowledge 기반 상담 챗봇
운영 로그 기반 Workflow Ops Assistant
```
