# 08_ai-workflow-automation

이 과정은 AIPP, n8n, Dify 같은 AI 워크플로우 도구를 사용해 업무 자동화 시나리오를 설계하고 실행하는 과정입니다.

수업 참여자는 코드를 많이 작성하기보다, 업무 흐름을 `Trigger`, `Condition`, `Action`, `LLM`, `Tool`, `Memory`, `Log` 구조로 나누고 이를 실제 도구 화면에 옮기는 방법을 학습합니다.

## 과정 목표

이 과정을 마치면 다음을 할 수 있어야 합니다.

- AI 워크플로우의 전체 구조를 설명할 수 있습니다.
- AIPP, n8n, Dify의 역할 차이를 구분할 수 있습니다.
- 업무 시나리오를 Trigger, Condition, Action 구조로 나눌 수 있습니다.
- RAG 노드, 데이터 처리 노드, 노드 간 상호작용 구조를 설계할 수 있습니다.
- AIPP에서 AI 워크플로우 설계 흐름을 이해할 수 있습니다.
- n8n에서 Webhook, IF, HTTP Request 기반 자동화 흐름을 만들 수 있습니다.
- Loop, Fork-Join, 병렬 처리, 데이터 파싱/변환/집계 흐름을 설계할 수 있습니다.
- Dify에서 Chatflow, Workflow, Knowledge/RAG 기반 AI 앱 구조를 이해할 수 있습니다.
- 워크플로우 운영에 필요한 로그, 오류 처리, 비용, 품질 검증 기준을 만들 수 있습니다.
- Prompt Injection 방어, 입력/출력 필터링, 리소스 관리, 확장성, Multi-Agent Workflow 운영 기준을 설계할 수 있습니다.
- 최종적으로 기업형 기술 지원 자동화 워크플로우 미니 프로젝트를 진행할 수 있습니다.

## 과정에서 사용하는 도구

| 도구 | 수업에서의 역할 | 수업 참여자가 익혀야 할 핵심 |
| --- | --- | --- |
| AIPP | AI 워크플로우를 제품 화면에서 설계하고 실행 | 업무를 노드와 단계로 나누는 사고방식 |
| n8n | Webhook, API, 외부 서비스 연결 자동화 | Trigger, IF, HTTP Request, 실행 로그 |
| Dify | AI 앱, Chatflow, Workflow, Knowledge/RAG 구성 | AI 답변 앱과 지식 검색 응답 흐름 |

이 과정은 04~07 과정처럼 Docker와 배포를 깊게 다루는 과정이 아닙니다. 다만 n8n을 로컬에서 실행하기 위해 Docker를 사용하며, Dify self-host는 선택 실습으로만 다룹니다. Docker Compose, AWS 배포, GitHub Actions 운영은 `06_multi-agent-service-ops`에서 본격적으로 학습합니다.

## 전체 구조

```text
08_ai-workflow-automation
├─ .venv
├─ .gitignore
├─ .env.example
├─ requirements.txt
├─ README.md
├─ SETUP.md
├─ 00_references
├─ 01_workflow-concepts
├─ 02_aipp-workflow
├─ 03_n8n-ai-workflow
├─ 04_dify-ai-workflow
├─ 05_workflow-ops-and-quality
└─ 99_mini-project
```

## 처음 시작하는 순서

처음에는 아래 순서대로 진행합니다.

1. `SETUP.md`를 열고 수업 환경을 준비합니다.
2. `00_references\11_aipp-n8n-dify-class-manual.md`를 읽고 세 도구의 실습 흐름을 확인합니다.
3. `00_references\12_curriculum-image-alignment.md`에서 이미지 커리큘럼과 실제 폴더 대응 관계를 확인합니다.
4. `01_workflow-concepts`에서 AI 워크플로우의 기본 구조를 학습합니다.
5. `02_aipp-workflow`에서 AIPP 방식의 워크플로우 설계를 학습합니다.
6. `03_n8n-ai-workflow`에서 n8n으로 Webhook/API 자동화를 실습합니다.
7. `04_dify-ai-workflow`에서 Dify 기반 AI 앱과 Knowledge/RAG 구조를 학습합니다.
8. `05_workflow-ops-and-quality`에서 운영, 비용, 오류, 품질 기준을 학습합니다.
9. `99_mini-project`에서 기술 지원 자동화 워크플로우를 설계하고 발표합니다.

이 과정에서는 하위 단원마다 `.venv`를 새로 만들지 않고, `08_ai-workflow-automation` 최상위의 `.venv` 하나를 사용합니다.

## 강의 진행 흐름

수업은 다음 흐름으로 진행하면 좋습니다.

```text
1. 같은 업무 시나리오를 제시한다.
2. 시나리오를 Trigger, Condition, Action으로 나눈다.
3. AIPP에서는 노드 기반 AI 업무 흐름으로 표현한다.
4. n8n에서는 Webhook, IF, HTTP Request로 표현한다.
5. Dify에서는 Chatflow, Workflow, Knowledge/RAG로 표현한다.
6. 실행 결과를 로그와 품질 기준으로 검토한다.
7. 미니 프로젝트에서 팀별 주제로 확장한다.
```

공통 실습 시나리오:

```text
기업 내부 기술 지원 문의 자동화
```

기본 흐름:

```text
문의 접수
-> 문의 유형 분류
-> 긴급도 판단
-> 관련 문서 검색
-> AI 답변 초안 생성
-> 위험/품질 검증
-> 운영팀 알림 또는 답변 후보 제공
-> 실행 로그 기록
```

## 단원별 핵심 내용

| 단원 | 내용 |
| --- | --- |
| 00_references | 과정 전체 지도, 도구 비교, 환경 준비, 수업용 매뉴얼 |
| 01_workflow-concepts | AI Workflow, LLM, Tool, Memory, RAG/Data Node, Trigger/Condition/Action |
| 02_aipp-workflow | AIPP 방식의 AI 워크플로우 설계와 노드 구조 |
| 03_n8n-ai-workflow | Docker 기반 n8n 실행, Webhook, IF, HTTP Request, Loop/Fork-Join/Data Transform |
| 04_dify-ai-workflow | Dify 앱, Chatflow, Workflow, Knowledge/RAG |
| 05_workflow-ops-and-quality | 버전, 비용, 오류 처리, 로그, 품질 검증, 보안 필터, 리소스/확장성, Multi-Agent Workflow Ops |
| 99_mini-project | 노코드/로코드 기반 기술 지원 자동화 미니 프로젝트 |

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

기본 명령:

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

`.env`에는 실제 API Key와 도구 주소를 입력합니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
AIPP_API_KEY=your-aipp-api-key
N8N_BASE_URL=http://localhost:5678
DIFY_API_KEY=your-dify-api-key
DIFY_BASE_URL=http://localhost
```

## Python 예제 실행

Python 예제는 도구 화면 실습 전에 개념을 이해하기 위한 보조 자료입니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
python .\01_workflow-concepts\01_ch1_ai-workflow-big-picture\01_ai_workflow_map.py
python .\01_workflow-concepts\03_ch3_trigger-condition-action\01_trigger_condition_action.py
```

## n8n 실행

n8n은 Docker Desktop을 실행한 뒤 아래 명령으로 시작합니다.

```powershell
docker run -d `
  --name n8n-ai-workflow `
  -p 5678:5678 `
  -v n8n-data:/home/node/.n8n `
  n8nio/n8n:latest
```

접속 주소:

```text
http://localhost:5678
```

중지:

```powershell
docker stop n8n-ai-workflow
```

다시 시작:

```powershell
docker start n8n-ai-workflow
```

## Dify 실습 방식

Dify는 초보자 수업에서는 Cloud 또는 수업에서 준비한 실습 환경을 먼저 사용하는 것을 권장합니다.

로컬 self-host는 Docker Compose와 여러 컨테이너를 사용하므로, 수업 상황에 따라 선택 실습으로 진행합니다. Dify self-host가 필요한 경우 `04_dify-ai-workflow` README의 설치 흐름을 참고합니다.

## 실습 체크리스트

각 단원 실습 후 아래 항목을 점검합니다.

```text
[ ] 내가 자동화하려는 업무를 한 문장으로 설명할 수 있다.
[ ] 입력 데이터와 출력 결과를 정했다.
[ ] Trigger를 정했다.
[ ] Condition이 필요한지 판단했다.
[ ] AI가 처리할 단계와 단순 자동화 단계를 구분했다.
[ ] AIPP, n8n, Dify 중 어떤 도구가 적합한지 설명할 수 있다.
[ ] 오류 발생 시 대체 흐름을 생각했다.
[ ] 실행 로그에서 확인할 항목을 정했다.
```

## 99 미니 프로젝트

최종 미니 프로젝트 주제는 다음과 같습니다.

```text
노코드·로코드 기반 기업형 지능형 기술 지원 자동화 워크플로우
```

샘플 프로젝트 위치:

```text
99_mini-project/sample-tech-support-workflow
```

팀 프로젝트 템플릿:

```text
99_mini-project/team-template
```

팀 프로젝트를 시작할 때는 템플릿을 복사합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
Copy-Item .\99_mini-project\team-template .\99_mini-project\team-01-tech-support-workflow -Recurse
```

최종 결과물에는 다음이 포함되어야 합니다.

- 업무 자동화 시나리오
- Trigger, Condition, Action 구조
- AIPP, n8n, Dify 중 최소 1개 이상을 활용한 설계 또는 구현 결과
- AI API 또는 Knowledge/RAG 연동 계획
- 오류 처리와 fallback 흐름
- 비용과 API 사용량 관리 계획
- 실행 로그와 품질 검증 체크리스트
- 최종 발표 자료

## 자주 만나는 오류

`ModuleNotFoundError`가 나오면 가상환경과 패키지 설치를 확인합니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

n8n 접속이 안 되면 Docker 컨테이너 상태를 확인합니다.

```powershell
docker ps
docker logs n8n-ai-workflow
```

Dify API 호출이 안 되면 `DIFY_BASE_URL`, `DIFY_API_KEY`, 앱의 API Access 설정을 확인합니다.

AI 응답 품질이 낮으면 입력 데이터, System Prompt, Knowledge 연결, 출력 검증 기준을 차례대로 점검합니다.

## 보안과 비용 주의

- API Key는 `.env`에만 저장합니다.
- `.env` 파일은 GitHub에 올리지 않습니다.
- 고객 정보, 개인정보, 회사 내부 문서는 실습용 더미 데이터로 대체합니다.
- AI API 호출은 비용이 발생할 수 있으므로 테스트 입력을 작게 시작합니다.
- 자동화 워크플로우가 외부 알림이나 실제 API를 호출할 때는 테스트 범위를 제한합니다.
