# 03_ch3_supervisor-router-workflow

Supervisor와 Router 기반 작업 분배 구조를 학습합니다.

## Supervisor와 Router 차이

- Router는 요청 유형에 따라 어느 Agent를 호출할지 선택합니다.
- Supervisor는 전체 실행 흐름, 중간 결과, 재시도 여부까지 관리합니다.

## 운영 관점

실서비스에서는 Supervisor가 아래 정보를 기록해야 합니다.

- 어떤 요청이 들어왔는가?
- 어떤 Agent가 선택되었는가?
- 실행 결과는 성공인가 실패인가?
- 재시도 또는 대체 경로가 필요한가?

## 실행

```powershell
python .\03_ch3_supervisor-router-workflow\01_supervisor-router-workflow.py
```
