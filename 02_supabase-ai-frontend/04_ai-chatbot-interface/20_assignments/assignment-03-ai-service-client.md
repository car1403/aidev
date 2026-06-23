# Assignment 03: AI Service Client

## 목표

Streamlit 챗봇 화면에서 03 단원의 샘플 백엔드 mock chat API를 호출하는 앱을 만듭니다.

## 요구사항

- API 기본 주소를 변수로 분리합니다.
- 질문을 `/api/chat/mock`에 POST 요청으로 보냅니다.
- 요청 JSON은 `{"question": "질문 내용"}` 형식을 사용합니다.
- 응답 JSON의 `answer` 값을 assistant 메시지로 표시합니다.
- 연결 실패, 타임아웃, HTTP 오류를 처리합니다.
- 실제 AI 모델 호출은 필수가 아닙니다.
- 선택 기능으로 Gemini SDK 호출을 추가할 수 있지만, API key가 없을 때는 mock 응답으로 대체해야 합니다.

## 제출 파일 예시

```text
assignment-03-ai-service-client.py
```
