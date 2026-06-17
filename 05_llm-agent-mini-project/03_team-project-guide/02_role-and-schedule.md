# 02 Role and Schedule

## 팀 역할 예시

- Agent 아키텍처 설계
- StateGraph Node/Edge 설계
- Tool 함수 구현
- Memory 또는 Mock data 설계
- Streamlit UI 구현
- 시험 시나리오 작성
- 에이전트 시험 결과 보고서 작성
- 발표 자료 정리

## 권장 일정

### Day 1: 설계와 첫 실행

- 주제 선정
- 사용자 요청 예시 작성
- Agent State 필드 정의
- Node와 Edge 초안 작성
- Tool 목록 정의
- 분기 조건과 fallback 조건 정의
- 에이전트 아키텍처 설계서 초안 작성

체크포인트:

```text
Agent State 초안 작성
StateGraph 흐름 초안 작성
Tool 2개 이상 정의
분기 조건 1개 이상 정의
```

### Day 2: 구현과 기본 시험

- Tool 함수 구현
- StateGraph 연결
- Decision Node 구현
- validate_result 또는 reflection Node 구현
- Streamlit UI 연결
- 정상 요청과 오류 요청 테스트

체크포인트:

```text
CLI 실행 성공
Streamlit 실행 성공
정상 요청 처리 성공
오류 요청 fallback 확인
```

### Day 3: 시험 보고서와 발표

- 판단 오류 유형 정리
- 재시도와 fallback 결과 기록
- 자기 성찰 적용 전후 비교
- 에이전트 시험 결과 보고서 작성
- 발표 자료 작성
- 최종 시연 리허설

체크포인트:

```text
에이전트 아키텍처 설계서 완성
에이전트 시험 결과 보고서 완성
성능 비교 수치 2개 이상 제시
3분 시연 가능
```
