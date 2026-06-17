# 04_ch4_recovery-result-validation

복구 조치 후 결과를 검증하는 방법을 학습합니다.

## 왜 검증이 필요한가?

재시작 명령을 보냈다고 복구가 완료된 것은 아닙니다.

반드시 아래를 확인해야 합니다.

- Health Check가 정상으로 돌아왔는가?
- 같은 오류 로그가 반복되지 않는가?
- 사용자가 다시 요청을 처리할 수 있는가?
- 수동 확인이 필요한 상태인가?

## 실행

```powershell
python .\04_ch4_recovery-result-validation\01_recovery-result-validation.py
```
