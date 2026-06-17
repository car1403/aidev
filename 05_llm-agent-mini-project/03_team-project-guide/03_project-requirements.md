# 03 Project Requirements

이번 프로젝트의 기준 주제는 **복합 API 연계 일정 조정 에이전트**입니다.

단순히 질문에 답하는 챗봇이 아니라, 사용자의 일정 요청을 분석하고, 필요한 도구를 선택하고, 도구 결과를 검증하고, 오류가 있으면 재시도하거나 fallback을 적용하는 LangGraph 기반 단일 에이전트를 구현합니다.

## 1. 필수 구현

- Agent State 정의
- LangGraph StateGraph 사용
- Start, Decision, Tools, Reflection 또는 Review, End를 포함한 Node 구성
- 조건 분기 1개 이상
- Tool 함수 2개 이상
- Function Calling 또는 Tool Use 호출 흐름 문서화
- Streamlit UI
- 실행 방법이 포함된 README
- 에이전트 아키텍처 설계서
- 에이전트 시험 결과 보고서

## 2. 에이전트 아키텍처 설계서 필수 항목

```text
docs/agent-architecture.md
```

아래 항목을 반드시 작성합니다.

- StateGraph의 각 Node(Start, Tools, Decision, Reflection/Review, End 등)가 에이전트의 사고 흐름인 `인지 -> 판단 -> 행동 -> 검증`에 맞게 배치되었는가?
- 분기 조건이 도구 필요 여부, 사용자 의도, 데이터 충분성, 오류 여부 같은 명확한 기준값 또는 정책으로 정의되었는가?
- 예외 흐름과 fallback이 설명뿐 아니라 edge 또는 node로 표현되었는가?
- 단기 기억(Session)과 장기 기억(Long-term Memory)의 연동 방식이 정리되었는가?
- 컨텍스트 윈도우 관리와 요약(Summarization) 전략이 설계에 반영되었는가?
- Function Calling 또는 Tool Use 흐름이 `선택 -> 호출 -> 결과 처리 -> 다음 노드 결정` 순서도로 표현되었는가?
- 공유 State 객체의 필드가 타입 힌트와 함께 명확히 정의되었는가?
- `messages`, `tools_called`, `error_count`, `iteration`, `memory_summary` 같은 필드가 중복 없이 설계되었는가?

## 3. 에이전트 시험 결과 보고서 필수 항목

```text
docs/agent-test-report.md
```

아래 항목을 반드시 작성합니다.

- 할루시네이션, 도구 선택 오류, 파라미터 누락, 응답 불일치 같은 에이전트 판단 오류 감지 기준이 정의되었는가?
- 오류 유형별 재시도 횟수와 fallback 전략이 정리되었는가?
- 프롬프트, 파라미터, 휴리스틱 수정 이력이 버전별로 문서화되었는가?
- `오류 감지 -> 원인 분석 -> 수정 전략 선택 -> 재실행 -> 검증` 흐름이 활동 다이어그램 또는 순서도로 표현되었는가?
- 각 단계의 입력과 출력이 정의되었는가?
- 자기 성찰 적용 전후의 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수가 비교되었는가?

## 4. 권장 Agent State 필드

```python
class AgentState(TypedDict):
    user_request: str
    intent: str
    required_tools: list[str]
    tools_called: list[str]
    tool_results: dict
    error_count: int
    iteration: int
    memory_summary: str
    decision_reason: str
    reflection_notes: list[str]
    final_answer: str
```

팀 프로젝트에 맞게 필드를 줄이거나 늘릴 수 있지만, 왜 필요한지 설명해야 합니다.

## 5. 권장 Node 구조

```text
START
-> collect_request
-> analyze_intent
-> decide_tool
-> call_tool
-> validate_result
-> reflect_or_retry
-> generate_final_answer
-> END
```

## 6. 선택 구현

- RAG 검색
- Session Memory
- Long-term Memory
- 로컬 파일 저장
- pgvector 기반 장기 기억
- LangSmith Tracing
- 로컬 Llama 기반 응답 생성

## 7. 05 과정의 기술 범위

05는 04에서 배운 LLM Agent 구현 내용을 팀 프로젝트로 연결하는 과정입니다.

- Docker를 사용한다면 단일 컨테이너를 `docker run`으로 실행합니다.
- Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 06 과정에서 다룹니다.

## 8. 보안 기준

- API Key를 코드에 직접 작성하지 않습니다.
- `.env` 파일은 제출하지 않습니다.
- `.env.example`에는 예시 값만 작성합니다.
