# 05. Streamlit Errors

Streamlit 실행 중 자주 만나는 오류입니다.

## streamlit 명령을 찾을 수 없습니다

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 화면은 열렸는데 API 호출이 실패합니다

확인:

```text
FastAPI 서버가 실행 중인가?
.env의 API_BASE_URL이 맞는가?
포트 번호가 맞는가?
```

## 포트를 바꾸고 싶을 때

```powershell
streamlit run app.py --server.port 8502
```
