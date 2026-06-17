# Team Template

팀별 AI 워크플로우 자동화 미니 프로젝트 템플릿입니다.

이 템플릿은 AIPP, n8n, Dify 중 최소 1개 이상을 사용하거나, 해당 도구로 옮길 수 있을 만큼 구체적인 설계 문서를 작성하는 것을 목표로 합니다.

## 진행 순서

1. `docs/project-plan.md`에 주제와 목표를 작성합니다.
2. `docs/workflow-design.md`에 Trigger, Condition, Action 흐름을 설계합니다.
3. AIPP, n8n, Dify 중 어떤 도구를 사용할지 정합니다.
4. `backend`에 API 또는 워크플로우 로직을 구현합니다.
5. `frontend`에 시연 화면을 구현합니다.
6. `docs/ops-quality-plan.md`에 운영/품질 기준을 정리합니다.
7. `docs/test-checklist.md`로 테스트 결과를 확인합니다.
8. 최종 발표 자료를 `presentation/final-presentation.md`에 작성합니다.

## 권장 구조

```text
team-template
├─ README.md
├─ .env.example
├─ backend
├─ frontend
├─ docs
└─ presentation
```

## 팀 프로젝트 필수 조건

```text
[ ] 업무 자동화 시나리오가 명확하다.
[ ] Trigger, Condition, Action이 포함되어 있다.
[ ] LLM 또는 AI API가 맡을 역할이 정의되어 있다.
[ ] Tool/API/Knowledge 중 하나 이상이 포함되어 있다.
[ ] AIPP, n8n, Dify 중 최소 1개 이상의 활용 방식이 정리되어 있다.
[ ] 오류 처리와 fallback 흐름이 있다.
[ ] 실행 로그 또는 운영 지표가 있다.
[ ] 테스트 입력과 기대 출력이 있다.
```

## 도구 선택 가이드

| 도구 | 선택하면 좋은 경우 |
| --- | --- |
| AIPP | AI 업무 흐름을 화면에서 노드로 설계하고 싶을 때 |
| n8n | Webhook, API, 알림, 외부 서비스 연결이 필요할 때 |
| Dify | Knowledge/RAG 기반 AI 답변 앱이 필요할 때 |

## 발표 준비

최종 발표에서는 아래 내용을 포함합니다.

```text
1. 프로젝트 주제
2. 해결하려는 업무 문제
3. 전체 워크플로우 구조
4. 선택한 도구와 선택 이유
5. 테스트 입력과 실행 결과
6. 오류 처리와 fallback
7. 운영/품질 관리 계획
8. 개선 방향
```
