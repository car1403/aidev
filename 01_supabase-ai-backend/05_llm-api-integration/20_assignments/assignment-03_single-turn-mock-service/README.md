# Assignment 03. Single-turn mock LLM 서비스

사용자 질문 하나와 메모 컨텍스트 하나를 받아 mock LLM 응답을 만드는 과제입니다.

실제 API를 호출하지 않지만, 응답 구조는 실제 LLM API 연동 결과처럼 설계합니다.

## 제출 목표

- `build_prompt()` 함수로 메모와 질문을 프롬프트로 정리합니다.
- `call_mock_llm()` 함수로 mock 응답을 반환합니다.
- 응답에 `provider`, `model`, `actual_api_called`, `answer`, `usage`를 포함합니다.
- token 사용량은 정확한 계산이 아니라 추정값으로 표시합니다.

## 제출 파일

```text
main.py
README.md
```

## 실행 예시

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\20_assignments\assignment-03_single-turn-mock-service\main.py
```

## 완성 기준

1. 질문과 메모 컨텍스트가 모두 프롬프트에 반영됩니다.
2. 실제 API 호출 없이 응답을 반환합니다.
3. 출력 결과가 이후 FastAPI 응답 구조로 옮기기 쉬운 딕셔너리 형태입니다.
