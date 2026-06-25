# Project Architecture

04 미니 프로젝트의 기본 아키텍처는 Streamlit 프론트엔드, FastAPI 백엔드, Supabase 데이터베이스, Gemini API로 구성합니다.

```text
User -> Streamlit UI -> FastAPI API -> Supabase
                         -> Gemini API
                         -> service_logs table
```

프론트엔드는 API Key를 직접 다루지 않고, 백엔드는 요청 검증, LLM 호출, Supabase 저장을 담당합니다.
