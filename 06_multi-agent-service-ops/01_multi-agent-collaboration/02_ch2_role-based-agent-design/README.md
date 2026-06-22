# 02_ch2_role-based-agent-design

역할(Role) 기반으로 Agent를 분리하는 방법을 학습합니다.

## 역할 설계 원칙

- Agent 이름은 역할을 설명해야 합니다.
- 각 Agent는 한 가지 책임을 중심으로 설계합니다.
- Agent 간 입력과 출력 형식을 명확히 합니다.
- 권한이 필요한 작업은 별도 Agent 또는 Tool로 분리합니다.

## Docker Compose 연결 관점

역할 분리는 나중에 서비스 분리 기준이 됩니다.

```text
planner/reviewer: backend 내부 함수로 시작 가능
executor: worker 서비스로 분리 가능
monitor: monitor 서비스로 분리 가능
```

## 실행

```powershell
python.\02_ch2_role-based-agent-design\01_role-based-agent-design.py
```
