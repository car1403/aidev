# 04. Multi Turn Call

이전 대화 이력을 함께 보내 문맥을 유지하는 멀티턴 호출 방식을 학습합니다.

## 예제 파일

```text
01_mock_multi_turn.py
02_conversation_memory.py
04_gemini_rest_multi_turn.py
03_openai_multi_turn.py
```

멀티턴은 모델이 자동으로 기억하는 것이 아니라, 이전 대화를 우리가 messages 목록에 다시 넣어 보내는 구조입니다.

01~03 과정에서는 `04_gemini_rest_multi_turn.py`를 기본 실제 API 호출 예제로 사용합니다. `03_openai_multi_turn.py`는 선택/비교 실습용으로 그대로 유지합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\04_multi-turn-call\01_mock_multi_turn.py
python .\05_llm-api-integration\04_multi-turn-call\04_gemini_rest_multi_turn.py
```
