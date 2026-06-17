# 05 Final Presentation

최종 발표에서는 에이전트가 어떤 판단 흐름으로 일정 조정 문제를 해결하는지 설명합니다.

## 발표 구성

1. 프로젝트 주제와 대상 사용자
2. 사용자 일정 요청 예시
3. 전체 Agent 아키텍처
4. Agent State 구조
5. StateGraph Node와 Edge 흐름
6. `인지 -> 판단 -> 행동 -> 검증` 사고 흐름 매핑
7. Decision Node의 분기 조건
8. Fallback edge 또는 fallback node 설명
9. Tool 목록과 역할
10. Function Calling 또는 Tool Use 호출 흐름
11. Session Memory, Long-term Memory, 컨텍스트 요약 전략
12. 오류 감지 기준
13. 재시도와 fallback 전략
14. 자기 성찰 적용 전후 비교
15. Streamlit 화면 시연
16. 어려웠던 점과 개선 방향
17. 06 과정 이후 운영/배포 확장 계획

## 시연 체크

- 사용자 요청 입력이 State에 저장되는가?
- Decision Node가 올바른 Tool을 선택하는가?
- Tool 결과가 State에 저장되는가?
- 오류 또는 애매한 요청에서 fallback이 동작하는가?
- 자기 성찰 또는 재시도 흐름을 설명할 수 있는가?
- 최종 일정 제안이 사용자에게 이해 가능하게 표시되는가?
- 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수 중 핵심 지표를 제시하는가?

## 발표에서 강조할 것

- 왜 이 문제에 Agent 구조가 필요한가?
- 단순 함수 호출과 LangGraph 기반 흐름의 차이는 무엇인가?
- 분기 조건을 어떤 기준으로 설계했는가?
- Tool 선택 오류를 어떻게 감지하고 수정했는가?
- 자기 성찰 적용 전후 결과가 수치로 어떻게 달라졌는가?
