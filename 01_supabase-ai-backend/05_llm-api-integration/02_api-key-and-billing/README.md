# 02. API Key And Billing

Gemini API를 기본으로 key 발급, 무료 범위, 과금, 보안 관리 기준을 학습합니다. OpenAI API는 기존 예제 파일을 유지하되 선택/비교 실습으로 다룹니다.

## 실행 예제

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python.\05_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
python.\05_llm-api-integration\02_api-key-and-billing\02_safe_config_loader.py
```

이 예제는 실제 API를 호출하지 않습니다. `.env`에 key가 설정되어 있는지 여부만 확인합니다.

## 환경변수

```env
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

01~03 과정에서 실제 LLM 호출은 Gemini API를 먼저 사용합니다. Gemini 무료 범위와 호출 제한은 수업 시점의 공식 화면에서 확인합니다.

OpenAI API key는 필수가 아닙니다. OpenAI 예제를 실행하거나 모델별 응답 차이를 비교할 때만 설정합니다.

실제 key 값은 README나 과제 문서에 적지 않습니다.
