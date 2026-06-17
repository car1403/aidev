# Project Alignment Checklist

이 문서는 `07_multi-agent-service-mini-project`가 이미지의 미니 프로젝트 기준과 `06_multi-agent-service-ops`에서 보강한 내용을 어떻게 반영하는지 확인하는 학생용 체크리스트입니다.

## 1. 프로젝트 방향

```text
분야:
멀티 에이전트 협업 및 서비스 운영

프로젝트:
에러 자가 치유(Auto Healing) 워크플로우

진행 방향:
1. 에이전트 협업 시나리오 및 구조 설계
2. 장애 유형별 복구 로직 및 자동화 파이프라인 구현
3. 협업 기반 실행 흐름 통합 구현
4. 서비스 배포 및 결과 검증
```

## 2. 산출물 체크

| 산출물 | 파일 | 체크 |
| --- | --- | --- |
| 멀티 에이전트 아키텍처 설계서 | `docs/multi-agent-architecture.md` | [ ] |
| 배포 및 장애 복구 보고서 | `docs/deployment-recovery-report.md` | [ ] |
| 파이프라인 구현 결과 보고서 | `docs/pipeline-result-report.md` | [ ] |

## 3. 아키텍처 설계서 체크

- [ ] 응답 속도, 결정 일관성, 장애 격리 기준을 바탕으로 아키텍처 선택 근거를 작성했습니다.
- [ ] Planner, Executor, Critic, Memory Keeper, Reporter의 역할과 책임 범위가 명확합니다.
- [ ] Agent 간 의존 관계가 정리되었습니다.
- [ ] Agent 간 책임 중복이나 공백이 없습니다.
- [ ] Handoff Context에 상태, 메모리, 중간 결과, 권한 정보가 포함됩니다.
- [ ] Agent 간 Context 동기화와 협업 일관성 유지 기준이 있습니다.

## 4. 배포 및 장애 복구 보고서 체크

- [ ] Docker Compose 또는 선택 확장 배포 매니페스트가 작성되었습니다.
- [ ] backend, frontend, worker, monitor의 역할과 port가 정리되었습니다.
- [ ] 서비스 디스커버리, 로드밸런싱, 시크릿 관리 방식을 설명했습니다.
- [ ] 네트워크, DB, API, LLM, Prompt Injection 등 장애 유형별 감지 메트릭을 작성했습니다.
- [ ] Retry, Restart, Reconnect, Fallback, 대체 모델 호출, 캐시 fallback 중 필요한 복구 전략을 정의했습니다.
- [ ] 수동 개입 없이 복구되는 시나리오 비율을 제시했습니다.

## 5. 파이프라인 구현 결과 보고서 체크

- [ ] 코드 커밋 -> 빌드 -> 테스트 -> 배포 흐름이 다이어그램으로 표현되었습니다.
- [ ] 각 단계의 입력과 출력이 정의되었습니다.
- [ ] 실패 시 블로킹 또는 재시도 정책이 정의되었습니다.
- [ ] 단위/통합 테스트 기준과 테스트 데이터 관리 방식이 있습니다.
- [ ] Slack, Teams, PagerDuty 등 알림 구조가 설명되었습니다.
- [ ] 담당자 할당과 에스컬레이션 기준이 있습니다.

## 6. 06 과정 수정 사항 반영 체크

- [ ] Agent 간 Context 동기화 기준을 문서에 반영했습니다.
- [ ] AWS App Runner/ECS 선택 기준을 제출물에 반영했습니다.
- [ ] OpenAI 모델 예시는 `gpt-4.1-mini`로 통일했습니다.
- [ ] 실제 AWS 배포는 필수가 아니며, 비용과 권한을 고려한 선택 실습으로 정리했습니다.
