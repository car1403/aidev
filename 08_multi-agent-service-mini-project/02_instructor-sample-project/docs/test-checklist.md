# Test Checklist

샘플 프로젝트 실행 후 아래 항목을 확인합니다.

## Local Docker Compose

- [ ] `Copy-Item .env.example .env`를 실행했다.
- [ ] `docker compose config`가 통과했다.
- [ ] `docker compose up --build`로 서비스가 실행되었다.
- [ ] backend `/health`가 정상 응답한다.
- [ ] frontend 화면에 접속할 수 있다.
- [ ] monitor 화면에 접속할 수 있다.
- [ ] worker 로그를 확인할 수 있다.
- [ ] Auto Healing 요청 또는 장애 이벤트 예시를 실행했다.
- [ ] 이벤트 이력이 화면이나 로그에 표시된다.
- [ ] `docker compose down`으로 정상 종료했다.

## Auto Healing Flow

- [ ] 장애 유형을 2개 이상 설명할 수 있다.
- [ ] 복구 전략을 2개 이상 설명할 수 있다.
- [ ] Retry, Restart, Fallback의 차이를 설명할 수 있다.
- [ ] 위험한 복구 명령을 제한해야 하는 이유를 설명할 수 있다.
- [ ] 복구 이후 Health Check가 왜 필요한지 설명할 수 있다.

## Extension

- [ ] 팀 프로젝트에서 추가할 장애 유형을 정했다.
- [ ] Tool 권한 제어 기준을 정했다.
- [ ] 실패 이벤트 로그 기준을 정했다.
- [ ] GitHub Actions build check 적용 여부를 정했다.
- [ ] AWS 배포 체크리스트 작성 여부를 정했다.
- [ ] 비용과 보안 주의 사항을 문서에 적었다.
