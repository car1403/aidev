# 01. Supabase Backend Plan

대상 폴더:

```text
C:\aidev\01_supabase-ai-backend
```

## 수업 목표

```text
Python 기초를 익힌다.
FastAPI 서버를 실행한다.
Gemini 2.5 Flash-Lite 기본 호출 흐름을 이해한다.
Supabase 프로젝트와 테이블을 이해한다.
백엔드에서 Supabase를 안전하게 호출한다.
Redis와 Upstash의 역할을 이해한다.
대화 이력과 서비스 로그 저장 구조를 이해한다.
```

## 수업 전 준비

```text
[ ] Python 설치 확인
[ ] VS Code 설치 확인
[ ] C:\aidev 폴더 열기
[ ] 01_supabase-ai-backend\.venv 준비
[ ] requirements.txt 설치
[ ] Supabase 계정 또는 수업용 프로젝트 준비
[ ] Gemini API Key 또는 수업용 테스트 Key 준비
[ ] Upstash Redis는 필요한 챕터에서 선택적으로 준비
```

## 강의 순서

```text
1. Python 기본 실행
2. 함수, 모듈, 예외 처리, 클래스
3. FastAPI /health API
4. Pydantic 요청 검증
5. Gemini API Key와 .env 설정
6. Gemini 2.5 Flash-Lite 기본 호출
7. Supabase URL/key/env 설명
8. Supabase CRUD
9. Auth/RLS/service role key 설명
10. Redis 개념과 Upstash 사용 위치
11. 대화 이력과 로그 저장 구조
```

## 강조할 점

```text
service role key는 서버에서만 사용합니다.
Streamlit 화면에 service role key를 넣지 않습니다.
01~03의 기본 AI 모델 예제는 Gemini 2.5 Flash-Lite를 사용합니다.
OpenAI 예제 파일은 비교 또는 심화 실습용으로 유지합니다.
Redis는 로컬 설치보다 Upstash Redis를 우선 사용합니다.
Docker는 이 과정에서 사용하지 않고 06에서 본격적으로 다룹니다.
SSE 스트리밍은 03 미니 프로젝트에서 통합 실습으로 다룹니다.
```
