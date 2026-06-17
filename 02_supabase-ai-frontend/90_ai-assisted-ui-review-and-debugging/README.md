# 90_ai-assisted-ui-review-and-debugging

Streamlit 프론트엔드 과정을 마친 뒤, 본인이 직접 작성한 코드를 AI 보조 도구와 함께 리뷰하고 디버깅하는 단원입니다.

이 단원은 코드를 대신 생성시키는 수업이 아닙니다. 학생이 먼저 코드를 작성하고 실행한 다음, Codex 같은 AI 보조 도구를 사용해 문제를 찾고, 설명을 검토하고, 직접 수정하는 방법을 학습합니다.

## 학습 목표

- Streamlit UI 코드의 구조와 사용자 흐름을 리뷰할 수 있다.
- 오류 메시지, 실행 명령, 관련 코드를 함께 제공해 디버깅 도움을 받을 수 있다.
- AI가 제안한 수정안을 그대로 복사하지 않고 직접 검토할 수 있다.
- 긴 Streamlit 파일을 함수와 모듈 단위로 리팩토링할 수 있다.
- API 연동, session_state, 캐시 사용에서 흔한 문제를 점검할 수 있다.
- 최종 제출물에 코드 리뷰 기록과 개선 근거를 포함할 수 있다.

## 학습 순서

```text
01_ch1_ui-code-review
-> 02_ch2_debugging-streamlit-errors
-> 03_ch3_refactoring-ui-code
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
90_ai-assisted-ui-review-and-debugging
├─ README.md
├─ 00_references
├─ 01_ch1_ui-code-review
├─ 02_ch2_debugging-streamlit-errors
├─ 03_ch3_refactoring-ui-code
├─ 10_labs
└─ 20_assignments
```

## 수업 운영 원칙

1. 먼저 학생이 직접 코드를 작성합니다.
2. 실행 결과와 오류 메시지를 직접 확인합니다.
3. AI에게 질문할 때는 코드, 실행 명령, 기대 결과, 실제 결과를 함께 제공합니다.
4. AI 답변은 검토 자료로 사용하고 최종 수정은 학생이 직접 반영합니다.
5. 제출물에는 수정 전 문제, 수정 근거, 수정 후 확인 결과를 기록합니다.

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
streamlit run .\90_ai-assisted-ui-review-and-debugging\01_ch1_ui-code-review\01_review-target-simple-app.py
```

## 확인 기준

- 리뷰 전 코드의 문제점을 스스로 설명할 수 있다.
- AI에게 전달할 질문을 구체적으로 작성할 수 있다.
- 오류 메시지와 원인 후보를 구분할 수 있다.
- 리팩토링 전후의 코드 구조 차이를 설명할 수 있다.
- 최종 앱이 `streamlit run`으로 정상 실행된다.

