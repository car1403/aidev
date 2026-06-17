# Test Checklist

## Local Docker Compose

- [ ] `Copy-Item .env.example .env` 실행
- [ ] `docker compose config` 통과
- [ ] `docker compose up --build` 실행 성공
- [ ] backend `/health` 확인
- [ ] frontend 화면 접속
- [ ] monitor 화면 접속
- [ ] worker 로그 확인
- [ ] Auto Healing 요청 실행
- [ ] 이벤트 이력 표시 확인
- [ ] `docker compose down` 정상 종료

## Auto Healing

- [ ] 장애 유형 2개 이상 테스트
- [ ] 복구 전략 2개 이상 확인
- [ ] Retry/Restart/Fallback 기준 설명
- [ ] 위험한 복구 명령을 제한하는 기준 설명

## Extension

- [ ] 장애 유형 추가
- [ ] Tool 권한 제어 추가
- [ ] 실패 이벤트 로그 추가
- [ ] GitHub Actions build check 설명
- [ ] AWS 배포 체크리스트 작성
- [ ] 비용/보안 주의 사항 작성
