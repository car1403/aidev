# 04_ch4_execution-status-management

Agent 실행 상태를 관리하는 방법을 학습합니다.

## 상태 값 예시

```text
pending: 실행 대기
running: 실행 중
success: 성공
failed: 실패
cancelled: 취소
```

## 왜 필요한가?

운영 환경에서는 사용자가 요청한 작업이 지금 어디까지 진행되었는지 알아야 합니다.

- 작업이 아직 대기 중인가?
- 어떤 Agent가 실행 중인가?
- 실패했다면 어느 단계에서 실패했는가?
- 다시 시도해도 되는가?

## 실행

```powershell
python .\04_ch4_execution-status-management\01_execution-status-manager.py
```
