# 03_single-turn-call

이 단원에서는 **싱글턴 LLM 호출**을 학습합니다.

싱글턴 호출은 이전 대화 이력을 포함하지 않고, 현재 질문 하나만 LLM에 보내 응답 하나를 받는 방식입니다. 처음부터 복잡한 대화 이력이나 데이터베이스 저장까지 연결하지 않고, "질문 1개 -> 모델 호출 -> 응답 1개"의 흐름을 먼저 이해합니다.

## 이번 단원의 핵심 방향

Gemini 실제 호출은 두 가지 방식으로 볼 수 있습니다.

```text
1. SDK 방식
   google-genai 패키지를 사용합니다.
   코드가 짧고 읽기 쉬워서 초보자가 처음 실제 호출을 성공시키기에 좋습니다.

2. REST 방식
   httpx로 HTTP 요청을 직접 보냅니다.
   URL, query parameter, JSON payload, 응답 JSON 구조를 직접 볼 수 있어 API 내부 구조를 이해하기 좋습니다.
```

이 과정에서는 **SDK 방식을 기본 실제 호출 예제**로 사용하고, **REST 방식은 HTTP 구조를 이해하는 보충 예제**로 둡니다.

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| `main.py` | 비용 없는 통합 mock 싱글턴 호출 예제 |
| `01_mock_single_turn.py` | 가장 단순한 mock 싱글턴 호출 예제 |
| `02_gemini_sdk_single_turn.py` | Gemini SDK 기반 실제 싱글턴 호출 기본 예제 |
| `03_gemini_rest_single_turn.py` | Gemini REST API 기반 HTTP 구조 확인 예제 |
| `04_openai_single_turn.py` | OpenAI API 선택/비교 싱글턴 호출 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 공통 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

필요한 패키지는 최상위 `requirements.txt`에 포함되어 있습니다.

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 1. 비용 없는 통합 mock 예제 실행

```powershell
python .\05_llm-api-integration\03_single-turn-call\main.py
```

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.

확인할 내용:

```text
1. 사용자 질문
2. 메모 컨텍스트
3. LLM에 전달할 프롬프트
4. mock 응답 구조
5. input_length, max_tokens 같은 사용량 관련 값
```

## 2. 가장 단순한 mock 호출 실행

```powershell
python .\05_llm-api-integration\03_single-turn-call\01_mock_single_turn.py
```

이 예제는 함수 하나로 질문 1개와 응답 1개의 흐름을 보여줍니다.

실제 API 호출 전에 mock 예제를 먼저 실행하는 이유:

```text
1. 비용이 발생하지 않습니다.
2. API key가 없어도 실행됩니다.
3. 입력, 파라미터, 응답 구조를 먼저 이해할 수 있습니다.
4. 이후 실제 API 호출 코드와 비교하기 쉽습니다.
```

## 3. Gemini SDK 실제 싱글턴 호출

Gemini는 01~03 과정의 기본 LLM 실습 provider입니다. 실제 호출을 처음 배울 때는 SDK 방식이 가장 쉽습니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행:

```powershell
python .\05_llm-api-integration\03_single-turn-call\02_gemini_sdk_single_turn.py
```

SDK 방식의 장점:

```text
1. URL을 직접 만들지 않아도 됩니다.
2. query parameter와 JSON payload를 직접 구성하지 않아도 됩니다.
3. response.text로 응답 텍스트를 쉽게 확인할 수 있습니다.
4. 실제 Gemini 호출을 처음 성공시키기에 좋습니다.
```

## 4. Gemini REST 실제 싱글턴 호출

REST 방식은 SDK보다 코드가 길지만 API 내부 구조를 이해하기 좋습니다.

실행:

```powershell
python .\05_llm-api-integration\03_single-turn-call\03_gemini_rest_single_turn.py
```

REST 방식에서 확인할 내용:

```text
1. Gemini API URL
2. API key를 전달하는 방식
3. HTTP 요청 Body에 들어가는 contents와 generationConfig
4. 응답 JSON에서 candidates -> content -> parts -> text를 꺼내는 과정
5. 외부 API 오류 발생 시 raise_for_status로 확인하는 흐름
```

REST 방식은 이후 FastAPI에서 외부 API를 호출하거나, `httpx.AsyncClient`로 비동기 호출을 다룰 때 도움이 됩니다.

## 5. OpenAI 선택/비교 싱글턴 호출

OpenAI 예제는 필수가 아닙니다. 모델 제공자별 호출 방식과 응답 차이를 비교할 때 사용합니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
OPENAI_API_KEY=your-real-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실행:

```powershell
python .\05_llm-api-integration\03_single-turn-call\04_openai_single_turn.py
```

OpenAI API 결제는 ChatGPT/Codex 앱 결제와 별도입니다. 실제 호출 전 OpenAI Platform의 Billing 화면을 확인합니다.

## 싱글턴 호출 흐름

```text
사용자 질문
-> 필요한 경우 메모 컨텍스트 추가
-> prompt 구성
-> LLM API 호출
-> 응답 텍스트 추출
-> FastAPI 응답 구조로 정리
```

## 싱글턴 호출에 적합한 경우

```text
1. 간단한 질문 응답
2. 짧은 문장 요약
3. 한 번에 끝나는 코드 설명
4. 이전 대화가 필요 없는 분류 작업
```

## 싱글턴 호출의 한계

```text
1. 이전 대화 내용을 기억하지 않습니다.
2. 사용자별 장기 기록을 반영하지 않습니다.
3. 같은 사용자가 이어서 질문해도 별도의 이력 관리가 필요합니다.
```

이 한계는 다음 단원인 `04_multi-turn-call`에서 이전 대화 이력을 함께 보내는 방식으로 다룹니다.

## 실제 API 호출 전 체크리스트

```text
1. .env에 실제 API key가 있는가?
2. your-... 형태의 placeholder 값이 아닌가?
3. 공식 가격, 무료 범위, 호출 제한을 확인했는가?
4. maxOutputTokens 또는 max_tokens가 너무 크지 않은가?
5. 반복 실행으로 비용이 발생하지 않도록 주의하고 있는가?
6. API key가 터미널, README, GitHub에 노출되지 않는가?
```

## 이후 단원과의 연결

```text
04_multi-turn-call:
  이전 user/model 메시지를 함께 보내 문맥을 유지합니다.

05_fastapi-llm-endpoint:
  FastAPI endpoint에서 사용자 질문을 받아 Gemini API를 호출합니다.

06_supabase-db-and-auth:
  사용자 정보와 대화 이력을 Supabase에 저장합니다.

03_supabase-ai-mini-project:
  SSE 스트리밍, Supabase 저장, Streamlit 화면까지 연결합니다.
```

## 확인 질문

```text
1. 싱글턴 호출과 멀티턴 호출의 차이는 무엇인가요?
2. 실제 API 호출 전에 mock 예제를 실행하는 이유는 무엇인가요?
3. Gemini SDK 방식이 REST 방식보다 쉬운 이유는 무엇인가요?
4. REST 방식이 학습에 여전히 필요한 이유는 무엇인가요?
5. OpenAI API 결제는 ChatGPT/Codex 앱 결제와 왜 별도로 확인해야 하나요?
```
