# AIPP Workflow Plan

## 목표

샘플 기술 지원 워크플로우를 AIPP식 노드 흐름으로 옮깁니다.

## 노드 흐름

```text
Trigger: 기술 지원 문의 접수
Input: 고객명, 등급, 제목, 문의 내용
LLM Node: 유형과 긴급도 분류
Tool Node: 관련 문서 검색
LLM Node: 답변 초안 생성
Condition Node: 품질 검증과 긴급도 분기
Action Node: 운영팀 알림 또는 답변 후보 저장
Log Node: 실행 이벤트와 품질 지표 기록
```

## 확인할 점

- 각 노드 입력과 출력이 명확한가?
- 긴급 문의와 일반 문의의 분기가 있는가?
- 검증 실패 시 사람 검토로 넘어가는가?
