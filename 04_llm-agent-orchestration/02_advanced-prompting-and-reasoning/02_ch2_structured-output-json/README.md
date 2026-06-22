# 02_ch2_structured-output-json

이 챕터에서는 LLM 응답을 JSON과 Pydantic 구조로 안정화하는 방법을 학습합니다.

## 핵심 개념

- 자유 문장 응답은 프로그램에서 처리하기 어렵습니다.
- JSON 응답은 필드 이름과 값의 구조를 맞추는 데 유리합니다.
- Pydantic은 응답 데이터의 타입과 필수 필드를 검증합니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\02_advanced-prompting-and-reasoning
.\.venv\Scripts\Activate.ps1
python.\02_ch2_structured-output-json\01_json-output-request.py
python.\02_ch2_structured-output-json\02_structured-output-pydantic.py
```

## 확인 질문

- JSON 형식 응답이 필요한 이유는 무엇인가요?
- Pydantic 검증이 없으면 어떤 문제가 생길 수 있나요?

