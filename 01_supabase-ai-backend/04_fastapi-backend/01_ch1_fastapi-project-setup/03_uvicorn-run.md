# Uvicorn 실행

```powershell
uvicorn main:app --reload
```

다른 파일명을 사용하는 경우:

```powershell
uvicorn 01_hello-fastapi:app --reload
```

파일명에 하이픈이 있으면 import 문제가 생길 수 있으므로 실제 프로젝트 파일명은 `main.py`를 권장합니다.

