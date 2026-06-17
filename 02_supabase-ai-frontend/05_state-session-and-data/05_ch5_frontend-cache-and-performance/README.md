# 05_ch5_frontend-cache-and-performance

반복 조회 데이터를 캐시하고 화면 응답 흐름을 개선하는 방법을 학습합니다.

Streamlit 앱은 입력이 바뀔 때마다 다시 실행되므로, 동일한 데이터를 반복해서 불러오면 화면 응답이 느려질 수 있습니다. 이 챕터에서는 `st.cache_data`를 사용해 반복 조회 결과를 캐시합니다.

이 과정의 기본 데이터 흐름은 `Streamlit -> FastAPI 백엔드 -> Supabase`입니다. 캐시는 프론트엔드 화면 응답을 빠르게 하기 위한 도구이며, Supabase 권한 검증이나 데이터 저장을 대신하지 않습니다.

## 학습 목표

- `st.cache_data`로 함수 결과를 캐시할 수 있다.
- API 조회 결과를 캐시할 수 있다.
- TTL을 사용해 캐시 유지 시간을 제한할 수 있다.
- 버튼으로 캐시를 초기화할 수 있다.
- 사용자별 데이터 캐시에서 주의할 점을 설명할 수 있다.

## 예제 파일

```text
01_cache-data-basic.py
02_cached-api-call.py
03_cache-ttl-example.py
04_clear-cache-button.py
```

## 기본 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\05_state-session-and-data\05_ch5_frontend-cache-and-performance\01_cache-data-basic.py
```

## API 캐시 예제 백엔드

API 캐시 예제는 백엔드 API가 필요합니다. 기본적으로는 `01_supabase-ai-backend`를 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

백엔드 과정이 아직 준비되지 않았을 때만 아래 샘플을 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-auth-session-sample:app --reload --host 127.0.0.1 --port 8000
```

## 확인할 내용

- 첫 실행과 두 번째 실행의 응답 흐름 차이를 확인했는가?
- TTL 시간이 지나면 캐시가 갱신되는가?
- 캐시 비우기 버튼을 누르면 다시 데이터를 불러오는가?
- 사용자별 데이터에 캐시를 적용할 때 token 또는 user id를 함수 인자로 포함했는가?

## 주의할 점

사용자별 데이터는 모든 사용자가 같은 캐시를 공유하지 않도록 주의해야 합니다. 토큰, 사용자 ID, 필터 조건처럼 결과를 구분하는 값은 캐시 함수의 인자로 전달하는 것이 좋습니다.

Docker 기반 캐시, 서비스 운영, 배포 환경 성능 점검은 `06_multi-agent-service-ops`에서 다룹니다.
