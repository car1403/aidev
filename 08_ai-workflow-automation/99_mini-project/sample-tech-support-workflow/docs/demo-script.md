# Demo Script

## 1. 문제 소개

기술 지원 문의가 많아지면 담당자가 유형 분류, 문서 검색, 답변 초안 작성, 긴급도 판단을 반복해야 합니다.

## 2. 해결 흐름

```text
문의 입력
-> 자동 분류
-> 관련 문서 매칭
-> 답변 초안 생성
-> 품질 검증
-> 운영팀 알림 또는 답변 후보 생성
```

## 3. 시연 순서

1. Backend health check
2. Frontend에서 샘플 문의 입력
3. 분석 결과 확인
4. next_action 확인
5. events와 metrics 확인
6. AIPP/n8n/Dify 설계 문서 설명
