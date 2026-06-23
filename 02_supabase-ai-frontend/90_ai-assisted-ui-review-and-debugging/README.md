# 90_ai-assisted-ui-review-and-debugging

`90_ai-assisted-ui-review-and-debugging`은 02 프론트엔드 과정에서 만든 Streamlit 코드를 AI 보조 도구와 함께 리뷰하고 디버깅하는 단원입니다.

이 단원은 AI에게 앱을 처음부터 대신 만들게 하는 과정이 아닙니다. 먼저 직접 코드를 작성하고 실행한 뒤, 오류 메시지, 실행 명령, 기대 결과, 실제 결과를 정리해서 AI에게 검토를 요청합니다. 최종 수정은 직접 판단해서 반영합니다.

## 이 단원에서 점검하는 범위

앞 단원에서 만든 내용을 기준으로 다음을 점검합니다.

- `01_streamlit-basic`: Streamlit 실행, 입력과 출력, 화면 구조
- `02_streamlit-ui-components`: 버튼, 폼, 표, 차트, 파일 업로드
- `03_api-integration`: `httpx` API 호출, `API_BASE_URL`, 오류 처리
- `04_ai-chatbot-interface`: 챗봇 UI, mock 응답, `/api/chat/mock`, Gemini 선택 실습
- `05_state-session-and-data`: `st.session_state`, 로그인 상태, Authorization header, 사용자별 대화 이력, 서비스 로그

## 학습 목표

- Streamlit UI 코드의 사용자 흐름과 코드 구조를 리뷰할 수 있다.
- 오류 메시지, 실행 명령, 관련 코드, 기대 결과를 함께 정리해 AI에게 질문할 수 있다.
- AI가 제안한 수정안을 그대로 복사하지 않고 검토할 수 있다.
- 긴 Streamlit 파일을 입력 검증, API 호출, 화면 출력 함수로 나눌 수 있다.
- API 연결, `session_state`, 캐시, Authorization header에서 흔한 문제를 점검할 수 있다.
- 최종 제출물에 코드 리뷰 기록, 디버깅 기록, 개선 근거를 포함할 수 있다.

## 학습 순서

```text
00_references
-> 01_ui-code-review
-> 02_debugging-streamlit-errors
-> 03_refactoring-ui-code
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
90_ai-assisted-ui-review-and-debugging
├─ README.md
├─ 00_references
├─ 01_ui-code-review
├─ 02_debugging-streamlit-errors
├─ 03_refactoring-ui-code
├─ 10_labs
└─ 20_assignments
```

## 수업 진행 흐름

1. 먼저 직접 코드를 실행합니다.
2. 기대 결과와 실제 결과를 비교합니다.
3. 오류 메시지와 실행 명령을 기록합니다.
4. AI에게 질문할 때 관련 코드와 상황을 함께 제공합니다.
5. AI 답변을 검토하고, 채택할 부분과 버릴 부분을 구분합니다.
6. 수정 후 다시 실행해서 결과를 확인합니다.
7. 수정 이유와 확인 결과를 문서로 남깁니다.

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\90_ai-assisted-ui-review-and-debugging\01_ui-code-review\01_review-target-simple-app.py
```

## 확인 기준

- 리뷰 대상 코드의 문제점을 직접 설명할 수 있는가?
- AI에게 전달한 질문이 구체적인가?
- 오류 메시지와 원인 후보를 구분했는가?
- `API_BASE_URL`, 백엔드 실행 여부, 요청 경로를 확인했는가?
- `st.session_state` 초기화 위치가 올바른가?
- Authorization header와 token을 화면에 노출하지 않는가?
- Supabase service role key나 Gemini API key를 프론트엔드에 두지 않았는가?
- 리팩토링 전후 실행 결과가 동일한가?
- 최종 앱이 `streamlit run`으로 정상 실행되는가?
