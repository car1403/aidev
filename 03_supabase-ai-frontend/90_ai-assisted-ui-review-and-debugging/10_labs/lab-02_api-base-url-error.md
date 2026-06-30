# Lab 02. API_BASE_URL Error

## 목표

프론트엔드가 백엔드에 연결되지 않을 때 확인할 순서를 익힙니다.

## 확인할 것

- 백엔드가 실행 중인가?
- `http://127.0.0.1:8000/docs`가 열리는가?
- `.env`의 `API_BASE_URL`이 같은 주소인가?
- Streamlit 코드가 `.env`를 읽고 있는가?
- 요청 URL과 HTTP Method가 백엔드와 맞는가?

## 질문 예시

```text
Streamlit에서 백엔드 API 호출이 실패합니다.
API_BASE_URL은 http://127.0.0.1:8000입니다.
백엔드 /docs는 열립니다.
가능한 원인을 우선순위로 알려주세요.
```
