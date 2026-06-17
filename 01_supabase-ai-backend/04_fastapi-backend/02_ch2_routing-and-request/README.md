# 02_ch2_routing-and-request

라우팅과 요청 데이터 처리 방식을 학습합니다.

이 챕터에서는 URL, HTTP Method, Path Parameter, Query Parameter, Request Body가 각각 어떤 역할을 하는지 예제로 확인합니다.

## 예제 파일

```text
01_http-methods.py
02_path-parameters.py
03_query-parameters.py
04_request-body.py
```

## 실행 예시

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\02_ch2_routing-and-request
..\..\.venv\Scripts\Activate.ps1
uvicorn 01_http-methods:app --reload
```

파일명에 하이픈이 들어 있어 실행이 불편한 환경에서는 파일을 `main.py`로 복사해서 실행해도 됩니다.

```powershell
Copy-Item .\01_http-methods.py .\main.py
uvicorn main:app --reload
```

