# Lab 06. Audit and Policy Violation Tracking

## 목표

Agent 실행 로그와 정책 위반 이력을 감사 추적(Audit Trail) 관점으로 설계합니다.

감사 추적은 누가, 언제, 어떤 요청을 했고, 어떤 정책이 적용되었으며, 어떤 조치가 수행되었는지 나중에 확인할 수 있게 남기는 기록입니다.

## 감사 로그에 남길 정보

```text
event_id
timestamp
request_id
user_id
agent_name
tool_name
policy_name
decision
reason
risk_level
action_taken
```

## decision 예시

```text
allow    정상 허용
block    차단
redact   민감 정보 마스킹
review   사람 검토 필요
escalate 운영자 알림
```

## 정책 위반 추적 예시

```text
사용자가 시스템 프롬프트를 보여 달라고 요청
-> Prompt Injection 정책 위반
-> block
-> audit log 저장
-> 반복 발생 시 운영자 알림
```

## 작성 실습

아래 표를 채웁니다.

| 항목 | 내용 |
| --- | --- |
| 정책 이름 |  |
| 위반 입력 예시 |  |
| 탐지 기준 |  |
| 처리 방식 | allow / block / redact / review / escalate |
| 로그 항목 |  |
| 운영자 확인 방법 |  |

## 운영 연결

감사 로그는 다음 운영 도구와 연결할 수 있습니다.

```text
로컬 파일 로그
Streamlit 운영 대시보드
CloudWatch Logs
CloudWatch Logs Insights
보안 이벤트 알림
```

## 확인 질문

- 모든 사용자 입력을 그대로 로그에 저장해도 되는가?
- API Key나 개인정보가 로그에 들어가면 어떻게 처리해야 하는가?
- 정책 위반 이벤트를 대시보드에서 어떤 기준으로 필터링할 것인가?
