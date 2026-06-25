# Deployment Guide Template

무료 배포 선택 확장 문서 템플릿입니다.

03 과정에서 배포는 필수가 아닙니다. 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되면 기본 제출 기준을 충족합니다.

## 1. 배포 여부

```text
배포 진행 여부:
진행 / 미진행
```

## 2. 권장 무료 배포 흐름

```text
FastAPI
-> Render

Redis 또는 캐시가 필요한 경우
-> Upstash

Streamlit
-> Streamlit Community Cloud

Database
-> Supabase
```

## 3. Render 환경 변수

```text
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
GEMINI_API_KEY=
```

## 4. Streamlit Community Cloud 환경 변수

Streamlit에는 백엔드 주소만 넣는 것을 권장합니다.

```text
API_BASE_URL=https://your-render-service.onrender.com
```

## 5. 배포 URL

```text
FastAPI URL:
Streamlit URL:
Supabase Project URL:
```

## 6. 주의사항

- 실제 `.env` 파일은 업로드하지 않습니다.
- service role key는 Render 같은 백엔드 배포 환경에만 넣습니다.
- Streamlit에는 service role key를 넣지 않습니다.
- 무료 서비스는 일정 시간 사용하지 않으면 잠들 수 있습니다.
