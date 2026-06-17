# 02. Supabase Frontend Plan

대상 폴더:

```text
C:\aidev\02_supabase-ai-frontend
```

## 수업 목표

```text
Streamlit 화면을 만든다.
사용자 입력과 버튼을 처리한다.
httpx로 FastAPI API를 호출한다.
대화 UI와 상태 관리를 구현한다.
백엔드 API를 통해 Supabase 데이터를 화면에 표시한다.
Gemini 기반 백엔드 응답을 화면에 표시한다.
Streamlit Community Cloud 배포 흐름을 선택 실습으로 이해한다.
```

## 수업 전 준비

```text
[ ] 02_supabase-ai-frontend\.venv 준비
[ ] requirements.txt 설치
[ ] 01_supabase-ai-backend 서버 실행 가능 여부 확인
[ ] .env의 API_BASE_URL 확인
[ ] 배포 선택 실습 시 Streamlit Community Cloud 계정 확인
```

## 강의 순서

```text
1. Streamlit hello 화면 실행
2. text_input, button, dataframe 사용
3. httpx GET/POST 요청
4. API_BASE_URL 환경변수 사용
5. 챗봇 UI 구성
6. session_state로 대화 상태 유지
7. 로그인/token/Authorization header 흐름 이해
8. Gemini 기반 백엔드 응답 표시
9. 선택 실습: Streamlit Community Cloud 배포 흐름 소개
```

## 강조할 점

```text
프론트엔드는 Supabase에 직접 service role key로 접근하지 않습니다.
Streamlit은 FastAPI API를 호출합니다.
AI 모델 호출도 프론트엔드가 직접 하지 않고 FastAPI 백엔드를 통해 처리합니다.
02의 최종 프론트엔드 예제는 03의 통합 프로젝트와 선택 배포 실습으로 연결됩니다.
SSE 스트리밍 UI는 03 미니 프로젝트에서 백엔드와 함께 다룹니다.
```
