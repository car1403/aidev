# API Integration Notes

## 기본 흐름

```text
사용자 입력
-> Streamlit 버튼 클릭
-> httpx로 API 요청
-> FastAPI에서 JSON 응답 반환
-> Streamlit 화면에 결과 출력
```

## 주요 개념

- GET: 서버에서 데이터를 조회할 때 사용합니다.
- POST: 서버에 데이터를 보낼 때 사용합니다.
- JSON: 프론트엔드와 백엔드가 주고받는 대표적인 데이터 형식입니다.
- status code: 요청 성공 또는 실패 상태를 나타내는 숫자입니다.
- timeout: 서버 응답을 기다릴 최대 시간입니다.

## 자주 확인할 것

- 백엔드 서버가 실행 중인가?
- API 주소가 정확한가?
- 요청 method가 GET인지 POST인지 맞는가?
- JSON key 이름이 백엔드 모델과 일치하는가?
- 응답 status code가 200인지 확인했는가?

