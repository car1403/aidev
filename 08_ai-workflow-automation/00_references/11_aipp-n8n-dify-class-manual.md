# 11. AIPP, n8n, Dify Class Manual

이 문서는 08 과정 수업에서 AIPP, n8n, Dify를 초보자도 따라 할 수 있도록 만든 강의 진행용 매뉴얼입니다.

수업에서는 세 도구를 모두 같은 질문으로 바라봅니다.

```text
이 도구는 어떤 업무 흐름을 자동화하기 좋은가?
입력은 어디서 들어오는가?
조건 분기는 어디서 처리하는가?
AI는 어느 단계에서 호출되는가?
결과는 어디로 전달되는가?
실행 로그와 오류는 어디서 확인하는가?
```

## 1. 공통 실습 시나리오

수업 전체에서 사용할 기본 시나리오는 다음과 같습니다.

```text
기업 내부 기술 지원 문의 자동화
```

사용자가 기술 지원 문의를 입력하면 워크플로우가 다음 일을 수행합니다.

```text
1. 문의 내용을 받는다.
2. 문의 유형을 분류한다.
3. 긴급도를 판단한다.
4. 관련 문서를 검색하거나 AI 답변 초안을 만든다.
5. 위험하거나 불확실한 답변은 사람 검토로 보낸다.
6. 일반 문의는 답변 후보를 생성한다.
7. 실행 결과와 품질 정보를 로그로 남긴다.
```

이 시나리오 하나를 AIPP, n8n, Dify에서 각각 다르게 표현해 봅니다.

## 2. 도구별 역할

| 도구 | 가장 잘하는 일 | 수업에서의 실습 초점 |
| --- | --- | --- |
| AIPP | AI 워크플로우를 제품 화면에서 설계하고 실행 | 업무 흐름을 노드로 나누기 |
| n8n | Webhook, API, 외부 서비스 연결 자동화 | 이벤트 수신, 조건 분기, HTTP 호출 |
| Dify | LLM 앱, Chatflow, Workflow, Knowledge/RAG 구성 | AI 답변 앱과 지식 검색 흐름 만들기 |

## 3. AIPP 실습 매뉴얼

### 3.1 수업 목표

AIPP 실습의 목표는 특정 메뉴를 외우는 것이 아니라, AI 워크플로우를 어떻게 설계해야 하는지 익히는 것입니다.

수업 참여자는 AIPP 화면에서 다음 구조를 찾을 수 있어야 합니다.

```text
Project
Workflow
Input
LLM / Agent
Tool / Knowledge
Condition
Output
Run
Log
```

### 3.2 화면 실습 순서

수업 진행에서는 아래 순서로 화면을 보여주며 진행합니다.

```text
1. AIPP 접속
2. 로그인
3. 새 프로젝트 생성
4. 새 워크플로우 생성
5. 워크플로우 이름 입력
6. 입력값 필드 생성
7. LLM 또는 Agent 노드 추가
8. 문의 유형 분류 프롬프트 작성
9. 조건 분기 노드 추가
10. 긴급 문의와 일반 문의 경로 분리
11. Tool 또는 Knowledge 연결
12. 응답 생성 노드 추가
13. 결과 출력 노드 추가
14. 테스트 입력 실행
15. 실행 결과와 로그 확인
```

### 3.3 실습 입력 예시

```text
사내 ERP 로그인이 되지 않습니다. 오전 업무 시작 전까지 해결이 필요합니다.
```

분류 기준 예시:

```text
유형: 계정/로그인
긴급도: 높음
처리 경로: 운영팀 알림 + 답변 초안 생성
```

### 3.4 AIPP에서 확인할 질문

수업 참여자는 실습 후 아래 질문에 답할 수 있어야 합니다.

```text
입력값은 어디서 정의했는가?
AI가 판단하는 단계는 어디인가?
조건 분기는 어느 노드에서 처리했는가?
외부 도구나 문서 검색은 어디에 연결되는가?
최종 결과는 어디에서 확인하는가?
실패하거나 애매한 결과는 어떻게 처리할 것인가?
```

## 4. n8n 실습 매뉴얼

### 4.1 수업 목표

n8n 실습의 목표는 이벤트 기반 자동화 흐름을 이해하는 것입니다.

기본 구조:

```text
Webhook Trigger
-> Set
-> IF
-> HTTP Request
-> Respond to Webhook
```

### 4.2 n8n 실행

Docker Desktop을 실행한 뒤 PowerShell에서 n8n을 실행합니다.

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

컨테이너 상태 확인:

```powershell
docker ps
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

### 4.3 n8n 화면 실습 순서

```text
1. 새 Workflow 생성
2. Webhook Trigger 노드 추가
3. HTTP Method를 POST로 설정
4. 테스트 URL 복사
5. Set 노드 추가
6. 문의 내용, 사용자, 긴급도 필드 예시 작성
7. IF 노드 추가
8. urgent 값 또는 keyword 기준으로 분기
9. HTTP Request 노드 추가
10. FastAPI, Dify API, 외부 AI API 중 하나로 요청 전송
11. Respond to Webhook 노드 추가
12. 테스트 실행
13. Executions 화면에서 실행 로그 확인
```

### 4.4 테스트 요청 예시

PowerShell에서 Webhook 테스트 URL로 요청을 보냅니다.

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

`YOUR_WEBHOOK_PATH`는 n8n 화면에서 복사한 테스트 URL로 바꿉니다.

### 4.5 n8n에서 확인할 질문

```text
Webhook은 어떤 이벤트를 받는가?
IF 노드의 조건은 무엇인가?
HTTP Request는 어느 API를 호출하는가?
실패했을 때 재시도나 대체 경로가 있는가?
실행 결과는 Executions 화면에서 확인되는가?
```

## 5. Dify 실습 매뉴얼

### 5.1 수업 목표

Dify 실습의 목표는 AI 앱과 Knowledge/RAG 기반 답변 흐름을 만드는 것입니다.

기본 구조:

```text
User Question
-> Chatflow or Workflow
-> Knowledge Search
-> LLM Answer
-> Output
-> API Access
```

### 5.2 권장 실습 방식

초보자 수업에서는 먼저 Dify Cloud 또는 수업에서 준비한 Dify 환경을 사용합니다.

로컬 self-host는 Docker Compose, 여러 컨테이너, 볼륨, 포트 설정을 함께 다루므로 선택 실습으로 진행합니다.

### 5.3 Dify 화면 실습 순서

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
15. API Access 또는 API Key 메뉴 확인
16. 외부 호출 구조 확인
```

### 5.4 Knowledge 문서 예시

수업용으로 아래와 같은 짧은 문서를 사용합니다.

```text
ERP 로그인 장애 대응 가이드

1. 비밀번호가 만료되었는지 확인한다.
2. 계정 잠금 여부를 확인한다.
3. VPN 접속 상태를 확인한다.
4. 10분 내 해결되지 않으면 운영팀에 티켓을 생성한다.
```

### 5.5 Dify에서 확인할 질문

```text
앱 유형은 왜 Chatbot, Chatflow, Workflow 중 이것을 선택했는가?
System Prompt는 어떤 역할을 하는가?
Knowledge를 연결하기 전과 후의 답변이 어떻게 달라졌는가?
API Key는 어디서 발급하는가?
n8n에서 Dify API를 호출하려면 어떤 정보가 필요한가?
```

## 6. 세 도구를 연결하는 예시

실무에서는 세 도구를 따로 쓰기도 하고, 함께 쓰기도 합니다.

```text
AIPP
-> 전체 AI 업무 흐름 설계

n8n
-> Webhook으로 문의 수신
-> 조건 분기
-> Dify API 호출
-> Slack, Email, DB로 결과 전달

Dify
-> Knowledge/RAG 기반 답변 생성
-> API로 외부에 제공
```

연결 예시:

```text
사용자 문의
-> n8n Webhook
-> IF로 긴급도 분류
-> Dify API 호출
-> 응답 결과를 n8n에서 정리
-> 결과 반환 또는 알림 전송
-> 실행 로그 확인
```

## 7. 수업 중 체크리스트

### 체크리스트

```text
[ ] 내가 자동화하려는 업무를 한 문장으로 설명할 수 있다.
[ ] 입력 데이터가 무엇인지 말할 수 있다.
[ ] Trigger가 무엇인지 정했다.
[ ] Condition이 필요한지 판단했다.
[ ] AI가 처리할 일을 정했다.
[ ] Tool 또는 Knowledge가 필요한지 판단했다.
[ ] 최종 Output 형태를 정했다.
[ ] 오류가 났을 때의 대체 흐름을 생각했다.
[ ] 실행 로그를 어디서 확인하는지 안다.
```

### 운영 체크리스트

```text
[ ] 수업 참여자가 도구 계정에 접속할 수 있는가?
[ ] n8n Docker 실행이 가능한가?
[ ] Dify 실습 환경이 준비되어 있는가?
[ ] API Key 노출 위험을 설명했는가?
[ ] 같은 시나리오를 세 도구 관점에서 비교했는가?
[ ] 실습 결과를 발표할 질문을 제시했는가?
```

## 8. 수업 마무리 질문

수업 마지막에는 아래 질문으로 정리합니다.

```text
이 업무는 AIPP, n8n, Dify 중 어떤 도구가 가장 적합한가?
그 이유는 무엇인가?
AI가 꼭 필요한 단계와 단순 자동화로 충분한 단계는 어디인가?
운영 중 오류가 발생하면 어디에서 확인할 수 있는가?
실제 회사 업무에 적용하려면 어떤 보안 기준이 필요한가?
```
