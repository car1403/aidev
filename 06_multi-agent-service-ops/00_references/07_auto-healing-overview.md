# 07 Auto Healing Overview

Auto Healing은 장애가 발생했을 때 시스템이 스스로 진단하고 복구 흐름을 실행하는 구조입니다.

## 기본 흐름

```text
Health Check
-> 장애 유형 분류
-> Retry 또는 Restart 결정
-> 복구 조치 실행
-> 결과 검증
-> 이벤트 로그 기록
```

## 장애 유형 예시

| 장애 유형 | 설명 | 대응 |
| --- | --- | --- |
| unhealthy | Health Check 실패 | restart |
| timeout | 응답 지연 | retry |
| dependency_error | DB/API 연결 실패 | dependency 확인 |
| permission_error | 권한/Secret 문제 | 권한 설정 확인 |
| unknown | 원인 불명 | 로그 수집 후 운영자 확인 |

## 중요한 원칙

무조건 재시작하지 않습니다.

먼저 상태를 확인하고, 실패 횟수와 장애 유형에 따라 복구 조치를 선택해야 합니다.

```text
1회 실패: retry
반복 실패: restart
권한/외부 의존성 문제: escalate
원인 불명: collect logs
```
