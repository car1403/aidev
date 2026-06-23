# 00_references

이 폴더는 Codex를 활용한 코드 설명, 생성, 디버깅, 리팩토링, 코드 리뷰, 보안 점검을 진행할 때 참고하는 보조 문서 모음입니다.

각 문서는 바로 복사해서 사용할 수 있는 요청 템플릿과 체크리스트를 제공합니다. 실제 key나 token은 어떤 템플릿에도 넣지 않습니다.

## 문서 목록

| 문서 | 용도 |
| --- | --- |
| `prompt-patterns.md` | Codex 요청문을 구조화하는 기본 패턴 |
| `codex-checklist.md` | 요청 전, 응답 확인, 오류 발생, 제출 전 체크리스트 |
| `debugging-template.md` | Python, FastAPI, Supabase, Redis 오류 분석 요청 템플릿 |
| `review-template.md` | 일반 코드 리뷰와 백엔드 코드 리뷰 요청 템플릿 |
| `learning-rules.md` | AI 보조 개발을 사용할 때의 기본 규칙 |
| `backend-review-checklist.md` | FastAPI, Supabase, LLM API, Upstash Redis 코드 리뷰 체크리스트 |
| `security-cost-checklist.md` | API key, token, 비용, 로그 보안 점검 체크리스트 |
| `ai-tool-selection-guide.md` | Codex와 다른 AI 도구를 목적에 맞게 선택하는 기준 |

## 활용 순서

1. 먼저 `prompt-patterns.md`에서 요청문 구조를 확인합니다.
2. 오류가 발생했다면 `debugging-template.md`를 사용합니다.
3. 코드 리뷰가 필요하다면 `review-template.md`와 `backend-review-checklist.md`를 함께 봅니다.
4. API key, Supabase key, Redis token, 비용 위험을 점검할 때는 `security-cost-checklist.md`를 사용합니다.
5. 최종 제출 전에는 `codex-checklist.md`를 기준으로 직접 확인합니다.
