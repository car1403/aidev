# 01. Backend SSE API

이 문서는 FastAPI에서 SSE 스트리밍 엔드포인트를 설계하는 방법을 설명합니다.

## 핵심 개념

FastAPI에서 SSE 응답을 만들 때는 `StreamingResponse`를 사용합니다.

```text
StreamingResponse:
서버가 응답 데이터를 한 번에 모두 만들지 않고, 여러 조각으로 나누어 계속 보내는 응답 방식

media_type="text/event-stream":
브라우저나 클라이언트에게 이 응답이 SSE 형식이라는 것을 알려주는 값
```

## 기본 응답 형식

SSE는 보통 아래 형식으로 데이터를 보냅니다.

```text
data: 첫 번째 응답 조각

data: 두 번째 응답 조각

data: [DONE]
```

각 이벤트 사이에는 빈 줄이 들어갑니다.

## FastAPI 예시

팀 템플릿에는 아래 예제 파일이 포함되어 있습니다.

```text
99_team-projects/supabase-team-template/backend/streaming_example.py
```

실행 예시:

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn streaming_example:app --reload --host 127.0.0.1 --port 8001
```

## 설계 시 주의할 점

```text
[ ] 스트리밍 응답은 일반 JSON 응답과 다르다.
[ ] Swagger UI에서는 SSE 동작을 보기 어렵다.
[ ] PowerShell, curl, Streamlit 같은 클라이언트로 테스트한다.
[ ] 중간 chunk는 화면 표시용으로 사용한다.
[ ] 최종 응답만 Supabase messages 테이블에 저장하는 방식을 권장한다.
```
