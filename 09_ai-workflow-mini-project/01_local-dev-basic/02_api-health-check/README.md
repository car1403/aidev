# 02_api-health-check

## 목표

수업용 샘플 backend의 `/health` API를 확인합니다.

## 실행

```powershell
cd C:\aidev\09_ai-workflow-mini-project\02_instructor-sample-project
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8900
```

확인:

```text
http://127.0.0.1:8900/health
```
