# 02_api-key-and-billing

이 단원에서는 LLM API를 사용하기 전에 필요한 **API key**, **환경변수**, **비용/결제 주의사항**, **보안 관리 기준**을 학습합니다.

`11_llm-api-concepts`에서는 실제 API 호출 없이 message 구조와 파라미터 개념을 보았습니다. 이번 단원에서도 실제 API 호출은 하지 않고, `.env`에 key가 있는지 안전하게 확인하는 단계까지만 진행합니다.

## 핵심 요약

```text
API key
  코드가 LLM 서비스를 호출할 수 있도록 발급받는 비밀 키입니다.

.env
  API key처럼 공개되면 안 되는 값을 저장하는 로컬 설정 파일입니다.

환경변수
  Python 코드에서 os.getenv(...)로 읽어오는 설정 값입니다.

Billing
  실제 API를 호출했을 때 사용량에 따라 비용이 발생할 수 있는 과금 체계입니다.

무료 범위
  provider가 제공할 수 있는 무료 사용량입니다. 시점과 계정 상태에 따라 달라질 수 있으므로 공식 화면에서 확인합니다.
```

## 이 과정의 LLM 사용 기준

```text
Gemini
  11~13 과정의 기본 LLM 실습 provider입니다.
  기본 모델 예시는 gemini-2.5-flash-lite를 사용합니다.

OpenAI
  선택/비교 실습 provider입니다.
  기존 OpenAI 예제 파일은 유지하지만 필수는 아닙니다.
  기본 모델 예시는 gpt-4.1-mini를 사용합니다.
```

중요한 점은 **ChatGPT/Codex 앱 사용 결제와 OpenAI API 사용 결제는 별개**라는 것입니다. 앱에서 결제했더라도 API 호출 비용이 자동으로 포함되는 것이 아닐 수 있으므로, API 사용 전 OpenAI 플랫폼의 Billing 화면을 별도로 확인해야 합니다.

## 폴더 파일

| 파일 | 역할 |
| --- | --- |
| `main.py` | Gemini/OpenAI key 설정 상태와 안전 체크리스트를 한 번에 확인 |
| `11_check_llm_env.py` | `.env`에서 LLM 관련 환경변수 설정 여부 확인 |
| `12_safe_config_loader.py` | 실제 key를 출력하지 않고 설정 객체로 안전하게 읽는 예제 |

## 실행 준비

가상환경은 `02_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

## 통합 예제 실행

```powershell
python .\02_llm-api-integration\02_api-key-and-billing\main.py
```

이 예제는 실제 Gemini 또는 OpenAI API를 호출하지 않습니다. `.env`에 key가 있는지 여부만 확인하므로 비용이 발생하지 않습니다.

## 1. API key는 왜 필요한가요?

LLM API는 누구나 무제한으로 호출할 수 있는 공개 함수가 아닙니다. provider는 API key를 통해 다음을 확인합니다.

```text
1. 누가 API를 호출하는지
2. 어떤 프로젝트에서 호출하는지
3. 얼마나 사용했는지
4. 비용을 어떤 계정에 연결할지
5. 호출 제한을 어떻게 적용할지
```

그래서 API key는 비밀번호처럼 다루어야 합니다.

## 2. Gemini API key 준비 흐름

Gemini API key는 Google AI Studio 또는 Google Cloud의 관련 화면에서 발급받을 수 있습니다.

공식 확인 위치:

```text
Google AI Studio:
  https://aistudio.google.com/

Gemini API 문서:
  https://ai.google.dev/gemini-api/docs

Gemini API 가격/제한 확인:
  https://ai.google.dev/pricing
```

진행 흐름:

```text
1. Google 계정으로 Google AI Studio에 접속합니다.
2. API key 생성 메뉴를 찾습니다.
3. 새 API key를 생성합니다.
4. 복사한 key를 코드에 직접 붙여 넣지 않습니다.
5. C:\aidev\02_supabase-ai-backend\.env 파일에 저장합니다.
```

## 3. OpenAI API key 준비 흐름

OpenAI API는 선택/비교 실습에서 사용합니다.

공식 확인 위치:

```text
OpenAI Platform:
  https://platform.openai.com/

OpenAI API keys:
  https://platform.openai.com/api-keys

OpenAI Billing:
  https://platform.openai.com/settings/organization/billing

OpenAI Pricing:
  https://openai.com/api/pricing/
```

주의할 점:

```text
ChatGPT/Codex 앱 결제:
  앱에서 ChatGPT 또는 Codex를 사용하는 결제입니다.

OpenAI API 결제:
  Python 코드나 서버에서 OpenAI API를 호출할 때의 별도 결제입니다.

따라서 앱 결제가 되어 있어도 API key 사용량과 결제는 별도로 확인해야 합니다.
```

## 4. .env 파일 작성

`C:\aidev\02_supabase-ai-backend\.env` 파일에 아래 형식으로 작성합니다.

```env
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

OpenAI API를 사용하지 않을 경우 `OPENAI_API_KEY`는 비워 두어도 됩니다.

```env
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
```

`your-gemini-api-key`, `your-openai-api-key`처럼 예시로 적어 둔 값은 실제 key가 아닙니다. 이 단원의 확인 스크립트는 이런 placeholder 값을 “설정 안 됨”으로 처리합니다.

## 5. .gitignore 확인

`.env` 파일은 GitHub에 올라가면 안 됩니다.

`C:\aidev\02_supabase-ai-backend\.gitignore` 또는 상위 `.gitignore`에 아래 항목이 있는지 확인합니다.

```gitignore
.env
.venv/
__pycache__/
```

`.env`가 GitHub에 올라가면 API key가 유출될 수 있습니다. key가 유출되면 즉시 삭제하거나 재발급해야 합니다.

## 6. 환경변수 확인 예제

```powershell
python .\02_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
```

출력 예시:

```text
GEMINI_API_KEY: abcd...1234
GEMINI_MODEL: gemini-2.5-flash-lite
OPENAI_API_KEY: 없음
OPENAI_MODEL: gpt-4.1-mini
```

실제 key 전체를 출력하지 않고 앞뒤 일부만 보여줍니다.

## 7. 안전한 설정 로더 예제

```powershell
python .\02_llm-api-integration\02_api-key-and-billing\02_safe_config_loader.py
```

이 예제는 provider별 설정 상태를 객체로 정리합니다.

```text
provider='gemini'
model='gemini-2.5-flash-lite'
has_api_key=True 또는 False
```

중요한 점은 실제 key 값을 객체에 직접 출력하지 않는다는 것입니다.

## 8. 실제 API 호출 전 체크리스트

실제 Gemini 또는 OpenAI API를 호출하기 전에 아래를 확인합니다.

```text
1. .env에 key를 저장했는가?
2. key를 코드나 README에 직접 적지 않았는가?
3. .env가 .gitignore에 포함되어 있는가?
4. 공식 가격/무료 범위/호출 제한 화면을 확인했는가?
5. max_tokens 또는 maxOutputTokens를 너무 크게 잡지 않았는가?
6. 반복문 안에서 실제 API를 무제한 호출하지 않는가?
7. 오류 발생 시 재시도 횟수를 제한했는가?
8. 화면 공유 중 API key가 보이지 않는가?
```

## 9. 비용을 줄이는 기본 습관

```text
1. 처음에는 mock 예제로 구조를 확인합니다.
2. 실제 API 호출은 작은 입력과 짧은 출력부터 시작합니다.
3. 같은 질문을 반복 호출하지 않도록 합니다.
4. 테스트 중에는 max_tokens 또는 maxOutputTokens를 작게 둡니다.
5. 반복문, 배치 처리, 자동 재시도 코드를 조심합니다.
6. 사용량 대시보드를 자주 확인합니다.
```

## 이후 단원과의 연결

```text
13_single-turn-call:
  Gemini API key가 있으면 실제 단일 질문 호출을 실행합니다.

14_multi-turn-call:
  이전 대화 이력을 포함한 메시지 구조를 실습합니다.

15_fastapi-llm-endpoint:
  FastAPI endpoint에서 key를 읽고 LLM API를 호출합니다.

14_supabase-ai-mini-project:
  사용자별 대화 이력, 응답 저장, SSE 스트리밍 흐름과 연결합니다.
```

## 확인 질문

```text
1. API key를 코드에 직접 적으면 왜 위험한가요?
2. .env와 .gitignore는 각각 어떤 역할을 하나요?
3. Gemini API와 OpenAI API를 이 과정에서 어떻게 구분해서 사용하나요?
4. ChatGPT/Codex 앱 결제와 OpenAI API 결제는 왜 별도로 봐야 하나요?
5. 실제 API 호출 전에 비용을 줄이기 위해 어떤 습관이 필요한가요?
```
