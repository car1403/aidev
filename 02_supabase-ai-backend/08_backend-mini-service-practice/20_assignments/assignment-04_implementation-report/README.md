# Assignment 04. Implementation Report

## 목표

mock 서버와 Supabase 서버 실행 결과를 보고서로 정리합니다.

## 참고 파일

```text
../04_implementation-guide/README.md
../04_implementation-guide/main_mock.py
../04_implementation-guide/main_supabase.py
```

## 제출 내용

아래 항목을 정리합니다.

| 항목 | 작성 내용 |
| --- | --- |
| mock 서버 실행 결과 | `main_mock.py` 실행 여부와 Swagger UI 주소 |
| Supabase 서버 실행 결과 | `main_supabase.py` 실행 여부와 Swagger UI 주소 |
| 질문 생성 결과 | `POST /questions` 요청/응답 예시 |
| 질문 목록 조회 결과 | `GET /questions` 응답 예시 |
| 서비스 로그 결과 | `GET /service-logs` 응답 예시 |
| Supabase 저장 확인 | Table Editor에서 확인한 테이블과 데이터 |
| 오류와 해결 | 발생한 오류, 원인, 해결 방법 |

## 실행 명령 예시

mock 서버:

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Supabase 서버:

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

## 완료 기준

- mock 서버와 Supabase 서버 결과가 구분되어 있습니다.
- 성공한 API 요청/응답 예시가 있습니다.
- Supabase 테이블 저장 결과가 확인되어 있습니다.
- 오류가 있었다면 해결 과정이 기록되어 있습니다.
