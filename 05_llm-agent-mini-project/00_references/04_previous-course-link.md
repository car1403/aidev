# Previous Course Link

이 문서는 `05_llm-agent-mini-project`가 바로 앞 과정인 `04_llm-agent-orchestration`과 어떻게 연결되는지 정리합니다.

05는 새로운 이론을 처음부터 다시 배우는 과정이 아니라, 04에서 배운 Agent 구성 요소를 하나의 미니 프로젝트로 묶어 보는 단계입니다.

## 04에서 배운 것

- 역할(Role), 지시문(Instruction), 맥락(Context) 기반 프롬프트 설계
- Structured Output과 응답 검증
- Function Calling과 Python Tool 연결
- RAG, Embedding, Memory 개념
- LangGraph State, Node, Edge 기반 흐름 제어
- Tracing, Debugging, Self-Reflection 개념
- Docker Desktop에서 `docker run`으로 Ollama 또는 pgvector를 실행하는 방식

## 05에서 하는 것

위 개념을 따로따로 연습하지 않고 하나의 프로젝트 안에서 조합합니다.

```text
사용자 요청 입력
-> Agent State 생성
-> 요청 분석
-> 필요한 Tool 선택
-> Tool 실행
-> RAG 또는 Memory 선택 적용
-> 결과 검증
-> 재시도 또는 fallback
-> 최종 응답 생성
-> Streamlit 화면 표시
```

## 04와 05의 차이

| 구분 | 04_llm-agent-orchestration | 05_llm-agent-mini-project |
| --- | --- | --- |
| 목적 | Agent 핵심 기술을 단원별로 학습 | 배운 기술을 팀 프로젝트로 통합 |
| 중심 활동 | Prompt, Tool, RAG, Memory, LangGraph 실습 | 일정 조정 Agent 설계와 구현 |
| 데이터 | 작은 예제와 단위 실습 | Mock 일정 데이터와 선택 확장 데이터 |
| 결과물 | 단원별 실습 코드와 문서 | 아키텍처 설계서, 시험 결과 보고서, 발표 자료 |
| Docker | 필요한 컨테이너를 `docker run`으로 실행 | 선택 확장으로 같은 방식 사용 |

## 프로젝트에서 확인할 것

- Tool이 실제 문제 해결에 필요한가?
- State에 너무 많은 값을 넣고 있지는 않은가?
- Graph 흐름이 README만 보고 이해되는가?
- API Key 없이도 최소 Mock 흐름을 확인할 수 있는가?
- 오류가 발생했을 때 재시도 또는 fallback 흐름이 있는가?
- 최종 발표에서 Agent 구조를 설명할 수 있는가?
