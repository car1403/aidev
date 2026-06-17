# 02_ch2_health-check-retry-restart

Health Check, Retry, Restart의 차이를 학습합니다.

## 개념 구분

| 개념 | 의미 |
| --- | --- |
| Health Check | 서비스가 정상인지 확인 |
| Retry | 같은 작업을 다시 시도 |
| Restart | 서비스 프로세스나 컨테이너를 다시 시작 |

## 중요한 순서

무조건 재시작부터 하면 안 됩니다.

```text
Health Check
-> 일시적 장애면 Retry
-> 반복 실패면 Restart 요청
-> 그래도 실패하면 수동 확인 또는 Fallback
```

## 실행

```powershell
python .\02_ch2_health-check-retry-restart\01_health-check-retry-restart.py
```
