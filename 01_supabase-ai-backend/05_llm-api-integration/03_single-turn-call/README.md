# 03. Single Turn Call

이전 대화 없이 현재 질문 하나만 모델에 보내고 응답을 받는 방식을 학습합니다.

## 예제 파일

```text
01_mock_single_turn.py
03_gemini_rest_single_turn.py
02_openai_single_turn.py
```

`01_mock_single_turn.py`는 비용 없이 실행됩니다.

`03_gemini_rest_single_turn.py`는 01~03 과정의 기본 실제 API 호출 예제입니다. `.env`에 `GEMINI_API_KEY`가 있을 때만 실제 호출합니다.

`02_openai_single_turn.py`는 선택/비교 실습용입니다. 기존 파일은 유지하며, `.env`에 `OPENAI_API_KEY`가 있을 때만 실제 호출합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\03_single-turn-call\01_mock_single_turn.py
python .\05_llm-api-integration\03_single-turn-call\03_gemini_rest_single_turn.py
```
