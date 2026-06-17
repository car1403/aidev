# 03. Tool Selection Map

## 도구 선택 기준

```text
외부 서비스와 API 연결이 중요하면 n8n
문서 기반 AI 답변이 중요하면 Dify
워크플로우 설계와 노드 흐름이 중요하면 AIPP
직접 API와 화면을 만들고 싶으면 FastAPI + Streamlit
```

## 조합 예시

```text
n8n + FastAPI:
  Webhook으로 문의를 받고 FastAPI 분석 API 호출

n8n + Dify:
  Webhook으로 문의를 받고 Dify API로 답변 생성

AIPP + Dify:
  AIPP에서 흐름을 설계하고 Dify로 AI 응답 구성
```
