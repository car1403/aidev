# 04. FastAPI Errors

FastAPI 실행 중 자주 만나는 오류입니다.

## uvicorn을 찾을 수 없습니다

해결:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 주소가 열리지 않습니다

확인:

```text
uvicorn이 실행 중인가?
포트 번호가 맞는가?
브라우저 주소가 http://127.0.0.1:8000/docs 인가?
```

## Port already in use

이미 같은 포트를 사용하는 서버가 있습니다.

해결:

```text
기존 서버에서 Ctrl + C
또는 다른 포트 사용
```

예:

```powershell
uvicorn main:app --reload --port 8001
```
