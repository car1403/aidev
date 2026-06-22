# 03_n8n-ai-workflow

이 단원은 n8n을 사용해 Webhook, 조건 분기, HTTP API 호출 기반의 AI 자동화 워크플로우를 학습합니다.

n8n은 여러 서비스와 API를 노드로 연결하는 자동화 도구입니다. 이 과정에서는 n8n을 단순 자동화 도구로만 보지 않고, AI 서비스와 외부 업무 시스템을 연결하는 실행 도구로 사용합니다.

## 학습 목표

- n8n의 기본 개념과 노드 기반 자동화 방식을 이해합니다.
- Webhook Trigger, Set, IF, HTTP Request, Respond to Webhook 노드의 역할을 설명할 수 있습니다.
- Loop, Fork-Join, 데이터 변환, 결과 집계 흐름을 설계할 수 있습니다.
- AI API 또는 Dify API를 n8n 워크플로우에 연결하는 구조를 이해합니다.
- 실행 로그를 확인하고 실패 원인을 추적할 수 있습니다.
- 기술 지원 문의 자동화 흐름을 n8n으로 설계할 수 있습니다.

## 전체 구조

```text
03_n8n-ai-workflow
├─ README.md
├─ 01_ch1_n8n-overview-and-docker
├─ 02_ch2_trigger-condition-action-nodes
├─ 03_ch3_ai-api-workflow-integration
├─ 04_ch4_loop-forkjoin-data-transform
├─ 10_labs
└─ 20_assignments
```

## 권장 학습 순서

```text
01_ch1_n8n-overview-and-docker
-> 02_ch2_trigger-condition-action-nodes
-> 03_ch3_ai-api-workflow-integration
-> 04_ch4_loop-forkjoin-data-transform
-> 10_labs
-> 20_assignments
```

## n8n에서 바라볼 핵심 구조

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
-> Execution Log
```

01 단원에서 배운 개념은 n8n에서 다음처럼 연결됩니다.

| 워크플로우 개념 | n8n 노드 예시 |
| --- | --- |
| Trigger | Webhook Trigger, Schedule Trigger |
| Input | Webhook Body, Set Node |
| Condition | IF Node, Switch Node |
| Action | HTTP Request, Email, Slack, Database Node |
| Tool | 외부 API 호출 |
| AI | OpenAI API, Dify API, 사내 AI API 호출 |
| Log | Executions, 노드별 Output |
| Loop | 여러 항목을 하나씩 반복 처리 |
| Fork/Join | 여러 경로 실행 후 결과 병합 |
| Transform | 데이터 파싱, 변환, 집계 |

## n8n 실행 준비

n8n은 Docker Desktop을 사용해 로컬에서 실행합니다.

먼저 Docker Desktop을 실행한 뒤 PowerShell에서 확인합니다.

```powershell
docker --version
docker ps
```

`docker ps`가 정상적으로 실행되면 n8n 컨테이너를 시작합니다.

```powershell
docker run -d `
  --name n8n-ai-workflow `
  -p 5678:5678 `
  -v n8n-data:/home/node/.n8n `
  n8nio/n8n:latest
```

브라우저 접속:

```text
http://localhost:5678
```

처음 접속하면 계정 생성 또는 초기 설정 화면이 나올 수 있습니다. 수업에서는 수업 안내에 따라 실습 계정을 만듭니다.

## n8n 컨테이너 관리

실행 중인 컨테이너 확인:

```powershell
docker ps
```

로그 확인:

```powershell
docker logs n8n-ai-workflow
```

중지:

```powershell
docker stop n8n-ai-workflow
```

다시 시작:

```powershell
docker start n8n-ai-workflow
```

삭제:

```powershell
docker rm n8n-ai-workflow
```

주의: `n8n-data` 볼륨에는 n8n 설정과 워크플로우 데이터가 저장됩니다. 실습 내용을 유지하려면 볼륨을 삭제하지 않습니다.

## 강의용 화면 실습 순서

처음에는 아래 흐름을 목표로 합니다.

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
```

화면 실습 순서:

```text
1. n8n 접속
2. 새 Workflow 생성
3. Webhook Trigger 노드 추가
4. HTTP Method를 POST로 설정
5. Test URL 복사
6. Set 노드 추가
7. message, user, channel 같은 필드 만들기
8. IF 노드 추가
9. message 안에 "급함", "장애", "로그인" 같은 키워드가 있는지 조건 설정
10. HTTP Request 노드 추가
11. FastAPI, Dify API, 외부 AI API 중 하나로 요청 보내기
12. Respond to Webhook 노드 추가
13. Test Workflow 실행
14. PowerShell 또는 Postman으로 Webhook 호출
15. Executions 화면에서 노드별 입력과 출력을 확인
```

## Webhook 테스트 예시

n8n에서 복사한 테스트 URL을 사용해 PowerShell에서 요청을 보냅니다.

```powershell
$body = @{
  user = "student01"
  message = "ERP 로그인이 되지 않습니다. 매우 급합니다."
  channel = "web"
} | ConvertTo-Json

Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:5678/webhook-test/YOUR_WEBHOOK_PATH" `
  -ContentType "application/json" `
  -Body $body
```

`YOUR_WEBHOOK_PATH`는 n8n 화면에서 복사한 Webhook Test URL로 바꿉니다.

## AI API 연결 방식

n8n에서 AI를 연결하는 대표적인 방식은 HTTP Request 노드입니다.

```text
n8n Webhook
-> IF 조건 분기
-> HTTP Request로 AI API 호출
-> 응답 결과 정리
-> Respond to Webhook
```

Dify와 연결하는 경우:

```text
n8n Webhook
-> Dify API 호출
-> Dify 응답을 사용자에게 반환
```

Python FastAPI와 연결하는 경우:

```text
n8n Webhook
-> FastAPI /analyze 호출
-> 분석 결과 반환
```

## Python 예제 실행 순서

Python 예제는 n8n 서버 없이도 실행됩니다. n8n 화면 실습 전에 데이터 흐름을 이해하기 위한 예제입니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
.\.venv\Scripts\Activate.ps1
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python .\01_ch1_n8n-overview-and-docker\01_n8n_node_map.py
python .\02_ch2_trigger-condition-action-nodes\01_n8n_branching_workflow.py
python .\03_ch3_ai-api-workflow-integration\01_ai_api_workflow_simulation.py
python .\04_ch4_loop-forkjoin-data-transform\01_loop_forkjoin_transform.py
```

## 실습 체크리스트

```text
[ ] Docker Desktop이 실행 중이다.
[ ] n8n 컨테이너가 실행 중이다.
[ ] http://localhost:5678 접속이 된다.
[ ] Webhook Trigger를 만들었다.
[ ] 테스트 URL을 복사했다.
[ ] IF 조건 분기를 만들었다.
[ ] HTTP Request 노드의 URL, Method, Body를 설정했다.
[ ] Respond to Webhook으로 결과를 반환했다.
[ ] Executions 화면에서 실행 로그를 확인했다.
```

## 자주 만나는 오류

### `http://localhost:5678` 접속이 안 됨

```powershell
docker ps
docker logs n8n-ai-workflow
```

확인할 것:

```text
Docker Desktop이 실행 중인가?
n8n 컨테이너가 실행 중인가?
포트 5678을 다른 프로그램이 사용하고 있지 않은가?
브라우저 주소가 정확한가?
```

### Webhook 호출이 안 됨

확인할 것:

```text
Test Workflow를 실행한 상태인가?
Test URL과 Production URL을 혼동하지 않았는가?
HTTP Method가 POST로 맞는가?
Content-Type이 application/json인가?
Body JSON 형식이 올바른가?
```

### HTTP Request 노드가 실패함

확인할 것:

```text
요청 URL이 맞는가?
API Key가 필요한 API인가?
Headers에 Authorization이 필요한가?
Body JSON 구조가 API 문서와 맞는가?
응답 오류 메시지를 확인했는가?
```

## 과제 방향

수업 참여자는 n8n으로 다음 중 하나를 설계합니다.

```text
Webhook 기반 기술 지원 문의 접수
문의 긴급도에 따른 조건 분기
Dify API 호출을 통한 답변 생성
Slack 또는 Email 알림 흐름
실행 로그 기반 오류 확인 흐름
```

결과물에는 워크플로우 캡처, 노드 설명, 테스트 입력/출력, 오류 처리 계획이 포함되어야 합니다.

## 이후 단원과의 연결

```text
03 n8n AI Workflow
-> 04 Dify AI Workflow
-> 05 Workflow Ops and Quality
-> 99 Mini Project
```
