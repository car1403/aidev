# 07. Workflow Ops Quality Map

## 운영 관점이 필요한 이유

AI 워크플로우는 만들어서 한 번 실행하면 끝나는 구조가 아닙니다.

운영 중에는 다음 문제가 발생합니다.

```text
AI 응답 품질 저하
외부 API 실패
입력 데이터 오류
출력 JSON 형식 오류
비용 증가
응답 지연
사용자 불만
```

## 운영 관리 항목

```text
Version: 모델, 프롬프트, 워크플로우 버전
Cost: 토큰, API 호출 수, 일일 비용
Latency: 응답 시간
Error: 실패 유형, 실패율
Log: 실행 단계별 기록
Quality: 입력/출력 검증, 사용자 피드백
```

## 기본 흐름

```text
Workflow 실행
-> 입력 검증
-> AI/Tool 실행
-> 오류 처리
-> 출력 검증
-> 로그 저장
-> 비용/사용량 기록
-> 품질 분석
-> 개선안 반영
```

## 05 단원에서 배우는 것

```text
버전과 비용 추적
Retry/Fallback/Escalation
로그 분석
입력/출력 데이터 품질 검증
Workflow Ops Assistant
```

## 미니 프로젝트 적용

99 미니 프로젝트에서는 다음 API와 화면을 통해 운영 관점을 확인합니다.

```text
GET /events
GET /metrics
Streamlit dashboard
ops-quality-checklist.md
```
