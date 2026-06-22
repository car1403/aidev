# 99_mini-project

08 과정에서 학습한 AI Workflow 개념, AIPP, n8n, Dify, 운영/품질 관점을 통합하는 미니 프로젝트입니다.

## 프로젝트 주제

```text
노코드·로코드 기반 기업형 지능형 기술 지원 자동화 워크플로우
```

## 프로젝트 목표

기술 지원 문의가 들어왔을 때 다음 흐름을 자동화합니다.

```text
문의 접수
-> 유형/긴급도 분류
-> 관련 기술 문서 검색
-> 답변 초안 생성
-> 위험/품질 검증
-> 긴급 건은 운영팀 알림
-> 일반 건은 답변 후보 생성
-> 실행 로그와 품질 지표 기록
```

이 프로젝트의 핵심은 완성도 높은 서비스를 만드는 것보다, 실제 업무를 AIPP, n8n, Dify 같은 도구에 옮길 수 있을 만큼 명확하게 설계하는 것입니다.

## 구성

```text
99_mini-project
├─ README.md
├─ sample-tech-support-workflow
└─ team-template
```

## 진행 순서

1. `sample-tech-support-workflow`를 실행해 전체 흐름을 확인합니다.
2. FastAPI backend의 `/analyze`, `/events`, `/metrics` API를 확인합니다.
3. Streamlit frontend에서 문의 입력과 분석 결과를 확인합니다.
4. `docs`의 AIPP, n8n, Dify 설계 문서를 읽고 같은 흐름을 도구 화면으로 옮기는 방식을 이해합니다.
5. `team-template`을 기반으로 팀별 미니 프로젝트를 설계합니다.
6. 05 단원에서 배운 운영/품질 기준을 적용합니다.
7. 최종 발표에서 어떤 도구를 왜 선택했는지 설명합니다.

## 샘플 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\99_mini-project\sample-tech-support-workflow
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item.env.example.env
```

Backend 실행:

```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8900
```

Frontend 실행:

```powershell
streamlit run frontend/app.py --server.port 8901
```

확인 주소:

```text
Backend health: http://127.0.0.1:8900/health
Frontend: http://127.0.0.1:8901
```

## 팀 프로젝트 시작

팀별 프로젝트를 시작할 때는 템플릿을 복사합니다.

```powershell
cd C:\aidev\08_ai-workflow-automation
Copy-Item.\99_mini-project\team-template.\99_mini-project\team-01-tech-support-workflow -Recurse
```

팀명에 맞게 폴더 이름을 변경해도 됩니다.

## 도구 선택 기준

팀 프로젝트에서는 AIPP, n8n, Dify 중 최소 1개 이상을 사용하거나, 사용할 수 있도록 구체적인 설계 문서를 작성해야 합니다.

| 선택 도구 | 적합한 경우 | 산출물 예시 |
| --- | --- | --- |
| AIPP | AI 업무 흐름을 노드와 단계로 설계하는 것이 중심 | AIPP 워크플로우 설계도, 노드별 역할 |
| n8n | Webhook, API, 알림, 외부 서비스 연결이 중심 | n8n 노드 구성도, Webhook 테스트 결과 |
| Dify | AI 답변 앱, Knowledge/RAG, Chatflow가 중심 | Dify 앱 설계, Knowledge 문서, 테스트 답변 |

도구를 여러 개 연결하는 것도 가능합니다.

```text
n8n Webhook
-> Dify API 호출
-> 결과 정리
-> Slack/Email/DB로 전달
```

또는:

```text
AIPP에서 전체 AI 흐름 설계
-> n8n으로 외부 시스템 연결
-> Dify로 Knowledge/RAG 답변 생성
```

## 팀 프로젝트 방향

팀별로 아래 중 하나를 확장합니다.

- 기술 지원 문의 자동 분류
- 장애 리포트 자동 요약
- 사내 문서 기반 RAG 응답
- n8n Webhook 기반 문의 접수 자동화
- Dify Knowledge 기반 답변 생성
- AIPP 기반 AI 업무 흐름 설계
- 운영 로그 기반 품질 개선 Assistant

## 필수 산출물

최종 제출물에는 다음이 포함되어야 합니다.

```text
[ ] 프로젝트 주제와 사용자 시나리오
[ ] Trigger, Condition, Action 구조
[ ] 입력 데이터와 출력 결과 예시
[ ] AIPP, n8n, Dify 중 최소 1개 이상의 활용 설계
[ ] AI 또는 LLM이 담당하는 역할
[ ] Tool, API, Knowledge 중 하나 이상의 활용 계획
[ ] 오류 처리와 fallback 흐름
[ ] 실행 로그 또는 운영 지표
[ ] 테스트 체크리스트
[ ] 최종 발표 자료
```

## 평가 기준

- 업무 시나리오가 명확한가?
- Trigger, Condition, Action 흐름이 자연스러운가?
- AIPP, n8n, Dify 중 선택한 도구의 역할이 명확한가?
- AI 응답 검증과 fallback 흐름이 있는가?
- 실행 로그, 비용, 품질 지표를 고려했는가?
- 최종 시연에서 사용자 입력부터 결과 확인까지 자연스럽게 이어지는가?

## 발표 질문

발표에서는 아래 질문에 답할 수 있어야 합니다.

```text
우리 팀은 어떤 업무를 자동화했는가?
왜 이 도구를 선택했는가?
AI가 꼭 필요한 단계는 어디인가?
단순 자동화로 충분한 단계는 어디인가?
오류가 발생하면 어떻게 처리하는가?
실제 회사에 적용하려면 어떤 보안과 운영 기준이 필요한가?
```
