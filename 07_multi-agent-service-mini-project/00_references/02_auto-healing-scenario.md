# Auto Healing Scenario

## 기본 장애 시나리오

- backend health check 실패
- worker timeout
- 외부 API 연결 실패
- 권한 또는 Secret 설정 오류
- 알 수 없는 컨테이너 종료

## 복구 조치 예시

- retry request
- restart service
- check dependency
- collect logs
- escalate to operator
