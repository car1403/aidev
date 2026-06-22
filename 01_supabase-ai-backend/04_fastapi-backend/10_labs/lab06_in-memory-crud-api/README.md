# Lab 06 - In Memory CRUD API

## 목표

Supabase에 연결하기 전에 FastAPI만으로 CRUD API 흐름을 연습합니다.

이 실습에서는 서버 메모리에 메모 데이터를 저장합니다. 서버를 재시작하면 데이터는 사라집니다. 실제 서비스에서는 이후 `06_supabase-db-and-auth`에서 Supabase 테이블에 저장하도록 확장합니다.

## 학습 내용

- `GET /memos`: 전체 메모 조회
- `GET /memos/{memo_id}`: 메모 한 개 조회
- `POST /memos`: 새 메모 생성
- `PUT /memos/{memo_id}`: 기존 메모 수정
- `DELETE /memos/{memo_id}`: 기존 메모 삭제
- `HTTPException`으로 404 오류 처리

## 실행 방법

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab06_in-memory-crud-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn solution:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 확인 순서

1. `GET /memos`로 기본 데이터 확인
2. `POST /memos`로 새 메모 생성
3. `GET /memos/{memo_id}`로 생성된 메모 확인
4. `PUT /memos/{memo_id}`로 메모 수정
5. `DELETE /memos/{memo_id}`로 메모 삭제
6. 없는 id를 조회해 404 응답 확인

## POST 요청 예시

```json
{
  "title": "FastAPI CRUD",
  "content": "메모 생성과 조회를 연습합니다.",
  "tags": ["fastapi", "crud"]
}
```

## 핵심 요약

```text
메모리 저장소
-> 배우기 쉽지만 서버를 재시작하면 사라짐

Supabase 저장소
-> 실제 서비스 데이터 저장에 적합
-> 다음 DB/Auth 단원에서 연결
```

