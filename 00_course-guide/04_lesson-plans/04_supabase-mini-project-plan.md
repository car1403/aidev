# 03. Supabase Mini Project Plan

대상 폴더:

```text
C:\aidev\04_supabase-ai-mini-project
```

## 수업 목표

```text
Supabase, FastAPI, Streamlit을 연결한다.
팀 프로젝트 주제를 정한다.
테이블, API, 화면을 설계한다.
Gemini 기반 AI 응답과 대화 이력을 저장한다.
SSE 기반 실시간 응답 스트리밍을 통합 실습으로 다룬다.
선택 실습으로 FastAPI, Redis, Streamlit 무료 배포 흐름을 이해한다.
```

## 수업 전 준비

```text
[ ] 04_supabase-ai-mini-project\.venv 준비
[ ] requirements.txt 설치
[ ] Supabase 프로젝트 준비
[ ].env에 Supabase URL/key 입력
[ ].env에 Gemini API Key 입력
[ ] 선택 배포 실습 시 Render, Upstash, Streamlit Community Cloud 계정 준비
[ ] FastAPI와 Streamlit을 각각 실행할 PowerShell 준비
```

## 강의 순서

```text
1. 수업용 샘플 실행
2. Supabase 테이블 구조 확인
3. FastAPI API 확인
4. Streamlit 화면 확인
5. Gemini 기반 일반 AI 응답 API 설계
6. SSE /api/chat/stream 실습
7. 최종 assistant 응답을 Supabase messages 테이블에 저장하는 흐름 설계
8. 선택 실습: FastAPI->Render, Redis->Upstash, Streamlit->Streamlit Community Cloud 배포 흐름 확인
9. 팀 프로젝트 템플릿 복사
10. docs 문서 작성
11. 발표 자료 준비
```

## SSE 설명 포인트

```text
SSE는 실시간 전송 기술입니다.
Supabase는 최종 데이터 저장소입니다.
chunk는 화면에 표시하고, 최종 응답만 messages 테이블에 저장하는 방식을 권장합니다.
배포는 필수 산출물이 아니라 선택 실습입니다.
배포를 진행하는 경우 FastAPI는 Render, Redis는 Upstash, Streamlit은 Streamlit Community Cloud를 기준으로 설명합니다.
```
