# 02_ch2_policy-based-response-validation

정책 기반 응답 검증은 Agent가 만든 응답이 서비스 운영 정책에 맞는지 확인하는 과정입니다.

## 왜 필요한가?

LLM 또는 Agent가 만든 응답은 항상 그대로 사용자에게 보여주면 안 됩니다.

예를 들어 운영 서비스에서는 다음을 막아야 합니다.

- 민감 정보 노출
- 승인 없는 삭제/재시작 안내
- 과도하게 확정적인 장애 원인 단정
- 위험한 명령어 직접 실행 유도

## 기본 흐름

```text
Agent 응답 생성
-> 정책 검증
-> 허용/수정/차단 결정
-> 사용자에게 전달
```

## 실행

```powershell
python .\02_ch2_policy-based-response-validation\01_policy-response-validator.py
```
