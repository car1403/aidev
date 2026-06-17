# Practice Material Checklist

이 문서는 `05_llm-agent-mini-project`의 실습 자료와 과제 자료가 어떤 역할을 하는지 정리합니다.

## 현재 구성

| 위치 | 역할 | 학생이 해야 할 일 |
| --- | --- | --- |
| `01_local-dev-basic` | Python, LangGraph, Streamlit 실행 확인 | 개발 환경과 기본 실행 흐름 확인 |
| `02_instructor-sample-project` | 강사와 함께 실행하는 일정 조정 에이전트 | 샘플 Agent 흐름 실행 및 코드 읽기 |
| `03_team-project-guide` | 팀 주제, 역할, 요구사항, 발표/제출 안내 | 팀 프로젝트 기준 문서 작성 |
| `04_agent-project-practice` | State, Tool, Graph, UI 설계 연습 | 최종 구현 전 설계 연습 |
| `05_llm-agent-sample-assets` | 추가 샘플 자산 보관 위치 | 필요한 샘플 데이터와 흐름도 참고 |
| `99_team-projects/llm-agent-team-template` | 팀별 프로젝트 시작 템플릿 | 팀 프로젝트 복사 후 구현 시작 |

## 수업 중 확인할 실습 흐름

```text
1. .venv 활성화
2. requirements.txt 설치
3. 강사 샘플 CLI 실행
4. Streamlit 화면 실행
5. Agent State 구조 확인
6. Tool 함수 입력과 출력 확인
7. LangGraph Node와 Edge 흐름 확인
8. 팀 템플릿 복사
9. 팀별 State, Tool, Graph 수정
10. 테스트 체크리스트와 발표 자료 작성
```

## 추가하면 좋은 확장 실습

- Session Memory 저장 실습
- Long-term Memory 설계 실습
- Hybrid Search 또는 RAG 검색 실습
- LangGraph 조건 분기 실습
- LangSmith Tracing 점검 실습
- 오류 유형별 재시도와 fallback 비교 실습

## 제출 전 확인

- [ ] 강사 샘플이 실행됩니다.
- [ ] 팀 템플릿이 실행됩니다.
- [ ] `docs/agent-architecture.md`가 작성되었습니다.
- [ ] `docs/agent-test-report.md`가 작성되었습니다.
- [ ] 정상 요청, 정보 부족 요청, 도구 오류, 응답 불일치 테스트가 포함되었습니다.
- [ ] 개선 전후 지표가 수치로 정리되었습니다.
