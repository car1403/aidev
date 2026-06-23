# Debugging Prompt Examples

## 오류 메시지 분석 요청

```text
아래 Streamlit 오류 메시지를 분석해 주세요.
실행 명령은 streamlit run app.py 입니다.
기대 결과는 버튼 클릭 후 count가 1 증가하는 것입니다.
실제 결과는 KeyError가 발생합니다.
원인을 먼저 설명하고 수정 순서를 알려 주세요.
```

## API 연결 오류 요청

```text
Streamlit에서 FastAPI /health API를 호출했는데 ConnectError가 발생합니다.
백엔드 실행 명령, 프론트엔드 실행 명령, API_BASE_URL 값을 함께 확인해 주세요.
```

## 챗봇 mock API 오류 요청

```text
Streamlit에서 03_api-integration 샘플 백엔드의 /api/chat/mock API를 호출하고 있습니다.
요청 JSON은 {"question": "..."} 형식이어야 하고, 응답 JSON의 answer 값을 화면에 표시해야 합니다.
현재 KeyError 또는 404 오류가 발생합니다.
요청 경로, 요청 본문, 응답 키 이름이 맞는지 순서대로 확인해 주세요.
```

## 로그인 token 오류 요청

```text
Streamlit에서 로그인 후 access token을 st.session_state에 저장했습니다.
그런데 /api/me 호출 시 401 Unauthorized가 발생합니다.
Authorization header가 Bearer 형식으로 구성되었는지, token이 None인지, 백엔드가 요구하는 header 이름이 맞는지 확인해 주세요.
```

## 답변 검토 질문

```text
제안한 수정이 왜 필요한지 설명해 주세요.
새로운 라이브러리를 추가하지 않고 해결할 수 있는지도 확인해 주세요.
```

