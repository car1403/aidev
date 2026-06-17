# 03_ch3_recovery-pipeline

Auto Healing 복구 파이프라인을 단계별로 설계합니다.

## 파이프라인 예시

```text
collect_status
-> classify_failure
-> choose_action
-> execute_action
-> validate_result
-> write_event_log
```

## 운영 관점

각 단계는 로그로 남겨야 합니다.

- 어떤 서비스가 문제였는가?
- 어떤 장애 유형으로 판단했는가?
- 어떤 복구 조치를 선택했는가?
- 복구가 성공했는가?
- 운영자 확인이 필요한가?

## 실행

```powershell
python .\03_ch3_recovery-pipeline\01_auto-healing-pipeline.py
```
