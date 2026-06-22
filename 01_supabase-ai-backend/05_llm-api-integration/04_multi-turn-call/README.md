# 04_multi-turn-call

이 단원에서는 **멀티턴 LLM 호출**을 학습합니다.

멀티턴 호출은 이전 대화 이력을 함께 보내서 모델이 문맥을 이어서 답변하도록 만드는 방식입니다. 중요한 점은 모델이 우리 서비스의 대화를 자동으로 기억하는 것이 아니라, 코드에서 이전 `user`/`assistant` 메시지를 다시 넣어 보내야 한다는 것입니다.

## 핵심 요약

```text
싱글턴 호출
  현재 질문 1개만 모델에 보냅니다.

멀티턴 호출
  이전 질문과 답변을 messages 목록에 함께 넣어 보냅니다.

대화 메모리
  사용자의 이전 질문과 AI 답변을 저장하고 다시 불러오는 구조입니다.

최근 메시지 자르기
  대화가 길어지면 비용과 응답 시간이 늘어나므로 최근 일부만 보낼 수 있습니다.
```

## 폴더 파일

| 파일 | 역할 |
| --- | --- |
| `main.py` | 비용 없는 통합 mock 멀티턴 호출 예제 |
| `01_mock_multi_turn.py` | 가장 단순한 멀티턴 messages 구조 예제 |
| `02_conversation_memory.py` | 대화 이력을 메모리에서 관리하는 예제 |
| `04_gemini_rest_multi_turn.py` | Gemini REST API 기반 실제 멀티턴 호출 예제 |
| `03_openai_multi_turn.py` | OpenAI API 선택/비교 멀티턴 호출 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

## 1. 비용 없는 통합 예제 실행

```powershell
python .\05_llm-api-integration\04_multi-turn-call\main.py
```

이 예제는 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.

확인할 내용:

```text
1. system 메시지
2. 이전 user 메시지
3. 이전 assistant 메시지
4. 최신 user 메시지
5. mock 멀티턴 응답
```

## 2. 가장 단순한 mock 멀티턴 실행

```powershell
python .\05_llm-api-integration\04_multi-turn-call\01_mock_multi_turn.py
```

이 예제는 `messages` 목록에 이전 대화를 직접 넣어 보내는 구조를 보여줍니다.

```text
system
user
assistant
user
```

모델은 이 목록을 보고 마지막 질문이 무엇을 이어서 묻는지 추론합니다.

## 3. 대화 메모리 구조 확인

```powershell
python .\05_llm-api-integration\04_multi-turn-call\02_conversation_memory.py
```

이 예제는 대화 이력을 메모리 리스트에 저장하고, 최근 메시지만 잘라서 LLM API에 보낼 목록을 만듭니다.

실제 서비스에서는 이 구조가 다음처럼 확장됩니다.

```text
메모리 리스트
-> Supabase conversations/messages 테이블
-> 사용자별 대화 이력 조회
-> 최근 메시지 또는 요약 메시지 구성
-> LLM API 호출
```

## 4. Gemini 실제 멀티턴 호출

Gemini는 01~03 과정의 기본 LLM 실습 provider입니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\04_gemini_rest_multi_turn.py
```

이 파일은 `GEMINI_API_KEY`가 실제 key로 설정되어 있을 때만 API를 호출합니다. key가 없거나 `your-gemini-api-key` 같은 예시 문자열이면 실제 호출하지 않고 안내 메시지를 출력합니다.

Gemini REST API에서는 이전 AI 답변을 `role: "model"`로 표현합니다.

## 5. OpenAI 선택/비교 멀티턴 호출

OpenAI 예제는 필수가 아닙니다. 모델 공급자별 메시지 구조 차이를 비교할 때 사용합니다.

실행 전 `.env`에 아래 값이 필요합니다.

```env
OPENAI_API_KEY=your-real-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실행:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\03_openai_multi_turn.py
```

OpenAI API 결제는 ChatGPT/Codex 앱 결제와 별개입니다. 실제 호출 전 OpenAI Platform의 Billing 화면을 확인합니다.

## 멀티턴 호출 흐름

```text
사용자 질문 입력
-> 이전 대화 이력 조회
-> system/user/assistant 메시지 목록 구성
-> 최신 user 메시지 추가
-> LLM API 호출
-> assistant 응답 저장
-> 응답 반환
```

## 멀티턴 호출이 필요한 경우

```text
1. 이어지는 질문에 답해야 할 때
2. 사용자가 "그 내용", "방금 말한 것"처럼 문맥을 참조할 때
3. 사용자별 대화 흐름을 유지해야 할 때
4. 이전 답변을 바탕으로 추가 설명이나 수정 요청을 받을 때
```

## 멀티턴 호출에서 주의할 점

```text
1. 대화가 길어질수록 입력 토큰이 늘어납니다.
2. 비용과 응답 시간이 증가할 수 있습니다.
3. 오래된 메시지를 모두 보내는 것이 항상 좋은 것은 아닙니다.
4. 필요한 경우 최근 메시지만 보내거나 요약본을 만들어야 합니다.
5. 실제 서비스에서는 사용자별로 대화 이력을 구분해야 합니다.
```

## 이후 단원과의 연결

```text
05_fastapi-llm-endpoint:
  FastAPI endpoint에서 사용자 질문과 대화 이력을 받아 LLM API를 호출합니다.

06_supabase-db-and-auth:
  대화 이력을 Supabase에 저장하고 사용자별로 조회합니다.

02_supabase-ai-frontend:
  Streamlit 화면에서 이전 대화를 보여주고 새 질문을 입력받습니다.

03_supabase-ai-mini-project:
  SSE 스트리밍, Supabase 저장, 대화 이력 조회를 통합합니다.
```

## 확인 질문

```text
1. 멀티턴 호출은 모델이 자동으로 기억하는 방식인가요?
2. 이전 assistant 답변을 다시 보내야 하는 이유는 무엇인가요?
3. 대화가 길어지면 왜 최근 메시지만 자르거나 요약해야 하나요?
4. Gemini의 role="model"과 OpenAI의 role="assistant"는 어떤 관계인가요?
5. 실제 서비스에서 대화 이력을 어디에 저장하게 되나요?
```
