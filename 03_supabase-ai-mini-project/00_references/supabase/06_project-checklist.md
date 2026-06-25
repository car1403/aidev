# 06 Project Checklist

Supabase 미니 프로젝트 제출 전 확인할 항목입니다.

## Supabase

- [ ] 프로젝트를 만들었다.
- [ ] `service_logs`, `messages`, `feedbacks` 등 팀 프로젝트에 필요한 테이블을 만들었다.
- [ ] 샘플 데이터를 넣었다.
- [ ] RLS 정책을 확인했다.
- [ ] Auth를 사용하는 경우 테스트 계정이 있다.

## Environment

- [ ] `.env.example`이 있다.
- [ ] `.env`는 제출하지 않는다.
- [ ] 실제 key가 코드에 없다.
- [ ] service role key가 노출되지 않았다.
- [ ] `GEMINI_API_KEY`와 `GEMINI_MODEL=gemini-2.5-flash-lite` 기준을 확인했다.
- [ ] OpenAI key는 선택/비교 실습용이라는 점을 구분했다.

## Backend

- [ ] FastAPI `/health`가 응답한다.
- [ ] Supabase CRUD API가 동작한다.
- [ ] 오류 상황을 처리한다.
- [ ] Gemini API 호출이 필요한 기능은 백엔드에서 처리한다.

## Frontend

- [ ] Streamlit 화면이 열린다.
- [ ] 데이터 조회가 된다.
- [ ] 데이터 등록이 된다.
- [ ] 오류 메시지가 사용자에게 이해 가능하다.
- [ ] Streamlit 화면에는 service role key를 직접 넣지 않았다.

## Optional Deployment

- [ ] 배포는 필수가 아니라 선택 확장임을 문서에 표시했다.
- [ ] 배포를 진행했다면 Render, Upstash, Streamlit Community Cloud URL을 정리했다.
- [ ] 배포 환경변수에 실제 key를 등록하고, GitHub에는 `.env`를 올리지 않았다.

## Presentation

- [ ] Supabase를 선택한 이유를 설명할 수 있다.
- [ ] 03 과정에서는 Docker를 사용하지 않고 06 과정에서 다룬다는 점을 설명할 수 있다.
- [ ] RLS와 key 보안 주의사항을 설명할 수 있다.
- [ ] `learning_logs`는 입문 샘플, `service_logs`는 팀 프로젝트 기준 테이블이라는 점을 설명할 수 있다.

