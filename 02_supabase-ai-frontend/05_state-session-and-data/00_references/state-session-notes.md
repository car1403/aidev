# State Session Notes

## 핵심 개념

Streamlit은 사용자가 입력하거나 버튼을 누를 때마다 스크립트를 다시 실행합니다. 따라서 화면에서 계속 유지해야 하는 값은 `st.session_state`에 저장합니다.

## 이 단원의 상태 종류

- UI 상태: 입력값, 선택값, 버튼 결과
- 로그인 상태: 사용자 이름, access token, 로그인 여부
- 데이터 상태: 사용자별 조회 결과, 대화 이력
- 캐시 상태: 반복 호출 결과

## 인증 연동 흐름

```text
로그인 폼 입력
-> FastAPI 로그인 API 호출
-> access token 응답 수신
-> st.session_state에 token 저장
-> Authorization header로 보호된 API 호출
-> 로그아웃 시 token 삭제
```

