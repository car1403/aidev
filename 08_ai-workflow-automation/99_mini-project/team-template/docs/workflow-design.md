# Workflow Design

팀 프로젝트의 워크플로우 설계 문서입니다.

각 항목을 비워 두지 말고, 수업에서 다룬 AIPP, n8n, Dify 관점으로 구체적으로 작성합니다.

## 1. 업무 시나리오

예시:

```text
사용자가 기술 지원 문의를 입력하면 문의 유형과 긴급도를 판단하고, 관련 문서를 참고해 답변 초안을 생성한다.
```

## 2. Trigger

워크플로우가 시작되는 이벤트를 작성합니다.

예시:

```text
사용자가 웹 폼으로 문의를 제출한다.
n8n Webhook으로 문의 데이터가 들어온다.
AIPP 워크플로우 실행 버튼을 누른다.
```

## 3. Input

입력 데이터 항목을 작성합니다.

```text
user_id:
message:
channel:
priority:
created_at:
```

## 4. Condition

분기 조건을 작성합니다.

```text
message에 "장애", "급함", "로그인 실패"가 포함되면 긴급 문의로 분류한다.
그 외에는 일반 문의로 분류한다.
```

## 5. LLM 또는 AI 역할

AI가 담당할 일을 작성합니다.

```text
문의 유형 분류
긴급도 판단
답변 초안 생성
응답 품질 검토
```

## 6. Tool/API/Knowledge 역할

외부 도구, API, Knowledge/RAG가 담당할 일을 작성합니다.

```text
Dify Knowledge에서 관련 문서를 검색한다.
n8n HTTP Request로 Dify API를 호출한다.
AIPP Tool 노드로 외부 시스템 조회를 수행한다.
```

## 7. Action

실제로 실행되는 작업을 작성합니다.

```text
답변 후보 생성
운영팀 알림
티켓 생성
로그 저장
```

## 8. Output

최종 출력 형태를 작성합니다.

```json
{
 "category": "login",
 "priority": "high",
 "answer": "먼저 비밀번호 만료 여부와 계정 잠금 상태를 확인해 주세요.",
 "next_action": "notify_ops"
}
```

## 9. Log

실행 후 남길 로그 항목을 작성합니다.

```text
request_id
input_message
category
priority
selected_tool
success
error_message
created_at
```

## 10. Fallback

오류나 불확실한 결과가 나왔을 때의 대체 흐름을 작성합니다.

```text
AI 답변 신뢰도가 낮으면 사람 검토로 보낸다.
Dify API 호출이 실패하면 기본 FAQ 답변을 반환한다.
n8n HTTP Request가 실패하면 재시도 후 실패 로그를 남긴다.
```

## 11. 선택 도구

사용할 도구를 체크합니다.

```text
[ ] AIPP
[ ] n8n
[ ] Dify
```

선택 이유:

```text
도구:
이유:
```
