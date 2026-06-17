# Test Checklist

## Local Docker Compose

- [ ] `Copy-Item .env.example .env` 실행
- [ ] `docker compose up --build` 실행 성공
- [ ] backend `/health` 확인
- [ ] frontend 화면 접속
- [ ] monitor 화면 접속
- [ ] Auto Healing 요청 실행
- [ ] 이벤트 이력 표시 확인

## Extension

- [ ] 장애 유형 추가
- [ ] Tool 권한 제어 추가
- [ ] 실패 이벤트 로그 추가
- [ ] AWS 배포 체크리스트 작성
