# Guardrails Validation

입력, Tool 실행, 출력 단계의 Guardrail 검증 기준을 작성합니다.

## 1. Guardrail 적용 위치

```text
사용자 입력
-> Input Guardrail
-> Agent 실행
-> Tool Permission Guardrail
-> LLM 또는 복구 결과 생성
-> Output Guardrail
-> Audit Log
-> 최종 응답
```

## 2. 입력 검증

```text
최소 입력 길이:
Prompt Injection 탐지 기준:
민감 정보 포함 여부:
금지 명령어:
```

## 3. Tool 실행 검증

```text
Agent 역할:
요청 Tool:
허용 여부:
승인 필요 여부:
차단 사유:
```

## 4. 출력 검증

```text
민감 정보 포함 여부:
정책 위반 응답 여부:
JSON 형식 검증:
운영자에게 보여줄 수 있는 표현인지:
```

## 5. 정책 위반 시 응답

```text
사용자에게 반환할 메시지:
운영 로그에 남길 내용:
사람 검토로 넘길 조건:
```
