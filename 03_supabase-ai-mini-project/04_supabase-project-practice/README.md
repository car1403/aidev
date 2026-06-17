# 04_supabase-project-practice

팀 미니 프로젝트를 시작하기 전에 Supabase 프로젝트, 테이블, 인증, RLS, 환경변수를 준비하는 단원입니다.

## 목표

- Supabase 프로젝트를 만들 수 있다.
- Project URL, anon key, service role key의 역할을 구분할 수 있다.
- `.env`와 `.env.example`을 안전하게 관리할 수 있다.
- 팀 프로젝트용 테이블을 설계할 수 있다.
- RLS 정책을 켜고 사용자별 데이터 접근을 테스트할 수 있다.
- FastAPI와 Streamlit에서 key를 어떻게 분리해야 하는지 설명할 수 있다.
- SSE 기반 실시간 AI 응답 스트리밍에서 FastAPI, Streamlit, Supabase의 역할을 구분할 수 있다.

## 권장 테이블 예시

```text
profiles
- id uuid primary key
- email text
- display_name text
- created_at timestamptz

conversations
- id uuid primary key
- user_id uuid
- title text
- created_at timestamptz

messages
- id uuid primary key
- conversation_id uuid
- role text
- content text
- created_at timestamptz

usage_logs
- id uuid primary key
- user_id uuid
- action text
- metadata jsonb
- created_at timestamptz
```

SSE 스트리밍을 적용할 때는 초보자 과정에서는 chunk를 모두 저장하기보다, 화면에는 실시간으로 표시하고 Supabase에는 최종 assistant 응답만 저장하는 방식을 권장합니다.

```text
streaming chunk: Streamlit 화면에 실시간 표시
final message: messages 테이블에 저장
error/fallback: usage_logs 테이블에 기록
```

## 진행 순서

1. Supabase 프로젝트 생성
2. API Settings에서 URL/key 확인
3. `.env.example`을 `.env`로 복사
4. 테이블 설계
5. SQL Editor에서 테이블 생성
6. RLS 활성화
7. anon/service role key 사용 위치 구분
8. FastAPI에서 Supabase 연결 확인
9. Streamlit에서는 FastAPI API 호출 확인
10. SSE 기반 AI 응답 스트리밍 흐름 설계
11. 스트리밍 완료 후 최종 메시지 저장 흐름 설계

## 참고 자료

```text
00_references/supabase/01_supabase-first-look.md
00_references/supabase/03_key-and-env-safety.md
00_references/supabase/04_rls-for-beginners.md
00_references/supabase/05_streamlit-fastapi-supabase-patterns.md
00_references/supabase/08_rls-troubleshooting-checklist.md
04_supabase-project-practice/05_sse-streaming-ai-response/README.md
```

## 체크리스트

- [ ] Supabase 프로젝트가 생성되어 있다.
- [ ] `.env`에 URL/key가 들어 있다.
- [ ] `.env`는 Git에 올리지 않는다.
- [ ] service role key는 서버 쪽에서만 사용한다.
- [ ] Streamlit에는 service role key를 넣지 않는다.
- [ ] Streamlit은 기본적으로 `API_BASE_URL`로 FastAPI를 호출한다.
- [ ] RLS 정책을 켠 뒤 select/insert 테스트를 했다.
- [ ] 팀 프로젝트 테이블 구조를 문서화했다.
- [ ] SSE는 실시간 전송, Supabase는 최종 데이터 저장이라는 역할 차이를 설명할 수 있다.
- [ ] 스트리밍 완료 후 최종 assistant 메시지를 어디에 저장할지 정했다.
