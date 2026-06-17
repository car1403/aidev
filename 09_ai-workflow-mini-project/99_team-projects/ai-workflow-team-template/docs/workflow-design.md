# Workflow Design

이 문서는 팀 프로젝트의 AI 워크플로우 설계 문서입니다.

AIPP, n8n, Dify 중 어떤 도구를 선택하더라도 아래 항목을 먼저 정리하면 프로젝트 흐름을 명확하게 설명할 수 있습니다.

## 1. 업무 시나리오

자동화하려는 업무를 한 문장으로 작성합니다.

```text
예시:
사용자가 기술지원 문의를 입력하면 문의 유형과 긴급도를 판단하고, 관련 문서를 참고해 답변 초안을 생성한다.
```

우리 팀 시나리오:

```text

```

## 2. 사용자

이 워크플로우를 사용하는 사람을 작성합니다.

```text
예시:
사내 직원
고객지원 담당자
운영팀
관리자
```

## 3. Trigger

워크플로우가 시작되는 이벤트를 작성합니다.

```text
예시:
사용자가 웹 화면에서 문의를 제출한다.
n8n Webhook으로 문의 데이터가 들어온다.
AIPP 워크플로우 실행 버튼을 누른다.
Dify Chatflow에 사용자가 질문을 입력한다.
```

우리 팀 Trigger:

```text

```

## 4. Input

입력 데이터 항목을 작성합니다.

```text
user_id:
message:
channel:
priority:
created_at:
```

## 5. Condition

분기 조건을 작성합니다.

```text
예시:
message에 "급함", "장애", "로그인 실패"가 포함되면 긴급 문의로 분류한다.
문서 검색 결과가 없으면 담당자 검토로 보낸다.
AI 응답 신뢰도가 낮으면 fallback 답변을 제공한다.
```

## 6. LLM 또는 AI 역할

AI가 담당하는 일을 작성합니다.

```text
문의 유형 분류:
긴급도 판단:
답변 초안 생성:
문서 기반 답변 생성:
응답 품질 검토:
```

## 7. Tool/API/Knowledge 역할

외부 도구, API, Knowledge/RAG가 담당하는 일을 작성합니다.

```text
Dify Knowledge에서 관련 문서를 검색한다.
n8n HTTP Request로 FastAPI 분석 API를 호출한다.
AIPP Tool 노드로 외부 시스템 조회를 수행한다.
FastAPI에서 문의 분류 로직을 실행한다.
```

## 8. RAG/Data Node 설계

RAG, Knowledge, 데이터 처리 노드를 사용하는 경우 작성합니다.

```text
검색 대상 문서:
검색 키워드 생성 방식:
전처리 방식:
데이터 변환 방식:
후처리 방식:
검색 결과가 없을 때 처리:
```

## 9. 노드 간 데이터 흐름

각 노드가 어떤 데이터를 주고받는지 작성합니다.

```text
사용자 입력
-> 입력 검증
-> 문의 분류
-> 검색어 변환
-> RAG/Knowledge 검색
-> LLM 답변 생성
-> 출력 검증
-> 사용자 응답 또는 담당자 알림
```

입력/출력 계약:

| 노드 | 입력 | 출력 |
| --- | --- | --- |
| 입력 검증 | user_id, message | is_valid, clean_message |
| 문의 분류 | clean_message | category, priority |
| 검색 | search_query | documents |
| 답변 생성 | clean_message, documents | draft_answer |
| 출력 검증 | draft_answer | final_answer, status |

## 10. Loop, Fork-Join, 집계

반복 처리나 병렬 처리가 필요한 경우 작성합니다.

```text
반복 처리할 대상:
병렬로 실행할 작업:
결과를 합치는 기준:
실패한 항목 처리 방식:
```

필요하지 않다면 아래처럼 이유를 작성합니다.

```text
이번 프로젝트는 단일 문의를 처리하는 구조이므로 Loop/Fork-Join은 적용하지 않는다.
향후 여러 문의를 일괄 처리할 때 적용할 수 있다.
```

## 11. Action

실제로 실행되는 작업을 작성합니다.

```text
답변 초안 생성
운영팀 알림
티켓 생성
로그 저장
사용자에게 처리 안내 반환
```

## 12. Output

최종 출력 형식을 작성합니다.

```json
{
  "category": "login",
  "priority": "high",
  "answer": "먼저 비밀번호 만료 여부와 계정 잠금 상태를 확인해 주세요.",
  "next_action": "notify_ops"
}
```

## 13. Log

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
api_calls
estimated_cost
```

## 14. Fallback

오류나 불확실한 결과가 나왔을 때의 대체 흐름을 작성합니다.

```text
AI 응답 신뢰도가 낮으면 담당자 검토로 보낸다.
Dify API 호출이 실패하면 기본 FAQ 답변을 반환한다.
n8n HTTP Request가 실패하면 재시도 후 실패 로그를 남긴다.
입력값이 너무 짧으면 추가 정보를 요청한다.
```

## 15. 선택 도구

사용할 도구를 체크합니다.

```text
[ ] AIPP
[ ] n8n
[ ] Dify
[ ] FastAPI
[ ] Streamlit
```

선택 이유:

```text
도구:
이유:
```

## 16. Multi-Agent Workflow 적용 여부

여러 Agent가 필요한지 판단합니다.

```text
[ ] 단일 Agent 구조
[ ] Multi-Agent 구조
```

Multi-Agent를 적용한다면 역할을 작성합니다.

| Agent | 역할 | 입력 | 출력 |
| --- | --- | --- | --- |
| Classifier Agent | 문의 분류 | message | category, priority |
| RAG Agent | 문서 검색 | query | documents |
| Answer Agent | 답변 생성 | message, documents | draft_answer |
| Review Agent | 품질/보안 검토 | draft_answer | final_answer |
