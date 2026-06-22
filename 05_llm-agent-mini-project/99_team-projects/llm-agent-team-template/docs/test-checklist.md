# Test Checklist

이 체크리스트의 명령은 아래 폴더에서 실행합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\99_team-projects\llm-agent-team-template
```

## 실행 확인

- [ ] 상위 폴더 `.venv` 활성화 완료
- [ ] `pip install -r..\..\requirements.txt` 실행 완료
- [ ] `python backend\graph.py` 실행 성공
- [ ] `streamlit run frontend\app.py --server.port 8702` 실행 성공

## Agent 구조 확인

- [ ] Agent State 필드와 타입 힌트 작성
- [ ] State 필드 중복 없음
- [ ] LangGraph StateGraph 사용
- [ ] Node 4개 이상 구현
- [ ] Node 흐름이 `인지 -> 판단 -> 행동 -> 검증`으로 설명됨
- [ ] Decision Node 구현
- [ ] 도구 필요 여부, 사용자 의도, 데이터 충분성, 오류 여부 기준 분기 구현
- [ ] Tool 함수 2개 이상 구현
- [ ] fallback 흐름 구현
- [ ] Session Memory, Long-term Memory, 요약 전략 적용 여부 정리
- [ ] 최종 답변 생성 구현

## 시험 확인

- [ ] 정상 일정 요청 처리 성공
- [ ] 정보 부족 요청 처리 성공
- [ ] 일정 충돌 요청 처리 성공
- [ ] 도구 선택 오류 상황 처리
- [ ] 파라미터 누락 상황 처리
- [ ] 응답 불일치 상황 처리
- [ ] 재시도 횟수 기록
- [ ] 자기 성찰 적용 전후 비교
- [ ] 오류 감지 -> 원인 분석 -> 수정 전략 선택 -> 재실행 -> 검증 흐름 기록
- [ ] 완료율, 도구 선택 정확도, 응답 일관성, 평균 재시도 횟수 기록

## 산출물 확인

- [ ] `docs/agent-architecture.md` 작성 완료
- [ ] `docs/agent-test-report.md` 작성 완료
- [ ] 최종 발표 시연 가능
