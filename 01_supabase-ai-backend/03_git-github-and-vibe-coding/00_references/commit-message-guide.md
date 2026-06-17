# Commit Message Guide

커밋 메시지는 변경 내용을 짧게 설명하는 문장입니다.

좋은 커밋 메시지는 나중에 코드를 다시 볼 때 큰 도움이 됩니다.

## 기본 형식

```text
type: short summary
```

예시:

```text
docs: add beginner Git guide
feat: add Upstash Redis practice
fix: correct FastAPI setup path
refactor: split API helper function
test: add Supabase CRUD check
```

## 자주 쓰는 type

| type | 의미 |
| --- | --- |
| `docs` | 문서 수정 |
| `feat` | 새 기능 추가 |
| `fix` | 오류 수정 |
| `refactor` | 동작은 같지만 코드 구조 개선 |
| `test` | 테스트 추가 또는 수정 |
| `chore` | 설정, 정리, 기타 작업 |

## 좋은 메시지와 아쉬운 메시지

| 아쉬운 예 | 이유 |
| --- | --- |
| `수정` | 무엇을 수정했는지 알 수 없습니다. |
| `update` | 변경 범위가 너무 모호합니다. |
| `final` | 나중에 의미를 알기 어렵습니다. |

| 좋은 예 | 이유 |
| --- | --- |
| `docs: add Supabase setup steps` | 문서 수정이며 내용이 명확합니다. |
| `fix: correct backend API path` | 어떤 오류를 고쳤는지 알 수 있습니다. |
| `feat: add Redis rate limit example` | 새 예제가 추가되었음을 알 수 있습니다. |

## Codex에게 요청하는 예시

```text
아래 git diff를 보고 커밋 메시지 후보를 5개 작성해 주세요.
초보자가 이해하기 쉬운 메시지와 실제 프로젝트에서 쓰기 좋은 메시지를 나누어 주세요.
```

