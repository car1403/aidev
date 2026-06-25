# 03. API 테스트 체크리스트

FastAPI API를 만든 뒤에는 브라우저와 Swagger UI에서 먼저 확인합니다.

## 실행 예시

```powershell
cd C:\aidev\04_supabase-ai-mini-project\99_team-projects\team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8000/docs
```

## 확인 항목

- [ ] `/health`가 정상 응답한다.
- [ ] Supabase URL/key를 읽을 수 있다.
- [ ] 조회 API가 빈 배열 또는 테스트 데이터를 반환한다.
- [ ] 생성 API 호출 후 Supabase Table Editor에서 데이터가 보인다.
- [ ] 잘못된 요청을 보냈을 때 오류 메시지가 이해하기 쉽게 나온다.
- [ ] 오류가 발생했을 때 `service_logs`에 기록할 수 있다.

## 자주 발생하는 문제

```text
환경 변수를 찾을 수 없음
-> .env 위치가 C:\aidev\04_supabase-ai-mini-project인지 확인합니다.

Supabase 인증 오류
-> anon key와 service role key를 바꿔 넣지 않았는지 확인합니다.

테이블이 없다는 오류
-> SQL Editor에서 테이블 생성 SQL을 실행했는지 확인합니다.
```
