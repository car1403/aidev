# 20_assignments

이 폴더는 `90_ai-assisted-code-review-and-debugging` 단원의 제출형 과제 모음입니다.

`10_labs`가 안내를 따라 직접 연습하는 실습이라면, `20_assignments`는 Codex를 어떻게 사용했고 무엇을 직접 검증했는지 정리하는 과제입니다. 결과 코드만 제출하는 것이 아니라, 요청문, 판단 기준, 실행 결과, 남은 질문까지 함께 기록합니다.

## 과제 목록

| 과제 | 폴더 | 핵심 내용 |
| --- | --- | --- |
| Assignment 01 | `assignment01_codex-learning-log` | Codex 사용 학습 기록 |
| Assignment 02 | `assignment02_prompt-improvement` | 모호한 요청을 명확한 개발 요청으로 개선 |
| Assignment 03 | `assignment03_debugging-report` | 오류 분석과 수정 과정 보고 |
| Assignment 04 | `assignment04_backend-code-review-report` | FastAPI/Supabase/Redis 백엔드 코드 리뷰 보고 |
| Assignment 05 | `assignment05_security-cost-review-report` | 보안과 비용 위험 점검 보고 |

## 공통 제출 기준

모든 과제는 다음 기준을 지킵니다.

- 사용한 Codex 요청문을 기록합니다.
- Codex 응답을 그대로 붙여 넣지 않고 핵심을 본인 말로 정리합니다.
- 생성 또는 수정한 코드가 있다면 직접 실행한 결과를 포함합니다.
- 어떤 부분을 직접 확인했고, 어떤 부분은 아직 이해가 필요한지 구분합니다.
- 실제 API key, Supabase key, Upstash Redis token은 절대 제출물에 포함하지 않습니다.
- `.env` 파일 대신 `.env.example` 형식으로 필요한 변수명만 정리합니다.

## 권장 진행 순서

1. 과제 README를 읽습니다.
2. 제출 파일 이름을 먼저 확인합니다.
3. Codex에게 요청할 문장을 직접 작성합니다.
4. Codex 응답에서 사용할 내용과 보류할 내용을 나눕니다.
5. 코드가 있다면 직접 실행하거나 문서와 비교합니다.
6. 보고서 템플릿에 맞춰 결과를 정리합니다.
7. 제출 전 민감 정보가 포함되어 있지 않은지 다시 확인합니다.

## 공통 보고서 품질 기준

좋은 보고서는 길기만 한 문서가 아닙니다. 다음 항목이 명확해야 합니다.

- 무엇을 하려고 했는가?
- 어떤 파일 또는 코드를 확인했는가?
- Codex에게 어떤 요청을 했는가?
- Codex가 제안한 내용 중 무엇을 받아들였는가?
- 직접 확인한 실행 결과는 무엇인가?
- 아직 판단하기 어려운 부분은 무엇인가?

## 최종 확인 체크리스트

- [ ] 제출 파일 이름이 과제 README와 일치한다.
- [ ] Codex 요청문이 포함되어 있다.
- [ ] Codex 응답을 그대로 복사하지 않고 요약했다.
- [ ] 직접 실행 또는 직접 확인한 결과가 있다.
- [ ] API key, token, password가 포함되어 있지 않다.
- [ ] 남은 질문 또는 보류한 판단이 정리되어 있다.
