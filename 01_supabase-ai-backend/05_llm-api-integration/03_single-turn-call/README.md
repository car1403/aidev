# 03_single-turn-call

이 단원에서는 **싱글턴 LLM 호출**을 학습합니다.

싱글턴 호출은 이전 대화 이력을 포함하지 않고, 현재 질문 하나만 LLM에 보내 응답을 받는 방식입니다. 앞 단원에서 API key와 비용 안전 기준을 확인했으므로, 이번 단원에서는 먼저 비용 없는 mock 예제로 구조를 이해한 뒤 Gemini API를 기본 실제 호출 예제로 다룹니다.

## 핵심 요약

```text
싱글턴 호출
  현재 질문 1개를 모델에 보내고 답변 1개를 받는 방식입니다.

mock 호출
  실제 API를 호출하지 않고 함수로 응답 구조만 흉내 냅니다.

Gemini 호출
  01~03 과정의 기본 실제 LLM 호출 방식입니다.

OpenAI 호출
  선택/비교 실습용으로 유지합니다.
```

## 폴더 파일

| 파일 | 역할 |
| --- | --- |
| `main.py` | 비용 없는 통합 mock 싱글턴 호출 예제 |
| `01_mock_single_turn.py` | 가장 단순한 mock 싱글턴 호출 예제 |
| `03_gemini_rest_single_turn.py` | Gemini REST API 기반 실제 싱글턴 호출 예제 |
| `02_openai_single_turn.py` | OpenAI API 선택/비교 싱글턴 호출 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

## 1. 비용 없는 통합 예제 실행

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

이 예제는 함수 하나로 “질문 1개 -> 답변 1개” 흐름을 보여줍니다.

실제 API 호출 전에 mock 예제를 먼저 실행하는 이유:

```text
1. 비용이 발생하지 않습니다.
2. API key가 없어도 실행됩니다.
3. 입력, 파라미터, 응답 구조를 먼저 이해할 수 있습니다.
4. 이후 실제 API 호출 코드와 비교하기 쉽습니다.
```

## 3. Gemini 실제 싱글턴 호출

Gemini는 01~03 과정의 기본 LLM 실습 provider입니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행:

```powershell
python .\05_llm-api-integration\03_single-turn-call\03_gemini_rest_single_turn.py
```

이 파일은 `GEMINI_API_KEY`가 실제 key로 설정되어 있을 때만 API를 호출합니다. key가 없거나 `your-gemini-api-key` 같은 예시 문자열이면 실제 호출하지 않고 안내 메시지를 출력합니다.

## 4. OpenAI 선택/비교 싱글턴 호출

OpenAI 예제는 필수가 아닙니다. 모델 공급자별 호출 방식과 응답 차이를 비교할 때 사용합니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
OPENAI_API_KEY=your-real-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실행:

```powershell
python .\05_llm-api-integration\03_single-turn-call\02_openai_single_turn.py
```

OpenAI API 결제는 ChatGPT/Codex 앱 결제와 별개입니다. 실제 호출 전 OpenAI Platform의 Billing 화면을 확인합니다.

## 싱글턴 호출 흐름

```text
사용자 질문
-> 필요한 경우 메모 컨텍스트 추가
-> system/user 메시지 또는 prompt 구성
-> LLM API 호출
-> 응답 텍스트 추출
-> FastAPI 응답 구조로 정리
```

## 싱글턴 호출이 적합한 경우

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
2. your-... 형태의 placeholder 값은 아닌가?
3. 공식 가격/무료 범위/호출 제한을 확인했는가?
4. max_tokens 또는 maxOutputTokens가 너무 크지 않은가?
5. 반복 실행으로 비용이 발생하지 않도록 주의하고 있는가?
6. API key가 터미널, README, GitHub에 노출되지 않는가?
```

## 이후 단원과의 연결

```text
04_multi-turn-call:
  이전 user/assistant 메시지를 함께 보내 문맥을 유지합니다.

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
3. Gemini 호출에서 maxOutputTokens는 왜 필요한가요?
4. OpenAI API 결제와 ChatGPT/Codex 앱 결제는 왜 별도로 확인해야 하나요?
5. 메모 컨텍스트를 질문과 함께 보내면 어떤 점이 좋아지나요?
```
