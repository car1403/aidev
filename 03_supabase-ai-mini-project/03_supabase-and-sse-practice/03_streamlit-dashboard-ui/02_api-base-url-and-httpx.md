# 02. API_BASE_URL과 httpx

Streamlit은 FastAPI API를 호출해서 데이터를 가져옵니다.

이때 API 서버 주소를 코드 여러 곳에 직접 쓰지 않고 `API_BASE_URL`이라는 환경 변수로 관리합니다.

## 환경 변수 예시

```env
API_BASE_URL=http://127.0.0.1:8000
```

## 호출 흐름

```text
Streamlit 버튼 클릭
-> httpx로 FastAPI API 호출
-> FastAPI가 Supabase 조회
-> JSON 응답 반환
-> Streamlit 화면에 표시
```

## httpx를 사용하는 이유

`httpx`는 Python에서 HTTP API를 호출할 때 사용하는 라이브러리입니다.

```text
GET 요청
-> 데이터 조회

POST 요청
-> 데이터 생성 또는 저장
```

## 확인 기준

- API 주소가 코드에 여러 번 하드코딩되어 있지 않습니다.
- FastAPI 서버가 꺼져 있을 때 오류 메시지가 표시됩니다.
- API 응답 JSON 구조를 화면 표시용 데이터로 변환할 수 있습니다.
