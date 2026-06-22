# 00_references

`02_supabase-ai-frontend`를 시작하기 전에 읽는 참고 자료입니다.

이 폴더는 별도 수업 단원이 아니라, Streamlit 프론트엔드 수업 전체에서 반복해서 확인하는 기준 문서 모음입니다.

## 문서 목록

```text
frontend-course-map.md
frontend-security-and-deployment-notes.md
```

## 먼저 확인할 내용

- 이 과정의 기본 UI 도구는 Streamlit입니다.
- React는 필수 실습이 아니라 진도와 난이도과 진도에 따라 선택적으로 소개합니다.
- Streamlit은 Supabase DB에 직접 접속하지 않고 `01_supabase-ai-backend`의 FastAPI API를 호출합니다.
- 프론트엔드 `.env`에는 `API_BASE_URL`만 둡니다.
- Supabase `service_role` key, Upstash token, LLM API key는 프론트엔드에 두지 않습니다.
- SSE 기반 실시간 응답 스트리밍은 `03_supabase-ai-mini-project`에서 백엔드, 프론트엔드, Supabase 저장 흐름을 함께 연결해 다룹니다.

## 확인 질문

```text
Streamlit은 전체 서비스에서 어떤 역할을 하나요?
프론트엔드에 service role key를 두면 왜 위험한가요?
API_BASE_URL은 어디에 사용되나요?
SSE는 왜 03 미니 프로젝트에서 다루나요?
```
