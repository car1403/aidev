# 06_ch6_prompt-injection-and-security-filters

AI 워크플로우 안에서 Prompt Injection 방어, 입력 검증, 출력 필터링을 설계하는 챕터입니다.

## 학습 목표

- Prompt Injection이 워크플로우에 어떤 위험을 만드는지 이해합니다.
- 입력 단계에서 차단하거나 사람 검토로 넘길 기준을 만들 수 있습니다.
- 출력 단계에서 민감 정보나 정책 위반 응답을 필터링할 수 있습니다.
- 노코드 워크플로우 도구에서 보안 필터 노드를 어디에 배치해야 하는지 설계할 수 있습니다.

## 기본 구조

```text
User Input
-> Input Security Filter
-> Workflow Nodes
-> LLM Response
-> Output Security Filter
-> Audit Log
-> Final Response
```

## 실행 예제

```powershell
cd C:\aidev\08_ai-workflow-automation\05_workflow-ops-and-quality
python.\06_ch6_prompt-injection-and-security-filters\01_prompt_injection_security_filter.py
```
