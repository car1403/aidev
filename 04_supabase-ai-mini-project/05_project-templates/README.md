# 05_project-templates

이 폴더는 팀 프로젝트에 바로 복사해서 사용할 수 있는 문서, SQL, 환경 변수, 체크리스트 템플릿을 모아 둔 공간입니다.

`02_instructor-sample-project`는 완성된 샘플을 보는 곳이고, `03_supabase-and-sse-practice`는 핵심 기능을 단계별로 연습하는 곳입니다. 이 폴더는 팀 프로젝트를 시작할 때 산출물 문서와 기본 SQL을 빠르게 준비하기 위한 템플릿 모음입니다.

## 폴더 구성

```text
05_project-templates
├─ README.md
├─ project-docs
│ ├─ project-plan-template.md
│ ├─ api-spec-template.md
│ ├─ ui-design-template.md
│ ├─ supabase-schema-template.md
│ ├─ dashboard-result-template.md
│ ├─ streaming-response-design-template.md
│ ├─ deployment-guide-template.md
│ └─ test-checklist-template.md
├─ sql
│ ├─ supabase-base-schema.sql
│ └─ seed-sample-data.sql
├─ env
│ └─ env.example.template
└─ checklists
  └─ final-submission-checklist.md
```

## 사용 방법

1. `99_team-projects` 아래에 팀 프로젝트 폴더를 만듭니다.
2. 필수 산출물 템플릿 4개를 팀 프로젝트의 `docs` 폴더로 복사합니다.
3. `sql/supabase-base-schema.sql`을 팀 주제에 맞게 수정합니다.
4. `env/env.example.template`을 팀 프로젝트의 `.env.example`로 복사합니다.
5. 필요하면 선택 보조 산출물 템플릿과 체크리스트를 추가로 사용합니다.

## 중요한 기준

- 실제 `.env` 파일은 제출하지 않습니다.
- `.env.example`에는 실제 key를 넣지 않습니다.
- Supabase service role key는 FastAPI 백엔드에서만 사용합니다.
- Streamlit 화면에는 service role key를 넣지 않습니다.
- 배포는 선택 확장입니다. 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되는 것입니다.

## 어떤 문서를 언제 쓰나요?

```text
API 구현 전
-> api-spec-template.md

화면 구현 전
-> ui-design-template.md

Supabase 테이블 생성 전
-> supabase-schema-template.md, supabase-base-schema.sql

대시보드 구현 후
-> dashboard-result-template.md

프로젝트 시작 또는 기획 보조가 필요할 때
-> project-plan-template.md

SSE 선택 확장 시
-> streaming-response-design-template.md

무료 배포 선택 시
-> deployment-guide-template.md

제출 전
-> test-checklist-template.md, final-submission-checklist.md
```

필수 산출물은 `api-spec-template.md`, `ui-design-template.md`, `supabase-schema-template.md`, `dashboard-result-template.md` 4가지입니다. 나머지 템플릿은 선택 보조 산출물입니다.
