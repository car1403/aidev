# 05. Final Presentation

최종 발표는 코드 설명보다 “문제, 구조, 실행, 검증”이 잘 보이도록 구성합니다.

## 발표 흐름

1. 프로젝트 주제와 해결하려는 장애 설명
2. 전체 서비스 구조 설명
3. Agent 역할과 Handoff Context 설명
4. 장애 이벤트 입력 시연
5. 복구 전략 선택 흐름 시연
6. Health Check와 결과 검증 시연
7. monitor 로그와 대시보드 확인
8. 보안/Guardrails/감사 로그 기준 설명
9. GitHub Actions/AWS 확장 기준 설명
10. 개선할 점과 다음 단계 정리

## 발표 자료에 들어가면 좋은 그림

```text
사용자/장애 이벤트
-> backend
-> Supervisor Agent
-> Diagnosis Agent
-> Recovery Agent
-> Validation Agent
-> monitor
```

## 시연 전 확인

- [ ] Docker Desktop이 실행 중이다.
- [ ] `docker compose down` 후 다시 `up --build`를 실행해 보았다.
- [ ] 시연할 장애 이벤트 입력값을 준비했다.
- [ ] 실패 상황이 생겼을 때 보여줄 로그 명령을 준비했다.
- [ ] 발표 자료의 URL과 실행 명령이 실제 프로젝트와 일치한다.
