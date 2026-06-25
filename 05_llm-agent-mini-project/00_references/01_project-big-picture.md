# Project Big Picture

LLM Agent 미니 프로젝트는 단순 챗봇보다 한 단계 더 나아간 구조입니다.

```text
사용자 요청
-> 요청 분석
-> 필요한 도구 선택
-> 도구 실행
-> 필요한 기억 또는 문서 검색
-> 최종 응답 생성
-> 실행 결과와 상태 표시
```

이 과정에서 중요한 것은 모델이 모든 일을 직접 하는 것이 아니라, Python 코드와 Tool, Graph가 역할을 나누어 처리한다는 점입니다.

## 최소 구현 범위

- 사용자 요청 입력
- Agent State 정의
- LangGraph Node 4개 이상
- Tool 함수 2개 이상
- Decision 또는 Reflection 흐름 1개 이상
- 오류 발생 시 fallback 흐름 1개 이상
- 최종 응답 생성
- Streamlit 화면 출력
- 테스트 체크리스트 작성

## 권장 구현 순서

처음부터 실제 API, RAG, Memory를 모두 붙이면 디버깅이 어려워집니다. 아래 순서로 작게 완성한 뒤 확장합니다.

```text
1. Mock data로 Tool 함수 작성
2. CLI에서 Tool 함수만 실행
3. Agent State 정의
4. LangGraph Node/Edge 연결
5. 최종 응답 생성
6. Streamlit 화면 연결
7. 테스트 체크리스트 작성
8. 필요할 때 LLM, RAG, Memory, 외부 API 추가
```

## 선택 확장

- RAG 문서 검색
- 사용자별 Session Memory
- 장기 기억 Vector Search
- 로컬 파일 저장 또는 pgvector docker run 기반 Vector DB 저장
- LangSmith Tracing

선택 확장은 필수 기능이 아닙니다. 프로젝트 시간이 부족하면 Mock data, Tool, LangGraph, Streamlit UI, 테스트 보고서까지만 완성해도 좋습니다.
