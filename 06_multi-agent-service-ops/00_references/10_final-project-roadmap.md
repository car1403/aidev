# 10 Final Project Roadmap

06 과정의 마지막 미니 프로젝트는 Auto Healing Multi-Agent Service입니다.

## 프로젝트 목표

```text
장애 메시지 입력
-> 장애 유형 분류
-> 복구 조치 선택
-> Docker Compose 서비스 상태 확인
-> 운영 이벤트 기록
-> 모니터 대시보드 표시
```

## 필수 구현

- backend API
- frontend Streamlit 화면
- worker 실행기
- monitor 대시보드
- Dockerfile
- docker-compose.yml
- `.env.example`
- 테스트 체크리스트

## 팀 프로젝트 확장 아이디어

- 장애 유형 추가
- Tool 권한 제어 추가
- 보안 가드레일 추가
- GitHub Actions build check 추가
- AWS 배포 체크리스트 작성
- CloudWatch 기반 운영 설계 작성

## 발표에 포함할 내용

1. 프로젝트 주제
2. 서비스 구조
3. Agent 역할
4. Auto Healing 흐름
5. Docker Compose 실행 화면
6. 운영 대시보드
7. 장애 대응 결과
8. 개선 방향
