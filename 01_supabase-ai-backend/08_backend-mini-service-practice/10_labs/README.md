# Labs

작은 백엔드 서비스를 단계별로 구현하는 수업 실습을 진행합니다.

## Lab 01 - 요구사항 확인

목표:

- 미니 서비스가 해결할 문제를 설명합니다.
- 필수 기능과 제외 범위를 구분합니다.

확인 파일:

```text
../01_requirements/service-requirements.md
```

## Lab 02 - API 설계 확인

목표:

- `/health`, `/qa`, `/service-logs` endpoint의 역할을 설명합니다.
- 요청/응답 JSON 구조를 확인합니다.

확인 파일:

```text
../02_api-design/api-design.md
```

## Lab 03 - mock LLM 함수 실행 흐름 이해

목표:

- 실제 LLM API 호출 전 mock 함수로 전체 백엔드 흐름을 완성합니다.
- 비용 없는 테스트와 실제 API 호출의 차이를 이해합니다.

확인 파일:

```text
../04_implementation-guide/llm_mock.py
```

## Lab 04 - mock FastAPI 서버 실행

목표:

- 메모리 저장소를 사용해 질문/답변 생성 API를 테스트합니다.
- 서비스 로그가 함께 생성되는지 확인합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

테스트 순서:

1. `GET /health`
2. `POST /qa`
3. `GET /qa`
4. `GET /service-logs`

## Lab 05 - Supabase 테이블 생성

목표:

- Supabase SQL Editor에서 미니 서비스 테이블을 생성합니다.
- 질문/답변 테이블과 서비스 로그 테이블을 구분합니다.

실행 파일:

```text
../03_supabase-schema/mini-service-schema.sql
```

## Lab 06 - Supabase FastAPI 서버 실행

목표:

- `main_supabase.py`로 실제 Supabase 저장 흐름을 확인합니다.
- Swagger UI에서 생성한 데이터가 Supabase Table Editor에 보이는지 확인합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

Swagger UI:

```text
http://127.0.0.1:8005/docs
```

주의:

Supabase 버전은 실제 데이터가 저장됩니다. 수업에서는 강사와 함께 `.env`와 테이블을 확인한 뒤 실행합니다.
