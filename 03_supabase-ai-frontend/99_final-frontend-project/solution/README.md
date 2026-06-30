# Solution

이 폴더는 `99_final-frontend-project`의 참고용 Streamlit solution입니다.

기본 실습에서는 같은 프로젝트 폴더의 `backend_mock`을 먼저 실행한 뒤, 이 Streamlit 앱을 실행합니다. 실제 서비스 연결까지 진행할 때는 `backend_service`를 실행하고 `API_BASE_URL`을 같은 주소로 유지하거나 배포 주소로 바꿉니다.

## 실행 방법

PowerShell 1:

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_mock
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

PowerShell 2:

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\solution
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

## 화면 구성

- 사이드바: API 주소, 회원가입, 로그인, 로그아웃, 현재 사용자
- 탭 1: 챗봇
- 탭 2: 대화 기록
- 탭 3: 서비스 로그
- 탭 4: 배포 전 점검

## 확인할 것

- 프론트엔드는 Supabase나 LLM API key를 직접 사용하지 않습니다.
- 로그인 성공 후 `st.session_state["access_token"]`에 token을 저장합니다.
- 보호 API 호출 시 `Authorization: Bearer ...` header를 보냅니다.
- 응답 생성 중 상태를 `st.spinner`로 표시합니다.
