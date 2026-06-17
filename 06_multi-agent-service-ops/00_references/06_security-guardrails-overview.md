# 06 Security Guardrails Overview

AI 서비스는 사용자의 자연어 입력을 처리하므로 일반 웹 서비스와 다른 보안 위험이 있습니다.

## 주요 위험

- Prompt Injection
- 민감 정보 노출
- 권한 없는 Tool 실행
- 위험 명령 실행
- Agent별 권한 과다 부여

## 기본 방어 구조

```text
입력 검증
-> Agent 역할 확인
-> Tool 권한 확인
-> 응답 정책 검증
-> 이벤트 로그 기록
```

## Guardrail 예시

- 특정 위험 문구 차단
- 민감 정보 포함 응답 차단
- 위험 명령어 포함 응답 수정
- viewer_agent는 read-only Tool만 허용
- ops_agent만 restart 요청 가능
- admin_agent만 위험 작업 승인 가능

## Docker/AWS와 연결

| 위치 | 보안 관리 |
| --- | --- |
| `.env` | API Key, 비밀번호 관리 |
| Docker Compose | 서비스별 환경 변수 분리 |
| backend | 입력 검증, 권한 검사 |
| worker | 위험 작업 실행 제한 |
| AWS IAM | 서비스별 권한 분리 |
| CloudWatch Logs | 보안 이벤트 기록 |
