# 05. Project Class Manual

이 문서는 `09_ai-workflow-mini-project` 수업에서 팀 프로젝트를 진행할 때 사용하는 강의용 매뉴얼입니다.

## 1. 프로젝트 목표

09 과정의 목표는 AIPP, n8n, Dify 중 하나 이상을 활용해 기술지원 자동화 워크플로우를 설계하고 시연하는 것입니다.

프로젝트 주제:

```text
기업형 지능형 기술지원 자동화 워크플로우
```

기본 흐름:

```text
문의 접수
-> 문의 유형 분류
-> 긴급도 판단
-> 관련 문서 검색
-> AI 답변 초안 생성
-> 운영팀 알림 또는 사용자 응답
-> 실행 로그와 품질 평가
```

## 2. 이번 프로젝트에서 반드시 강조할 내용

08 과정 보강 내용을 09 프로젝트에 반영합니다.

```text
RAG 또는 Knowledge 검색 구조
데이터 처리 노드와 노드 간 데이터 흐름
Loop, Fork-Join, 병렬 처리, 집계 적용 여부
Prompt Injection 방어
입력 검증과 출력 필터링
비용, API 사용량, 리소스 관리
Workflow Template 운영
Multi-Agent Workflow 역할 분리
```

모든 항목을 실제로 구현하지 않아도 됩니다. 하지만 각 팀은 "적용했는지", "적용하지 않았다면 왜인지", "향후 확장한다면 어떻게 할 것인지"를 설명할 수 있어야 합니다.

## 3. 수업 진행 순서

```text
1. 수업용 샘플 실행
2. 샘플 화면에서 사용자 입력과 결과 확인
3. AIPP, n8n, Dify 설계 문서 비교
4. 팀별 주제 선택
5. Trigger, Condition, Action 작성
6. RAG/Data Node 필요 여부 판단
7. 사용할 도구 선택
8. 팀 템플릿 복사
9. 문서 작성
10. 코드 또는 도구 화면 실습
11. 테스트 체크리스트 작성
12. 발표 자료 작성
13. 최종 시연
```

## 4. 첫 시간 강의 흐름

| 단계 | 내용 | 목표 |
| --- | --- | --- |
| 1 | 09 과정 목표 설명 | 미니 프로젝트 방향 이해 |
| 2 | 수업용 샘플 실행 | 완성 예시 확인 |
| 3 | `/docs` API 확인 | backend 구조 이해 |
| 4 | Streamlit 화면 확인 | 사용자 시연 흐름 이해 |
| 5 | AIPP/n8n/Dify 설계 문서 비교 | 도구별 역할 이해 |
| 6 | 팀 주제 브레인스토밍 | 프로젝트 방향 결정 |
| 7 | 팀 템플릿 복사 | 작업 공간 준비 |

## 5. 팀 프로젝트 기본 질문

팀은 아래 질문에 답하면서 프로젝트를 진행합니다.

```text
우리 팀은 어떤 문제를 해결하는가?
사용자는 누구인가?
입력 데이터는 무엇인가?
워크플로우는 어떤 이벤트로 시작하는가?
어떤 조건에서 분기하는가?
AI가 판단하거나 생성하는 내용은 무엇인가?
어떤 Tool/API/Knowledge/RAG가 필요한가?
데이터는 어떤 노드를 거쳐 변환되는가?
최종 결과는 어떤 형태로 보여줄 것인가?
실패했을 때 대체 흐름은 무엇인가?
Prompt Injection 같은 위험한 입력은 어떻게 처리할 것인가?
비용과 리소스는 어떻게 관리할 것인가?
Multi-Agent가 필요하다면 역할을 어떻게 나눌 것인가?
```

## 6. 도구 선택 매뉴얼

| 도구 | 선택하면 좋은 경우 | 결과물 |
| --- | --- | --- |
| AIPP | AI 업무 흐름을 노드로 설계하는 것이 중요할 때 | 워크플로우 노드 설계안 |
| n8n | Webhook, API, 알림, 외부 서비스 연결이 중요할 때 | n8n 노드 흐름과 테스트 결과 |
| Dify | Knowledge/RAG 기반 AI 응답이 중요할 때 | Dify 앱, Prompt, Knowledge 설계 |
| FastAPI | 샘플 API나 분석 로직을 직접 구현할 때 | API endpoint와 Swagger 화면 |
| Streamlit | 시연용 사용자 화면이 필요할 때 | 입력/결과 확인 화면 |

초보자 팀은 아래 조합 중 하나를 선택하는 것이 좋습니다.

```text
FastAPI + Streamlit
n8n + FastAPI
n8n + Dify
AIPP 설계 + FastAPI 샘플
Dify Knowledge + Streamlit 시연
```

## 7. 팀 템플릿 복사

```powershell
cd C:\aidev\09_ai-workflow-mini-project
Copy-Item .\99_team-projects\ai-workflow-team-template .\99_team-projects\team-01-tech-support-workflow -Recurse
```

복사 후 먼저 작성할 문서:

```text
docs/project-plan.md
docs/workflow-design.md
docs/ops-quality-plan.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 8. 최소 완성 기준

```text
[ ] 프로젝트 주제가 명확하다.
[ ] 사용자 입력 예시가 있다.
[ ] Trigger, Condition, Action이 있다.
[ ] AI 역할이 정의되어 있다.
[ ] Tool/API/Knowledge/RAG 역할이 정의되어 있다.
[ ] RAG/Data Node 필요 여부가 작성되어 있다.
[ ] AIPP, n8n, Dify 중 최소 1개 이상의 사용 방식이 있다.
[ ] 오류 처리 또는 fallback이 있다.
[ ] Prompt Injection 방어와 입력/출력 검증 기준이 있다.
[ ] 비용, 로그, 리소스 관리 계획이 있다.
[ ] 테스트 체크리스트가 작성되어 있다.
[ ] 발표 자료가 있다.
```

## 9. 발표 구성

발표는 아래 순서로 구성합니다.

```text
1. 프로젝트 제목
2. 해결하려는 문제
3. 사용자 시나리오
4. 전체 워크플로우 구조
5. RAG/Data Node와 데이터 흐름
6. 선택한 도구와 선택 이유
7. 시연 화면 또는 설계 결과
8. 테스트 결과
9. 오류 처리, 보안, 운영 품질 계획
10. 비용과 리소스 관리 계획
11. Multi-Agent 적용 여부와 향후 확장
12. 개선 방향
```

## 10. 평가 질문

팀별 중간 점검 때 아래 질문을 사용합니다.

```text
지금 만든 흐름에서 Trigger는 무엇인가요?
Condition은 어떤 기준으로 나누나요?
AI가 맡는 역할은 너무 크지 않나요?
RAG가 필요한 이유는 무엇인가요?
검색 결과가 없으면 어떻게 처리하나요?
선택한 도구가 이 문제에 맞나요?
위험한 입력을 넣으면 어떻게 되나요?
API 호출이 실패하면 사용자는 어떤 안내를 받나요?
운영 로그에서 무엇을 확인하나요?
발표에서 실제로 무엇을 보여줄 수 있나요?
```
