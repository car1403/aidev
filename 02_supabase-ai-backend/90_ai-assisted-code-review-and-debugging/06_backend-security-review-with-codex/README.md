# 06_backend-security-review-with-codex

이 단원에서는 Codex를 활용해 FastAPI, Supabase, Upstash Redis, LLM API 코드의 보안 위험과 비용 위험을 점검하는 방법을 학습합니다.

보안 리뷰는 어렵고 거창한 작업처럼 느껴질 수 있지만, 초보 단계에서는 먼저 "노출되면 안 되는 값이 코드, 화면, 로그에 남아 있는가?"를 확인하는 것부터 시작하면 됩니다. 이 과정에서는 실제 서비스에서 자주 발생하는 실수를 중심으로 점검합니다.

## 이 단원에서 다루는 내용

- API key, token, password 같은 민감 정보 노출 여부 확인
- `.env` 파일과 `.env.example` 파일의 역할 구분
- FastAPI endpoint에서 입력값을 검증하는 방법
- Supabase anon key와 service role key의 차이 이해
- Supabase RLS와 사용자별 데이터 접근 제어 점검
- Upstash Redis token, key 이름, TTL 설정 점검
- LLM API 호출 비용이 과도하게 발생할 수 있는 코드 확인
- 서비스 로그에 민감 정보가 저장되지 않는지 확인
- Codex에게 보안 리뷰를 요청하는 방법

## 보안 리뷰를 먼저 해야 하는 이유

기능이 잘 동작하더라도 다음 문제가 있으면 실제 서비스로 사용하기 어렵습니다.

- API key가 GitHub에 올라가 버린 경우
- Supabase service role key가 프론트엔드 코드에 들어간 경우
- 사용자별 데이터 조회 조건이 빠져 다른 사용자의 데이터가 보이는 경우
- Redis token이 로그에 출력되는 경우
- LLM API 호출이 반복문 안에서 계속 실행되어 비용이 커지는 경우
- 오류 로그에 사용자의 질문, 이메일, token이 그대로 저장되는 경우

코드 리뷰 단계에서 이런 문제를 미리 찾으면 나중에 큰 수정 없이 안전한 구조로 바꿀 수 있습니다.

## 민감 정보의 종류

보안 리뷰에서 가장 먼저 확인할 것은 민감 정보입니다.

| 구분 | 예시 | 코드 리뷰 기준 |
| --- | --- | --- |
| API key | Gemini API key, OpenAI API key | 코드에 직접 적지 않고 `.env`에서 읽어야 합니다. |
| Supabase key | anon key, service role key | service role key는 백엔드에서만 사용해야 합니다. |
| Redis token | Upstash Redis REST token | 출력, 로그, 프론트엔드 노출을 피해야 합니다. |
| 사용자 정보 | 이메일, user_id, 대화 내용 | 필요한 범위만 저장하고 로그에는 최소화해야 합니다. |
| 설정값 | DB URL, 프로젝트 URL | 공개 가능한 값과 비공개 값을 구분해야 합니다. |

`.env.example`에는 실제 key를 넣지 않습니다. 대신 다음처럼 어떤 값이 필요한지만 보여줍니다.

```env
SUPABASE_URL=your-supabase-project-url
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
UPSTASH_REDIS_REST_URL=your-upstash-redis-rest-url
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key
```

## FastAPI 보안 리뷰 기준

FastAPI 코드를 볼 때는 endpoint가 정상 동작하는지만 확인하지 않습니다. 외부에서 들어오는 요청을 얼마나 안전하게 다루는지도 확인해야 합니다.

확인할 항목은 다음과 같습니다.

- 요청 Body가 Pydantic 모델로 검증되는가?
- 빈 문자열, 너무 긴 문자열, 잘못된 role 값이 차단되는가?
- 사용자가 직접 보낸 `user_id`를 그대로 신뢰하지 않는가?
- 오류 메시지에 내부 설정값이나 key가 노출되지 않는가?
- CORS 설정이 필요 이상으로 넓게 열려 있지 않은가?
- 실제 서비스용 endpoint와 테스트용 endpoint가 구분되어 있는가?
- 관리자 기능이 일반 사용자 endpoint와 섞여 있지 않은가?

초보 단계에서는 "입력값을 믿지 않는다"는 기준만 기억해도 좋습니다. 사용자가 보낸 값은 항상 검증한 뒤 사용해야 합니다.

## Supabase 보안 리뷰 기준

Supabase는 데이터 저장과 인증을 함께 다루기 때문에 key 사용 위치와 RLS 정책이 중요합니다.

확인할 항목은 다음과 같습니다.

- Supabase URL과 key를 `.env`에서 읽는가?
- anon key와 service role key의 역할을 구분하는가?
- service role key가 Streamlit 또는 React 같은 프론트엔드 코드에 들어가지 않는가?
- 사용자별 데이터 조회 시 `user_id` 또는 `owner_id` 조건이 있는가?
- update와 delete에 `.eq(...)` 조건이 빠지지 않았는가?
- RLS가 필요한 테이블에 정책이 설계되어 있는가?
- 로그 테이블에 민감 정보가 저장되지 않는가?

특히 service role key는 모든 데이터에 접근할 수 있는 강한 권한입니다. 이 key는 백엔드 서버에서만 사용하고, 화면 코드나 GitHub에 올라가면 안 됩니다.

## Upstash Redis 보안 리뷰 기준

Upstash Redis는 세션, 캐시, rate limit처럼 빠르게 읽고 쓰는 임시 데이터를 다룰 때 사용합니다.

확인할 항목은 다음과 같습니다.

- Redis URL과 token이 `.env`에만 있는가?
- token을 print하거나 로그에 남기지 않는가?
- key 이름에 이메일, 전화번호 같은 민감 정보가 그대로 들어가지 않는가?
- 세션 key, 캐시 key, rate limit key가 목적별로 구분되는가?
- 임시 데이터에는 TTL이 설정되어 있는가?
- 장기 보관이 필요한 대화 이력은 Redis가 아니라 Supabase에 저장되는가?

예를 들어 `cache:user-question:123`처럼 목적과 범위를 알 수 있는 key는 괜찮지만, 사용자의 이메일을 그대로 key에 넣는 방식은 피하는 것이 좋습니다.

## LLM API 비용 리뷰 기준

Gemini SDK를 기본으로 사용하더라도 실제 API 호출에는 사용량 제한과 비용 관리가 필요합니다. REST 호출 예제는 구조 이해용 보충으로 보고, OpenAI는 선택 실습 또는 비교 실습으로 유지하되, 비용이 발생할 수 있다는 점을 명확히 확인해야 합니다.

확인할 항목은 다음과 같습니다.

- mock-first 호출과 실제 Gemini SDK 호출이 분리되어 있는가?
- REST 호출 예제가 기본 경로처럼 섞이지 않았는가?
- `actual_api_called`, `llm_call_mode`로 실제 호출 여부를 구분하는가?
- 실제 API 호출 전에 key 존재 여부를 확인하는가?
- 반복문 안에서 실제 LLM API를 계속 호출하지 않는가?
- 한 요청에서 너무 긴 prompt를 그대로 보내지 않는가?
- 최대 출력 길이 또는 토큰 제한이 있는가?
- 오류 발생 시 무한 재시도하지 않는가?
- 테스트용 코드가 실제 API를 자동으로 호출하지 않는가?

LLM API는 코드 한 줄로 호출할 수 있지만, 반복문이나 자동 테스트에서 호출되면 예상보다 많은 사용량이 발생할 수 있습니다.

## 서비스 로그 보안 리뷰 기준

로그는 문제를 찾는 데 필요하지만, 민감 정보를 저장하면 또 다른 보안 문제가 됩니다.

확인할 항목은 다음과 같습니다.

- 로그에 API key, token, password가 들어가지 않는가?
- 사용자의 전체 질문을 항상 저장해야 하는지 판단했는가?
- 오류 메시지에 내부 경로, 환경 변수 이름, key 일부가 노출되지 않는가?
- 성공 로그와 실패 로그가 구분되는가?
- 로그 저장 실패가 전체 API 실패로 이어지지 않는가?
- `metadata`에는 문제 분석에 필요한 최소 정보만 들어가는가?

좋은 로그는 문제를 찾을 수 있을 만큼 충분하지만, 불필요한 개인 정보와 key를 포함하지 않습니다.

## Codex 보안 리뷰 요청 예시

아래처럼 요청하면 Codex가 보안 관점에서 코드를 더 명확하게 검토할 수 있습니다.

```text
다음 FastAPI/Supabase 코드를 보안 관점에서 리뷰해주세요.

파일 위치:
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide\main_supabase.py

코드 목적:
사용자 질문, AI 응답, 서비스 로그를 Supabase에 저장하는 백엔드 예제입니다.

중점 확인:
1. API key나 token이 코드, print, 로그에 노출되는 부분이 있는가?
2. Supabase service role key가 프론트엔드로 노출될 가능성이 있는가?
3. 사용자별 데이터 조회 조건이 빠져 있지 않은가?
4. update/delete 조건 누락으로 여러 데이터가 수정 또는 삭제될 위험이 있는가?
5. 로그 metadata에 민감 정보가 들어갈 수 있는가?
6. 실제 LLM API 호출이 반복문이나 테스트에서 과도하게 실행될 수 있는가?
7. 초보자가 이해할 수 있는 방식으로 수정 방향을 설명해달라.

출력 형식:
- 즉시 수정해야 할 보안 위험
- 비용 증가 가능성이 있는 부분
- 데이터 접근 제어 문제
- 로그와 민감 정보 문제
- 수정 전 확인 질문
- 안전하게 고치는 순서

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 리뷰 결과를 적용하는 순서

보안 리뷰 결과를 받으면 모든 항목을 한 번에 고치려고 하지 않아도 됩니다. 위험도가 높은 것부터 처리합니다.

1. 코드에 직접 적힌 API key, token 제거
2. `.env`와 `.env.example` 분리
3. service role key 사용 위치 확인
4. 사용자별 데이터 조회 조건 추가
5. update/delete 조건 누락 확인
6. 로그에서 민감 정보 제거
7. LLM API 호출 횟수와 비용 제한 확인
8. 오류 응답을 사용자에게 안전한 메시지로 변경
9. 실행 또는 테스트로 수정 결과 확인

## 안전한 `.env` 관리 기준

`.env` 파일은 실제 key가 들어가는 파일입니다. GitHub에 올리면 안 됩니다.

확인할 항목은 다음과 같습니다.

- `.gitignore`에 `.env`가 포함되어 있는가?
- `.env.example`에는 실제 key가 없는가?
- README에는 key 발급 방법만 설명하고 실제 key를 적지 않았는가?
- 화면 캡처를 공유할 때 key가 보이지 않도록 가렸는가?
- Codex에게 질문할 때 실제 key를 붙여 넣지 않았는가?

실수로 key를 GitHub에 올렸다면 파일에서 지우는 것만으로는 충분하지 않습니다. 해당 key를 서비스 사이트에서 폐기하고 새 key를 발급해야 합니다.

## 완료 체크리스트

- [ ] API key와 token이 코드에 직접 적혀 있지 않은지 확인할 수 있다.
- [ ] `.env`와 `.env.example`의 차이를 설명할 수 있다.
- [ ] Supabase anon key와 service role key의 차이를 설명할 수 있다.
- [ ] service role key를 백엔드에서만 사용해야 하는 이유를 설명할 수 있다.
- [ ] update/delete 조건 누락의 위험을 설명할 수 있다.
- [ ] Upstash Redis token과 TTL 설정을 점검할 수 있다.
- [ ] LLM API 호출 비용이 커질 수 있는 코드를 찾을 수 있다.
- [ ] 서비스 로그에서 민감 정보를 제거해야 하는 이유를 설명할 수 있다.
- [ ] Codex에게 보안 리뷰를 요청할 때 리뷰 관점을 구체적으로 작성할 수 있다.
