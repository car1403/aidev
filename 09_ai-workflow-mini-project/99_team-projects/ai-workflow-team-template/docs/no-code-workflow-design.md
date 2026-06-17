# No-Code Workflow Design

이 문서는 팀 프로젝트의 노코드 워크플로우 설계서입니다.

작성 목표는 “도구 화면을 만들었다”가 아니라, 기술 지원 자동화 업무가 어떤 Trigger로 시작되고, 어떤 노드를 거쳐, 어떤 결과로 끝나는지 명확히 설명하는 것입니다.

## 1. 워크플로우 개요

| 항목 | 내용 |
| --- | --- |
| 워크플로우 이름 |  |
| 해결하려는 기술 지원 문제 |  |
| 주요 사용자 |  |
| 사용 도구 | AIPP / n8n / Dify / FastAPI / Streamlit / 기타 |
| 최종 출력 | 답변 생성 / 티켓 생성 / 담당자 알림 / 로그 저장 / 기타 |

## 2. 전체 흐름

아래 형식으로 Trigger -> 처리 -> 출력 흐름을 작성합니다.

```text
Trigger:
  사용자가 기술 지원 문의를 제출한다.

처리:
  1. 문의 내용을 분류한다.
  2. 필요한 문서를 검색한다.
  3. 답변 초안을 생성한다.
  4. 긴급도를 판단한다.
  5. 담당자 알림 또는 티켓 생성을 수행한다.

출력:
  사용자에게 답변을 제공하고, 실행 로그를 저장한다.
```

## 3. 노드 목록

| 노드명 | 역할 | 입력 | 출력 | 사용 도구 |
| --- | --- | --- | --- | --- |
| Trigger Node | 문의 접수 | 사용자 입력 | ticket_payload | Webhook/Form |
| Classifier Node | 문의 유형 분류 | ticket_payload | category_result | LLM |
| RAG Search Node | 관련 문서 검색 | query | retrieved_docs | Dify Knowledge / Vector DB |
| Response Node | 답변 초안 생성 | category_result, retrieved_docs | draft_answer | LLM |
| Notify Node | 담당자 알림 | final_result | notification_result | Slack/Email/Jira |

## 4. 제어 구조

워크플로우에 사용하는 제어 구조를 표시합니다.

| 구조 | 사용 여부 | 사용 이유 |
| --- | --- | --- |
| 조건 분기 | 예 / 아니오 |  |
| 반복 처리 | 예 / 아니오 |  |
| 병렬 처리 | 예 / 아니오 |  |
| 수동 승인 | 예 / 아니오 |  |

예시:

```text
긴급도가 높으면 Slack 알림과 Jira 티켓 생성을 병렬로 실행한다.
긴급도가 낮으면 사용자에게 FAQ 기반 답변만 제공한다.
```

## 5. 외부 서비스 연동

| 서비스 | 연동 목적 | 인증 방식 | 실패 시 처리 |
| --- | --- | --- | --- |
| Slack | 긴급 문의 알림 | Webhook URL | 재시도 후 실패 로그 저장 |
| Email | 사용자 답변 발송 | SMTP/OAuth | 담당자 확인 필요 표시 |
| Jira | 티켓 생성 | API Key/OAuth | 수동 티켓 생성 안내 |
| Notion | 처리 이력 저장 | API Key | 로컬 로그에 임시 저장 |
| Database | 실행 로그 저장 | DB URL/계정 | 파일 로그 fallback |

API Key와 OAuth Client Secret은 문서에 직접 적지 않습니다. 문서에는 “어떤 인증 방식이 필요한지”만 작성합니다.

### 5.1 외부 서비스 연동 점검

이미지 기준 산출물에서는 외부 서비스 연동 노드가 안정적으로 설계되었는지를 중요하게 봅니다.
아래 항목을 서비스별로 작성합니다.

| 점검 항목 | 작성 내용 |
| --- | --- |
| 인증 방식 | OAuth / API Key / Webhook Secret / 기타 |
| 인증 정보 보관 위치 | `.env`, 도구의 Secret Manager, 테스트 계정 등 |
| 성공 응답 기준 | HTTP 200/201, 응답 JSON 필드, 화면 상태 등 |
| 실패 응답 기준 | 401/403, 404, 429, 5xx, timeout 등 |
| 재시도 기준 | 몇 번 재시도할지, 몇 초 뒤 다시 시도할지 |
| fallback | Slack 실패 시 Email, Jira 실패 시 수동 등록 안내 등 |

## 6. Payload 스키마

노드 간 전달되는 데이터 구조를 작성합니다.

### 6.1 입력 payload

```json
{
  "ticket_id": "TCK-001",
  "user_id": "user-123",
  "channel": "web",
  "message": "VPN 접속이 되지 않습니다.",
  "created_at": "2026-06-15T09:00:00+09:00"
}
```

### 6.2 처리 결과 payload

```json
{
  "ticket_id": "TCK-001",
  "category": "network",
  "priority": "high",
  "retrieved_docs": ["vpn-guide-01", "vpn-error-03"],
  "draft_answer": "VPN 클라이언트 재설치와 OTP 상태를 확인해 주세요.",
  "next_action": "notify_operator"
}
```

## 7. 필드 정의

| 필드명 | 타입 | 필수 여부 | 설명 | 예시 |
| --- | --- | --- | --- | --- |
| ticket_id | string | 필수 | 문의 식별자 | TCK-001 |
| user_id | string | 필수 | 사용자 식별자 | user-123 |
| message | string | 필수 | 사용자 문의 내용 | VPN 접속이 되지 않습니다. |
| category | string | 선택 | 문의 분류 결과 | network |
| priority | string | 선택 | 긴급도 | high |
| next_action | string | 선택 | 다음 처리 방식 | notify_operator |

## 8. Mapper와 Formatter

노드 사이에서 데이터 형식이 바뀌는 경우 작성합니다.

| 구간 | 변환 전 | 변환 후 | 변환 이유 |
| --- | --- | --- | --- |
| Form -> LLM | message | prompt_input | LLM 입력 형식에 맞추기 위해 |
| RAG -> Response | retrieved_docs | context | 검색 결과를 답변 생성 context로 사용하기 위해 |
| Response -> Slack | final_result | slack_message | Slack 메시지 형식에 맞추기 위해 |

### 8.1 Edge별 payload 계약

노코드 도구에서는 노드와 노드 사이의 연결선을 edge라고 볼 수 있습니다.
각 edge마다 어떤 데이터가 넘어가는지 작성하면 오류를 줄일 수 있습니다.

| Edge | 전달 payload | 필수 필드 | 선택 필드 | 예시 |
| --- | --- | --- | --- | --- |
| Trigger -> Classifier | ticket_payload | ticket_id, message | channel, user_id | VPN 오류 문의 |
| Classifier -> RAG Search | search_payload | ticket_id, category, query | priority | network 문의 검색 |
| RAG Search -> Response | context_payload | ticket_id, retrieved_docs | score, source | VPN 매뉴얼 2건 |
| Response -> Notify | notification_payload | ticket_id, final_answer, priority | assignee | Slack 알림 |

## 9. 오류 처리

| 오류 상황 | 감지 기준 | 처리 방식 |
| --- | --- | --- |
| 입력값 누락 | message가 비어 있음 | 사용자에게 다시 입력 요청 |
| 인증 실패 | 401/403 응답 | 관리자에게 설정 확인 요청 |
| API 실패 | 5xx 응답 | 2회 재시도 후 fallback |
| 검색 결과 없음 | retrieved_docs가 빈 배열 | 일반 안내 답변 생성 |
| 알림 실패 | Slack API 실패 | Email로 대체 발송 |

## 10. 최종 점검

- Trigger -> 처리 -> 출력 흐름이 명확한가?
- 각 노드의 입력과 출력이 작성되어 있는가?
- 외부 서비스 인증 방식이 설명되어 있는가?
- 실패 상황과 대체 흐름이 포함되어 있는가?
- payload 예시가 실제 테스트에 사용할 수 있을 정도로 구체적인가?
- Mapper/Formatter 같은 데이터 변환 기준이 작성되어 있는가?
- 각 edge별 필수/선택 필드가 정리되어 있는가?
