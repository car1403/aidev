# 04_dify-ai-workflow

이 단원은 Dify를 사용해 AI 앱, Chatflow, Workflow, Knowledge/RAG 구조를 학습합니다.

Dify는 LLM 기반 앱을 만들고 운영할 수 있는 플랫폼입니다. 이 과정에서는 Dify를 단순 챗봇 제작 도구로만 보지 않고, 업무 자동화에 필요한 AI 답변 기능을 만들고 API로 외부 워크플로우와 연결하는 도구로 다룹니다.

## 학습 목표

- Dify의 기본 개념과 앱 유형을 이해합니다.
- Chatbot, Chatflow, Workflow의 차이를 설명할 수 있습니다.
- Knowledge/RAG 기반 답변 흐름을 설계할 수 있습니다.
- Dify 앱을 n8n 또는 Python에서 API로 호출하는 구조를 이해합니다.
- AI 워크플로우를 설계할 때 입력, 출력, 검증, 운영 로그를 함께 고려합니다.

## 전체 구조

```text
04_dify-ai-workflow
├─ README.md
├─ 01_ch1_dify-overview
├─ 02_ch2_dify-chatflow-workflow
├─ 03_ch3_dify-rag-agent-flow
├─ 10_labs
└─ 20_assignments
```

## 권장 학습 순서

```text
01_ch1_dify-overview
-> 02_ch2_dify-chatflow-workflow
-> 03_ch3_dify-rag-agent-flow
-> 10_labs
-> 20_assignments
```

## Dify에서 바라볼 핵심 구조

```text
User Question
-> App
-> Prompt
-> Chatflow or Workflow
-> Knowledge Search
-> LLM Answer
-> Output
-> API Access
-> Log
```

## Dify의 주요 기능

| 기능 | 설명 |
| --- | --- |
| Chatbot | 기본 대화형 AI 앱 |
| Chatflow | 대화 흐름을 노드로 설계하는 방식 |
| Workflow | 입력, 처리, 출력 단계를 명시적으로 설계하는 방식 |
| Knowledge | 문서를 업로드하고 검색 가능한 지식으로 만드는 기능 |
| RAG | Knowledge에서 관련 문서를 찾고 LLM 답변에 반영하는 구조 |
| Tool | 외부 API나 기능을 AI 앱에 연결하는 구조 |
| API Access | 만든 AI 앱을 외부 서비스에서 호출할 수 있게 하는 기능 |

## n8n과 Dify의 역할 차이

```text
n8n: 여러 서비스와 이벤트를 연결하는 자동화 실행 도구
Dify: LLM 앱, Chatflow, Workflow, Knowledge 기반 AI 기능을 만드는 도구
```

함께 사용할 때:

```text
n8n Webhook
-> 조건 분기
-> Dify API 호출
-> 결과를 Slack/Email/DB로 전달
```

## 권장 실습 방식

초보자 수업에서는 먼저 Dify Cloud 또는 수업에서 준비한 Dify 환경을 사용합니다.

로컬 self-host 방식은 Docker Compose, 여러 컨테이너, 볼륨, 포트 설정을 함께 다루므로 선택 실습으로 진행합니다. Docker Compose와 배포 운영은 `06_multi-agent-service-ops`에서 더 자세히 다룹니다.

## 강의용 화면 실습 순서

처음에는 아래 순서로 진행합니다.

```text
1. Dify 접속
2. 로그인
3. 새 앱 생성
4. Chatbot 또는 Chatflow 선택
5. 앱 이름 입력
6. 사용할 모델 선택
7. System Prompt 작성
8. 테스트 질문 입력
9. Knowledge 메뉴 이동
10. 새 Knowledge 생성
11. 샘플 문서 업로드
12. 문서 인덱싱 완료 확인
13. 앱에 Knowledge 연결
14. 같은 질문을 다시 테스트
15. 답변 차이 비교
16. API Access 또는 API Key 메뉴 확인
17. 외부 호출 구조 확인
```

## 수업용 Knowledge 문서 예시

아래 내용을 짧은 텍스트 문서로 만들어 Knowledge에 업로드할 수 있습니다.

```text
ERP 로그인 장애 대응 가이드

1. 비밀번호가 만료되었는지 확인한다.
2. 계정 잠금 여부를 확인한다.
3. VPN 접속 상태를 확인한다.
4. 브라우저 캐시를 삭제하고 다시 시도한다.
5. 10분 내 해결되지 않으면 운영팀에 티켓을 생성한다.
```

테스트 질문:

```text
ERP 로그인이 안 됩니다. 어떻게 해야 하나요?
```

비교할 것:

```text
Knowledge 연결 전 답변
Knowledge 연결 후 답변
근거 문서가 반영되었는지 여부
답변이 너무 단정적이지 않은지 여부
```

## Dify API 연결 흐름

Dify에서 만든 앱은 API로 외부에서 호출할 수 있습니다.

일반적인 연결 구조:

```text
n8n Webhook
-> HTTP Request
-> Dify API
-> Dify Response
-> n8n Respond to Webhook
```

API 호출 시 확인할 정보:

```text
DIFY_BASE_URL
DIFY_API_KEY
App ID 또는 API endpoint
요청 Body JSON 형식
응답 JSON 구조
```

실제 API endpoint와 요청 형식은 Dify 환경과 앱 유형에 따라 달라질 수 있으므로, 수업에서는 Dify 화면의 API Access 안내를 기준으로 확인합니다.

## Dify Docker Compose 설치 흐름

Dify self-host는 공식 문서 기준으로 Docker Compose를 사용합니다. 초보자 수업에서는 필수 실습이 아니라 선택 실습입니다.

PowerShell에서 Docker를 확인합니다.

```powershell
docker --version
docker compose version
docker ps
```

일반적인 흐름:

```powershell
git clone https://github.com/langgenius/dify.git
cd dify\docker
Copy-Item .env.example .env
docker compose up -d
```

브라우저 접속:

```text
http://localhost/install
```

주의:

- Dify 공식 설치 방식은 버전에 따라 세부 명령이 바뀔 수 있습니다.
- 실제 설치 전에는 공식 Docker Compose 설치 문서를 확인합니다.
- Windows에서는 Docker Desktop과 WSL2 설정이 중요합니다.
- Dify는 여러 컨테이너와 볼륨을 사용하므로 디스크 공간과 포트 충돌을 확인합니다.
- 로컬 self-host 실습이 어렵다면 Dify Cloud 또는 수업 제공 환경으로 먼저 진행합니다.

## Python 예제 실행 순서

04 단원의 Python 예제는 Dify 서버 없이 실행됩니다. Dify 화면 실습 전에 개념을 이해하기 위한 보조 자료입니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
cd C:\aidev\08_ai-workflow-automation\04_dify-ai-workflow
python .\01_ch1_dify-overview\01_dify_app_map.py
python .\02_ch2_dify-chatflow-workflow\01_chatflow_vs_workflow.py
python .\03_ch3_dify-rag-agent-flow\01_dify_rag_agent_flow.py
```

## 실습 체크리스트

```text
[ ] Dify에 접속했다.
[ ] 새 앱을 만들었다.
[ ] 모델을 선택했다.
[ ] System Prompt를 작성했다.
[ ] 테스트 질문을 실행했다.
[ ] Knowledge를 생성했다.
[ ] 문서를 업로드하고 인덱싱을 확인했다.
[ ] Knowledge를 앱에 연결했다.
[ ] 연결 전과 후의 답변을 비교했다.
[ ] API Access 또는 API Key 위치를 확인했다.
[ ] n8n에서 호출할 때 필요한 정보를 정리했다.
```

## 자주 만나는 오류

### 답변이 문서를 반영하지 않음

확인할 것:

```text
Knowledge가 앱에 연결되어 있는가?
문서 인덱싱이 완료되었는가?
질문이 문서 내용과 관련되어 있는가?
Prompt에서 Knowledge를 참고하라고 명확히 지시했는가?
```

### API 호출이 실패함

확인할 것:

```text
API Key가 맞는가?
API endpoint가 맞는가?
Headers에 Authorization이 들어갔는가?
요청 Body JSON이 앱 유형에 맞는가?
Dify 서버 또는 Cloud 환경이 정상인가?
```

### 로컬 Dify가 실행되지 않음

확인할 것:

```text
Docker Desktop이 실행 중인가?
docker compose version이 정상인가?
필요한 포트를 다른 프로그램이 사용 중이지 않은가?
.env 설정을 복사했는가?
디스크 공간이 충분한가?
```

## 과제 방향

수업 참여자는 Dify로 다음 중 하나를 설계합니다.

```text
사내 문서 기반 기술 지원 챗봇
FAQ 기반 고객 문의 답변 앱
회의록 요약 Workflow
장애 리포트 분류 Chatflow
n8n에서 호출하는 Dify AI API
```

결과물에는 앱 유형, Prompt, Knowledge 구성, 테스트 질문/답변, API 연결 계획, 품질 검증 기준이 포함되어야 합니다.

## 이후 단원과의 연결

```text
04 Dify AI Workflow
-> 05 Workflow Ops and Quality
-> 99 Mini Project
```

## 참고 공식 문서

- Dify Key Concepts: https://docs.dify.ai/en/use-dify/getting-started/key-concepts
- Dify Workflow & Chatflow: https://docs.dify.ai/en/use-dify/build/workflow-chatflow
- Dify Docker Compose: https://docs.dify.ai/getting-started/install-self-hosted/docker-compose
