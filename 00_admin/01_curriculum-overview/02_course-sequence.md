# 02. Course Sequence

이 문서는 과정 진행 순서를 설명합니다.

## 01~03 Supabase 기반 AI 서비스

```text
01_supabase-ai-backend
Python 기초, FastAPI, Gemini 2.5 Flash-Lite 기본 호출, Supabase 저장, Auth/RLS, 대화 이력, Upstash Redis 개념

02_supabase-ai-frontend
Streamlit UI, API 호출, 챗봇 화면, 상태 관리

03_supabase-ai-mini-project
Supabase + FastAPI + Streamlit 통합 프로젝트
SSE 기반 실시간 AI 응답 스트리밍 통합 실습
선택 배포: FastAPI -> Render, Redis -> Upstash, Streamlit -> Streamlit Community Cloud
```

목표:

```text
사용자 입력
-> FastAPI 처리
-> Supabase 저장
-> Streamlit 화면 표시
-> AI 응답 또는 데이터 처리 결과 제공
```

## 04~05 LLM Agent

```text
04_llm-agent-orchestration
Docker Desktop에서 LLM, PostgreSQL, pgvector 기반 환경을 사용합니다.
Prompt, Function Calling, MCP, Memory, RAG, LangGraph 흐름을 배웁니다.

05_llm-agent-mini-project
04에서 배운 내용을 바탕으로 Agent 미니 프로젝트를 만듭니다.
```

목표:

```text
LLM이 답변하는 구조
-> Tool을 호출하는 구조
-> Memory를 사용하는 구조
-> RAG로 지식을 검색하는 구조
-> Agent Workflow로 확장
```

## 06~07 Multi-Agent Service Ops

```text
06_multi-agent-service-ops
Docker Compose, AWS, GitHub Actions, 모니터링, 보안, 가드레일, Auto Healing

07_multi-agent-service-mini-project
운영 관점의 Multi-Agent Auto Healing 미니 프로젝트
```

목표:

```text
서비스 패키징
-> Docker Compose 실행
-> CI/CD 흐름 이해
-> 로그와 모니터링
-> 장애 대응
-> 보안 정책
-> Multi-Agent 운영 프로젝트
```
