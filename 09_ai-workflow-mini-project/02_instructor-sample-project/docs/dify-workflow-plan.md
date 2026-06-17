# Dify Workflow Plan

## 목표

Dify Knowledge와 Workflow를 사용해 기술 지원 답변 초안을 생성합니다.

## 구성

```text
Knowledge: 기술 지원 문서, 장애 대응 가이드, FAQ
Workflow Input: 문의 제목, 문의 내용, 고객 등급
LLM Node: 유형과 긴급도 분류
Knowledge Retrieval: 관련 문서 검색
LLM Node: 답변 초안 생성
Condition: 위험 표현 또는 짧은 답변 검증
Output: JSON 또는 자연어 답변
```

## 외부 연동

n8n 또는 FastAPI backend에서 Dify API를 호출해 답변 초안을 받아올 수 있습니다.
