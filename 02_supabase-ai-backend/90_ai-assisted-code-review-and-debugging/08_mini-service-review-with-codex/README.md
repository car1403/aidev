# 08_mini-service-review-with-codex

이 단원에서는 `08_backend-mini-service-practice`에서 만든 백엔드 미니 서비스를 Codex와 함께 종합 리뷰하는 방법을 학습합니다.

앞 단원에서는 파일 하나 또는 특정 오류를 중심으로 리뷰했습니다. 이번 단원에서는 요구사항, API 설계, Pydantic 모델, Supabase 저장, Upstash Redis 활용, 서비스 로그, 보안, 실행 확인까지 미니 서비스 전체 흐름을 하나의 기준으로 점검합니다.

## 이 단원에서 다루는 내용

- 요구사항과 구현 결과가 일치하는지 확인하는 방법
- mock-first 구현과 Supabase 구현의 차이를 설명하는 방법
- API endpoint, HTTP Method, 요청/응답 모델을 종합 리뷰하는 방법
- Supabase 테이블, 컬럼, 저장 흐름을 확인하는 방법
- Upstash Redis 캐시, 세션, rate limit 활용 가능성을 점검하는 방법
- 서비스 로그가 운영에 필요한 정보를 담는지 확인하는 방법
- API key, token, 사용자 정보 노출 위험을 확인하는 방법
- 최종 백엔드 프로젝트로 확장하기 전에 개선 목록을 정리하는 방법

## 리뷰 대상 파일

미니 서비스 리뷰는 한 파일만 보는 것이 아니라 관련 파일을 묶어서 확인합니다.

```text
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\01_requirements\README.md
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\02_api-design\README.md
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\03_supabase-schema\mini-service-schema.sql
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_supabase.py
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\schemas.py
```

처음에는 모든 파일을 한 번에 리뷰하지 말고, 요구사항 문서와 API 설계 문서를 먼저 확인한 뒤 구현 파일을 보는 것이 좋습니다.

## 종합 리뷰 순서

미니 서비스는 다음 순서로 리뷰합니다.

1. 요구사항 문서를 읽고 서비스 목적을 한 문장으로 정리합니다.
2. API 설계 문서의 endpoint 목록을 확인합니다.
3. Pydantic 요청/응답 모델이 API 설계와 일치하는지 확인합니다.
4. mock-first 구현이 요구사항을 단순하게 재현하는지 확인합니다.
5. Supabase 구현이 실제 테이블 구조와 일치하는지 확인합니다.
6. 서비스 로그가 성공, 실패, 오류 상황을 구분하는지 확인합니다.
7. API key, Supabase key, Redis token이 노출되지 않는지 확인합니다.
8. 오류 상황에서 적절한 HTTP Status Code를 반환하는지 확인합니다.
9. 최종 프로젝트로 확장할 때 남은 개선 사항을 정리합니다.

이 순서대로 보면 "코드는 있는데 요구사항과 다르다"거나 "문서에는 endpoint가 있는데 구현이 없다" 같은 문제를 쉽게 찾을 수 있습니다.

## 요구사항 리뷰 기준

요구사항은 미니 서비스가 무엇을 해야 하는지 정리한 기준입니다.

확인할 항목은 다음과 같습니다.

- 서비스 목적이 한 문장으로 설명되는가?
- 핵심 기능이 너무 많지 않은가?
- 질문 저장, 응답 생성, 로그 저장 같은 주요 흐름이 구분되어 있는가?
- mock-first 단계에서 가능한 기능과 Supabase 단계에서 필요한 기능이 구분되어 있는가?
- 이후 Gemini SDK 호출로 교체할 위치와 저장 필드가 분리되어 있는가?
- 최종 프로젝트로 확장할 수 있는 여지가 남아 있는가?

요구사항이 모호하면 코드 리뷰도 흔들립니다. Codex에게 리뷰를 요청하기 전에 먼저 "이 서비스가 무엇을 하는가"를 정리해야 합니다.

## API 설계 리뷰 기준

API 설계는 프론트엔드 또는 다른 서비스가 백엔드를 어떻게 호출할지 정하는 약속입니다.

확인할 항목은 다음과 같습니다.

- endpoint URL이 리소스 중심으로 작성되어 있는가?
- GET, POST, PUT, DELETE가 의미에 맞게 사용되는가?
- 요청 Body와 응답 Body가 문서에 정리되어 있는가?
- 성공 응답과 실패 응답 형식이 일관적인가?
- 400, 404, 500 같은 HTTP Status Code가 상황에 맞게 사용되는가?
- Swagger UI에서 테스트하기 쉬운 구조인가?

예를 들어 질문 생성은 `POST /questions`, 질문 목록 조회는 `GET /questions`처럼 역할이 명확해야 합니다.

## Pydantic 모델 리뷰 기준

Pydantic 모델은 API 입력과 출력을 안정적으로 다루기 위한 기준입니다.

확인할 항목은 다음과 같습니다.

- 요청 모델과 응답 모델이 분리되어 있는가?
- 필수 필드와 선택 필드가 구분되어 있는가?
- 문자열 길이, 빈 값, role 값 같은 검증 조건이 있는가?
- 응답 모델이 실제 반환값과 일치하는가?
- 예시 데이터가 제공되어 Swagger UI에서 이해하기 쉬운가?

Pydantic 모델이 부족하면 FastAPI가 잘못된 입력을 걸러내지 못합니다. 반대로 모델이 너무 복잡하면 초보 단계에서 흐름을 이해하기 어려워집니다.

## mock-first 구현 리뷰 기준

mock-first 구현은 실제 Supabase나 LLM API 없이 서비스 흐름을 먼저 이해하기 위한 코드입니다.

확인할 항목은 다음과 같습니다.

- 외부 API key 없이 실행 가능한가?
- 메모리 저장소나 샘플 데이터로 흐름을 확인할 수 있는가?
- 실제 구현으로 바꾸기 전 구조를 이해하기 쉬운가?
- mock-first 응답이라는 점이 코드와 문서에 명확히 표시되어 있는가?
- `actual_api_called=false`, `llm_call_mode=mock-first` 기준이 응답과 저장 구조에 반영되어 있는가?
- 실제 API 호출이 실수로 섞여 있지 않은가?

mock-first 단계는 비용 없이 흐름을 연습하는 단계입니다. 여기서 endpoint, provider, 모델, 오류 처리 흐름을 먼저 안정화하면 실제 Supabase 연동과 Gemini SDK 연동이 쉬워집니다.

## Supabase 구현 리뷰 기준

Supabase 구현은 실제 데이터가 저장되는 단계입니다.

확인할 항목은 다음과 같습니다.

- SQL 파일의 테이블명과 Python 코드의 테이블명이 일치하는가?
- 컬럼명과 Python dict key가 일치하는가?
- insert 결과가 비어 있을 때 오류 처리가 있는가?
- select 조건이 사용자별 또는 리소스별로 적절히 들어가는가?
- update/delete에 `.eq(...)` 조건이 빠져 있지 않은가?
- service role key가 백엔드에서만 사용되는가?
- 로그 테이블에 민감 정보가 저장되지 않는가?

Supabase 구현 리뷰에서는 "저장된다"만 확인하지 말고 "올바른 사용자와 올바른 데이터만 다루는가"를 함께 봐야 합니다.

## Upstash Redis 활용 리뷰 기준

미니 서비스에서 Redis가 꼭 모든 기능에 들어갈 필요는 없습니다. 다만 캐시, 세션, rate limit이 필요한 경우 Upstash Redis를 어디에 붙일 수 있는지 판단할 수 있어야 합니다.

확인할 항목은 다음과 같습니다.

- Redis가 필요한 기능인지 먼저 판단했는가?
- 짧게 보관할 데이터와 오래 보관할 데이터를 구분했는가?
- Redis key가 사용자별 또는 기능별로 분리되어 있는가?
- TTL이 필요한 key에 만료 시간이 있는가?
- Redis token이 코드나 로그에 노출되지 않는가?
- Supabase에 저장해야 할 장기 데이터를 Redis에만 저장하지 않는가?

예를 들어 질문 응답 캐시는 Redis에 잠시 저장할 수 있지만, 최종 대화 이력은 Supabase에 저장해야 합니다.

## 서비스 로그 리뷰 기준

서비스 로그는 나중에 오류 원인을 찾고 사용 흐름을 개선하기 위한 데이터입니다.

확인할 항목은 다음과 같습니다.

- 질문 생성, 응답 생성, 오류 발생 같은 이벤트가 구분되는가?
- `event_type` 값이 일관적인가?
- 성공 로그와 실패 로그가 모두 남는가?
- `metadata`에 endpoint, provider, model, actual_api_called, llm_call_mode, item_id처럼 분석에 필요한 정보가 있는가?
- API key, token, 비밀번호, 민감한 사용자 정보가 로그에 들어가지 않는가?
- 로그 저장 실패가 전체 API 실패로 이어지지 않도록 처리되어 있는가?

좋은 로그는 문제를 찾는 데 충분하지만, 민감 정보는 포함하지 않습니다.

## 보안과 비용 리뷰 기준

미니 서비스가 정상 동작하더라도 보안과 비용 문제가 있으면 최종 프로젝트로 확장하기 어렵습니다.

확인할 항목은 다음과 같습니다.

- `.env`에 실제 key가 있고, `.env.example`에는 예시 값만 있는가?
- `.gitignore`에 `.env`가 포함되어 있는가?
- Gemini API key와 OpenAI API key가 코드에 직접 적혀 있지 않은가?
- Gemini SDK가 기본 경로이고, REST 호출은 보충 예제, OpenAI 예제는 선택 실습 또는 비교 실습으로 분리되어 있는가?
- 반복문 안에서 실제 LLM API를 과도하게 호출하지 않는가?
- Supabase service role key가 프론트엔드로 노출될 가능성이 없는가?
- 오류 메시지에 내부 설정값이 그대로 노출되지 않는가?

보안 리뷰는 기능 리뷰 뒤에 하는 작업이 아니라, 기능 리뷰와 함께 진행해야 합니다.

## Codex 종합 리뷰 요청 예시

아래 예시는 미니 서비스 전체를 리뷰할 때 사용할 수 있는 요청입니다.

```text
08_backend-mini-service-practice의 미니 서비스를 종합 리뷰해주세요.

리뷰 대상:
1. 01_requirements/README.md
2. 02_api-design/README.md
3. 03_supabase-schema/mini-service-schema.sql
4. 04_implementation-guide/main_mock.py
5. 04_implementation-guide/main_supabase.py
6. 04_implementation-guide/schemas.py

서비스 목적:
사용자 질문을 저장하고, AI 응답을 생성한 뒤, 서비스 로그를 남기는 백엔드 미니 서비스입니다.

리뷰 관점:
1. 요구사항과 구현 결과가 일치하는가?
2. endpoint URL과 HTTP Method가 적절한가?
3. Pydantic 요청/응답 모델이 충분한가?
4. mock-first 구현과 Supabase 구현의 역할이 명확히 구분되는가?
5. Supabase 테이블명, 컬럼명, 저장 흐름이 일치하는가?
6. Upstash Redis를 추가한다면 캐시, 세션, rate limit 중 어디에 쓰는 것이 적절한가?
7. 서비스 로그가 운영에 필요한 정보를 담고 민감 정보는 제외하는가?
8. API key, token, service role key 노출 위험이 있는가?
9. provider, model, actual_api_called, llm_call_mode 기준이 문서, SQL, Python 코드에 일치하는가?
10. 최종 프로젝트로 확장하기 전에 무엇을 먼저 개선해야 하는가?

출력 형식:
- 치명적인 문제
- 수정이 필요한 문제
- 개선하면 좋은 문제
- 최종 프로젝트 전 확인 질문
- 실행 또는 테스트 방법

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 리뷰 결과 정리 예시

Codex의 답변을 받은 뒤에는 아래 형식으로 정리하면 좋습니다.

```md
## 미니 서비스 리뷰 결과

### 치명적인 문제
- `.env` 예시와 실제 코드의 환경 변수 이름이 다릅니다.

### 수정이 필요한 문제
- `POST /questions`의 응답 모델에 `created_at`이 빠져 있습니다.
- Supabase insert 결과가 비어 있을 때 오류 처리가 없습니다.

### 개선하면 좋은 문제
- mock 저장소와 Supabase 저장소의 함수 이름을 맞추면 비교하기 쉽습니다.

### 최종 프로젝트 전 확인 질문
- 사용자별 데이터 접근 제어를 어디에서 처리할 것인가?
- Redis 캐시는 어떤 endpoint에 적용할 것인가?

### 실행 확인
- `uvicorn main_mock:app --reload`
- Swagger UI에서 질문 생성 요청 테스트
- Supabase 테이블에 저장 결과 확인
```

이렇게 정리하면 수정할 항목의 우선순위가 명확해집니다.

## 최종 프로젝트 전 확인 체크리스트

- [ ] 요구사항 문서와 구현 결과가 일치한다.
- [ ] API endpoint URL과 HTTP Method가 의미에 맞게 작성되어 있다.
- [ ] Pydantic 요청/응답 모델이 실제 데이터 구조와 일치한다.
- [ ] mock-first 구현과 Supabase 구현의 역할이 명확히 구분되어 있다.
- [ ] `provider`, `model`, `actual_api_called`, `llm_call_mode` 저장 기준이 문서, SQL, Python 코드에 일치한다.
- [ ] Supabase 테이블명과 컬럼명이 코드와 일치한다.
- [ ] update/delete 조건 누락 위험이 없다.
- [ ] 서비스 로그가 성공, 실패, 오류 상황을 구분한다.
- [ ] 로그에 API key, token, 민감 정보가 저장되지 않는다.
- [ ] Upstash Redis를 사용할 경우 TTL과 key 설계가 명확하다.
- [ ] 실제 LLM API 호출이 과도하게 반복되지 않는다.
- [ ] Codex 리뷰 결과를 치명도별로 분류할 수 있다.
- [ ] 최종 프로젝트로 확장하기 전 개선 항목을 정리할 수 있다.
