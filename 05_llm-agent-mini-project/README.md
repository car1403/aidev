# 05_llm-agent-mini-project

`04_llm-agent-orchestration` 과정에서 배운 Prompt, Function Calling, Tool Use, RAG, Memory, LangGraph를 하나의 팀 미니 프로젝트로 구현하는 과정입니다.

이 과정의 기준은 `04_llm-agent-orchestration`입니다. 04에서 배운 로컬 LLM 실행 방식, Python Tool 설계, LangGraph 실행 흐름을 바탕으로 직접 팀별 Agent 앱을 완성합니다.

Docker는 04와 동일하게 Docker Desktop에서 `docker run`으로 필요한 컨테이너만 실행하는 수준으로 다룹니다. Docker Compose, AWS 배포, GitHub Actions, 서비스 운영 자동화는 `06_multi-agent-service-ops`에서 본격적으로 학습합니다.

Docker Desktop 설치가 아직 되어 있지 않다면 [00_references/05_docker-local-extension-guide.md](./00_references/05_docker-local-extension-guide.md)를 먼저 확인합니다. 05에서는 Docker를 필수로 쓰지 않지만, 로컬 Llama 또는 pgvector 기반 RAG/Memory를 붙이는 팀은 Docker 실행 환경이 필요합니다.

## 과정 목표

- 복합 API 연계 일정 조정 에이전트의 사용자 시나리오를 정의한다.
- Agent State, Node, Edge, Tool, Decision, Fallback 구조를 설계한다.
- Function Calling 또는 Python Tool로 일정, 사용자, 데이터 조회 기능을 연결한다.
- RAG 또는 Memory를 프로젝트에 필요한 범위로 적용한다.
- LangGraph StateGraph로 에이전트 실행 흐름을 구성한다.
- 에이전트 자기 성찰과 피드백 루프를 설계하고 시험한다.
- Streamlit UI에서 에이전트를 실행하고 결과를 확인한다.
- 팀 프로젝트를 에이전트 아키텍처 설계서, 시험 결과 보고서, 발표 자료로 정리한다.

## 이번 프로젝트에서 만드는 것

최종 목표는 **복합 API 연계 일정 조정 에이전트**를 만드는 것입니다.

이번 프로젝트의 기준 주제는 다음과 같습니다.

```text
분야:
단일 에이전트 추론 및 AI 오케스트레이션

프로젝트:
복합 API 연계 일정 조정 에이전트

진행 방향:
1. LangGraph를 이용한 다중 도구(Multi-tool) 선택 및 순환형 워크플로우 설계
2. 에이전트의 판단 오류를 스스로 수정하는 자기 성찰 및 피드백 루프 구현
3. 실시간 API 데이터 기반의 의사결정 시나리오 테스트 및 서비스 배포 실습
```

예시 기능:

- 사용자 일정 요청 분석
- 참석자 일정 조회
- 회의 가능 시간 계산
- 일정 충돌 감지
- 대체 시간 제안
- 일정 제안 메시지 생성
- 도구 선택 오류나 응답 불일치 감지
- 자기 성찰 후 재시도 또는 fallback 처리

처음에는 복잡한 Agent를 만들기보다 아래 흐름이 한 번 끝까지 실행되는 것을 목표로 합니다.

```text
사용자 요청 입력
-> Agent State에 요청 저장
-> Node에서 요청 분석
-> Decision Node에서 필요한 Tool 선택
-> Tool 실행
-> Tool 결과를 State에 저장
-> 결과 검증
-> 필요하면 피드백 루프 또는 재시도
-> 최종 응답 생성
-> Streamlit 화면에 표시
```

## 필수 산출물

팀 프로젝트는 아래 2가지 산출물을 기준으로 평가합니다.

| 산출물 | 핵심 확인 기준 |
| --- | --- |
| 에이전트 아키텍처 설계서 | StateGraph Node, 분기 조건, Memory, Tool 호출 흐름, 공유 State 필드가 명확한가 |
| 에이전트 시험 결과 보고서 | 판단 오류 감지 기준, 재시도/Fallback 전략, 피드백 루프, 개선 전후 성능 비교가 정리되었는가 |

### 에이전트 아키텍처 설계서에 꼭 들어갈 내용

`docs/agent-architecture.md`에는 아래 기준을 직접 설명해야 합니다.

- StateGraph의 Start, Decision, Tools, Reflection 또는 Review, End 노드가 에이전트의 사고 흐름인 `인지 -> 판단 -> 행동 -> 검증` 순서에 맞게 배치되었는가?
- 분기 조건이 도구 필요 여부, 사용자 의도, 데이터 충분성, 오류 여부 같은 기준값 또는 정책으로 정의되었는가?
- 예외 흐름이 단순 설명으로 끝나지 않고 fallback edge 또는 fallback node로 표현되었는가?
- 단기 기억(Session Memory)과 장기 기억(Long-term Memory)을 언제, 어떤 데이터에 사용할지 구분했는가?
- 컨텍스트 윈도우가 길어질 때 어떤 정보를 요약(Summarization)하고 어떤 정보는 버릴지 전략을 세웠는가?
- Function Calling 또는 Tool Use 흐름이 `도구 선택 -> 도구 호출 -> 결과 처리 -> 다음 노드 결정` 순서로 표현되었는가?
- 공유 State 객체의 필드가 `messages`, `tools_called`, `error_count`, `iteration`, `memory_summary`처럼 타입 힌트와 함께 정리되었는가?
- 같은 의미의 값을 여러 필드에 중복 저장하지 않도록 State 구조를 단순하게 유지했는가?

### 에이전트 시험 결과 보고서에 꼭 들어갈 내용

`docs/agent-test-report.md`에는 아래 기준을 직접 시험하고 기록해야 합니다.

- 할루시네이션, 도구 선택 오류, 파라미터 누락, 응답 불일치 같은 판단 오류를 어떤 기준으로 감지하는가?
- 오류 유형별 재시도 횟수, fallback 전략, 사용자에게 다시 질문하는 조건이 정리되었는가?
- 프롬프트 수정, 파라미터 조정, 휴리스틱 업데이트 이력이 버전별로 기록되었는가?
- `오류 감지 -> 원인 분석 -> 수정 전략 선택 -> 재실행 -> 검증` 흐름이 순서도 또는 활동 다이어그램으로 표현되었는가?
- 자기 성찰 적용 전후의 태스크 완료율, 도구 선택 정확도, 응답 일관성 점수, 평균 재시도 횟수가 수치로 비교되었는가?

### 수업 중 점검 기준

프로젝트를 진행하면서 아래 질문을 반복해서 확인합니다.

- 프로젝트 흐름이 `사용자 요청 -> 요청 분석 -> 도구 선택 -> 도구 실행 -> 결과 검증 -> 재시도 또는 fallback -> 최종 응답`으로 이어지는가?
- API Key가 없어도 Mock data 기반으로 최소 Agent 흐름을 실행할 수 있는가?
- 실제 Calendar API를 붙이기 전에 Python 함수와 Mock 일정 데이터로 먼저 검증했는가?
- State에 너무 많은 값을 넣지 않고, 필요한 값만 타입 힌트와 함께 정리했는가?
- 최종 발표에서 Agent 구조, 오류 처리, 개선 전후 결과를 직접 설명할 수 있는가?

## 04 과정과의 연결

`04_llm-agent-orchestration`에서 배운 내용은 이 미니 프로젝트에서 다음처럼 사용합니다.

| 04 과정 내용 | 05 프로젝트 적용 |
| --- | --- |
| Prompt Engineering | 사용자 요청 분석, 최종 응답 문장 생성 |
| Structured Output | 의도 분석, Tool 입력값, 검증 결과를 구조화 |
| Function Calling / Tool Use | Python 함수 또는 외부 API를 Agent가 사용할 수 있게 설계 |
| RAG / Memory | 문서 검색, 대화 이력, 사용자 상태 저장에 선택 적용 |
| LangGraph | State, Node, Edge, 조건 분기로 Agent 실행 흐름 구성 |
| Docker run 기반 로컬 환경 | Ollama 또는 pgvector를 선택적으로 실행해 로컬 실습 확장 |
| Tracing / Debugging | 실행 단계별 결과 확인, 테스트 체크리스트 작성 |

## 과정 구조

```text
05_llm-agent-mini-project
├─.venv
├─.gitignore
├─ README.md
├─ SETUP.md
├─.env.example
├─ requirements.txt
├─ 00_references
├─ 01_local-dev-basic
├─ 02_instructor-sample-project
├─ 03_team-project-guide
├─ 04_agent-project-practice
├─ 05_llm-agent-sample-assets
└─ 99_team-projects
 └─ llm-agent-team-template
```

## 폴더를 읽는 방법

각 폴더의 역할은 다음과 같습니다.

```text
00_references Agent 프로젝트 참고 자료
01_local-dev-basic 로컬 실행 환경과 기본 앱 실행 감각 확인
02_instructor-sample-project 수업용 샘플 Agent 프로젝트
03_team-project-guide 팀 프로젝트 주제, 역할, 일정 가이드
04_agent-project-practice Agent 설계 문서 작성 실습
05_llm-agent-sample-assets Agent 샘플 자료와 참고 코드
99_team-projects 팀별 최종 프로젝트 작업 공간
```

초보자는 `02_instructor-sample-project`를 먼저 실행해 보고, 그 다음 `99_team-projects\llm-agent-team-template`을 복사해서 자기 팀 프로젝트를 시작하면 됩니다.

## 구성 기준

### 04_llm-agent-orchestration에서 가져온 것

- 일정 조정 에이전트 샘플 프로젝트
- LangGraph 기반 팀 템플릿
- Prompt, Tool, RAG, Memory, LangGraph 커리큘럼 점검 자료
- Docker Desktop에서 `docker run`으로 Ollama 또는 pgvector를 실행하는 로컬 실습 방식
- Docker Desktop 설치, `hello-world` 테스트, WSL 2 확인 흐름

### 06_multi-agent-service-ops로 넘기는 것

아래 내용은 05에서 깊게 다루지 않고, 06에서 서비스 운영 관점으로 학습합니다.

- Docker Compose로 여러 컨테이너를 함께 실행하는 방법
- AWS 기반 배포와 운영 환경 구성
- GitHub Actions 기반 CI/CD 자동화
- 서비스 로그 수집, Health Check, Restart, Retry, Auto Healing
- 운영 대시보드와 장애 대응 흐름

## 권장 학습 흐름

```text
00_references 읽기
-> 01_local-dev-basic에서 환경과 실행 방식 확인
-> 02_instructor-sample-project에서 수업용 샘플 실행
-> 03_team-project-guide에서 팀 주제/역할/일정 확정
-> 04_agent-project-practice에서 Agent 설계 문서 작성
-> 99_team-projects/llm-agent-team-template 기반 팀 프로젝트 진행
```

초보자에게는 아래처럼 더 작게 나누어 진행하는 것을 권장합니다.

1. `SETUP.md`를 보고 `.venv`와 `.env`를 준비합니다.
2. Docker 확장을 사용할 팀은 Docker Desktop과 `docker ps`를 확인합니다.
3. `02_instructor-sample-project`에서 수업용 샘플 Agent를 실행합니다.
4. 샘플의 `docs/agent-flow.md`와 `docs/tool-spec.md`를 읽습니다.
5. 팀 주제를 정하고 사용자 요청 예시를 3개 이상 작성합니다.
6. Agent가 기억해야 할 값을 `Agent State`로 정리합니다.
7. Agent가 실행할 Tool 함수를 2개 이상 설계합니다.
8. LangGraph Node/Edge 흐름을 문서로 먼저 그립니다.
9. Mock data로 먼저 Agent 흐름을 실행합니다.
10. 필요할 때만 OpenAI API, RAG, Memory, 외부 API를 붙입니다.
11. Streamlit UI와 테스트 체크리스트, 발표 자료를 정리합니다.

## 수업 운영 메모

처음부터 실제 Calendar API를 붙이도록 요구하지 않습니다. 먼저 Mock data로 아래 흐름을 완성하도록 안내합니다.

```text
1. 사용자 일정 요청을 State에 저장한다.
2. 요청 의도를 분석한다.
3. 필요한 Tool을 선택한다.
4. Mock 일정 데이터를 조회한다.
5. 가능한 시간을 계산한다.
6. 결과를 검증한다.
7. 오류가 있으면 한 번 재시도하거나 fallback한다.
8. 최종 일정 제안 메시지를 생성한다.
9. Streamlit 화면에서 State와 최종 답변을 확인한다.
10. 시험 결과 보고서에 개선 전후 결과를 기록한다.
```

## 실행 방식

```text
LLM: OpenAI API, 기본 모델 gpt-4.1-mini
Local LLM: 선택 사항으로 Ollama + Llama 계열 모델 사용 가능
Graph: LangGraph
Tool: Python 함수 또는 외부 API
Memory/RAG: Mock data 우선, 선택 확장으로 로컬 파일 또는 pgvector docker run
Frontend: Streamlit
.env: OPENAI_API_KEY, OPENAI_MODEL=gpt-4.1-mini 관리
Docker: 필요할 때만 docker run 사용
```

이 과정은 Supabase 기반 프로젝트가 아닙니다. Supabase는 01, 02, 03 과정에서 다루고, 05는 04를 기반으로 한 LLM Agent 프로젝트에 집중합니다.

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

PowerShell 기준 기본 흐름은 다음과 같습니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
python -m venv.venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
Copy-Item.env.example.env
```

[requirements.txt](C:/aidev/05_llm-agent-mini-project/requirements.txt)에는 Streamlit, LangGraph, LangChain, OpenAI SDK와 pgvector 연결용 Python 패키지가 정리되어 있습니다. 데이터베이스 서버는 이 파일로 설치되는 것이 아니라, 필요한 경우 Docker의 `rag-pgvector` 컨테이너로 실행합니다.

이미 `.venv`가 만들어져 있다면 다시 만들 필요는 없습니다. 그때는 아래처럼 활성화부터 시작하면 됩니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
.\.venv\Scripts\Activate.ps1
```

이 과정에서는 `05_llm-agent-mini-project` 최상위의 `.venv` 하나를 사용합니다.

## 수업용 샘플 실행 방법

먼저 수업용 샘플을 실행해 전체 흐름을 확인합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

Streamlit 화면으로 확인하려면 아래 명령을 실행합니다.

```powershell
streamlit run.\frontend\streamlit_app.py --server.port 8701
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8701
```

서버를 멈출 때는 PowerShell에서 `Ctrl + C`를 누릅니다.

## 팀 프로젝트 시작 방법

팀 프로젝트는 `99_team-projects\llm-agent-team-template`을 복사해서 시작합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
Copy-Item.\99_team-projects\llm-agent-team-template.\99_team-projects\team-01-study-agent -Recurse
```

팀 이름에 맞게 `team-01-study-agent` 부분만 바꾸면 됩니다.

복사한 뒤에는 아래 문서를 먼저 채웁니다.

```text
docs/project-plan.md 프로젝트 주제, 사용자, 주요 기능
docs/agent-architecture.md Agent State, Node, Edge, Tool, Memory 설계
docs/agent-test-report.md 판단 오류, 재시도, 피드백 루프 시험 결과
docs/agent-design.md 기존 호환용 Agent 설계 문서
docs/test-checklist.md 테스트 체크리스트
presentation/final-presentation.md 발표 자료 초안
```

코드는 아래 파일부터 작은 단위로 수정합니다.

```text
backend/agent_state.py Agent가 기억할 상태 정의
backend/tools.py Agent가 사용할 Tool 함수
backend/graph.py LangGraph 흐름
frontend/app.py Streamlit 화면
```

## 팀 템플릿 실행 방법

```powershell
cd C:\aidev\05_llm-agent-mini-project\99_team-projects\llm-agent-team-template
..\..\.venv\Scripts\Activate.ps1
python backend\graph.py
streamlit run frontend\app.py --server.port 8702
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8702
```

## OpenAI API Key 없이 가능한 것

API Key가 없어도 아래 작업은 진행할 수 있습니다.

- Agent State 설계
- Tool 함수 설계
- Mock data 기반 Tool 실행
- LangGraph Node/Edge 흐름 이해
- Streamlit 화면 구성
- 테스트 체크리스트 작성
- 발표 자료 작성

API Key가 있으면 최종 응답 생성, 자연어 요약, 사용자 요청 분석 같은 LLM 기반 기능까지 확장할 수 있습니다.

## Docker를 사용하는 경우

05에서는 Docker를 필수로 사용하지 않습니다. 다만 팀 프로젝트에서 아래 기능을 선택할 경우 04에서 배운 방식대로 Docker Desktop과 `docker run`을 사용할 수 있습니다.

```text
Ollama + Llama 모델 OpenAI API 대신 로컬 LLM 응답 실험
pgvector 컨테이너 RAG 또는 장기 기억 데이터를 로컬 Vector DB에 저장
```

여기서는 단일 컨테이너 실행까지만 사용합니다. 여러 서비스를 하나로 묶는 Docker Compose는 06에서 학습합니다.

Docker를 처음 설치할 때는 아래 순서로 준비합니다.

```text
1. Docker Desktop 설치
2. Docker Desktop 실행
3. PowerShell에서 docker --version 확인
4. PowerShell에서 docker ps 확인
5. docker run hello-world 테스트
6. 필요한 경우 Ollama 또는 pgvector 컨테이너 실행
```

pgvector를 사용할 때는 PostgreSQL을 PC에 직접 설치하지 않습니다. 04와 동일하게 `pgvector/pgvector:pg16` Docker 이미지를 실행합니다.

## 자주 만나는 오류

`ModuleNotFoundError`가 나오면 가상환경이 활성화되어 있는지 확인하고 패키지를 다시 설치합니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

OpenAI 관련 오류가 나오면 `.env`에 실제 API Key가 들어 있는지 확인합니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

Streamlit 포트가 이미 사용 중이면 다른 포트를 사용합니다.

```powershell
streamlit run frontend\app.py --server.port 8703
```

Agent 결과가 예상과 다르면 먼저 아래 순서로 확인합니다.

1. 사용자 입력이 State에 저장되는가?
2. Node가 올바른 순서로 실행되는가?
3. Tool 함수 입력값이 맞는가?
4. Tool 결과가 State에 저장되는가?
5. 최종 응답 Node가 State를 제대로 읽는가?

## 최종 목표

이 과정을 마친 뒤 다음을 설명하고 구현할 수 있어야 합니다.

```text
Agent State는 무엇을 저장해야 하는가?
Tool은 언제 호출되고 결과는 어디에 저장되는가?
RAG와 Memory는 어떤 문제를 해결하는가?
LangGraph Node/Edge는 에이전트 흐름을 어떻게 제어하는가?
팀 프로젝트를 어떻게 테스트하고 발표할 것인가?
```
