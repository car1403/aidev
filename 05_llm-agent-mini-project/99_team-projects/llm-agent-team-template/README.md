# LLM Agent Team Template

이 폴더는 팀별 LLM Agent 미니 프로젝트를 시작하기 위한 템플릿입니다.

이번 팀 프로젝트의 기준 주제는 **복합 API 연계 일정 조정 에이전트**입니다. 이 템플릿은 `04_llm-agent-orchestration`에서 배운 Prompt, Tool, State, Memory, LangGraph 흐름을 기반으로 합니다.

기본 구현은 Mock data로 시작하고, 필요한 경우에만 04 방식의 `docker run`으로 Ollama 또는 pgvector를 붙입니다. Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 06 과정에서 다룹니다.

## 팀 프로젝트 목표

- 일정 조정 에이전트의 사용자 요청 시나리오를 정의한다.
- Agent State와 공유 상태 필드를 타입 힌트와 함께 설계한다.
- Start, Decision, Tools, Review 또는 Reflection, End 노드를 가진 StateGraph를 구현한다.
- Tool 함수 2개 이상을 구현한다.
- 도구 선택 오류, 파라미터 누락, 응답 불일치 같은 판단 오류를 시험한다.
- 자기 성찰 또는 피드백 루프 적용 전후 결과를 비교한다.
- Streamlit UI에서 에이전트를 실행한다.

## 권장 구조

```text
llm-agent-team-template
|-- README.md
|-- backend
| |-- agent_state.py
| |-- graph.py
| |-- tools.py
| `-- requirements.txt
|-- frontend
| `-- app.py
|-- docs
| |-- project-plan.md
| |-- agent-architecture.md
| |-- agent-design.md
| |-- agent-test-report.md
| `-- test-checklist.md
`-- presentation
 `-- final-presentation.md
```

## 필수 산출물

| 산출물 | 파일 | 반드시 포함할 내용 |
| --- | --- | --- |
| 에이전트 아키텍처 설계서 | `docs/agent-architecture.md` | StateGraph 노드, `인지 -> 판단 -> 행동 -> 검증` 흐름, 분기 조건, fallback edge, Memory 전략, Tool Use 흐름, State 필드 타입 |
| 에이전트 시험 결과 보고서 | `docs/agent-test-report.md` | 판단 오류 감지 기준, 오류 유형별 재시도와 fallback, 프롬프트/파라미터 수정 이력, 피드백 루프, 개선 전후 수치 비교 |

## 기본 흐름

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

## 필수 구현 기준

- Agent State 정의
- LangGraph StateGraph 사용
- LangGraph 노드 4개 이상
- 조건 분기 1개 이상
- Tool 함수 2개 이상
- fallback 흐름 1개 이상
- 자기 성찰 또는 피드백 루프 1개 이상
- 오류 유형별 테스트 케이스 3개 이상
- 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수 중 4개 지표 기록
- Streamlit 실행 화면
- 에이전트 아키텍처 설계서
- 에이전트 시험 결과 보고서

## 실행 안내 예시

```powershell
cd C:\aidev\05_llm-agent-mini-project\99_team-projects\llm-agent-team-template
..\..\.venv\Scripts\Activate.ps1
pip install -r..\..\requirements.txt
python backend\graph.py
streamlit run frontend\app.py --server.port 8702
```

## 확장 기준

- OpenAI API Key가 없으면 Mock 응답과 Tool 실행 흐름부터 완성합니다.
- 로컬 Llama 모델을 실험할 때는 04에서 배운 Ollama `docker run` 방식을 사용합니다.
- RAG 또는 장기 기억이 필요하면 먼저 로컬 파일 또는 Mock 문서로 구현하고, 이후 pgvector 컨테이너로 확장합니다.
- Docker를 처음 설치하는 팀은 `00_references/05_docker-local-extension-guide.md`를 먼저 확인합니다.
