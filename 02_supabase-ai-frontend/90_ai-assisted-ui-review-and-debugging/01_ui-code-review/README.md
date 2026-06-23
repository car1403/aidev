# 01_ui-code-review

본인이 작성한 Streamlit UI 코드를 리뷰하는 방법을 학습합니다.

이 단원에서는 화면이 예쁘게 보이는지만 보지 않습니다. 사용자가 어떤 순서로 입력하는지, 오류가 났을 때 무엇을 알 수 있는지, API 호출과 화면 출력이 적절히 분리되어 있는지, 보안상 위험한 값이 화면이나 코드에 노출되지 않는지를 함께 확인합니다.

## 예제 파일

```text
01_review-target-simple-app.py
02_review-target-api-page.py
03_review-report-example.md
```

## 학습 내용

- 화면 흐름 리뷰
- 입력값 검증 리뷰
- API 호출 위치 리뷰
- 오류 메시지 문구 리뷰
- `session_state` 사용 위치 리뷰
- `/api/chat/mock` 같은 백엔드 API 호출 구조 리뷰
- token과 API key 노출 여부 리뷰

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\90_ai-assisted-ui-review-and-debugging\01_ui-code-review\01_review-target-simple-app.py
```

## 리뷰 질문 예시

```text
아래 Streamlit 코드를 리뷰해 주세요.
사용자 입력 흐름, 오류 처리, session_state 초기화, API 호출 분리, 보안상 위험한 값 노출 여부를 기준으로 봐 주세요.
수정 코드를 바로 만들기보다 문제점과 수정 방향을 먼저 설명해 주세요.
```

## 확인 내용

- 입력값이 비어 있을 때 적절히 안내하는가?
- API 호출 실패 시 사용자가 이해할 수 있는 메시지가 보이는가?
- API 호출 함수와 화면 출력 코드가 너무 강하게 섞여 있지 않은가?
- `API_BASE_URL` 같은 설정값이 한 곳에서 관리되는가?
- 프론트엔드에 Supabase service role key나 Gemini API key가 들어 있지 않은가?
