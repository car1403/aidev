# Project Big Picture

이 미니 프로젝트는 여러 Agent가 협업해 서비스 장애를 분석하고 복구 조치를 제안하는 구조입니다.

```text
장애 메시지 입력
-> Supervisor Agent가 장애 유형 분류
-> Ops Agent가 Health Check 수행
-> Recovery Agent가 Retry/Restart/Fallback 결정
-> Reviewer Agent가 복구 결과 검증
-> Monitor 화면에서 이벤트 확인
```
