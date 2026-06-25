# Common Commands

04 미니 프로젝트에서 자주 쓰는 명령어입니다.

```powershell
cd C:/aidev/04_supabase-ai-mini-project
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

FastAPI는 `uvicorn main:app --reload --port 8000`, Streamlit은 `streamlit run app.py`로 실행합니다.
