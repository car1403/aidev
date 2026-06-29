# 03_single-turn-call

이 폴더는 한 번의 사용자 입력에 대해 한 번의 LLM 응답을 받는 single-turn 호출 예제를 다룹니다.

## 실행 흐름

```powershell
cd C:/aidev/02_supabase-ai-backend
./.venv/Scripts/Activate.ps1
cd ./02_llm-api-integration/03_single-turn-call
python ./01_mock_single_turn.py
```

Mock 예제가 정상 동작한 뒤 Gemini SDK 예제와 REST 보충 예제를 확인합니다. OpenAI 예제는 선택/비교 실습입니다.

## Gemini 503 UNAVAILABLE 오류

실제 Gemini API를 호출할 때 아래와 같은 오류가 날 수 있습니다.

```text
503 UNAVAILABLE
This model is currently experiencing high demand.
```

이 오류는 Python 코드 문법 오류가 아니라 Gemini API 서버가 일시적으로 바쁘거나 해당 모델 수요가 높은 상태라는 뜻입니다.

이럴 때는 아래 순서로 확인합니다.

```text
1. 잠시 뒤 같은 명령을 다시 실행합니다.
2. .env의 GEMINI_MODEL 값이 현재 사용 가능한 모델인지 확인합니다.
3. Google AI Studio에서 quota, rate limit, billing 상태를 확인합니다.
4. 수업 흐름을 계속 진행해야 하면 01_mock_single_turn.py로 구조를 먼저 복습합니다.
```

가상환경을 활성화한 뒤에는 `py`보다 `python` 명령을 사용하는 것을 권장합니다. 그래야 현재 `.venv`의 Python을 사용하는지 확인하기 쉽습니다.

```powershell
python -c "import sys; print(sys.executable)"
python .\02_llm-api-integration\03_single-turn-call\02_gemini_sdk_single_turn.py
```
