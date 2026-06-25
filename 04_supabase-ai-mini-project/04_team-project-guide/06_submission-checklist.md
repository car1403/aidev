# 06 Submission Checklist

최종 제출 전 확인할 체크리스트입니다.

## 필수 제출 기준

```text
README.md
.env.example
backend/main.py
backend/requirements.txt
frontend/app.py
frontend/requirements.txt
docs/api-spec.md
docs/ui-design.md
docs/supabase-schema.md
docs/dashboard-result.md
```

필수 산출물은 `API 설계 문서`, `화면 설계서`, `데이터베이스 스키마 설계서`, `대시보드 구현 결과물` 4가지입니다. 실행에 필요한 README, `.env.example`, backend/frontend 파일은 프로젝트 확인을 위해 함께 유지합니다.

아래 문서는 선택 보조 산출물입니다. 작성하지 않아도 04 과정의 필수 제출 기준에는 영향을 주지 않습니다.

```text
docs/project-plan.md
docs/streaming-response-design.md
docs/deployment-guide.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 실행 체크리스트

- [ ] `C:\aidev\04_supabase-ai-mini-project\.venv`를 사용한다.
- [ ] 프로젝트 안에 별도 `.venv`를 만들지 않았다.
- [ ] `.env.example`에는 실제 key가 없다.
- [ ] 실제 `.env`는 제출하지 않는다.
- [ ] FastAPI가 로컬에서 실행된다.
- [ ] Streamlit이 로컬에서 실행된다.
- [ ] Streamlit이 FastAPI API를 호출한다.
- [ ] FastAPI가 Supabase에 데이터를 저장하거나 조회한다.

## 문서 체크리스트

- [ ] API 설계 문서에 URL, Method, Request, Response가 있다.
- [ ] 화면 설계서에 주요 화면과 사용자 액션 흐름이 있다.
- [ ] 데이터베이스 스키마 설계서에 테이블, 컬럼, 관계, 제약조건이 있다.
- [ ] 대시보드 구현 결과물 문서에 실행 화면과 핵심 기능 설명이 있다.
- [ ] 배포를 진행했다면 배포 URL과 환경 변수 설정 방법이 있다.
- [ ] 배포를 진행하지 않았다면 로컬 실행 기준을 명확히 작성했다.

## 보안 체크리스트

- [ ] `SUPABASE_SERVICE_ROLE_KEY`가 프론트엔드 코드에 없다.
- [ ] Gemini API key와 OpenAI API key가 코드에 직접 적혀 있지 않다.
- [ ] `.env`가 GitHub에 올라가지 않았다.
- [ ] 로그에 key, token, password가 남지 않는다.

## 선택 확장 체크리스트

- [ ] SSE 기반 실시간 응답 표시를 구현했다.
- [ ] 무료 배포 서비스를 사용해 시연 URL을 만들었다.
- [ ] 사용자 피드백 데이터를 AI 응답 품질 개선 기준으로 정리했다.
- [ ] OpenAI 예제를 선택 비교로 실행해 보았다.
- [ ] 테스트 체크리스트에 정상/오류/빈 데이터 상황을 정리했다.
- [ ] 발표 자료를 작성했다.

선택 확장은 필수가 아닙니다. 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되고 필수 산출물이 정리되어 있는 것입니다.
