# 01_llm-api-concepts

이 단원에서는 LLM API가 무엇인지, FastAPI 백엔드에서 왜 LLM API를 호출하는지, 실제 API 호출 전에 어떤 구조를 먼저 이해해야 하는지 학습합니다.

앞 단원인 `04_fastapi-backend`에서는 메모 API를 만들었습니다. 이번 단원부터는 사용자의 질문, 저장된 메모, 이전 대화 이력 같은 데이터를 LLM에 전달하고 응답을 받아오는 흐름을 배웁니다.

## 핵심 요약

```text
LLM
  Large Language Model의 줄임말입니다. 사용자의 문장을 입력받아 답변, 요약, 분류, 변환 등을 수행하는 모델입니다.

LLM API
  Python 코드나 FastAPI 서버에서 LLM을 호출하기 위한 HTTP/API 방식입니다.

Prompt
  모델에게 전달하는 지시문, 질문, 참고 자료를 말합니다.

Message
  role과 content로 구성된 대화 단위입니다.

Token
  모델이 입력과 출력을 처리하는 단위입니다. 실제 사용량과 비용 계산에 영향을 줍니다.

Parameter
  temperature, top_p, max_tokens처럼 응답의 길이와 성격을 조절하는 설정입니다.
```

## 이 단원에서 중요한 방향

```text
1. 실제 API 호출은 아직 하지 않습니다.
2. API key가 없어도 실행할 수 있는 예제로 시작합니다.
3. 01~03 과정에서는 Gemini API를 기본 실습 모델로 사용합니다.
4. OpenAI API 예제는 선택/비교 실습으로 유지합니다.
5. 실제 API 호출, 비용, key 설정은 다음 단원부터 단계적으로 다룹니다.
```

기본 모델 예시는 `gemini-2.5-flash-lite`를 사용합니다. 이 단원에서는 문자열 예시로만 다루며, 실제 호출은 `03_single-turn-call` 이후에 진행합니다.

## 폴더 파일

| 파일 | 역할 |
| --- | --- |
| `main.py` | LLM API 개념을 한 번에 확인하는 통합 실행 예제 |
| `01_message_structure.py` | role/content 기반 message 구조 예제 |
| `02_parameter_simulator.py` | temperature, top_p, max_tokens 의미를 비용 없이 확인하는 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

## 통합 예제 실행

```powershell
python .\05_llm-api-integration\01_llm-api-concepts\main.py
```

이 예제는 실제 Gemini 또는 OpenAI API를 호출하지 않습니다. 따라서 API key가 없어도 실행되고 비용도 발생하지 않습니다.

## 1. Message 구조 이해

LLM API는 보통 단순 문자열 하나가 아니라 `role`과 `content`로 이루어진 메시지 목록을 받습니다.

```python
{
    "role": "user",
    "content": "FastAPI에서 GET과 POST의 차이를 설명해 주세요."
}
```

대표적인 role은 다음과 같습니다.

| role | 의미 |
| --- | --- |
| `system` | 모델이 따라야 할 역할과 규칙을 정합니다. |
| `user` | 사용자가 입력한 질문이나 요청입니다. |
| `assistant` | 모델이 이전에 답변한 내용입니다. |

이번 단원에서는 메모 API 흐름과 연결하기 위해 다음과 같은 구조를 사용합니다.

```text
system:
  학습 도우미 역할을 지정합니다.

user:
  참고할 메모 내용을 전달합니다.

user:
  실제 질문을 전달합니다.
```

## 2. Prompt와 Context 구분

프롬프트는 모델에게 전달되는 전체 입력입니다. 그 안에는 질문뿐 아니라 참고 자료도 포함될 수 있습니다.

```text
질문:
  "FastAPI 요청 처리 흐름을 설명해 주세요."

컨텍스트:
  "GET은 조회, POST는 생성, Pydantic은 요청 검증에 사용된다."
```

이후 미니 프로젝트에서는 사용자의 이전 대화, Supabase에 저장된 기록, 서비스 로그 같은 데이터도 컨텍스트로 사용할 수 있습니다.

## 3. Token 개념 이해

토큰은 모델이 문장을 처리하는 단위입니다.

초보 단계에서는 아래처럼 이해하면 충분합니다.

```text
입력이 길수록:
  처리해야 할 토큰이 많아집니다.

출력이 길수록:
  생성해야 할 토큰이 많아집니다.

토큰이 많아질수록:
  응답 시간이 길어지거나 비용이 증가할 수 있습니다.
```

`main.py`에서는 실제 토큰 계산 대신 글자 수와 단어 수를 간단히 출력합니다. 실제 토큰 수는 모델별 tokenizer가 계산합니다.

## 4. 생성 파라미터 이해

| 파라미터 | 의미 | 초보자 기준 설명 |
| --- | --- | --- |
| `model` | 사용할 모델 이름 | 이 과정에서는 Gemini를 기본으로 보고 OpenAI는 선택/비교로 둡니다. |
| `temperature` | 응답의 다양성 | 낮으면 안정적이고, 높으면 표현이 다양해질 수 있습니다. |
| `top_p` | 후보 단어 선택 범위 | 응답 다양성 조절에 관여합니다. |
| `max_tokens` | 최대 출력 길이 | 너무 크게 잡으면 비용과 응답 시간이 늘 수 있습니다. |

처음 실습할 때는 안정적인 응답을 위해 낮은 `temperature`와 적당한 `max_tokens`부터 시작합니다.

## 5. ChatGPT 화면과 API 호출의 차이

```text
ChatGPT 화면:
  브라우저에서 사람이 직접 질문하고 답변을 확인합니다.

LLM API:
  Python 코드나 FastAPI 서버가 모델에게 요청을 보내고 JSON 응답을 받습니다.
```

API를 사용하면 웹 서비스 안에서 다음 기능을 만들 수 있습니다.

```text
1. 사용자의 질문에 자동 응답
2. 메모 내용 요약
3. 서비스 로그 분석
4. 사용자 피드백 분류
5. 대화 이력 기반 개인화 응답
```

## 이후 단원과의 연결

```text
02_api-key-and-billing:
  Gemini API key 발급, .env 설정, 비용과 보안 주의사항을 다룹니다.

03_single-turn-call:
  이전 대화 없이 질문 1개를 Gemini API로 호출합니다.

04_multi-turn-call:
  이전 대화 이력을 포함해 문맥을 유지하는 호출을 다룹니다.

05_fastapi-llm-endpoint:
  FastAPI endpoint에서 LLM API를 호출하는 구조를 만듭니다.

03_supabase-ai-mini-project:
  SSE 스트리밍, Supabase 저장, Streamlit 화면까지 연결합니다.
```

## 확인 질문

```text
1. ChatGPT 화면에서 질문하는 것과 API로 호출하는 것은 무엇이 다른가요?
2. role과 content는 각각 어떤 의미인가요?
3. 실제 API 호출 전에 mock 또는 concept 예제를 먼저 실행하는 이유는 무엇인가요?
4. token이 많아지면 어떤 문제가 생길 수 있나요?
5. 01~03 과정에서 Gemini를 기본으로 두고 OpenAI를 선택/비교로 두는 이유는 무엇인가요?
```
