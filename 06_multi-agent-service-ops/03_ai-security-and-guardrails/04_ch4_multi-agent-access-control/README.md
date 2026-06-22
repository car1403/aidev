# 04_ch4_multi-agent-access-control

Multi-Agent 환경에서 Agent별 접근 권한을 설계하는 방법을 학습합니다.

## 핵심 개념

Multi-Agent 서비스에서는 Agent마다 접근할 수 있는 데이터와 실행할 수 있는 작업이 달라야 합니다.

```text
planner_agent: 계획 수립만 가능
ops_agent: 운영 Tool 일부 사용 가능
security_agent: 보안 이벤트 확인 가능
admin_agent: 승인된 위험 작업 관리 가능
```

## 운영 관점

이 구조는 나중에 Docker/AWS에서 다음 개념으로 이어집니다.

- 서비스별 환경 변수 분리
- IAM Role 분리
- 관리자 API와 일반 API 분리
- 보안 로그와 감사 로그 수집

## 실행

```powershell
python.\04_ch4_multi-agent-access-control\01_multi-agent-access-control.py
```
