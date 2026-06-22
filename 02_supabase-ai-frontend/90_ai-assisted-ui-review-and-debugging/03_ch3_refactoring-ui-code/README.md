# 03_ch3_refactoring-ui-code

작동하는 Streamlit 코드를 더 읽기 쉽고 유지보수하기 좋은 구조로 바꾸는 방법을 학습합니다.

이 챕터에서는 기능을 새로 추가하는 것보다, 이미 동작하는 코드를 함수로 나누고 역할을 분리하는 데 집중합니다. AI 보조 도구는 리팩토링 후보를 찾는 데 사용하고, 최종 수정은 수업 참여자가 직접 판단해서 반영합니다.

## 예제 파일

```text
01_before-long-app.py
02_after-function-split.py
03_after-api-client-split.py
04_refactoring-checklist.md
```

## 학습 내용

- 화면 영역별 함수 분리
- 입력 검증 함수 분리
- API 호출 함수 분리
- 설정값 상수화
- 리팩토링 전후 비교

## 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
streamlit run .\90_ai-assisted-ui-review-and-debugging\03_ch3_refactoring-ui-code\01_before-long-app.py
```

## 리팩토링 요청 예시

```text
아래 Streamlit 코드는 동작하지만 한 파일에 입력, 피드백 생성, 화면 출력이 모두 섞여 있습니다.
기능을 바꾸지 않고 어떤 함수로 나누면 좋을지 먼저 제안해 주세요.
코드는 바로 수정하지 말고 분리 기준과 이유를 설명해 주세요.
```

## 확인할 내용

- 리팩토링 전후 실행 결과가 같은가?
- 입력 검증 로직이 유지되는가?
- API 호출 함수와 화면 출력 코드가 분리되었는가?
- 함수 이름만 보고 역할을 이해할 수 있는가?
- README의 실행 명령이 변경된 파일 구조와 일치하는가?

## 제출 연결

리팩토링 결과는 `20_assignments\assignment-03-refactoring-report.md` 양식에 맞춰 정리합니다.

