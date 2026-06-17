# Lab 07. Guardrails AI Integrated Validation

## 목표

Guardrails AI 같은 검증 도구를 AI 서비스의 입력, 출력, Tool 실행 전후에 어떻게 배치할지 설계합니다.

이 실습은 특정 라이브러리 사용법을 외우는 시간이 아니라, Guardrail을 서비스 구조 어디에 넣어야 하는지 이해하는 것이 목표입니다.

## Guardrail 적용 위치

```text
사용자 입력
-> 입력 검증 Guardrail
-> Agent 실행
-> Tool 실행 권한 검증
-> LLM 응답 생성
-> 출력 검증 Guardrail
-> 정책 위반 로그
-> 최종 응답
```

## 검증할 수 있는 항목

```text
입력 길이
금지어 또는 위험 문구
Prompt Injection 패턴
개인정보 포함 여부
JSON 출력 형식
정책 위반 응답
Tool 실행 권한
민감 정보 노출
```

## 통합 설계 예시

```text
Input Guardrail:
  - prompt injection 문구 탐지
  - 개인정보 포함 여부 확인

Tool Guardrail:
  - Agent 역할별 허용 Tool 확인
  - 위험 Tool 실행 전 승인 필요

Output Guardrail:
  - 응답에 API Key, 비밀번호, 개인정보 포함 여부 확인
  - JSON Schema 형식 검증
  - 정책 위반 시 fallback 응답 반환
```

## 팀 프로젝트 적용 양식

```text
프로젝트 이름:
입력 검증 기준:
Tool 권한 검증 기준:
출력 검증 기준:
정책 위반 시 응답:
로그에 남길 정보:
사람 검토로 넘길 조건:
```

## 선택 구현 방향

초보자 실습에서는 먼저 규칙 기반 Python 코드로 Guardrail을 구현합니다.

```text
if 위험 입력:
    block
elif 민감 정보 포함:
    redact
else:
    allow
```

이후 실제 Guardrails AI 또는 유사 검증 도구를 붙일 때는 같은 기준을 라이브러리 설정이나 Validator로 옮깁니다.

## 확인 질문

- Guardrail은 입력에만 적용하면 충분한가?
- Tool 실행 전 Guardrail이 필요한 이유는 무엇인가?
- 정책 위반 시 무조건 차단해야 하는가, 수정 후 응답할 수도 있는가?
