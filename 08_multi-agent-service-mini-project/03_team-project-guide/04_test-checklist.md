# 04. Test Checklist

최종 제출 전에 아래 항목을 확인합니다.

## 실행 테스트

- [ ] `Copy-Item .env.example .env`를 실행했다.
- [ ] `docker compose config`가 통과한다.
- [ ] `docker compose up --build`로 모든 서비스가 실행된다.
- [ ] backend `/health`가 정상 응답한다.
- [ ] frontend 화면이 열린다.
- [ ] monitor 화면이 열린다.
- [ ] worker 로그가 출력된다.

## 기능 테스트

- [ ] 장애 이벤트를 입력할 수 있다.
- [ ] 장애 유형이 분류된다.
- [ ] 복구 전략이 선택된다.
- [ ] 복구 결과가 기록된다.
- [ ] 실패 시 fallback 또는 manual review 상태가 표시된다.
- [ ] monitor에서 이벤트를 확인할 수 있다.

## 문서 테스트

- [ ] Agent 역할이 문서화되어 있다.
- [ ] Handoff Context가 문서화되어 있다.
- [ ] 장애 유형과 복구 전략이 문서화되어 있다.
- [ ] 배포 및 장애 복구 보고서가 작성되어 있다.
- [ ] 파이프라인 구현 결과 보고서가 작성되어 있다.
- [ ] 보안/감사/Guardrails 기준이 작성되어 있다.

## 보안 테스트

- [ ] `.env`가 Git에 올라가지 않는다.
- [ ] API Key가 문서에 적혀 있지 않다.
- [ ] 위험한 Tool 실행 제한 기준이 있다.
- [ ] 정책 위반 이벤트 기록 기준이 있다.
