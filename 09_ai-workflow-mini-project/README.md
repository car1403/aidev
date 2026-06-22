# 09. AI Workflow Mini Project

이 과정은 `08_ai-workflow-automation`에서 배운 AIPP, n8n, Dify, RAG, Tool, API 연동, 운영 품질 관리 내용을 하나의 팀 미니 프로젝트로 정리하는 단계입니다.

수업 참여자는 실제 기업에서 사용할 수 있는 기술 지원 자동화 시나리오를 정하고, 노코드 또는 로코드 도구를 활용해 워크플로우를 설계하고, 실행 결과를 검증합니다.

## 프로젝트 주제

노코드·로코드 기반 기업형 지능형 기술 지원 자동화(Tech Support) 워크플로우 구축

예시 흐름은 다음과 같습니다.

```text
사용자 문의 접수
-> 문의 내용 분류
-> 관련 문서 검색 또는 RAG 조회
-> 답변 초안 생성
-> 긴급도 판단
-> 담당자 알림 또는 티켓 생성
-> 실행 로그 기록
-> 결과 검증
```

## 프로젝트 진행 방향

이 프로젝트에서는 아래 네 가지를 반드시 다룹니다.

| 순서 | 진행 내용 | 설명 |
| --- | --- | --- |
| 1 | 노코드·로코드 기반 RAG 및 도구 노드 구현 | AIPP, n8n, Dify 중 하나 이상을 활용해 검색, 데이터 처리, 외부 도구 호출 노드를 설계합니다. |
| 2 | 멀티 에이전트 오케스트레이션 구현 | Planner, Retriever, Responder, Reviewer처럼 역할을 나누거나, 워크플로우 노드 단위로 역할을 분리합니다. |
| 3 | 운영 안정화 및 예외 처리 | 인증 실패, API 오류, 검색 결과 없음, 알림 실패 같은 예외 상황을 정의하고 대응 흐름을 설계합니다. |
| 4 | 서비스 테스트 및 결과 검증 | 주요 시나리오를 실행하고, 실행 로그와 결과를 근거로 정상 동작 여부를 검증합니다. |

## 최종 산출물

최종 제출물은 구현 화면만이 아니라, 설계와 검증 근거를 포함해야 합니다.

| 산출물 | 작성 파일 | 반드시 포함할 내용 |
| --- | --- | --- |
| 노코드 워크플로우 설계서 | `docs/no-code-workflow-design.md` | Trigger -> 처리 -> 출력 흐름, 분기/반복/병렬 구조, 외부 서비스 연동, 인증, 오류 처리, 노드 간 데이터 payload 스키마 |
| RAG 아키텍처 설계서 | `docs/rag-architecture.md` | 원본 문서 특성, chunking/overlap 전략, embedding 모델 선정 이유, vector DB 구조, 인덱스/컬렉션 설계, 백업과 확장 전략 |
| 워크플로우 실행 결과서 | `docs/workflow-execution-result.md` | 주요 시나리오 실행 로그, 정상/예외 케이스 테스트 결과, 외부 연동 결과, RAG 검색 반영 결과, 개선할 점 |

이미지 기준의 세부 제출 기준은 [00_references/06_project-output-alignment.md](C:/aidev/09_ai-workflow-mini-project/00_references/06_project-output-alignment.md)에 정리되어 있습니다.
수업 중에는 이 문서를 열어 두고 팀별 산출물이 빠짐없이 작성되었는지 점검합니다.

## 사용할 수 있는 도구

팀별로 아래 도구 중 하나 이상을 선택합니다.

| 도구 | 사용 목적 |
| --- | --- |
| AIPP | AI 워크플로우의 전체 노드 구조와 업무 흐름을 설계합니다. |
| n8n | Webhook, HTTP Request, Slack, Email, Notion, Jira 등 외부 서비스 연동을 구성합니다. |
| Dify | LLM 앱, Chatflow, Workflow, Knowledge/RAG 기반 응답 흐름을 구성합니다. |
| FastAPI | 로코드 방식으로 API 또는 테스트용 백엔드를 구현합니다. |
| Streamlit | 간단한 시연 화면 또는 운영 대시보드를 만듭니다. |

## 폴더 구성

```text
09_ai-workflow-mini-project/
  README.md
  SETUP.md
  00_references/
  01_local-dev-basic/
  02_instructor-sample-project/
  03_team-project-guide/
  04_ai-workflow-project-practice/
  05_ai-workflow-sample-assets/
  99_team-projects/
    ai-workflow-team-template/
```

| 폴더 | 수업에서 사용하는 방식 |
| --- | --- |
| `00_references` | 프로젝트 큰 그림, 기술 지원 시나리오, 도구 선택 기준을 확인합니다. |
| `01_local-dev-basic` | Python, FastAPI, Streamlit 실행 환경을 점검합니다. |
| `02_instructor-sample-project` | 먼저 실행해 보여주는 기술 지원 자동화 샘플입니다. |
| `03_team-project-guide` | 팀 프로젝트 주제, 역할, 요구사항, 테스트, 제출 기준을 안내합니다. |
| `04_ai-workflow-project-practice` | 워크플로우 설계, 도구 선택, RAG, 보안, 운영 품질을 단계별로 작성합니다. |
| `05_ai-workflow-sample-assets` | 팀 프로젝트에 사용할 샘플 문의, FAQ, 장애 유형 자료를 둡니다. |
| `99_team-projects` | 팀별 프로젝트 결과물을 작성하는 위치입니다. |

## 실습 시작 순서

처음 진행하는 수업 참여자는 아래 순서대로 따라오면 됩니다.

1. `SETUP.md`를 열고 Python, VS Code, 가상환경, 실행 명령을 확인합니다.
2. `01_local-dev-basic`에서 로컬 실행 환경을 점검합니다.
3. `02_instructor-sample-project`를 실행해 기술 지원 자동화 흐름을 먼저 체험합니다.
4. `03_team-project-guide`를 보면서 팀 주제와 역할을 정합니다.
5. `04_ai-workflow-project-practice` 문서를 작성하며 설계를 구체화합니다.
6. `99_team-projects/ai-workflow-team-template`를 팀 이름으로 복사해 최종 산출물을 작성합니다.

## 샘플 프로젝트 실행

PowerShell에서 아래 명령을 순서대로 실행합니다.

```powershell
cd C:\aidev\09_ai-workflow-mini-project\02_instructor-sample-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

백엔드 실행:

```powershell
uvicorn backend.main:app --reload --port 8900
```

프론트엔드 실행:

```powershell
streamlit run frontend\app.py --server.port 8901
```

브라우저에서 아래 주소를 확인합니다.

```text
API 문서: http://127.0.0.1:8900/docs
Streamlit 화면: http://127.0.0.1:8901
```

## 팀 프로젝트 작성 위치

팀 프로젝트는 아래 템플릿을 복사해서 시작합니다.

```text
C:\aidev\09_ai-workflow-mini-project\99_team-projects\ai-workflow-team-template
```

예시:

```text
C:\aidev\09_ai-workflow-mini-project\99_team-projects\team01-tech-support-workflow
```

팀 폴더 안에서는 아래 문서를 우선 작성합니다.

```text
docs/project-plan.md
docs/no-code-workflow-design.md
docs/rag-architecture.md
docs/workflow-execution-result.md
docs/ops-quality-plan.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 제출 전 확인 기준

아래 질문에 답할 수 있어야 프로젝트가 완성된 상태입니다.

- 사용자의 기술 지원 문의가 어떤 Trigger로 시작되는지 설명할 수 있습니까?
- 처리 흐름이 `Trigger -> 처리 -> 출력`으로 자연스럽게 연결됩니까?
- 분기, 반복, 병렬 처리 구조를 사용했다면 그 이유가 명확합니까?
- Slack, Email, Jira, Notion, Database, API 같은 외부 서비스 연동 노드에 인증과 오류 처리가 포함되어 있습니까?
- 노드 간 전달되는 데이터 payload의 필드와 예시가 문서화되어 있습니까?
- Mapper/Formatter 같은 데이터 변환 로직과 필수/선택 필드가 정리되어 있습니까?
- RAG를 사용한다면 chunking, embedding, vector DB, 검색 기준이 설명되어 있습니까?
- embedding 모델 선정 이유, vector dimension, 거리 계산 방식이 설명되어 있습니까?
- 컬렉션/인덱스 명명 규칙, metadata 저장 방식, 백업/복구, 확장 전략이 포함되어 있습니까?
- 정상 케이스와 예외 케이스를 모두 테스트했습니까?
- 인증 실패, 검색 결과 없음, 외부 API 실패 같은 예외 상황 테스트 결과가 있습니까?
- 실행 로그와 결과 화면을 근거로 프로젝트를 설명할 수 있습니까?

## 수업 운영 메모

이 과정은 완성도 높은 상용 서비스를 만드는 것이 1차 목표가 아닙니다. 더 중요한 것은 수업 참여자가 AI 워크플로우를 업무 흐름으로 해석하고, 노드 구조와 데이터 흐름을 설명하며, 실행 결과를 검증하는 경험을 갖는 것입니다.

수업 진행에서는 먼저 샘플 프로젝트를 실행해 전체 흐름을 보여준 뒤, 팀별로 도구를 선택하게 하고, 문서 작성과 간단한 시연을 병행하도록 안내하면 좋습니다.
