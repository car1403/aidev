# 03_ch3_fastapi-supabase-integration

이 단원은 FastAPI에서 Supabase를 호출해 API 서버를 만드는 단계입니다.

## 학습 목표

- FastAPI endpoint에서 Supabase client를 사용합니다.
- `/health`로 서버 상태를 확인합니다.
- `/notes` API로 Supabase 테이블 데이터를 조회합니다.
- `/notes` POST API로 새 데이터를 저장합니다.
- `/notes/{note_id}` API로 단건 조회, 수정, 삭제를 실습합니다.

## 제공 endpoint

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버와 설정 상태를 확인합니다. |
| GET | `/notes` | 최근 학습 메모 목록을 조회합니다. |
| GET | `/notes/{note_id}` | 학습 메모 1개를 id로 조회합니다. |
| POST | `/notes` | 새 학습 메모를 저장합니다. |
| PUT | `/notes/{note_id}` | 기존 학습 메모의 title/content를 수정합니다. |
| DELETE | `/notes/{note_id}` | 학습 메모를 삭제합니다. |

## 실행 예시

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인 주소:

```text
http://127.0.0.1:8000/docs
```

## 주의

이 예제는 Supabase 관리형 DB를 사용합니다. 로컬 Docker PostgreSQL은 사용하지 않습니다.

## 수업 진행 순서

1. Swagger UI에서 `GET /health`를 호출합니다.
2. `POST /notes`로 새 메모를 만듭니다.
3. 응답에 들어 있는 `id`를 복사합니다.
4. `GET /notes/{note_id}`로 단건 조회를 확인합니다.
5. `PUT /notes/{note_id}`로 제목이나 내용을 수정합니다.
6. `DELETE /notes/{note_id}`로 실습 데이터를 삭제합니다.

수정과 삭제에서는 반드시 id 조건이 필요하다는 점을 강조합니다. 백엔드에서 조건 없는 update/delete는 실제 서비스 데이터 전체에 영향을 줄 수 있습니다.
