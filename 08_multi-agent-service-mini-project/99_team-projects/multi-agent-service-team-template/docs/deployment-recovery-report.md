# Deployment Recovery Report

## 1. 실행 환경

```text
실행 위치:
Docker Desktop 버전:
Docker Compose 버전:
실행 명령:
```

## 2. 서비스 구성

| 서비스 | 역할 | 포트 | Health Check |
| --- | --- | --- | --- |
| backend | API 서버 | 8000 | `/health` |
| frontend | 입력/결과 화면 | 8801 | 화면 접속 |
| worker | 장애 처리 | 없음 | 로그 확인 |
| monitor | 운영 대시보드 | 8802 | 화면 접속 |

## 3. 장애 유형

| 장애 유형 | 감지 기준 | 영향 범위 | 복구 전략 |
| --- | --- | --- | --- |
| timeout | 응답 지연 | backend | retry |
| api_5xx | 500번대 응답 | backend | fallback |
| prompt_injection | 위험 지시문 | LLM/Tool | block |

## 4. 복구 전략

| 전략 | 적용 조건 | 성공 기준 | 실패 시 다음 조치 |
| --- | --- | --- | --- |
| Retry | 일시적 오류 | 재요청 성공 | fallback |
| Restart | worker 오류 | worker 로그 정상 | manual review |
| Fallback | 원 경로 실패 | 대체 응답 제공 | report |
| Block | 정책 위반 | 위험 작업 미실행 | audit log |

## 5. 검증 결과

```text
테스트한 장애:
적용한 복구 전략:
복구 성공 여부:
monitor 표시 여부:
worker 로그 확인 여부:
개선할 점:
```

## 6. AWS 확장 계획

실제 배포를 하지 않았다면 선택 확장 설계로 작성합니다.

- ECR image 저장 전략
- App Runner 또는 ECS 선택 이유
- 환경변수와 secret 관리
- `/health` 기반 Health Check
- CloudWatch Logs 확인 방식
- 실습 후 리소스 삭제 계획
