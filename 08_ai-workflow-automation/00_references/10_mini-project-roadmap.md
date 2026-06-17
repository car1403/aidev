# 10. Mini Project Roadmap

## 미니 프로젝트 주제

```text
노코드·로코드 기반 기업형 지능형 기술 지원 자동화 워크플로우
```

## 목표 흐름

```text
기술 지원 문의 접수
-> 유형과 긴급도 분류
-> 관련 기술 문서 검색
-> 답변 초안 생성
-> 품질 검증
-> 운영팀 알림 또는 답변 후보 저장
-> 이벤트와 지표 기록
```

## 99 샘플 프로젝트

위치:

```text
99_mini-project/sample-tech-support-workflow
```

구성:

```text
FastAPI backend
Streamlit frontend
workflow.py
events
metrics
AIPP/n8n/Dify 설계 문서
```

## 팀 프로젝트 진행 순서

```text
1. 업무 문제 정의
2. Trigger, Condition, Action 설계
3. LLM/Tool/Knowledge 역할 분리
4. AIPP/n8n/Dify 중 구현 도구 선택
5. Python 샘플 또는 API 구현
6. 오류 처리와 fallback 설계
7. 로그와 품질 지표 추가
8. 최종 시연 준비
```

## 발표 체크리스트

```text
[ ] 어떤 업무 문제를 해결하는지 설명
[ ] 워크플로우 구조 설명
[ ] 사용하는 도구와 이유 설명
[ ] 입력부터 결과까지 시연
[ ] 오류 처리와 품질 검증 설명
[ ] 운영 로그 또는 지표 설명
[ ] 개선 방향 제시
```
