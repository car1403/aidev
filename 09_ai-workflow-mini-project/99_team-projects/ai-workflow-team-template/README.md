# AI Workflow Team Project Template

이 폴더는 `09_ai-workflow-mini-project` 팀 프로젝트를 시작하기 위한 기본 템플릿입니다.

팀은 이 폴더를 복사한 뒤, 팀명에 맞게 폴더 이름을 바꾸고 문서를 채워 나갑니다.

## 프로젝트 주제

노코드·로코드 기반 기업형 지능형 기술 지원 자동화(Tech Support) 워크플로우 구축

## 권장 폴더명

```text
team01-tech-support-workflow
team02-rag-helpdesk
team03-it-support-automation
```

## 최종 목표

팀은 아래 네 가지를 프로젝트 안에 반영합니다.

1. 노코드·로코드 기반 RAG 및 도구 노드 구현
2. 멀티 에이전트 오케스트레이션 구현
3. 운영 안정화 및 예외 처리(Error Handling)
4. 서비스 테스트 및 결과 검증

## 폴더 구성

```text
ai-workflow-team-template/
  README.md
  docs/
    project-plan.md
    no-code-workflow-design.md
    rag-architecture.md
    workflow-execution-result.md
    ops-quality-plan.md
    test-checklist.md
    workflow-design.md
  backend/
    README.md
  frontend/
    README.md
  presentation/
    final-presentation.md
```

`workflow-design.md`는 기존 통합 설계 문서입니다. 이번 프로젝트에서는 아래 세 문서를 우선 산출물로 작성합니다.

- `docs/no-code-workflow-design.md`
- `docs/rag-architecture.md`
- `docs/workflow-execution-result.md`

## 작성 순서

| 순서 | 파일 | 작성 내용 |
| --- | --- | --- |
| 1 | `docs/project-plan.md` | 프로젝트 주제, 사용자, 문제, 범위를 정합니다. |
| 2 | `docs/no-code-workflow-design.md` | Trigger, 처리 노드, 출력, 외부 서비스 연동, payload를 설계합니다. |
| 3 | `docs/rag-architecture.md` | chunking, embedding, vector DB, metadata, 백업과 확장을 설계합니다. |
| 4 | `docs/ops-quality-plan.md` | 오류 처리, 재시도, fallback, 운영 모니터링을 정리합니다. |
| 5 | `docs/workflow-execution-result.md` | 정상/예외 시나리오 실행 결과와 로그를 정리합니다. |
| 6 | `docs/test-checklist.md` | 제출 전 테스트 항목을 확인합니다. |
| 7 | `presentation/final-presentation.md` | 발표 자료를 준비합니다. |

## 구현 방식 선택

팀 상황에 따라 아래 방식 중 하나를 선택합니다.

| 방식 | 설명 |
| --- | --- |
| 설계 중심 | 실제 도구 구현보다 워크플로우 설계서와 실행 시뮬레이션을 중심으로 제출합니다. |
| 노코드 구현 중심 | AIPP, n8n, Dify 화면에서 실제 워크플로우를 구성하고 결과를 캡처합니다. |
| 로코드 구현 중심 | FastAPI, Streamlit, Python 코드로 일부 노드를 직접 구현합니다. |
| 혼합 방식 | AIPP/n8n/Dify로 큰 흐름을 만들고, 필요한 부분만 Python API로 구현합니다. |

## 제출 전 최소 기준

아래 항목을 모두 만족해야 합니다.

- 기술 지원 자동화 시나리오가 구체적입니다.
- Trigger -> 처리 -> 출력 흐름이 문서화되어 있습니다.
- 외부 서비스 연동 노드의 인증과 오류 처리가 설명되어 있습니다.
- 노드 간 payload 스키마와 예시가 있습니다.
- RAG 사용 여부와 아키텍처가 설명되어 있습니다.
- 정상 시나리오와 예외 시나리오 테스트 결과가 있습니다.
- API Key, OAuth Secret, 개인정보를 제출물에 포함하지 않았습니다.

## 팀 README 작성 예시

팀 폴더의 `README.md`에는 아래 내용을 작성합니다.

```text
팀명:
프로젝트 제목:
해결하려는 문제:
주요 사용자:
사용 도구:
실행 또는 시연 방법:
최종 산출물 위치:
```

## 발표 준비

발표에서는 구현 화면보다 “왜 이렇게 설계했는가”를 설명하는 것이 중요합니다.

특히 아래 세 가지는 반드시 설명합니다.

- 노코드 워크플로우의 전체 흐름
- RAG 아키텍처와 검색 기준
- 테스트 결과와 예외 처리 방식
