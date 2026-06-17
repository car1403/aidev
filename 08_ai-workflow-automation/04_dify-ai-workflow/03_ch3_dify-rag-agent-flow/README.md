# 03_ch3_dify-rag-agent-flow

Dify에서 Knowledge/RAG, Agent, Tool 흐름을 설계하는 챕터입니다.

## 핵심 개념

```text
Knowledge: Dify에 업로드한 문서 기반 지식
RAG: 질문과 관련된 문서를 검색해 LLM 답변에 반영하는 구조
Agent: 목표를 수행하기 위해 Tool과 지식을 활용하는 AI 실행 단위
Tool: 외부 API나 기능 호출
```

## 기본 흐름

```text
사용자 질문
-> Query 정리
-> Knowledge 검색
-> 관련 문서 선택
-> LLM 답변 생성
-> 검증
-> 응답
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\04_dify-ai-workflow
python .\03_ch3_dify-rag-agent-flow\01_dify_rag_agent_flow.py
```
