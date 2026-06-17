# 03. AIPP, n8n, Dify Comparison

## 한 줄 비교

```text
AIPP: AI 워크플로우를 설계하고 실행하는 도구 관점
n8n: 여러 서비스와 API를 연결하는 자동화 도구
Dify: LLM 앱, Chatflow, Workflow, Knowledge/RAG를 만드는 AI 앱 플랫폼
```

## 역할 비교

| 도구 | 강점 | 적합한 작업 |
| --- | --- | --- |
| AIPP | AI 워크플로우 설계와 실행 흐름 | AI 노드 기반 업무 자동화 설계 |
| n8n | Webhook, API, 외부 서비스 연결 | 이벤트 기반 자동화, API 연동, 알림 |
| Dify | LLM 앱, Knowledge/RAG, Chatflow | AI 챗봇, 문서 검색 답변, AI API 앱 |

## 같이 사용할 때의 구조

```text
n8n Webhook
-> 문의 데이터 수신
-> 조건 분기
-> Dify API 호출
-> 결과를 Slack/Email/DB로 전달
-> 실행 로그 기록
```

또는:

```text
AIPP에서 워크플로우 설계
-> n8n으로 외부 서비스 자동화 연결
-> Dify로 AI 답변 생성 기능 구현
```

## 선택 기준

```text
API와 외부 서비스 연결이 중심이면 n8n
문서 기반 AI 앱과 챗봇이 중심이면 Dify
AI 업무 흐름 자체의 설계가 중심이면 AIPP
```

## 초보자 학습 순서

```text
1. AI Workflow 개념 이해
2. AIPP식 노드 설계
3. n8n으로 Webhook/API 연결
4. Dify로 AI 앱과 Knowledge 구성
5. 운영/품질 기준 적용
```
