# 10 Curriculum and Lab Review

이 문서는 `04_llm-agent-orchestration` 과정의 커리큘럼 반영 상태와 실습 운영 기준을 한곳에 정리한 참고 자료입니다.

기존에는 최상위에 `CURRICULUM_REVIEW.md`, `LAB_ASSIGNMENT_REVIEW.md`를 따로 두었지만, 직접 수업 중 여러 문서를 오가며 확인하지 않도록 `00_references` 안의 참고 자료로 통합합니다.

## 전체 판단

현재 과정은 다음 흐름을 기준으로 구성되어 있습니다.

```text
고급 프롬프트 및 추론 전략
-> Function Calling 및 오케스트레이션
-> 지식 저장소 및 장기 기억
-> 상태 기계 기반 흐름 제어
-> Agent 미니 프로젝트
```

04 과정은 Supabase 중심 과정이 아닙니다. 01, 02, 03에서 Supabase 기반 백엔드, 프론트엔드, 미니 프로젝트를 학습했다면, 04에서는 Docker Desktop의 `docker run`을 사용해 로컬 Llama와 pgvector PostgreSQL을 실행하고 Agent 구조를 이해합니다.

Docker Compose, AWS 배포, GitHub Actions, 운영 자동화는 06 과정에서 본격적으로 다룹니다.

## 커리큘럼 대응표

| 구분 | 요구 내용 | 현재 반영 위치 |
| --- | --- | --- |
| 고급 프롬프트 및 추론 전략 | Role, Instruction, Context 기반 프롬프트 설계 | `02_advanced-prompting-and-reasoning` |
| 고급 프롬프트 및 추론 전략 | CoT, ReAct 기반 단계적 문제 해결 | `02_advanced-prompting-and-reasoning` |
| 고급 프롬프트 및 추론 전략 | JSON Schema, Pydantic 기반 Structured Output | `02_advanced-prompting-and-reasoning`, `03_langchain-basics` |
| 고급 프롬프트 및 추론 전략 | Prompt Injection 이해와 입력 검증 | `02_advanced-prompting-and-reasoning` |
| Function Calling 및 오케스트레이션 | LLM 외부 기능 호출 구조 이해 | `04_function-calling-and-tool-use` |
| Function Calling 및 오케스트레이션 | Python 함수 Tool, 외부 API Tool 등록 | `04_function-calling-and-tool-use` |
| Function Calling 및 오케스트레이션 | MCP 개념과 Function Calling 비교 | `04_function-calling-and-tool-use` |
| Function Calling 및 오케스트레이션 | Multi-Tool Agent 흐름 설계 | `04_function-calling-and-tool-use`, `06_langgraph-state-flow` |
| 지식 저장소 및 장기 기억 | Embedding, Vector DB, pgvector 검색 | `05_rag-memory-and-vector-search` |
| 지식 저장소 및 장기 기억 | Session Memory와 Long-term Memory | `05_rag-memory-and-vector-search`, `06_langgraph-state-flow` |
| 지식 저장소 및 장기 기억 | Hybrid Search, RRF, RAG 품질 평가 | `05_rag-memory-and-vector-search` |
| 상태 기계 기반 흐름 제어 | LangGraph Node, Edge, State | `06_langgraph-state-flow` |
| 상태 기계 기반 흐름 제어 | 조건 분기, Retry, Fallback, Self-Reflection | `06_langgraph-state-flow` |
| 상태 기계 기반 흐름 제어 | Planning, Tracing, Evaluation | `06_langgraph-state-flow` |
| 미니 프로젝트 | 일정 조정 Agent 통합 구현 | `99_agent-mini-project` |

## Lab 운영 기준

각 단원의 실습은 별도 Markdown lab 문서보다 코드 실행과 수업 설명 중심으로 진행합니다.

수업 중에는 다음 순서로 진행합니다.

```text
1. README에서 오늘 배울 단원의 위치를 확인한다.
2. SETUP에서 가상환경과 필요한 패키지를 확인한다.
3. 단원 폴더의 Python 예제를 실행한다.
4. 출력 결과를 함께 읽는다.
5. 코드의 주석과 실행 흐름을 설명한다.
6. 직접 파라미터, 프롬프트, Tool 입력값을 바꿔본다.
7. 최종적으로 미니 프로젝트에 해당 개념을 연결한다.
```

## 단원별 실습 요약

| 단원 | 실습 초점 |
| --- | --- |
| `01_llm-api-and-prompt-basics` | OpenAI API 호출, Ollama/Llama 호출, 클라우드 LLM과 로컬 LLM 비교 |
| `02_advanced-prompting-and-reasoning` | 프롬프트 개선, JSON 출력, ReAct 흐름, Prompt Injection 방어 |
| `03_langchain-basics` | PromptTemplate, ChatPromptTemplate, Runnable Chain, Structured Output, 문서 분할 |
| `04_function-calling-and-tool-use` | 계산 Tool, 학습 로그 Tool, 외부 API Tool, Multi-Tool Router |
| `05_rag-memory-and-vector-search` | Embedding, pgvector, Chunking, RAG 응답, Memory, Hybrid Search, RAG 품질 평가 |
| `06_langgraph-state-flow` | StateGraph, 조건 라우팅, Tool/RAG Node, Hybrid Memory, Planning/Tracing/Evaluation |
| `99_agent-mini-project` | 일정 조정 Agent 샘플과 팀 템플릿 구현 |

## 산출물 기준

04 과정이 끝날 때 다음을 제출하거나 설명할 수 있어야 합니다.

- Agent가 해결할 문제 정의
- Agent State 필드 설계
- Node, Edge, 조건 분기 구조
- Tool 목록과 입력/출력 스키마
- Memory 또는 RAG 적용 여부와 이유
- Retry, Fallback, Self-Reflection 전략
- Streamlit 또는 CLI 기반 실행 결과
- 테스트 시나리오와 개선 전후 비교

## 점검 체크리스트

- [ ] OpenAI API와 로컬 Llama의 차이를 설명할 수 있는가?
- [ ] Docker Desktop에서 Ollama 컨테이너를 실행할 수 있는가?
- [ ] Docker Desktop에서 pgvector PostgreSQL 컨테이너를 실행할 수 있는가?
- [ ] Prompt를 Role, Instruction, Context로 나누어 설계할 수 있는가?
- [ ] Structured Output이 필요한 이유를 설명할 수 있는가?
- [ ] Tool 호출 흐름을 선택, 호출, 결과 처리, 다음 판단 순서로 설명할 수 있는가?
- [ ] RAG에서 chunk, embedding, vector search, context 전달의 역할을 설명할 수 있는가?
- [ ] LangGraph의 State, Node, Edge 개념을 설명할 수 있는가?
- [ ] Retry, Fallback, Reflection이 필요한 상황을 구분할 수 있는가?
- [ ] 최종 미니 프로젝트에서 Agent 실행 흐름을 문서와 코드로 보여줄 수 있는가?

## 운영 메모

처음부터 모든 기술을 완성형으로 붙이기보다, 작은 흐름을 먼저 이해하고 단계적으로 연결하는 것이 좋습니다.

권장 흐름은 다음과 같습니다.

```text
Mock data로 Agent 흐름 이해
-> Tool 함수를 Python으로 직접 작성
-> LLM 호출 연결
-> 필요할 때 RAG 또는 Memory 추가
-> LangGraph로 상태 흐름 정리
-> 마지막에 Streamlit 화면 또는 CLI로 결과 확인
```

LangChain은 필수 프레임워크라기보다 Prompt, Model, Parser, Tool을 연결하는 구조를 이해하기 위한 최소 학습 도구로 사용합니다.

LangGraph는 Agent 상태 흐름을 명시적으로 보여주기 때문에 04 과정의 핵심 도구로 다룹니다.
