# 02_debugging-streamlit-errors

Streamlit 실행 중 발생하는 오류를 분석하고 해결하는 방법을 학습합니다.

이 단원에서는 오류 메시지를 복사해서 바로 AI에게 던지는 방식보다, 어떤 명령을 실행했고 무엇을 기대했으며 실제로 어떤 결과가 나왔는지를 함께 정리하는 연습을 합니다.

## 예제 파일

```text
01_missing-import-fixed.py
02_session-state-fixed.py
03_api-error-handling-fixed.py
04_debugging-prompt-examples.md
```

## 학습 내용

- import 오류 확인
- `session_state` 초기화 오류 확인
- API 연결 실패 처리
- 백엔드 미실행과 API 경로 오류 구분
- `API_BASE_URL` 설정 확인
- Authorization header 누락 확인
- 오류 메시지를 AI에게 전달하는 방법

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\90_ai-assisted-ui-review-and-debugging\02_debugging-streamlit-errors\02_session-state-fixed.py
```

## 디버깅 순서

1. 실행 명령을 확인합니다.
2. 오류 메시지 전체를 복사합니다.
3. 문제가 난 파일과 관련 코드를 확인합니다.
4. 백엔드가 필요한 예제라면 백엔드 실행 여부를 확인합니다.
5. `.env`의 `API_BASE_URL`을 확인합니다.
6. token이 필요한 API라면 Authorization header가 포함되었는지 확인합니다.
7. AI에게 질문할 때 위 정보를 함께 전달합니다.
8. 수정 후 다시 실행해 결과를 확인합니다.

## 확인 내용

- 오류 메시지와 원인 후보를 구분했는가?
- `Connection refused`가 백엔드 미실행 문제라는 점을 설명할 수 있는가?
- `401 Unauthorized`가 token 또는 Authorization header 문제일 수 있음을 설명할 수 있는가?
- `KeyError`가 `session_state` 초기화 누락 때문에 생길 수 있음을 설명할 수 있는가?
