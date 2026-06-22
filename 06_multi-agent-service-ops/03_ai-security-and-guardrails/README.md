# 03 AI Security and Guardrails

이 단원은 AI 서비스와 Multi-Agent 시스템에서 필요한 보안과 가드레일을 학습합니다.

AI 서비스는 일반 웹 서비스와 달리 사용자의 자연어 입력을 모델과 Agent가 해석합니다. 그래서 Prompt Injection, 위험한 Tool 실행, 권한이 없는 Agent의 작업 수행, 정책 위반 응답 같은 문제가 생길 수 있습니다.

## 이 단원의 목표

- Prompt Injection이 무엇인지 이해하고 기본 방어 구조를 만들 수 있다.
- 입력 검증과 출력 필터링의 차이를 설명할 수 있다.
- 정책 기반 응답 검증 구조를 설계할 수 있다.
- Tool 실행 권한을 Agent 역할별로 제한할 수 있다.
- Multi-Agent 환경에서 Agent별 접근 권한을 설계할 수 있다.
- AI 서비스 보안 운영 Runbook을 작성할 수 있다.
- 정책 위반 이력과 감사 로그를 설계할 수 있다.
- Guardrails AI 같은 검증 도구의 통합 위치를 설명할 수 있다.
- Docker/AWS 운영 환경에서 보안 설정이 어디에 들어가는지 이해한다.

## 학습 순서

```text
01_ch1_prompt-injection-defense
-> 02_ch2_policy-based-response-validation
-> 03_ch3_tool-permission-control
-> 04_ch4_multi-agent-access-control
-> 10_labs
-> 20_assignments
```

## 환경 준비

03 단원 예제는 외부 API 없이 실행됩니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
```

03 단원 폴더로 이동합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\03_ai-security-and-guardrails
```

## 왜 보안과 가드레일이 필요한가?

AI 서비스는 다음과 같은 위험을 가질 수 있습니다.

```text
사용자가 시스템 지시를 무시하라고 입력함
Agent가 권한 없는 Tool을 실행함
응답에 민감 정보가 포함됨
운영 정책에 맞지 않는 답변이 생성됨
여러 Agent 중 하나가 과도한 권한을 가짐
```

이 단원에서는 완벽한 보안 솔루션을 만드는 것이 아니라, 초보자가 이해할 수 있는 기본 방어 패턴을 코드로 연습합니다.

## Docker/AWS 운영과 연결

보안 설정은 코드에만 있지 않습니다.

| 위치 | 보안 관리 예시 |
| --- | --- |
| `.env` | API Key, 토큰, 비밀번호 관리 |
| Docker Compose | 서비스별 환경 변수, 네트워크 분리 |
| backend | 입력 검증, 권한 확인, Tool 실행 제한 |
| worker | 위험 작업 실행 전 승인 확인 |
| monitor | 보안 이벤트와 차단 로그 확인 |
| AWS | Secrets Manager, IAM Role, Security Group, CloudWatch Logs |

## 실행 예제

```powershell
python.\01_ch1_prompt-injection-defense\01_prompt-injection-filter.py
python.\02_ch2_policy-based-response-validation\01_policy-response-validator.py
python.\03_ch3_tool-permission-control\01_tool-permission-control.py
python.\04_ch4_multi-agent-access-control\01_multi-agent-access-control.py
```

## 추가 Lab

10_labs에는 운영 보안 관점의 추가 실습이 포함되어 있습니다.

```text
lab-05_security-policy-runbook.md
lab-06_audit-policy-violation-tracking.md
lab-07_guardrails-ai-integrated-validation.md
```

이 Lab들은 팀 미니 프로젝트에서 보안 정책, 감사 로그, Guardrail 통합 설계를 작성할 때 사용합니다.
