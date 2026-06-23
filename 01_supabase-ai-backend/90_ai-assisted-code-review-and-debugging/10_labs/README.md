# 10_labs

이 폴더는 `90_ai-assisted-code-review-and-debugging`에서 배운 내용을 직접 연습하는 실습 모음입니다.

앞 단원에서 Codex 사용법, 코드 생성 요청, 오류 디버깅, 리팩토링, 코드 리뷰, 보안 리뷰, Supabase/Redis 디버깅, 미니 서비스 종합 리뷰를 학습했습니다. 이 lab에서는 그 내용을 작은 실습으로 나누어 반복합니다.

## 진행 방법

각 lab은 다음 흐름으로 진행합니다.

1. README를 먼저 읽습니다.
2. 실습 대상 파일이 있으면 파일 내용을 확인합니다.
3. Codex에게 요청할 내용을 직접 작성합니다.
4. Codex 답변을 그대로 믿지 않고 요구사항과 비교합니다.
5. 필요한 경우 코드를 수정하거나 개선 방향을 정리합니다.
6. 실행 결과 또는 리뷰 결과를 짧게 기록합니다.

중요한 기준은 "Codex가 대신 해준 결과"가 아니라 "왜 그렇게 판단했는지 설명할 수 있는가"입니다.

## 실습 목록

| Lab | 폴더 | 핵심 내용 |
| --- | --- | --- |
| Lab 01 | `lab01_explain-code` | Python 코드 설명 요청 |
| Lab 02 | `lab02_generate-python-function` | 요구사항 기반 함수 생성 |
| Lab 03 | `lab03_debug-error-message` | 오류 메시지 디버깅 |
| Lab 04 | `lab04_refactor-script` | 동작을 유지한 리팩토링 |
| Lab 05 | `lab05_review-my-code` | 직접 작성한 코드 리뷰 |
| Lab 06 | `lab06_review-fastapi-supabase-code` | FastAPI/Supabase 코드 리뷰 |
| Lab 07 | `lab07_debug-env-and-api-key-error` | `.env`, API key, token 오류 디버깅 |
| Lab 08 | `lab08_review-mini-service` | 백엔드 미니 서비스 종합 리뷰 |
| Lab 09 | `lab09_security-and-cost-check` | 보안과 비용 체크리스트 적용 |

## 학습 흐름

Lab 01부터 Lab 04까지는 Codex를 개발 보조 도구로 사용하는 기본 흐름을 연습합니다.

- 코드를 설명하게 하기
- 요구사항을 주고 함수 생성하기
- 오류 메시지를 함께 분석하기
- 기존 동작을 유지하며 구조 개선하기

Lab 05부터 Lab 09까지는 실제 백엔드 과정과 연결됩니다.

- FastAPI endpoint 리뷰
- Pydantic 모델과 응답 형식 점검
- Supabase 테이블, 컬럼, 권한 확인
- Upstash Redis token, key, TTL 확인
- Gemini SDK 기본 사용 흐름, REST 보충 예제, OpenAI 선택 사용 흐름의 비용 위험 확인
- 미니 서비스 전체 흐름 리뷰

## 결과 정리 양식

각 lab을 마친 뒤에는 아래 형식으로 짧게 기록합니다.

```md
## Lab 결과

- 진행한 lab:
- 사용한 파일:
- Codex에게 요청한 내용:
- Codex가 찾은 문제 또는 제안:
- 직접 판단한 최종 수정 방향:
- 실행 또는 확인 결과:
- 아직 헷갈리는 부분:
```

이 기록은 나중에 최종 프로젝트를 점검할 때 좋은 참고 자료가 됩니다.
