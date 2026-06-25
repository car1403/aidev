# 06. Submission Checklist

최종 제출 전에 아래 항목을 확인합니다.

## 파일 구조

- [ ] `README.md`가 있다.
- [ ] `SETUP.md` 또는 실행 방법이 정리되어 있다.
- [ ] `.env.example`이 있다.
- [ ] `.env`는 제외되어 있다.
- [ ] `docker-compose.yml`이 있다.
- [ ] `backend`, `frontend`, `worker`, `monitor` 폴더가 있다.
- [ ] `docs` 폴더에 필수 산출물이 있다.

## 실행

- [ ] `docker compose config`가 통과한다.
- [ ] `docker compose up --build`가 동작한다.
- [ ] backend `/health`가 정상이다.
- [ ] frontend와 monitor 화면이 열린다.
- [ ] worker 로그가 확인된다.

## 산출물

- [ ] 멀티 에이전트 아키텍처 설계서
- [ ] 배포 및 장애 복구 보고서
- [ ] 파이프라인 구현 결과 보고서

## 선택 보조 산출물

- [ ] 테스트 체크리스트
- [ ] 보안 Runbook
- [ ] 감사 로그/정책 위반 추적 문서
- [ ] Guardrails 검증 문서
- [ ] LangSmith식 실행 추적 계획

## 보안

- [ ] API Key가 노출되지 않았다.
- [ ] AWS Key가 노출되지 않았다.
- [ ] `.env`가 Git에 올라가지 않았다.
- [ ] 민감 정보가 로그에 출력되지 않는다.

## 발표

- [ ] 시연 순서가 정리되어 있다.
- [ ] 장애 입력 예시가 준비되어 있다.
- [ ] 로그 확인 명령이 준비되어 있다.
- [ ] 개선할 점과 다음 단계가 정리되어 있다.
