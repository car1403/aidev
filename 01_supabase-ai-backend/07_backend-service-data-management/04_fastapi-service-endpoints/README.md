# 04. FastAPI Service Endpoints

사용자 정보, 대화 이력, 서비스 로그를 조회하고 저장하는 FastAPI endpoint를 설계합니다.

## 이 단원에서 만들 endpoint

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버 상태 확인 |
| GET | `/profiles/{user_id}` | 사용자 프로필 조회 |
| POST | `/conversations` | 새 대화방 생성 |
| POST | `/conversations/{conversation_id}/messages` | 대화방에 메시지 추가 |
| GET | `/conversations/{conversation_id}/messages` | 대화방 메시지 조회 |
| POST | `/service-logs` | 서비스 로그 저장 |

## 실습 파일

```text
main_mock.py
-> 외부 서비스 없이 메모리 리스트로 전체 API 구조를 실습합니다.

main_supabase.py
-> Supabase 테이블에 실제 데이터를 저장하고 조회합니다.
```

초보자는 먼저 `main_mock.py`로 API 흐름을 익힌 뒤 `main_supabase.py`로 넘어갑니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

Swagger UI:

```text
http://127.0.0.1:8003/docs
```
