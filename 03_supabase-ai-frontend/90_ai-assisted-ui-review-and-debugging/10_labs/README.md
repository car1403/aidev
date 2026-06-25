# 10_labs

AI 보조 리뷰와 디버깅을 수업 중 직접 연습하는 실습입니다.

## 실습 목록

```text
lab-01-review-my-streamlit-app.md
lab-02-debugging-record.md
lab-03-refactor-before-after.py
```

## 실습 기준

- 먼저 직접 코드를 실행합니다.
- 문제를 본인 말로 정리합니다.
- AI에게 물어볼 질문을 작성합니다.
- AI 답변 중 채택한 부분과 버린 부분을 구분합니다.
- 직접 수정한 뒤 실행 결과를 확인합니다.

## 추천 리뷰 대상

- `03_api-integration`의 API 호출 화면
- `04_ai-chatbot-interface`의 mock 챗봇 UI
- `05_state-session-and-data`의 로그인 token 저장 화면
- `05_state-session-and-data`의 서비스 로그 조회 화면

## 확인 기준

- 실행 명령과 파일 경로를 정확히 기록했는가?
- `API_BASE_URL`, 요청 경로, 응답 키 이름을 확인했는가?
- `st.session_state` 초기화 위치를 확인했는가?
- Authorization header가 필요한 API인지 확인했는가?
- 수정 후 다시 실행해 결과를 확인했는가?
