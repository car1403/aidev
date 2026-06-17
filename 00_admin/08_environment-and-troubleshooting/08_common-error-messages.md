# 08. Common Error Messages

자주 만나는 오류 메시지와 확인 순서입니다.

## ModuleNotFoundError

```text
패키지가 설치되지 않았거나 .venv가 활성화되지 않았습니다.
```

확인:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## FileNotFoundError

```text
파일 경로가 잘못되었거나 현재 폴더가 다릅니다.
```

확인:

```powershell
pwd
dir
```

## Connection refused

```text
API 서버가 실행 중이 아닐 가능성이 큽니다.
```

확인:

```text
FastAPI 서버 실행 여부
포트 번호
API_BASE_URL
```

## 401 Unauthorized

```text
인증 토큰 또는 API Key 문제입니다.
```

## 403 Forbidden

```text
권한 문제입니다. Supabase RLS 정책 또는 key 사용 위치를 확인합니다.
```
