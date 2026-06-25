# Assignment 07 - Supabase, Auth, Redis 통합 설계

Supabase DB, Supabase Auth, Upstash Redis를 하나의 AI 서비스 구조로 연결해 보는 통합 설계 과제입니다.

LLM 호출은 앞 단원 기준에 맞춰 `mock-first`로 설계하고, 실제 프로젝트 기본 구현은 Gemini SDK 호출로 확장하는 흐름을 사용합니다.

## 목표

- 인증, 데이터 저장, 캐시, 요청 제한을 하나의 흐름으로 설명할 수 있습니다.
- 백엔드에서 어떤 key를 사용해야 하는지 구분할 수 있습니다.
- 사용자 요청이 들어왔을 때 어떤 순서로 기능이 실행되는지 설계할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. 전체 아키텍처 설명
2. 사용자 요청 처리 순서
3. Supabase Auth 역할
4. Supabase DB 역할
5. Upstash Redis 역할
6. FastAPI endpoint 목록
7. 환경변수 목록
8. 보안상 주의할 점
9. 예상 오류와 대응 방법
```

## 요청 처리 흐름 예시

```text
1. 사용자가 로그인한다.
2. 프론트엔드가 access token을 백엔드에 보낸다.
3. 백엔드는 token을 확인한다.
4. Redis에서 rate limit을 확인한다.
5. Supabase에서 필요한 대화 이력을 조회한다.
6. mock 응답을 생성하거나 Gemini SDK 응답을 생성한다.
7. 응답을 Supabase에 저장한다.
8. 서비스 로그를 저장한다.
```

## 확인 기준

- Supabase와 Redis의 역할이 겹치지 않습니다.
- 보안 key의 사용 위치가 올바릅니다.
- 장애 상황 또는 오류 상황을 최소 3개 이상 정리했습니다.
- LLM 호출 결과에 `provider`, `model`, `actual_api_called` 같은 기록 정보가 포함됩니다.
