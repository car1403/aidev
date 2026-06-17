# 03. Team Project Guide

이 폴더는 `09_ai-workflow-mini-project` 팀 프로젝트를 진행하기 위한 안내 문서입니다.

이번 프로젝트는 단순히 챗봇 화면을 만드는 과제가 아닙니다. 학생들은 기술 지원 업무를 자동화하는 AI 워크플로우를 설계하고, 노코드·로코드 도구로 구현 가능한 구조를 만들고, 테스트 결과를 문서로 검증해야 합니다.

## 프로젝트 주제

노코드·로코드 기반 기업형 지능형 기술 지원 자동화(Tech Support) 워크플로우 구축

## 필수 진행 내용

1. 노코드·로코드 기반 RAG 및 도구 노드 구현
2. 멀티 에이전트 오케스트레이션 구현
3. 운영 안정화 및 예외 처리(Error Handling)
4. 서비스 테스트 및 결과 검증

## 이 폴더의 사용 순서

| 순서 | 파일 | 수업에서 하는 일 |
| --- | --- | --- |
| 1 | `01_topic-selection.md` | 팀 프로젝트 주제와 업무 시나리오를 정합니다. |
| 2 | `02_role-and-schedule.md` | 팀원 역할과 일정 계획을 정합니다. |
| 3 | `03_project-requirements.md` | 필수 요구사항과 산출물 기준을 확인합니다. |
| 4 | `04_test-checklist.md` | 정상 케이스와 예외 케이스 테스트 항목을 정합니다. |
| 5 | `05_final-presentation.md` | 최종 발표 흐름을 준비합니다. |
| 6 | `06_submission-checklist.md` | 제출 전 누락된 문서와 테스트 결과를 확인합니다. |

## 최종 산출물

팀 폴더에는 아래 문서가 반드시 포함되어야 합니다.

```text
docs/project-plan.md
docs/no-code-workflow-design.md
docs/rag-architecture.md
docs/workflow-execution-result.md
docs/ops-quality-plan.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 강의 진행 팁

강사는 먼저 학생들에게 “어떤 기술 지원 문제가 반복적으로 발생하는가?”를 질문하면 좋습니다. 예를 들어 비밀번호 초기화, 사내 시스템 접속 오류, 소프트웨어 설치 문의, 장애 신고, 권한 요청 같은 주제는 워크플로우 설계 연습에 적합합니다.

학생들은 주제를 정한 뒤 바로 구현부터 시작하지 말고, Trigger, 입력 데이터, 처리 노드, 출력 결과, 예외 상황을 먼저 문서로 정리해야 합니다.
