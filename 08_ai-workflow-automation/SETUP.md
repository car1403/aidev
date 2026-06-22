# SETUP

`08_ai-workflow-automation` 과정의 실습 환경을 준비하는 문서입니다.

이 과정은 Python 코드를 많이 작성하는 과정이라기보다, AIPP, n8n, Dify 같은 워크플로우 도구를 사용해 업무 자동화 흐름을 설계하고 실행해 보는 과정입니다. 그래서 환경 준비도 다음 세 가지를 중심으로 진행합니다.

```text
1. Python 예제 실행 환경
2. AIPP, n8n, Dify 도구 사용 환경
3. API Key, Webhook, 실행 로그 확인 환경
```

## 1. 수업 전 준비물

수업을 시작하기 전에 아래 항목을 확인합니다.

```text
[ ] Windows PC
[ ] VS Code 또는 Cursor
[ ] Python 3.11 이상
[ ] PowerShell
[ ] Git
[ ] Docker Desktop
[ ] Chrome 또는 Edge 브라우저
[ ] OpenAI API Key 또는 수업에서 제공한 실습용 API Key
[ ] AIPP 계정 또는 수업에서 제공한 실습 계정
[ ] n8n 로컬 실행 준비
[ ] Dify 계정 또는 수업에서 제공한 실습 계정
```

초보자는 모든 도구를 한 번에 완벽히 준비하려고 하기보다, 아래 순서대로 하나씩 확인하는 것이 좋습니다.

```text
Python 확인
->.venv 활성화
-> requirements.txt 설치
->.env 생성
-> n8n 실행 확인
-> AIPP 접속 확인
-> Dify 접속 확인
```

## 2. 과정 폴더로 이동

PowerShell을 열고 08 과정 폴더로 이동합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
```

현재 위치가 맞는지 확인합니다.

```powershell
Get-Location
```

결과가 아래와 비슷하면 정상입니다.

```text
C:\aidev\08_ai-workflow-automation
```

## 3. Python 버전 확인

Python이 설치되어 있는지 확인합니다.

```powershell
python --version
pip --version
```

권장 버전은 Python 3.11 이상입니다.

Python 명령이 동작하지 않으면 다음을 확인합니다.

```text
1. Python이 설치되어 있는가?
2. 설치할 때 Add python.exe to PATH를 체크했는가?
3. PowerShell을 완전히 닫았다가 다시 열었는가?
```

## 4. 가상환경 활성화

08 과정은 `08_ai-workflow-automation` 폴더의 `.venv` 하나를 사용합니다. 각 하위 단원마다 `.venv`를 새로 만들지 않습니다.

이미 `.venv`가 있으면 아래 명령으로 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

명령줄 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

```text
(.venv) PS C:\aidev\08_ai-workflow-automation>
```

만약 `.venv`가 없다면 한 번만 생성합니다.

```powershell
python -m venv.venv
.\.venv\Scripts\Activate.ps1
```

PowerShell 실행 정책 오류가 나오면 현재 사용자 범위에서 스크립트 실행을 허용합니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

그 다음 PowerShell을 다시 열고 가상환경을 활성화합니다.

## 5. Python 패키지 설치

가상환경이 활성화된 상태에서 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

설치가 끝난 뒤 간단히 확인합니다.

```powershell
python.\01_workflow-concepts\01_ch1_ai-workflow-big-picture\01_ai_workflow_map.py
```

이 예제는 외부 API 없이 실행됩니다. 처음에는 이런 로컬 예제로 워크플로우 구조를 먼저 이해합니다.

## 6..env 파일 준비

`.env.example` 파일을 복사해 `.env`를 만듭니다.

```powershell
Copy-Item.env.example.env
```

`.env` 파일에는 실제 API Key와 도구 주소를 입력합니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
AIPP_API_KEY=your-aipp-api-key
N8N_BASE_URL=http://localhost:5678
DIFY_API_KEY=your-dify-api-key
DIFY_BASE_URL=http://localhost
```

수업에서는 수업에서 제공한 키가 있다면 해당 값을 사용합니다. 개인 키를 사용하는 경우 절대 화면 공유 중에 전체 값을 노출하지 않습니다.

주의:

```text
.env 파일은 GitHub에 올리지 않습니다.
API Key는 README, 코드, 발표 자료에 직접 적지 않습니다.
실습용 Key와 실제 운영용 Key는 분리합니다.
```

## 7. AIPP 준비

AIPP는 이 과정에서 AI 워크플로우를 설계하고 실행하는 제품형 도구로 사용합니다.

수업에서 AIPP를 사용할 때는 다음 순서로 진행합니다.

```text
1. AIPP 접속
2. 로그인
3. 새 프로젝트 또는 새 워크플로우 생성
4. 입력값 정의
5. LLM 또는 Agent 노드 추가
6. Tool 또는 Knowledge 연결
7. 조건 분기 또는 검증 단계 추가
8. 결과 출력 노드 추가
9. 테스트 실행
10. 실행 로그 확인
```

도구 화면의 메뉴 이름은 제품 버전이나 계정 권한에 따라 다를 수 있습니다. 중요한 것은 메뉴 이름을 외우는 것이 아니라, 아래 구조를 이해하는 것입니다.

```text
Trigger
-> Input
-> LLM / Agent
-> Tool / Knowledge
-> Condition
-> Output
-> Log
```

AIPP 실습에서는 02 단원의 README와 `10_labs` 문서를 같이 보면서 진행합니다.

## 8. n8n 준비

n8n은 여러 서비스와 API를 연결하는 자동화 도구입니다. 08 과정에서는 Docker로 n8n을 로컬에서 실행합니다.

먼저 Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

`docker ps`가 정상적으로 실행되면 n8n을 실행합니다.

```powershell
docker run -d `
 --name n8n-ai-workflow `
 -p 5678:5678 `
 -v n8n-data:/home/node/.n8n `
 n8nio/n8n:latest
```

브라우저에서 접속합니다.

```text
http://localhost:5678
```

처음 접속하면 계정 생성 또는 초기 설정 화면이 나올 수 있습니다. 수업에서는 수업 안내에 따라 실습 계정을 만듭니다.

n8n에서 처음 만들어 볼 기본 흐름은 다음과 같습니다.

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
```

컨테이너를 중지할 때:

```powershell
docker stop n8n-ai-workflow
```

다시 시작할 때:

```powershell
docker start n8n-ai-workflow
```

컨테이너를 삭제할 때:

```powershell
docker rm n8n-ai-workflow
```

주의: `n8n-data` 볼륨에는 n8n 설정과 워크플로우 데이터가 저장됩니다. 수업 중 만든 워크플로우를 유지하려면 볼륨을 삭제하지 않습니다.

## 9. Dify 준비

Dify는 LLM 앱, Chatflow, Workflow, Knowledge/RAG를 만들고 API로 배포할 수 있는 도구입니다.

초보자 수업에서는 먼저 Dify Cloud 또는 수업에서 제공한 Dify 환경을 사용하는 것을 권장합니다. 로컬 self-host 방식은 Docker Compose와 여러 컨테이너를 다루므로, 기본 흐름을 이해한 뒤 선택 실습으로 진행합니다.

Dify 수업 진행 순서:

```text
1. Dify 접속
2. 로그인
3. 새 앱 생성
4. Chatbot, Chatflow, Workflow 중 앱 유형 선택
5. 모델 설정
6. System Prompt 작성
7. 테스트 질문 입력
8. Knowledge 생성
9. 문서 업로드
10. Knowledge를 앱에 연결
11. API Key 발급
12. n8n 또는 Python에서 API 호출 구조 확인
```

Dify에서 꼭 확인해야 하는 화면:

```text
앱 설정
Prompt 설정
Knowledge 설정
Workflow 또는 Chatflow 편집 화면
실행 테스트 화면
API Access 또는 API Key 화면
로그 또는 모니터링 화면
```

로컬 self-host가 필요한 경우에는 04 단원 README의 Docker Compose 설치 흐름을 참고합니다. 실제 명령은 Dify 공식 문서 기준으로 변경될 수 있으므로 수업 당일 최신 설치 페이지를 확인한 뒤 진행합니다.

## 10. 도구별 역할 정리

| 도구 | 수업에서의 역할 | 초보자가 집중할 부분 |
| --- | --- | --- |
| AIPP | AI 워크플로우 설계와 제품형 실행 흐름 이해 | 업무를 노드와 단계로 나누기 |
| n8n | Webhook, API, 외부 서비스 자동화 연결 | Trigger, IF, HTTP Request 연결 |
| Dify | LLM 앱, Chatflow, Workflow, Knowledge/RAG 구성 | AI 앱과 지식 검색 응답 만들기 |

## 11. 수업 중 공통 실습 흐름

각 도구 실습은 아래 순서를 반복합니다.

```text
1. 업무 시나리오를 한 문장으로 정의한다.
2. 입력 데이터를 정한다.
3. Trigger를 정한다.
4. Condition을 정한다.
5. AI 또는 Tool이 처리할 일을 정한다.
6. 결과 출력 형태를 정한다.
7. 오류가 났을 때의 대체 흐름을 정한다.
8. 실행 로그에서 무엇을 확인할지 정한다.
9. 실제 도구 화면에 옮긴다.
10. 테스트 입력으로 실행해 본다.
```

## 12. 자주 만나는 오류

### `.venv`가 활성화되지 않음

```powershell
.\.venv\Scripts\Activate.ps1
```

실행 정책 오류가 있으면:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 패키지를 찾을 수 없음

```powershell
pip install -r requirements.txt
```

### n8n 접속이 안 됨

```powershell
docker ps
docker logs n8n-ai-workflow
```

확인할 것:

```text
Docker Desktop이 실행 중인가?
컨테이너가 실행 중인가?
포트 5678을 다른 프로그램이 사용하고 있지 않은가?
브라우저 주소가 http://localhost:5678 인가?
```

### Dify API 호출이 안 됨

확인할 것:

```text
DIFY_BASE_URL이 맞는가?
DIFY_API_KEY가 맞는가?
앱의 API Access가 활성화되어 있는가?
요청 본문 JSON 형식이 맞는가?
```

### AI 응답 품질이 좋지 않음

확인할 것:

```text
입력 데이터가 충분한가?
System Prompt가 명확한가?
출력 형식이 구체적인가?
Knowledge 문서가 연결되어 있는가?
검증 단계가 있는가?
```

## 13. 첫 수업 권장 진행표

| 단계 | 내용 | 목표 |
| --- | --- | --- |
| 1 | 08 과정 구조 소개 | 전체 흐름 이해 |
| 2 | Python `.venv` 확인 | 예제 실행 준비 |
| 3 | `.env` 생성 | API Key 관리 이해 |
| 4 | AIPP 흐름 소개 | AI 워크플로우 설계 관점 이해 |
| 5 | n8n Docker 실행 | 로컬 자동화 도구 실행 |
| 6 | Dify 앱 구조 소개 | AI 앱과 Knowledge/RAG 이해 |
| 7 | 간단한 문의 자동화 시나리오 설계 | 미니 프로젝트 방향 잡기 |

이 문서를 완료하면 `README.md`를 읽고 01 단원부터 순서대로 진행합니다.
