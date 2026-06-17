# 08. Backend Mini Service Practice

이 단원은 01~07에서 배운 내용을 작은 백엔드 서비스로 묶어 보는 실습 단계입니다.

최종 프로젝트를 하기 전에, FastAPI, Supabase, LLM API, 사용자 데이터 저장, 서비스 로그를 작은 단위로 연결해 봅니다.

## 학습 목표

- CRUD API와 LLM API 호출을 하나의 백엔드 흐름으로 연결합니다.
- Supabase 테이블에 사용자 요청과 AI 응답을 저장합니다.
- 서비스 로그를 남겨 오류와 실행 결과를 확인합니다.
- Codex를 활용해 코드 리뷰와 리팩토링을 진행합니다.

## 권장 구성

```text
08_backend-mini-service-practice
├─ README.md
├─ 00_references
├─ 01_requirements
├─ 02_api-design
├─ 03_supabase-schema
├─ 04_implementation-guide
├─ 10_labs
└─ 20_assignments
```

## 이번 단원의 구현 주제

이번 단원에서는 아래 주제로 작은 백엔드 서비스를 만듭니다.

```text
AI 질문 응답 백엔드 미니 서비스
```

사용자가 질문을 보내면 백엔드가 다음 일을 처리합니다.

1. 요청 데이터를 검증합니다.
2. mock LLM 또는 실제 LLM 호출 위치를 통해 답변을 만듭니다.
3. 질문과 답변을 저장합니다.
4. 서비스 로그를 저장합니다.
5. JSON 응답을 반환합니다.

## 미니 서비스 예시

```text
사용자가 질문을 보낸다.
-> FastAPI가 요청을 검증한다.
-> LLM API가 답변 초안을 만든다.
-> Supabase에 질문과 답변을 저장한다.
-> 서비스 로그를 저장한다.
-> JSON 응답을 반환한다.
```

## 산출물

- API 설계 문서
- Supabase 테이블 설계
- FastAPI endpoint
- LLM API 호출 코드 또는 호출 설계
- 실행 로그
- Codex 코드 리뷰 기록

## 실습 파일

```text
01_requirements/service-requirements.md
-> 미니 서비스 요구사항을 정리합니다.

02_api-design/api-design.md
-> endpoint, 요청/응답, 오류 형식을 설계합니다.

03_supabase-schema/mini-service-schema.sql
-> Supabase SQL Editor에서 실행할 테이블 생성 SQL입니다.

04_implementation-guide/schemas.py
-> FastAPI 요청/응답 Pydantic 모델입니다.

04_implementation-guide/llm_mock.py
-> 비용 없이 AI 답변 생성을 흉내 내는 함수입니다.

04_implementation-guide/service_logger.py
-> 서비스 로그 데이터를 만드는 보조 함수입니다.

04_implementation-guide/supabase_client.py
-> Supabase client 생성 함수를 분리한 파일입니다.

04_implementation-guide/main_mock.py
-> 외부 서비스 없이 메모리 저장소로 실행하는 FastAPI 앱입니다.

04_implementation-guide/main_supabase.py
-> Supabase 테이블에 실제 저장하는 FastAPI 앱입니다.
```

## 실행 순서

처음에는 외부 서비스 영향을 주지 않는 mock 서버부터 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

Supabase 연동 버전은 `.env`와 테이블 생성 SQL을 확인한 뒤 실행합니다.

```powershell
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

## 다음 단계

이 단원을 마친 뒤 `99_final-backend-project`에서 백엔드 최종 프로젝트를 진행합니다.
