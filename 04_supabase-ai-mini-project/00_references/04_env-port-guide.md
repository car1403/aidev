# 04 ENV and Port Guide

이 문서는 03 과정에서 사용하는 환경변수와 포트 번호를 초보자 기준으로 설명합니다.

## 환경변수란 무엇인가요?

환경변수는 코드에 직접 적기 부담스러운 설정값을 바깥에서 주입하는 방법입니다.

예를 들어 Supabase key, Gemini API key, 백엔드 주소는 코드에 직접 적지 않고 `.env` 파일에 넣습니다.

03 과정에서 사용하는 `.env` 위치는 다음입니다.

```text
C:\aidev\04_supabase-ai-mini-project\.env
```

예시:

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini

API_BASE_URL=http://127.0.0.1:8000
```

## 환경변수별 역할

| 이름 | 주로 사용하는 곳 | 설명 |
| --- | --- | --- |
| `SUPABASE_URL` | Backend, 일부 실습 Frontend | Supabase 프로젝트 API 주소 |
| `SUPABASE_ANON_KEY` | Backend 또는 제한된 Frontend | RLS 정책과 함께 사용하는 공개 가능 key |
| `SUPABASE_SERVICE_ROLE_KEY` | Backend only | 강한 권한을 가진 서버용 key |
| `GEMINI_API_KEY` | Backend | 03 과정의 기본 AI API 호출용 key |
| `GEMINI_MODEL` | Backend | 사용할 Gemini 모델 이름. 기본 예시는 `gemini-2.5-flash-lite` |
| `OPENAI_API_KEY` | Backend | 선택/비교 실습용 OpenAI API key |
| `OPENAI_MODEL` | Backend | 선택/비교 실습용 OpenAI 모델 이름. 기본 예시는 `gpt-4.1-mini` |
| `API_BASE_URL` | Frontend | Streamlit이 호출할 FastAPI 주소 |

## 주요 포트

| 포트 | 용도 |
| --- | --- |
| 8000 | FastAPI 백엔드 |
| 8501 | Streamlit 프론트엔드 |

Supabase는 클라우드 프로젝트 URL을 사용하므로 로컬 DB 포트를 열지 않습니다.

## localhost와 127.0.0.1

03 과정에서 FastAPI와 Streamlit은 로컬 PC에서 실행됩니다. 백엔드 주소는 보통 다음 값을 사용합니다.

```text
http://127.0.0.1:8000
```

Streamlit은 `.env`의 `API_BASE_URL` 값을 읽어 이 주소로 FastAPI를 호출합니다.

## 포트가 이미 사용 중일 때

8000 포트가 이미 사용 중이면 FastAPI를 다른 포트로 실행할 수 있습니다.

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

이 경우 `.env`의 `API_BASE_URL`도 함께 바꿉니다.

```env
API_BASE_URL=http://127.0.0.1:8001
```
