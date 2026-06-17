# API Test Guide

## Backend Run

```powershell
cd backend
uvicorn main:app --reload
```

## Health

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Logs

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/logs
```

