# Docker Compose Service Map

```text
backend: Auto Healing API
frontend: 사용자 요청 입력 화면
worker: 주기적 Health Check와 백그라운드 작업
monitor: 운영 이벤트와 상태 확인 화면
```

이 구조는 나중에 AWS ECS, CloudWatch, Load Balancer Health Check로 확장할 수 있습니다.
