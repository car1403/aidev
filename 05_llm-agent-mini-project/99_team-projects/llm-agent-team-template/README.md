# LLM Agent Team Template

이 폴더는 05 미니 프로젝트를 시작하기 위한 기본 템플릿입니다.

기본 주제는 **복합 API 연계 일정 조정 에이전트**입니다. 04 과정에서 배운 Prompt, Tool, State, Memory, LangGraph, Self-Reflection 흐름을 실제 작은 프로젝트로 연결하는 데 목적이 있습니다.

처음에는 Mock data로 동작하게 만들고, 필요할 때만 OpenAI API, Ollama 기반 Llama, pgvector 기반 장기 기억을 선택적으로 확장합니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 06 과정에서 다룹니다.

## 프로젝트 목표

- 사용자 일정 조정 요청 시나리오를 정의합니다.
- Agent State와 공유 상태 필드를 명확하게 설계합니다.
- Start, Decision, Tools, Review 또는 Reflection, End 노드를 가진 StateGraph를 구현합니다.
- Tool 함수를 2개 이상 구현합니다.
- Tool 선택 오류, 파라미터 누락, 응답 불일치 같은 판단 오류를 테스트합니다.
- 자기 성찰 또는 피드백 루프 적용 전후 결과를 비교합니다.
- Streamlit UI에서 에이전트를 실행하고 결과를 확인합니다.

## 폴더 구조

```text
llm-agent-team-template
├─ README.md
├─ backend
│  ├─ agent_state.py
│  ├─ graph.py
│  ├─ tools.py
│  └─ requirements.txt
├─ frontend
│  └─ app.py
├─ docs
│  ├─ project-plan.md
│  ├─ agent-architecture.md
│  ├─ agent-design.md
│  ├─ agent-test-report.md
│  └─ test-checklist.md
└─ presentation
   └─ final-presentation.md
```

## 필수 산출물

| 산출물 | 파일 | 포함할 내용 |
| --- | --- | --- |
| 프로젝트 계획서 | `docs/project-plan.md` | 주제, 사용자 요청, 주요 기능, Tool 목록, 일정 |
| 에이전트 아키텍처 설계서 | `docs/agent-architecture.md` | StateGraph 노드, 판단 기준, fallback 흐름, Memory 전략, Tool Use 흐름 |
| 에이전트 설계 요약 | `docs/agent-design.md` | State, Node, Tool을 한눈에 볼 수 있는 요약 |
| 에이전트 시험 결과 보고서 | `docs/agent-test-report.md` | 오류 감지 기준, retry/fallback, 개선 전후 비교 |
| 테스트 체크리스트 | `docs/test-checklist.md` | 실행, 구조, 오류 상황, 문서 제출 확인 |
| 최종 발표 자료 | `presentation/final-presentation.md` | 문제 정의, 구조, 실행 결과, 개선 방향 |

## 기본 실행 흐름

```text
사용자 일정 요청 입력
-> Agent State에 요청 저장
-> 요청 의도 분석
-> Decision Node에서 필요한 Tool 선택
-> Tool 실행
-> 결과 검증
-> 오류가 있으면 reflection 또는 fallback
-> 최종 일정 제안 생성
-> Streamlit 화면에 표시
```

## 실행 예시

루트 과정의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
cd .\99_team-projects\llm-agent-team-template
python .\backend\graph.py
streamlit run .\frontend\app.py --server.port 8702
```

## 구현 기준

- Agent State 정의
- LangGraph StateGraph 사용
- LangGraph 노드 4개 이상
- 조건 분기 1개 이상
- Tool 함수 2개 이상
- fallback 흐름 1개 이상
- 자기 성찰 또는 피드백 루프 1개 이상
- 오류 유형별 테스트 케이스 3개 이상
- 완료율, Tool 선택 정확도, 응답 일관성, 평균 재시도 횟수 중 2개 이상 기록
- Streamlit 실행 화면
- 에이전트 아키텍처 설계서
- 에이전트 시험 결과 보고서

## 확장 기준

- OpenAI API Key가 없으면 Mock 응답과 Tool 실행 흐름부터 완성합니다.
- OpenAI 모델을 사용할 때는 `gpt-4.1-mini`를 기본 예시로 사용합니다.
- 로컬 Llama 모델은 04 과정에서 배운 Ollama `docker run` 방식으로 선택 적용합니다.
- RAG 또는 장기 기억이 필요하면 먼저 로컬 파일이나 Mock 문서로 구현하고, 이후 pgvector 컨테이너로 확장합니다.
- 서비스 운영, 배포 자동화, 관측성, 장애 복구는 06 과정에서 다룹니다.
