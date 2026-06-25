# 04 Test Checklist

팀 프로젝트 테스트 체크리스트 예시입니다.

## 실행 환경

- [ ] `.venv` 생성 및 활성화
- [ ] `python -m pip install --upgrade pip` 실행
- [ ] `pip install -r requirements.txt` 또는 팀 프로젝트 requirements 설치
- [ ] Docker 확장을 사용한다면 Docker Desktop 실행 확인
- [ ] Docker 확장을 사용한다면 `docker ps` 확인
- [ ] 로컬 Llama를 사용한다면 `ollama-llm` 컨테이너 실행 확인
- [ ] pgvector를 사용한다면 `rag-pgvector` 컨테이너 실행 확인
- [ ] CLI 실행 성공
- [ ] Streamlit 실행 성공

## 아키텍처 검증

- [ ] Agent State 필드와 타입이 정의되어 있습니다.
- [ ] State 필드에 불필요한 중복이 없습니다.
- [ ] StateGraph Node가 4개 이상 있습니다.
- [ ] Node 흐름이 `인지 -> 판단 -> 행동 -> 검증` 순서로 설명됩니다.
- [ ] Decision Node 또는 조건 분기가 있습니다.
- [ ] 분기 조건이 도구 필요 여부, 사용자 의도, 데이터 충분성, 오류 여부로 정의되어 있습니다.
- [ ] Tool 함수 2개 이상이 동작합니다.
- [ ] Tool 호출 결과가 State에 저장됩니다.
- [ ] End Node에서 최종 응답이 생성됩니다.
- [ ] fallback 흐름이 edge 또는 node로 구현되어 있습니다.
- [ ] Session Memory, Long-term Memory, Context 요약 전략 적용 여부가 설명되어 있습니다.

## 시험 결과 검증

- [ ] 정상 요청 처리 성공
- [ ] 도구가 필요 없는 요청 처리 확인
- [ ] 잘못된 요청 처리 확인
- [ ] Tool 선택 오류 상황 테스트
- [ ] 파라미터 누락 상황 테스트
- [ ] 응답 불일치 상황 테스트
- [ ] 재시도 횟수 기록
- [ ] fallback 응답 기록
- [ ] Self-Reflection 적용 전후 결과 비교
- [ ] `오류 감지 -> 원인 분석 -> 수정 전략 선택 -> 재실행 -> 검증` 흐름 기록
- [ ] 완료율, Tool 선택 정확도, 응답 일관성, 평균 재시도 횟수 기록

## 문서 검증

- [ ] Agent Architecture 설계서 작성 완료
- [ ] Agent Test Report 작성 완료
- [ ] README 실행 방법 확인
- [ ] 발표 자료 작성 완료
