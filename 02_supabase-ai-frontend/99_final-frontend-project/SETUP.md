# SETUP

이 문서는 `99_final-frontend-project`를 로컬 PC에서 실행하는 방법을 안내합니다.

초보자는 백엔드와 프론트엔드를 한 번에 이해하려고 하기보다, 아래 순서대로 하나씩 실행하는 것이 좋습니다.

```text
FastAPI 백엔드 실행
-> /health 확인
-> Streamlit 프론트엔드 실행
-> Streamlit에서 백엔드 호출 확인
```

## 1. 작업 위치로 이동

```powershell
cd C:\aidev\02_supabase-ai-frontend\99_final-frontend-project
```

## 2. 상위 과정 가상환경 활성화

이 실습은 `02_supabase-ai-frontend`의 `.venv`를 함께 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
```

가상환경이 없다면 먼저 다음 명령으로 만듭니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 3. 환경 변수 파일 만들기

```powershell
cd C:\aidev\02_supabase-ai-frontend\99_final-frontend-project
Copy-Item .env.example .env
```

처음 로컬 실행에서는 아래 값만 확인하면 됩니다.

```env
API_BASE_URL=http://127.0.0.1:8000
```

Upstash Redis는 선택입니다. 값을 비워 두면 백엔드는 메모리에만 로그를 저장합니다.

## 4. FastAPI 백엔드 실행

첫 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
cd C:\aidev\02_supabase-ai-frontend\99_final-frontend-project\backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 아래 주소를 열어 확인합니다.

```text
http://127.0.0.1:8000/health
```

정상이라면 다음과 비슷한 JSON이 보입니다.

```json
{
  "ok": true,
  "service": "final-frontend-project-backend"
}
```

API 문서는 아래 주소에서 볼 수 있습니다.

```text
http://127.0.0.1:8000/docs
```

## 5. Streamlit 프론트엔드 실행

두 번째 PowerShell을 열고 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
cd C:\aidev\02_supabase-ai-frontend\99_final-frontend-project\frontend
streamlit run app.py --server.port 8501
```

브라우저에서 아래 주소를 열어 확인합니다.

```text
http://localhost:8501
```

## 6. 실습 확인 순서

1. 홈 화면에서 백엔드 연결 상태를 확인합니다.
2. `Chatbot` 화면에서 사용자 이름과 질문을 입력합니다.
3. 응답이 화면에 표시되는지 확인합니다.
4. `Chat History` 화면에서 대화 이력이 보이는지 확인합니다.
5. `Service Logs` 화면에서 API 호출 로그가 보이는지 확인합니다.
6. `Deployment Check` 화면에서 배포 전 점검 항목을 확인합니다.

## 7. 서버 종료

각 PowerShell에서 `Ctrl + C`를 누르면 실행 중인 서버가 종료됩니다.

