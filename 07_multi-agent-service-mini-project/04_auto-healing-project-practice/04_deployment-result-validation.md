# 04. Deployment Result Validation

배포와 결과 검증은 프로젝트가 실제로 실행 가능한지 확인하는 단계입니다.

## 로컬 검증

```powershell
docker compose config
docker compose up --build
```

확인할 것:

- backend `/health`가 정상인가?
- frontend가 열리는가?
- monitor가 열리는가?
- worker 로그가 출력되는가?
- 장애 이벤트가 처리되는가?
- 복구 결과가 기록되는가?

## GitHub Actions 검증

선택 확장으로 아래 흐름을 구성할 수 있습니다.

```text
push
-> Python 문법 검사
-> docker compose config
-> Docker image build
```

실제 자동 배포까지 하지 않아도, build check가 통과하면 프로젝트 구조가 깨지지 않았는지 확인할 수 있습니다.

## AWS 배포 검증

AWS 실제 배포는 필수가 아닙니다. 문서에는 아래 내용을 정리합니다.

- App Runner 또는 ECS 중 어떤 방식을 선택할 것인가?
- Docker image는 ECR에 저장할 것인가?
- 환경변수와 secret은 어떻게 관리할 것인가?
- Health Check 경로는 무엇인가?
- CloudWatch Logs에서 어떤 로그를 볼 것인가?
- 실습 후 어떤 리소스를 삭제할 것인가?

## 결과 보고서에 쓸 내용

```text
실행 명령:
확인한 URL:
테스트한 장애 유형:
적용한 복구 전략:
복구 성공 여부:
실패 시 원인:
monitor에서 확인한 로그:
추가 개선 사항:
```
