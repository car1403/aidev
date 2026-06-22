# 10_labs

LLM API key 확인, 싱글턴 호출, 멀티턴 호출, FastAPI endpoint 연동을 수업 중 실습합니다.

## 실습 순서

```text
Lab 01 - 환경변수 확인
Lab 02 - mock 싱글턴 호출
Lab 03 - mock 멀티턴 호출
Lab 04 - FastAPI mock LLM endpoint
Lab 05 - 실제 API 호출 전 보안/비용 체크
```

## 실행 명령

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
python .\05_llm-api-integration\03_single-turn-call\01_mock_single_turn.py
python .\05_llm-api-integration\04_multi-turn-call\01_mock_multi_turn.py
```

FastAPI endpoint:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload
```

## 수업 기준

실제 Gemini API 호출은 진행자가 무료 범위, 호출 제한, key 설정을 확인한 뒤 진행합니다. OpenAI API 호출은 선택/비교 실습으로 진행할 때만 별도로 확인합니다.
