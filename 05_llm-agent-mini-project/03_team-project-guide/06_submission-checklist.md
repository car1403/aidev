# 06 Submission Checklist

제출 전 확인합니다.

## 필수 파일

```text
README.md
.env.example
backend/agent_state.py
backend/tools.py
backend/graph.py
frontend/app.py
docs/project-plan.md
docs/agent-architecture.md
docs/agent-test-report.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 에이전트 아키텍처 설계서 확인

- [ ] StateGraph의 각 Node가 `인지 -> 판단 -> 행동 -> 검증` 사고 흐름에 맞게 배치되어 있습니다.
- [ ] Start, Tools, Decision, Review 또는 Reflection, End 흐름이 설명되어 있습니다.
- [ ] 분기 조건이 도구 필요 여부, 사용자 의도, 데이터 충분성, 오류 여부 같은 기준값 또는 정책으로 정의되어 있습니다.
- [ ] 예외 흐름과 fallback이 edge 또는 node로 문서화되어 있습니다.
- [ ] Session Memory와 Long-term Memory 적용 여부가 설명되어 있습니다.
- [ ] 컨텍스트 윈도우 관리와 요약(Summarization) 전략이 설명되어 있습니다.
- [ ] Function Calling 또는 Tool Use 호출 흐름이 `선택 -> 호출 -> 결과 처리 -> 다음 노드 결정` 순서로 표현되어 있습니다.
- [ ] 공유 State 필드가 타입 힌트와 함께 정의되어 있습니다.
- [ ] `messages`, `tools_called`, `error_count`, `iteration` 같은 필드가 중복 없이 설계되어 있습니다.

## 에이전트 시험 결과 보고서 확인

- [ ] 할루시네이션, 도구 선택 오류, 파라미터 누락, 응답 불일치 판단 오류 감지 기준이 정의되어 있습니다.
- [ ] 오류 유형별 재시도 횟수와 대체 전략이 정리되어 있습니다.
- [ ] 프롬프트, 파라미터, 휴리스틱 수정 이력이 버전별로 정리되어 있습니다.
- [ ] 오류 감지 -> 원인 분석 -> 수정 전략 선택 -> 재실행 -> 검증 흐름이 순서도 또는 활동 다이어그램으로 표현되어 있습니다.
- [ ] 피드백 루프 각 단계의 입력과 출력이 정의되어 있습니다.
- [ ] 자기 성찰 적용 전후 성능 비교가 있습니다.
- [ ] 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수를 수치로 제시했습니다.

## 실행 검증

- [ ] `.venv` 활성화 후 실행됩니다.
- [ ] CLI 실행이 됩니다.
- [ ] Streamlit 실행이 됩니다.
- [ ] 기본 요청 처리가 됩니다.
- [ ] 잘못된 요청 처리 또는 fallback이 됩니다.
- [ ] `.env` 파일은 제출물에 포함되지 않았습니다.
- [ ] 불필요한 `__pycache__`가 없습니다.
